# Copyright (c) 2022, Alexander and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
	date_from = filters.get("date_from")
	date_to = filters.get("date_to")

	if(filters.get("count")):
		count=filters.get("count")
	else: count=1000

	columns, data = [
			{
            'fieldname': 'Freq',
            'label': _('Case Number'),
            'fieldtype': 'Data'
        },
		{
            'fieldname': 'animal_spicies',
            'label': _('Animal Species'),
            'fieldtype': 'Data'
        }
	]
	
	data=[]
	cases_freq = frappe.db.sql(
								"""select
									count(animal_species) as Freq,
									animal_species
								    from `tabCases` where date_of_arrest between %s and %s
									group by animal_species
									order by Freq desc LIMIT %s
								""",(date_from,date_to,count)
								)
	for species in cases_freq:
		data.append(species)
	return columns, data
