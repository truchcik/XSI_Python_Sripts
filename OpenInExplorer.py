#opens location of current scene in windows explorer

ap = Application
import subprocess

#print ap.ActiveProject.Path
print ap.ActiveProject.ActiveScene.Parameters("Filename").Value

cmd = '''explorer /select,"'''+ap.ActiveProject.ActiveScene.Parameters("Filename").Value+'''"'''
subprocess.Popen(cmd)
