frappe.ui.form.on("ToDo", {
    refresh(frm) {
        console.log("ToDo Refresh Triggered");
    },

    validate(frm) {
        console.log("ToDo Validate Triggered");
    }
})