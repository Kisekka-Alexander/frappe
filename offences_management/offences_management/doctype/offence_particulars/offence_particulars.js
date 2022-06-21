// Copyright (c) 2022, Alexander and contributors
// For license information, please see license.txt

frappe.ui.form.on('Offence Particulars', {
	refresh: function(frm) {
		set_css(frm);

	}
});

var set_css = function (frm)
{
	document.querySelectorAll("[data-fieldname='continue']")[1].style.backgroundColor="#284A87";
	document.querySelectorAll("[data-fieldname='continue']")[1].style.color="#FFFFFF";
	document.querySelectorAll("[data-fieldname='continue']")[1].style.fontSize="18px";
	document.querySelectorAll("[data-fieldname='exhibit_present']")[1].style.fontWeight="normal";

}
