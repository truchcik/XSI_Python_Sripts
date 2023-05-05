#Load point positions from json (maya format)
ap=Application

def save_json (comp_dict, path):
	import json
	json=json.dumps(comp_dict)
	f=open(path,"w")
	f.write(json)
	f.close()

def open_json(path):
	import json
	with open(path) as json_file:
		data = json.load(json_file)
	return data
	

path = r'G:\nauka\xsi2maya\pos.json'

allSel = ap.selection
posall = open_json(path)

for obj_nr, oSel in enumerate(allSel):
	maya_pos = posall[obj_nr]
	oGeometry = oSel.ActivePrimitive.Geometry
	obj_pos = oGeometry.Points.PositionArray
	soft_pos = [list(x) for x in obj_pos]

	for a,v in enumerate(maya_pos):
		for b,val in enumerate(v):
			soft_pos[b][a] = maya_pos[a][b]
			
	oGeometry.Points.PositionArray = soft_pos
