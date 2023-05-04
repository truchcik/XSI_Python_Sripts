set oRoot = Application.ActiveProject.ActiveScene.Root
'wczytuje deformery i wagi z customproperty "Deformerki" i "envki"
dim aDef	'tablica 1d deformerow
dim aEnv	'tablica 2d wag


for x=0 to selection.count-1
	set oObj=Selection(x)
	oModel = ""
	if oObj.Parent <> oRoot then oModel = oObj.Parent
	logmessage "oModel = " & oModel

	set oDefki= oObj.localproperties("Deformerki")
	set oEnvki= oObj.localproperties("envki")
	if typename(oDefki)<>"Nothing" then
		time_in=timer
		redim aDef(oDefki.parameters.count-1)

		'dane z customproperty na tablice "aDef"
		for a= 0 to oDefki.parameters.count-1
			aDef(a)=oDefki.parameters(a).value
		next
		
			'check if skeleton is hidden in model
			Set kids = oRoot.FindChildren(aDef(0))
			If kids.count>0 then
				sFind= kids(0).fullname
				'if mesh in not in model try to choose bones not in model too (under Scene_Root)
				if mModel = "" then
					for k = 0 to kids.count-1
						if InStr(".",kids(k))=0 then sFind = kids(k)
					Next
				End If
				
				'if mesh is in model, try to choose bones in the same model
				if oModel<>"" then
					logmessage "Model = " & oModel
					for k = 0 to kids.count-1
						if InStr(oModel,kids(k))>0 Then sFind = kids(k)
					Next
				End If
				
				if aDef(0)<>sFind then
					sPrzed= replace(sFind, aDef(0),"")
					for n=0 to ubound(aDef)-1
						aDef(n)=sPrzed+aDef(n)
						logmessage aDef(n)
					next
				End If	
			End If
			'***************************************

		
		logmessage "defki: " & round(timer-time_in,3)
		time_in=timer

		'dane z grida na tablice 2d "aEnv)
		set oGrid=oEnvki.parameters(0).value
		aEnv=oGrid.Data
		logmessage "envki: " & round(timer-time_in,3)

		if oObj.envelopes.count>0 then RemoveFlexEnv oObj

		'nadaj deformery

		sString=oObj.fullname + ";"
		for a=0 to ubound(aDef)
		sString= sString+aDef(a)+","

		next
		logmessage sString
		ApplyFlexEnv sString, , 2

		set oEnv=oObj.envelopes(0)
		oEnv.Weights.Array=aEnv
	End If
next 
