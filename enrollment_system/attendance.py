import frappe
from frappe.utils import nowdate

def update_attendance_count():

    today = nowdate()

    attendance_list = frappe.get_all(
        "Student Attendance",
        filters={"attendance_date": today},
        pluck="name"
    )

    for attendance in attendance_list:

        doc = frappe.get_doc(
            "Student Attendance",
            attendance
        )

        for row in doc.students:

            frappe.db.sql("""
                UPDATE `tabStudent`
                SET attendance_count =
                    IFNULL(attendance_count, 0) + 1
                WHERE name = %s
            """, row.student)

    frappe.db.commit()