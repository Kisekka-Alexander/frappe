// Copyright (c) 2022, Alexander and contributors
// For license information, please see license.txt
/* eslint-disable */


frappe.query_reports["Protected Areas with Most Cases"] = {
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
            fieldname: 'count',
            label: __('Top Most'),
            fieldtype: 'Link',
			options: 'Frequency Count'
        }

	]
};
