#saves skin to JSONs in format compatible with Maya IOSkin. 2 Jsons are made:
#fitting name ...\object_name.json
#fitting order in selection ...\_copy_n.json

import sys, json
ap = Application

def save_json (comp_dict, path):
	pliczek = json.dumps(comp_dict, indent=4)
	f=open(path,"w")
	f.write(pliczek)
	f.close()
	print 'Saved weights to', path

def getFullName(obj):
	oParents = []
	while str(obj.Parent) != "Scene_Root":
		oParents.append(str(obj.Parent.name))
		obj = obj.Parent
	oParents = '|' + '|'.join(oParents[::-1])
	return oParents

def weights_2_dic(oObj):
	#prepare Maya-compatible dictionary with weights and deformers
	oEnv = oObj.Envelopes[0]
	oDef = [getFullName(x) for x in oEnv.deformers]
	oWts = oEnv.weights

	vertexEnvDic = {}   #dictionary with weights per vertex
						#vID {deformerID : weight, ...}
	for k,vEnv in enumerate([x for x in oWts]):
		vertexEnvDic[str(k)] = {}
		for n, weight in enumerate(vEnv):
			if weight > 0:
				vertexEnvDic[str(k)][str(n)]= weight/100
		
	#temporary solution for MAYA compatibility
	infIds = {}
	for k in range(len(oDef)):
		infIds[str(k)]= k
		
	dWeights = {"weights": vertexEnvDic, "infs": oDef, "infIds": infIds}
	return dWeights

sciezka = r'Z:\p4\WX\wx.assets\characters\_tech\Char_Scripts_Data\XENVS\fast_skin'

if len(ap.Selection)==0: print ('Please, select at least one mesh and run script')
elif len(ap.Selection)>0:
	for k,oObj in enumerate(ap.Selection):
		dWeights = weights_2_dic(oObj)
		
		for nazwa in [str(oObj), '_copy_'+str(k)]:
			sciezka_temp = sciezka + '\\' + nazwa + '.json'
			save_json(dWeights, sciezka_temp)
		
print 'done'
