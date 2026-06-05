// Copyright (c) 2026, Apoorv Singh and contributors
// For license information, please see license.txt

frappe.ui.form.on("Enrollment", {
	course_fee(frm) {
		frm.set_value(
			"total_fee",
			(frm.doc.course_fee || 0) + (frm.doc.registration_fee || 0)
		);
	},

	registration_fee(frm) {
		frm.set_value(
			"total_fee",
			(frm.doc.course_fee || 0) + (frm.doc.registration_fee || 0)
		);
	}
});