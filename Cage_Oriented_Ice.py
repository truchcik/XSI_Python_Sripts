#sets Ice CageOri on selection clone
#picks source and target cages

#CageOri is fast wrap deformer taking both translations of vertieces and rotations of cage triangles into consideration

ap = Application
compound=r'G:\Software_Settings\xsi\compounds\dm_CP_Cloth_Prototype\Cage_Oriented.xsicompound'

obj_src = ap.selection[0]
obj_trg = ap.Clone(obj_src, '', 1, 1, 0, 0, 1, 0, 1, '', '', '', '', '', '', '', '', '', '')[0]

newname = obj_src.name
if newname[-3:].lower()=='src':	newname = newname[:-3] + 'TRG'
obj_trg.name=newname

cage_src = ap.PickObject ('Get source cage', 'Get source cage','' , '')[2]
cage_trg = ap.PickObject ('Get target cage', 'Get target cage','' , '')[2]

oIce=ap.ApplyOp ('ICETree',obj_trg, 'siNode','' ,'' , 1)
oIce(0).name = "iCageOri"
nCageOri = ap.AddICECompoundNode(compound, oIce(0))

ap.ConnectICENodes (oIce(0).fullname+".port1", nCageOri.fullname+".Execute")
ap.SetValue( nCageOri.fullname+".Cage_SRC", cage_src.fullname)
ap.SetValue( nCageOri.fullname+".Cage_TRG", cage_trg.fullname)
ap.SetValue( nCageOri.fullname+".Model_SRC", obj_src.fullname)


ap.inspectObj(nCageOri)
