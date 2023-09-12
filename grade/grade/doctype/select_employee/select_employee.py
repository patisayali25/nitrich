# Copyright (c) 2023, Quantbit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SelectEmployee(Document):
	@frappe.whitelist()
	def forggfg(self):
		if self.date and self.grade:
			doc = frappe.get_all("Employee", filters ={'designation':"Seperator"} ,fields =['name'])
			for d in doc:

				self.append("child",{

					"eid" : d.name,
					"employee_name" : frappe.get_value("Employee",d.name,'employee_name'),
					"grade": self.grade,
					'rate' : self.rate,
					'date': self.date,
					# 'weight' : self.weight,
					# 'total'	:self.rate * self.weight,	
					
					

				})
				
		else:
			frappe.throw('Please select Date and Grade')