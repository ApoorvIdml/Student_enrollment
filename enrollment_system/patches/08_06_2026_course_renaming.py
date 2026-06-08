import frappe

def execute():

    frappe.db.sql("""
        UPDATE `tabEnrollment` e
        INNER JOIN `tabCourse` c
            ON e.course = c.course_name
        SET e.course_name = c.course_name
    """)

frappe.db.commit()