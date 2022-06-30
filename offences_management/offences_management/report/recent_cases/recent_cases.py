import frappe
from frappe import _


def execute(filters=None):

	date_from = filters.get("date_from")
	date_to = filters.get("date_to")

	case_status = filters.get("case_status")

	if (filters.get("suspect_district")):
		suspect_district=filters.get("suspect_district")
	else: suspect_district=''

	if (filters.get("conservation_area")):
		conservation_area=filters.get("conservation_area")
	else: conservation_area=''

	columns=[
		{
            'fieldname': 'uwa_case_number',
            'label': _('Case Number'),
            'fieldtype': 'Data'
        },
		{
            'fieldname': 'full_name',
            'label': _('Offender Name'),
            'fieldtype': 'Data'
        },
		{
            'fieldname': 'date_of_arrest',
            'label': _('Date Of Reporting'),
            'fieldtype': 'Date'
        },
		{
            'fieldname': 'suspect_district',
            'label': _('District'),
            'fieldtype': 'Link',
			'options': 'Districts'

        },
		{
            'fieldname': 'conservation_area',
            'label': _('Protected Area'),
            'fieldtype': 'Link',
			'options': 'Parks'
        },
			{
            'fieldname': 'case_status',
            'label': _('Status'),
            'fieldtype': 'Data'
        }
	] 


	data = []
	cases_list = frappe.db.sql(
								"""select
									uwa_case_number,
									full_name,
									date_of_arrest,
									suspect_district,
									conservation_area,
									case_status
								    from `tabCases` where date_of_arrest between %s and %s
									order by date_of_arrest
								""",(date_from,date_to)
								)
	for case in cases_list:
		if((case[3]==suspect_district or suspect_district=='') 
					and (case[4]==conservation_area or conservation_area=='')
					and (case[5]==case_status or case_status=='All')
					):
			data.append(case)
		else: continue
		
	return columns, data

def get_cases_list():
	return frappe.db.sql(
	"""select
		uwa_case_number,
		full_name,
		date_of_arrest,
		suspect_district,
		conservation_area,
		case_status
		
	from `tabCases` """
	)

