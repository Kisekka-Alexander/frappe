# Copyright (c) 2022, Alexander and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
	date_from = filters.get("date_from")
	date_to = filters.get("date_to")

	if(filters.get("count")):
		count=int(filters.get("count"))
	else: count=1000

	columns=[
			{
            'fieldname': 'Freq',
            'label': _('Cases Number'),
            'fieldtype': 'Data'
        },
		{
            'fieldname': 'conservation_area',
            'label': _('Protected Area'),
            'fieldtype': 'Data'
        }
	]
	
	data=[]
	cases_freq = frappe.db.sql(
								"""select
									count(conservation_area) as Freq,
									conservation_area
								    from `tabCases` where date_of_arrest between %s and %s
									group by conservation_area
									order by Freq desc LIMIT %s
								""",(date_from,date_to,count)
								)
	for area in cases_freq:
		data.append(area)

	return columns, data
