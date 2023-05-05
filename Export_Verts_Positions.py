#Save selectet mesh positions
ap=Application

def save_json (comp_dict, path):
	import json
	json=json.dumps(comp_dict)
	f=open(path,"w")
	f.write(json)
	f.close()	

path = r'G:\nauka\xsi2maya\pos.json'


allSel = ap.selection
posall = []
for oSel in allSel:
	pos = []
	posarray = oSel.activeprimitive.geometry.points.PositionArray

	for i,v in enumerate(posarray[0]):
		x,y,z = posarray[0][i], posarray[1][i], posarray[2][i]
		pos.append([x,y,z])
			
	posall.append(pos)
		
save_json (posall,  path)
print pos
Application.ActivateObjectSelTool("")
