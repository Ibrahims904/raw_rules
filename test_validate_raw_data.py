from rules import laodRules 
import json 
from datetime import datetime

def test_getInvalidDataFrom(filepath=r'C:\Users\Ibrahim\Desktop\Demo\raw_data\raw_data.json'):
	with open(filepath,'r') as raw_data:
		loaded_raw_data=json.load(raw_data)
		for rule in laodRules():
			for filtered_loaded_raw_data in filter(lambda x:  x['signal'].lower()==rule['signal'] and x['value_type'].lower()==rule['value_type'] ,loaded_raw_data):
				if rule['value_type']=='integer':
					if '<' in rule['condition']:
						if float(filtered_loaded_raw_data['value'])>rule['value']:
							print(filtered_loaded_raw_data)
					elif '>' in rule['condition']:
						if float(filtered_loaded_raw_data['value'])<rule['value']:
							print(filtered_loaded_raw_data)
				elif rule['value_type']=='string':
					if '!=' in rule['condition']:
						if filtered_loaded_raw_data['value'].lower() == rule['value']:
							print(filtered_loaded_raw_data)
					elif '==' in rule['condition']:
						if filtered_loaded_raw_data['value'].lower()!= rule['value']:
							print(filtered_loaded_raw_data)
				elif rule['value_type']=='datetime':
					raw_time=datetime.strptime(filtered_loaded_raw_data['value'],'%Y-%m-%d %H:%M:%S')
					currentTime=datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'%Y-%m-%d %H:%M:%S')
					if rule['condition']=='==':
						if rule['value']=='future':
							if raw_time< currentTime:
								print(filtered_loaded_raw_data)
						elif rule['value']=='past':
							if filtered_loaded_raw_data['value']> currentTime:
								print(filtered_loaded_raw_data)
					elif rule['condition']=='!=':
						if rule['value']=='future':
							if raw_time> currentTime:
								print(filtered_loaded_raw_data)
						elif rule['value']=='past':
							if filtered_loaded_raw_data['value']< currentTime:
								print(filtered_loaded_raw_data)


if __name__ == '__main__':
	getInvalidDataFrom(r'C:\Users\Ibrahim\Desktop\Demo\raw_data\raw_data.json')