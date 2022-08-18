import frappe
import re


def get_context(context):
	translation_table= frappe.db.get_list('Translation Table',
	fields=['oldstring','newstring'])
	
	query_parameter=frappe.request.environ.get('QUERY_STRING')	
	
	
	checked = query_parameter.find("checkbox=Y")		
	if checked == -1: #checkbox-casesensitive not checked
		
		query_params=query_parameter.replace('yourtext=','')		
		context.oldtxt = "You entered: " + query_params.replace('+',' ')
				
		for i in translation_table:
			#fromst= (i.oldstring).lower()
			#tost = (i.newstring).lower()
			#query_params =  query_params.lower().replace(fromst,tost)
			pat=re.compile(i.oldstring, re.IGNORECASE)
			query_params =pat.sub(i.newstring,query_params.replace('+',' '))
		
	else:
		#query_params=query_parameter.replace('yourtext=','').rstrip("&checkbox=Y").replace('+',' ')
		query_params=query_parameter.replace('yourtext=','').replace('&checkbox=Y','').replace('+',' ')
		context.oldtxt = "You entered: " + query_params
		
		for i in translation_table:
			fromst= i.oldstring
			tost = i.newstring
			query_params =  query_params.replace(fromst,tost)
	
	context.translation_table=translation_table
	context.qparam = "TRANSLATION: "+query_params	
	
	return context
