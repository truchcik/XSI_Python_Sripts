#Set Garment Stream generator

ap = Application

IceCompound = "G:\\Software_Settings\\xsi\\compounds\\dm_CP_Cloth_Prototype\\GS_Generator.xsicompound"
IceName = 'GS_gen'
IceLevel = 1
IceOut = '.Execute'
IceIn = '.port1'

for obj in ap.selection:
	oIce=ap.ApplyOp ('ICETree',obj, 'siNode','' ,'' , IceLevel)
	oIce(0).name = IceName
	MyNode = ap.AddICECompoundNode(IceCompound, oIce(0))

	ap.ConnectICENodes (oIce(0).fullname+".port1", MyNode.fullname+".Execute")
	ap.inspectObj(MyNode)
