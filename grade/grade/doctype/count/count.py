# Copyright (c) 2023, Quantbit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Count(Document):
	@frappe.whitelist()
	def forggfg(self):
		if self.from_date and self.to_date:
			list=[]
			doc=frappe.get_all("Select Employee",
					 filters = {"date" : ["between" ,[self.from_date,self.to_date]]})
			for d in doc:
				MOC = frappe.get_all("Employee Child",
					 filters = {"Parent" : d.name},
					 fields = {"eid", "weight", "total"})
			for m in MOC:
				list.append({
					"eid" : m.eid,
					"weight" : m.weight,
					"total" : m.total,
				})

       
			weight_list = {}
			total_list = {}
			result_list = {}
			accumulated_values = {}
			for item in list:
				eid = item['eid']
				weight = item['weight']
				total = item['total']
				if eid in accumulated_values:
					accumulated_values[eid]['weight'] += weight
					accumulated_values[eid]['total'] += total
				else:
					accumulated_values[eid] = {'weight': weight, 'total': total}
			result_list = [{'eid': eid, 'weight': values['weight'], 'total': values['total']} for eid, values in accumulated_values.items()]
		# for item in result_list:
			# frappe.msgprint(str(item))
		
			for i in result_list:
				self.append('child',{
                   'employee_name' : i["eid"],			   
					'weight':i['weight'],
				   'total_amount': i["total"],
				   
			        
			})
		else:
			frappe.throw('Please select From Date and To ')

