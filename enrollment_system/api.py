# import frappe
# from frappe.model.mapper import get_mapped_doc


# @frappe.whitelist()
# def make_todo(source_name, target_doc=None):

#     referenceType = "Assignment"      # Hardcoded

#     def set_hardCoded_values(source, target):
#         _set_hardCoded_values(referenceType, source, target)

#     target_doc = get_mapped_doc(
#         referenceType,
#         source_name,
#         {
#             "Assignment": {
#                 "doctype": "ToDo",
#                 "field_map": {
#                     "name": "reference_name"
#                 },
#                 "field_no_map": ["date"]
#             }
#         },
#         target_doc,
#         set_hardCoded_values,
#     )

#     return target_doc

      


# def _set_hardCoded_values(referenceType,source, target):

#     target.reference_type = "Assignment"   # Hardcoded
#     target.date = frappe.utils.nowdate()   # Current Date

import frappe
from frappe.model.mapper import get_mapped_doc


@frappe.whitelist()
def make_todo(source_name, target_doc=None):

    target_doc = get_mapped_doc(
        "Assignment",
        source_name,
        {
            "Assignment": {
                "doctype": "ToDo",
                "field_map": {
                    "name": "reference_name"
                }
            }
        },
        target_doc,
    )

    assignment = frappe.get_doc("Assignment", source_name)

    target_doc.reference_type = "Assignment"
    target_doc.date = frappe.utils.nowdate()

    target_doc.assigned_by = "suryansh chaudhary"
    target_doc.allocated_to = assignment.student_name

    return target_doc