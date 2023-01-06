#Save selection pose 2 json
#Loads pose from json if unselected
#{bone_name:[[posx,posy,posz],[rotx,roty,rotz],[sclx,sclyl,sclz]]}
#[[bone_name,[posx,posy,posz],[rotx,roty,rotz],[sclx,sclyl,sclz]]
# r'G:\nauka\xsi2maya\sel.json'

def save_json (comp_dict, path):
	import json
	json=json.dumps(comp_dict)
	f=open(path,"w")
	f.write(json)
	f.close()	


def read_json(file_pose):
	import json
	with open(file_pose) as json_data:
		return json.load(json_data)


def get_local_transform(obj):
	pose = []
	tl = obj.kinematics.local
	pos = [tl.posx, tl.posy, tl.posz]
	rot = [tl.rotx, tl.roty, tl.rotz]
	scl = [tl.sclx, tl.scly, tl.sclz]
	pose.append([[x.value for x in pos],
				[x.value for x in rot],
				[x.value for x in scl]])
	return pose[0]


ap = Application
path = r'G:\nauka\xsi2maya\sel.json'

sel = ap.selection
sel = [x for x in sel]

if sel != []:
	#SAVING POSE
	
	#pose_dir = {}
	#for bone in sel: pose_dir[str(bone.name)]= get_local_transform(bone)
	pose_list = []
	for bone in sel:
		pose_list.append([str(bone.name),get_local_transform(bone)[0],get_local_transform(bone)[1],get_local_transform(bone)[2]])

	save_json(pose_list, path)
	#for p in pose_list[:10]: print pz
	print 'Pose saved to', path
	
else:
	#LOADING POSE
	sel = []
	pose = read_json(path)
	for bone,pose,rota,scal in pose:
		bone = ap.dictionary.getobject(bone)
		sel.append(bone)
		
		bone.kinematics.local.posx.value=pose[0]
		bone.kinematics.local.posy.value=pose[1]
		bone.kinematics.local.posz.value=pose[2]
		bone.kinematics.local.rotx.value=rota[0]
		bone.kinematics.local.roty.value=rota[1]
		bone.kinematics.local.rotz.value=rota[2]
		bone.kinematics.local.sclx.value=scal[0]
		bone.kinematics.local.scly.value=scal[1]
		bone.kinematics.local.sclz.value=scal[2]
		
	ap.selectobj(sel)
		

	

