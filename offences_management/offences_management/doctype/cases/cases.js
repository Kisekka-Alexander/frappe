// Copyright (c) 2022, Alexander and contributors
// For license information, please see license.txt

frappe.ui.form.on('Cases', {
	refresh: function(frm) {
		// By default dont display/load/show the exhibit_particulars_section
		
		frm.toggle_display(['exhibit_particulars_section']);
	},

	exhibit_present: function(frm){

		// display/show the exhibit_particulars_section when the exhibit present field is checked
		frm.toggle_display(['exhibit_particulars_section'],frm.doc.exhibit_present===1);

		// Make the following fields mandatory when the exhibit present field is checked
		frm.toggle_reqd(['exhibit_type','nature_of_exhibit','animal_species',
		'exhibit_unit_of_measure','exhibit_weight','investigating_officer',
		'exhibit_narrative','officer_in_charge_of_exhibit','officer_in_charge_of_exhibit_contact',
	    'date_of_exhibit_storage','place_of_exhibit_storage','upload_exhibit_images'], frm.doc.exhibit_present===1);
	}

});
