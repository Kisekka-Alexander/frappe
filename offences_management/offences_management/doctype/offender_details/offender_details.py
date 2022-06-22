
import frappe
from frappe import _
from frappe.website.website_generator import WebsiteGenerator

class OffenderDetails(WebsiteGenerator):

	website = frappe._dict(
		template="templates/offender_details.html",
		condition_field="published",
		page_title_field="name1",
	)
	
	
