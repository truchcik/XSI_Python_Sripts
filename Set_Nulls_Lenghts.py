#Set length of nulls to fit ther children
#Works only on selected bones 
#ignoring other bones make this better solution than previous ones
#have function building  skeleton hierarchy as dictionary

import sys

ap = Application

def sel_2_list():
	sel_list =  []
	for x in ap.selection:
		sel_list.append(str(x.fullname))		
	return sel_list

def listRelatives(parent): #(name)
	children = []	
	parent = ap.dictionary.GetObject(parent)
	
	for x in parent.children:
		if x.fullname in main_bone_list:
			children.append(str(x.fullname))
	return children

def saveHierarchy(obj):
	def hierarchyTree(parent, tree): #(name, dictionary)
		#print 'Parent =', parent	
		children = listRelatives(parent)
		
		if children:
			#print '\tChildren =',children
			tree[parent] = (children, {})
			for child in children:
				child = ap.dictionary.GetObject(child)			
				hierarchyTree(child.fullname, tree[parent][1]) 				 
	oTree = {}	
	hierarchyTree(obj.fullname, oTree)
	return oTree

		
#main_bone_list = ['Hips', 'Spine', 'Spine1', 'Spine2', 'Spine3', 'LeftShoulder', 'LeftArm', 'LeftForeArm', 'LeftHand', 'LeftInHandThumb', 'LeftHandThumb1', 'LeftHandThumb2', 'LeftInHandIndex', 'LeftHandIndex1', 'LeftHandIndex2', 'LeftHandIndex3', 'LeftInHandMiddle', 'LeftHandMiddle1', 'LeftHandMiddle2', 'LeftHandMiddle3', 'LeftInHandRing', 'LeftHandRing1', 'LeftHandRing2', 'LeftHandRing3', 'LeftInHandPinky', 'LeftHandPinky1', 'LeftHandPinky2', 'LeftHandPinky3', 'RightShoulder', 'RightArm', 'RightForeArm', 'RightHand', 'RightInHandThumb', 'RightHandThumb1', 'RightHandThumb2', 'RightInHandIndex', 'RightHandIndex1', 'RightHandIndex2', 'RightHandIndex3', 'RightInHandMiddle', 'RightHandMiddle1', 'RightHandMiddle2', 'RightHandMiddle3', 'RightInHandRing', 'RightHandRing1', 'RightHandRing2', 'RightHandRing3', 'RightInHandPinky', 'RightHandPinky1', 'RightHandPinky2', 'RightHandPinky3', 'Neck', 'Neck1', 'Head', 'LeftUpLeg', 'LeftLeg', 'LeftFoot', 'LeftToeBase', 'RightUpLeg', 'RightLeg', 'RightFoot', 'RightToeBase']
main_bone_list = sel_2_list()	
hips = ap.dictionary.GetObject('Hips')
oTree = saveHierarchy(hips)

def set_length(tree):
	#odtwarzam hierarchie z drzewa tree
	for parent, data in tree.iteritems():
		children, child_tree = data
		print parent, children[0]
		child = ap.Dictionary.GetObject(children[0])
		ap.SetValue(parent+'.null.primary_icon', 0, '')
		ap.SetValue(parent+'.null.shadow_icon', 4, '')	
		length = child.posx.value
		if len(children)>0:
			ap.SetValue(parent+'.null.shadow_scaleX', abs(length), '')
			ap.SetValue(parent+'.null.shadow_offsetX', length/2	, '')
			#SetValue selection(n).fullname & ".null.shadow_offsetX", length/2	
		try: set_length(child_tree)
		except: pass
		
set_length(oTree)
