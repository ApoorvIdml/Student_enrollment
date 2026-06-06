// Copyright (c) 2026, Apoorv Singh and contributors
// For license information, please see license.txt

frappe.ui.form.on("Student", {
	refresh(frm) {

		frm.add_custom_button("Get Assignment Details", function() {

			frappe.call({
				method: "enrollment_system.enrollment_system.doctype.student.student.get_assignment_details",
				args: {
					student: frm.doc.name
				},
				callback: function(r) {

					if (r.message) {

						frappe.msgprint({
							title: "Latest Assignment",
							message: `
								<b>Course:</b> ${r.message.course}<br>
								<b>Semester:</b> ${r.message.semester}<br>
								<b>Assignment:</b> ${r.message.assignment_details}
							`,
							indicator: "blue"
						});

					} else {

						frappe.msgprint("No Assignment Found");

					}
				}
			});

		});

	}
});