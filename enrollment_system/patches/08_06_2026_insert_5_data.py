import frappe

def execute():


    frappe.db.sql("""INSERT INTO `tabCourse` (name, course_name, course_fee)
        VALUES
        ('COURSE001', 'Python Programming', 15000),
        ('COURSE002', 'Java Programming', 18000),
        ('COURSE003', 'Data Structures', 20000),
        ('COURSE004', 'Machine Learning', 30000),
        ('COURSE005', 'Web Development', 25000)
    """)

frappe.db.commit()