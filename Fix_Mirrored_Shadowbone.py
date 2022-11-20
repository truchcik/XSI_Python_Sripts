#Copy shadow null size and position to other sided
# Fixes Null_Length bugs appearing on specific skeleton types

ap = Application
sel = [str(x) for x in ap.selection]

for s in sel:
	obj = ap.dictionary.getobject(s)
	sizeX = ap.GetValue(obj.fullname + ".null.shadow_scaleX")
	posX  = ap.GetValue(obj.fullname + ".null.shadow_offsetX")
	sizeY = ap.GetValue(obj.fullname + ".null.shadow_scaleY")
	posY  = ap.GetValue(obj.fullname + ".null.shadow_offsetY")
	sizeZ = ap.GetValue(obj.fullname + ".null.shadow_scaleZ")
	posZ  = ap.GetValue(obj.fullname + ".null.shadow_offsetZ")
	
	if '_l' in s: s = s.replace('_l','_r')
	elif '_r' in s: s = s.replace('_r','_l')
	elif 'Left' in s: s = s.replace('Left','Right')
	elif 'Right' in s: s = s.replace('Right','Left')
	else: continue

	obj_mirror = ap.dictionary.getobject(s)
	ap.SetValue(obj_mirror.fullname + ".null.shadow_scaleX", sizeX)
	ap.SetValue(obj_mirror.fullname + ".null.shadow_offsetX", -posX)
	ap.SetValue(obj_mirror.fullname + ".null.shadow_scaleY", sizeY)
	ap.SetValue(obj_mirror.fullname + ".null.shadow_offsetY", -posY)
	ap.SetValue(obj_mirror.fullname + ".null.shadow_scaleZ", sizeZ)
	ap.SetValue(obj_mirror.fullname + ".null.shadow_offsetZ", -posZ)
