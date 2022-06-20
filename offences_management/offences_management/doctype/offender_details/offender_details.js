// Copyright (c) 2022, Alexander and contributors
// For license information, please see license.txt

frappe.ui.form.on('Offender Details' ,{
	refresh: function(frm) {
			
			// frappe.set_route("Form", "Offence Particulars", document.name);
			frm.add_custom_button('Continue', () => {
				frappe.new_doc('Offence Particulars')
			}).css({'color':'white','font-weight': 'bold','background-color':'#284A87'});
		
			set_css(frm);
	}

});

var set_css = function (frm)
{
	document.querySelectorAll("[data-fieldname='continue']")[1].style.backgroundColor="#284A87";
	document.querySelectorAll("[data-fieldname='continue']")[1].style.color="#FFFFFF";
	document.querySelectorAll("[data-fieldname='continue']")[1].style.fontSize="18px";
	document.querySelectorAll("[data-fieldname='continue']")[1].style.fontWeight="normal";

}
