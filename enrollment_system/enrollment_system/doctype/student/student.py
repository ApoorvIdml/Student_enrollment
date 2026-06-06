# Copyright (c) 2026, Apoorv Singh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Student(Document):
	pass


@frappe.whitelist()
def get_assignment_details(student):

	assignment = frappe.get_all(
		"Assignment",
		filters={
			"student_name": student
		},
		fields=[
			"course",
			"semester",
			"assignment_details",
			"creation"
		],
		order_by="creation desc",
		limit=1
	)

	if assignment:
		
		return assignment[0]

	return None