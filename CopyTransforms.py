#Copy local transforms and  shadow parameters
#Select source bone, run script, select target bone when asked for

ap = Application
src = ap.selection(0)

posX = src.posx.value
posY = src.posy.value
posZ = src.posz.value
rotX = src.rotx.value
rotY = src.roty.value
rotZ = src.rotz.value

shad_sizeX = ap.GetValue(src.fullname + ".null.shadow_scaleX")
shad_posX  = ap.GetValue(src.fullname + ".null.shadow_offsetX")
shad_sizeY = ap.GetValue(src.fullname + ".null.shadow_scaleY")
shad_posY  = ap.GetValue(src.fullname + ".null.shadow_offsetY")
shad_sizeZ = ap.GetValue(src.fullname + ".null.shadow_scaleZ")
shad_posZ  = ap.GetValue(src.fullname + ".null.shadow_offsetZ")

trg=ap.PickObject ("Select parent", "Select parent")
trg = trg[2]

LP=trg.Kinematics.Local.Parameters
ap.SetValue(trg.fullname + '.kine.local.posx', posX)
ap.SetValue(trg.fullname + '.kine.local.posy', posY)
ap.SetValue(trg.fullname + '.kine.local.posz', posZ)
ap.SetValue(trg.fullname + '.kine.local.rotx', rotX)
ap.SetValue(trg.fullname + '.kine.local.roty', rotY)
ap.SetValue(trg.fullname + '.kine.local.rotz', rotZ)

ap.SetValue(trg.fullname + ".null.shadow_scaleX", shad_sizeX)
ap.SetValue(trg.fullname + ".null.shadow_offsetX", shad_posX)
ap.SetValue(trg.fullname + ".null.shadow_scaleY", shad_sizeY)
ap.SetValue(trg.fullname + ".null.shadow_offsetY", shad_posY)
ap.SetValue(trg.fullname + ".null.shadow_scaleZ", shad_sizeZ)
ap.SetValue(trg.fullname + ".null.shadow_offsetZ", shad_posZ)


