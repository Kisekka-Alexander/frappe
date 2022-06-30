// Copyright (c) 2022, Alexander and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Recent Cases"] = {
	"filters": [
		{
            fieldname: 'date_from',
            label: __('Date From'),
            fieldtype: 'Date'
           
        },
		{
            fieldname: 'date_to',
            label: __('Date To'),
            fieldtype: 'Date'
           
        },
		{
            fieldname: 'suspect_district',
            label: __('District'),
            fieldtype: 'Link',
			options: 'Districts'

           
        },
		{
            fieldname: 'case_status',
            label: __('Status'),
            fieldtype: 'Select',
			options: [
				'All',
				'Under Investigation',
				'Prosecution',
				'Review',
				'Open',
				'Closed'
			]
           
        },
		{
            fieldname: 'conservation_area',
            label: __('Protected Area'),
            fieldtype: 'Link',
			options: 'Parks'
           
        }

	]
};
