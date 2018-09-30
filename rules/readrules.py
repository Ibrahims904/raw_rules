def laodRules():
	with open(r'C:\Users\Ibrahim\Desktop\Demo\rules\rules.txt','r') as rules:
		rulelist=[]
		for rulesplit in [rule.lower().strip().split(' ') for rule in rules]:
			rulelistd={}
			rulelistd['signal']=rulesplit[0]
			try:
				value=float(rulesplit[-1])
				value_type='integer'
			except ValueError as valerr:
				if rulesplit[-1] in ['high','low','medium']:
					value_type='string'
					value=rulesplit[-1]
				else:
					value_type='datetime'
					value=rulesplit[-1]
			rulelistd['value_type']= value_type
			rulelistd['value']=value
			if any(element in rulesplit for element in ['not','never']):
				if  any(element in rulesplit for element in ['less','lesser','below']):
					rulelistd['condition']='>='
				elif any(element in rulesplit for element in ['great','greater','above','more']):
					rulelistd['condition']='<='
				else:
					rulelistd['condition']='!='
			else :
				if  any(element in rulesplit for element in ['less','lesser','below']):
					rulelistd['condition']='<='
				elif  any(element in rulesplit for element in ['great','greater','above','more']):
					rulelistd['condition']='>='
				else:
					rulelistd['condition']='=='
			rulelist.append(rulelistd)
	return rulelist

if __name__=='__main__':
	print(laodRules())