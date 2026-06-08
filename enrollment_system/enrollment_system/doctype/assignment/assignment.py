# Copyright (c) 2026, Apoorv Singh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Assignment(Document):

	def validate(self):

		enrollment = frappe.db.exists(
			"Enrollment",
			{
				"student_name": self.student_name,
				"course": self.course,
				"semester": self.semester
			}
		)

		if not enrollment:
			frappe.throw(
				"Selected student is not enrolled in the selected course or semester"
			)

	def on_update(self):

		if self.status == "Completed" and not self.grade:

			frappe.enqueue(
				"enrollment_system.assignment.assign_grade",
				assignment_name=self.name
			)


@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def get_students(doctype, txt, searchfield, start, page_len, filters):

	conditions = {}

	if filters.get("course"):
		conditions["course"] = filters.get("course")

	if filters.get("semester"):
		conditions["semester"] = filters.get("semester")

	enrollments = frappe.get_all(
		"Enrollment",
		filters=conditions,
		fields=["student_name"]
	)

	students = [d.student_name for d in enrollments]

	if not students:
		return []

	return frappe.db.sql("""
		SELECT
			name,
			student_name
		FROM `tabStudent`
		WHERE name IN %(students)s
		AND ({key} LIKE %(txt)s
			OR student_name LIKE %(txt)s)
		LIMIT %(start)s, %(page_len)s
	""".format(key=searchfield), {
		"students": tuple(students),
		"txt": f"%{txt}%",
		"start": start,
		"page_len": page_len
	})