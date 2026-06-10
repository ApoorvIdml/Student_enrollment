import frappe
from frappe.desk.doctype.todo.todo import ToDo


class CustomToDo(ToDo):

    def on_update(self):

        frappe.msgprint("Custom ToDo on_update called")

        super().on_update()