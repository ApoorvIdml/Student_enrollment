// Copyright (c) 2026, Apoorv Singh and contributors
// For license information, please see license.txt

frappe.ui.form.on("Assignment", {
	setup(frm) {
		frm.make_methods = {
			"ToDo": () => {
				frappe.model.open_mapped_doc({
					method: "enrollment_system.api.make_todo",
					// args: {
					// 	referenceType: "Assignment",
					// 	source_name: frm.doc.name
					// }
					frm: frm
				});
			}
		};
	},

	refresh(frm) {
		set_student_name_filter(frm);
	},

	course(frm) {
		set_student_name_filter(frm);
	},

	semester(frm) {
		set_student_name_filter(frm);
	}
});

function set_student_name_filter(frm) {
	frm.set_query("student_name", function() {

		let filters = {};

		if (frm.doc.course) {
			filters.course = frm.doc.course;
		}

		if (frm.doc.semester) {
			filters.semester = frm.doc.semester;
		}

		return {
			query: "enrollment_system.enrollment_system.doctype.assignment.assignment.get_students",
			filters: filters
		};
	});
}