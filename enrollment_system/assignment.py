import frappe
import random


def assign_grade(assignment_name):

    grade = random.choice(["A", "B", "C"])

    frappe.db.set_value(
        "Assignment",
        assignment_name,
        "grade",
        grade
    )

    frappe.db.commit()