# DragDropFBXImport.py
#
# Drag & drop .fbx into viewport => runs FBXImport on the dropped file.

import win32com.client
from win32com.client import constants as c
import re

# ----------------------------------------------------------------------
# Plugin registration
# ----------------------------------------------------------------------
def XSILoadPlugin(in_reg):
    in_reg.Author = "YourName"
    in_reg.Name = "DragDropFBXImport"
    # Register the global drag-and-drop event
    in_reg.RegisterEvent("siOnDragAndDropEvent", c.siOnDragAndDrop)
    return 1

def XSIUnloadPlugin(in_reg):
    return 1

# ----------------------------------------------------------------------
# Drag & Drop handler
# ----------------------------------------------------------------------
def siOnDragAndDropEvent_OnEvent(in_ctxt):
    """
    Softimage calls this whenever something is dragged/dropped over the scene.
    We only allow dropping if it's an .fbx file, and on drop we call FBXImport.
    """
    app = Application

    action = in_ctxt.GetAttribute("DragAndDropAction")
    src    = in_ctxt.GetAttribute("DragSource")  # usually full file path

    if not src:
        return 1

    # Normalize path and check extension
    is_fbx = re.search(r"\.fbx$", src, re.IGNORECASE) is not None

    if action == c.siSourceDragAction:
        # While dragging: tell Softimage whether this thing *can* be dropped
        in_ctxt.SetAttribute("DragSourceSupported", 1 if is_fbx else 0)

    else:  # c.siSourceDropAction
        if is_fbx:
            app.LogMessage("DragDropFBXImport: importing FBX from [%s]" % src)

            # --- simplest possible import ---
            # If you want to control import options, configure FBXImportMode /
            # ImportFBXOptions separately, then call FBXImport.
            try:
                app.FBXImport(src)
            except Exception as e:
                app.LogMessage("DragDropFBXImport: FBXImport failed: %s" % e, c.siError)

    return 1
