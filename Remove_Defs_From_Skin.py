#Remove deformer bones from skin on selected mesh
#Need fix for cases if one of parent bones is not in skinning
#Example E:\000W4\02_BodyTypes\scenes\W3\Wa_Base wa_W3_Full_Skel|body_01_wa_full__missing_main_bones
#
# -easy-  catch error and remove this bone children from def_skel
# -proper- add this bone to skinning on the beggining of script

import sys

def sel_2_list():
	sel = [str(x.name) for x in ap.selection]
	return sel

def get_children(name):
	deformer_children =  []
	obj = ap.Dictionary.GetObject(name)
	for x in obj.FindChildren2('','','',False):
		if str(x.name) in def_skel:
			deformer_children.append(str(x.name))
	return deformer_children

def apply_new_weights_2():
	myEnv = None
	for clust in oObj.ActivePrimitive.Geometry.Clusters:
		if 'cls.envelop' in clust.fullname.lower():
			for myEnv in clust.properties:
				if myEnv.type == 'envweights':break

	error = False
	for pInd in range(len(oObj.ActivePrimitive.Geometry.Points)):
		pRef = str(oObj.name)+'.pnt[' + str(pInd) + ']'	#point reference, f.ex cube.pnt[12]"
		for bone in oDef:
			bInd = oDef.index(bone)
			try:
				oWeight = oWts[pInd][bInd]
				nWeight = nWts[pInd][bInd]
				if nWeight != oWeight:
					#print 'Diff weight. Pnt['+str(pInd)+'],', bone,', delta=', nWeight - oWeight
					ap.SIModifyFlexEnvWght(myEnv, bone, pRef, 0, nWeight, "") 
			except Exception as e:
				print 'pnt:',pInd,'bone:', bone, 'boneID:', bInd, 'pntRef:', pRef, nWeight, oWeight
				print 'ap.SIModifyFlexEnvWght(',myEnv, bone, pRef, 0, nWeight, '''"")'''
				print e
				error = True
				break
			if error: break
		if error: break
	print 'Done'

ap = Application
main_skel = ['pelvis', 'l_thigh', 'l_shin', 'l_foot', 'l_toe', 'r_thigh', 'r_shin', 'r_foot', 'r_toe', 'torso', 'torso2', 'torso3', 'neck', 'head', 'l_shoulder', 'l_bicep', 'l_forearm', 'l_hand', 'l_thumb1', 'l_thumb2', 'l_thumb3', 'l_index1', 'l_index2', 'l_index3', 'l_middle1', 'l_middle2', 'l_middle3', 'l_ring1', 'l_ring2', 'l_ring3', 'l_pinky1', 'l_pinky2', 'l_pinky3', 'r_shoulder', 'r_bicep', 'r_forearm', 'r_hand', 'r_thumb1', 'r_thumb2', 'r_thumb3', 'r_index1', 'r_index2', 'r_index3', 'r_middle1', 'r_middle2', 'r_middle3', 'r_ring1', 'r_ring2', 'r_ring3', 'r_pinky1', 'r_pinky2', 'r_pinky3', 'l_pinky0', 'r_pinky0']
def_skel = ['l_kneeRoll', 'l_legRoll2', 'r_kneeRoll', 'r_legRoll2', 'hroll', 'l_index_knuckleRoll', 'l_middle_knuckleRoll', 'l_ring_knuckleRoll', 'l_pinky_knuckleRoll', 'l_thumb_roll', 'l_weapon', 'l_elbowRoll', 'l_forearmRoll1', 'l_forearmRoll2', 'l_handRoll', 'l_bicep2', 'l_shoulderRoll', 'r_index_knuckleRoll', 'r_middle_knuckleRoll', 'r_ring_knuckleRoll', 'r_pinky_knuckleRoll', 'r_thumb_roll', 'r_weapon', 'r_elbowRoll', 'r_forearmRoll1', 'r_forearmRoll2', 'r_handRoll', 'r_bicep2', 'r_shoulderRoll', 'l_boob', 'r_boob', 'r_legRoll', 'l_legRoll', 'Hips_AUX']
main_skel_ind, def_skel_ind = [],[]
temp_skin = (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 18.218652725219727, 81.781349182128906, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

oObj = ap.Selection[0]
oEnv = oObj.Envelopes[0]
oDef = [str(x.name) for x in oEnv.deformers]
oWts = oEnv.weights

for bone in main_skel:
	try: main_skel_ind.append(oDef.index(bone))
	except: pass
for bone in def_skel:
	try: def_skel_ind.append(oDef.index(bone))
	except: pass

skel_dic = {}
for n in def_skel_ind:
	oBone = ap.Dictionary.GetObject(oDef[n])
	while True:
		oParent = oBone.Parent()
		if str(oParent) in main_skel: break
		oBone = ap.Dictionary.GetObject(oParent)
	try: skel_dic[n] = oDef.index(oParent)
	except:
		print 'Error', oParent, n, oDef.index(oParent)
		sys.exit()

nWts = [] #New weights
for k,vEnv in enumerate([x for x in oWts]):
	#print 'Original', round(sum(vEnv)), vEnv
	vEnv = [x for x in vEnv]
	for idBone in def_skel_ind:
		if vEnv[idBone]>0.0:
			idParent = skel_dic[idBone]
			#print '    ',oDef[idBone], idBone, vEnv[idBone], oDef[idParent], idParent, vEnv[idParent]
			vEnv[idParent]+=vEnv[idBone]
			vEnv[idBone] = 0.0
	vEnv = tuple(vEnv)
	nWts.append(vEnv)
	
if oWts!=nWts:
	apply_new_weights_2()
	print 'Applying new weights'
else: print ('No changes')

def remove_def_from_deformers():
	for bone in def_skel:
		command = oObj.name+';'+bone
		print command
		Application.RemoveFlexEnvDeformer(command, "")	

remove_def_from_deformers()
print 'removed deformers'
