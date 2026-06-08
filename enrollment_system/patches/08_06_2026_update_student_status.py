import frappe


def execute():
    frappe.db.sql("""
        UPDATE `tabStudent`
        SET status = 'Active'
        WHERE enrollment_date > '2025-01-01'
    """)

frappe.db.commit()