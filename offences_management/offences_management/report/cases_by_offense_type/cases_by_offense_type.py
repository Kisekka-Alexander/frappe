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
            'fieldname': 'offense_category',
            'label': _('Offense Category'),
            'fieldtype': 'Data'
        }
	]
	
	data=[]
	cases_freq = frappe.db.sql(
								"""select
									count(offense_category) as Freq,
									offense_category
								    from `tabCases` where date_of_arrest between %s and %s
									group by offense_category
									order by Freq desc LIMIT %s
								""",(date_from,date_to,count)
								)
	for offense in cases_freq:
		data.append(offense)

	return columns, data
