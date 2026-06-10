# Copyright (c) 2026, Apoorv Singh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Enrollment(Document):
    def validate(self):
        frappe.msgprint("Validation logic executed for Enrollment")

        if not self.student_name:
            frappe.throw("Student is required")

        if not self.course:
            frappe.throw("Course is required")

        if self.registration_fee < 0:
            frappe.throw("Registration Fee cannot be negative")

    def on_submit(self):

        try:

            course = frappe.get_doc("Course", self.course)

            course.available_seats -= 1

            course.save()

        except Exception as e:

            frappe.log_error(
                f"Error while decreasing seats: {str(e)}"
            )

    def on_cancel(self):

        try:

            course = frappe.get_doc("Course", self.course)

            course.available_seats += 1

            course.save()

        except Exception as e:

            frappe.log_error(
                f"Error while increasing seats: {str(e)}"
            )