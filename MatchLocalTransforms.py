# MatchLocalTransforms.py
# 1 Compute transformation matrix T between two meshes
#	using positions of their 3 vertices id[0,1,2]
# 2 Applies Scale Rotation Transformations from T to source LocalTransforms		

ap = Application

def setIce(obj, trgObj, level, name, cpmnd_path):
	oIce = ap.ApplyOp("ICETree", obj, "siNode", "", "", level)
	ap.SetValue(oIce()+".Name", name , "")
	ap.AddICECompoundNode(cpmnd_path, oIce)
	
	#"base.polymsh.iGetSRT.GetSRT_From_2Meshes"
	Node = oIce() + '.' + cpmnd_path.split('\\')[-1].split('.')[0].replace(' ','_')
	#"base.polymsh.iGetSRT.port1"
	IceInPort = oIce() + ".port1" 	
	#"base.polymsh.iGetSRT.GetSRT_From_2Meshes.Execute"	
	NodeOutPort = Node + ".Execute"
	ap.ConnectICENodes(IceInPort, NodeOutPort)
	
	#"base.polymsh.iGetSRT.GetSRT_From_2Meshes.Reference"
	NodeRefPort = Node + ".Reference"
	ap.SetValue(NodeRefPort ,trgObj.fullname)
	return oIce

def getIceVector3(obj, attrName):
	att = obj.ActivePrimitive.GetICEAttributeFromName(attrName).DataArray[0]
	return [att.X, att.Y, att.Z]
	#other datatypes: constans.siICENodeData..., where ...=
	#Quaternion .W .X .Y .Z
	#Rotation .RotX .RotY .RotZ
	#Matrix33 elem[n].Value(a,b))
	#Color4 .Red .Green .Blue .Alpha

def setLocalTransform(suffix, values):
	for n in range(3):
		ap.SetValue("base.kine.local."+suffix[n], values[n], '')
	
srcObj = ap.Selection(0)
trgObj = ap.PickObject ("Select parent", "Select parent")
trgObj = trgObj[2]	# tak uzyskuje sie'picked object'

#Set Ice for computing TMatrix and SRT
cpmnd_path = "G:\\Software_Settings\\xsi\\compounds\\GetSRT From 2Meshes.xsicompound"
level = 0
name = "iGetSRT"
oIce = setIce(srcObj, trgObj, level, name, cpmnd_path)

#Read SRT data from Ice
scale = getIceVector3(srcObj, '_scale')
euler = getIceVector3(srcObj, '_euler')
move = getIceVector3(srcObj, '_move')

#Apply SRT to Local Transform
setLocalTransform(['sclx','scly','sclz'], scale)
setLocalTransform(['rotx','roty','rotz'], euler)
setLocalTransform(['posx','posy','posz'], move)

ap.FreezeModeling("", "", "")

