# DragDropImport.py
#
# Drag & drop .fbx or .obj into viewport => imports the dropped file.

import re
from win32com.client import constants as c

# ----------------------------------------------------------------------
# Plugin registration
# ----------------------------------------------------------------------
def XSILoadPlugin(in_reg):
    in_reg.Author = "Truchcik"
    in_reg.Name = "DragDropImport"
    in_reg.RegisterEvent("siOnDragAndDropEvent", c.siOnDragAndDrop)
    return 1

def XSIUnloadPlugin(in_reg):
    return 1

# ----------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------
def _normalize_src(src):
    # Softimage typically gives a single full path string.
    # Some setups/tools might provide multiple paths separated by | or ; or newlines.
    if not src:
        return []
    s = str(src).strip()

    # Split on common separators if it looks like multiple files
    parts = re.split(r"[|\n\r;]+", s)
    parts = [p.strip() for p in parts if p.strip()]
    return parts

def _ext(path):
    m = re.search(r"\.([A-Za-z0-9]+)$", path)
    return m.group(1).lower() if m else ""

# ----------------------------------------------------------------------
# Drag & Drop handler
# ----------------------------------------------------------------------
def siOnDragAndDropEvent_OnEvent(in_ctxt):
    """
    - FBX => Application.FBXImport(path)
    - OBJ => Application.ObjImport(path, Group, hrc, Material, UV, UserNormal, UVwrapping)
    """
    app = Application

    action = in_ctxt.GetAttribute("DragAndDropAction")
    src    = in_ctxt.GetAttribute("DragSource")

    paths = _normalize_src(src)
    if not paths:
        return 1

    # Supported filetypes
    supported_exts = {"fbx", "obj"}
    is_supported = any(_ext(p) in supported_exts for p in paths)

    if action == c.siSourceDragAction:
        in_ctxt.SetAttribute("DragSourceSupported", 1 if is_supported else 0)
        return 1

    # Drop action
    for path in paths:
        e = _ext(path)
        if e == "fbx":
            app.LogMessage("DragDropFBXImport: importing FBX from [%s]" % path)
            try:
                app.FBXImport(path)
            except Exception as ex:
                app.LogMessage("DragDropFBXImport: FBXImport failed: %s" % ex, c.siError)

        elif e == "obj":
            app.LogMessage("DragDropFBXImport: importing OBJ from [%s]" % path)
            try:
                group_name   = ""   # empty => no group, or set e.g. "Imported_OBJ"
                import_hrc   = 1    # import hierarchy
                import_mtl   = 1    # import materials
                import_uv    = 1    # import UVs
                use_normals  = 1    # import user normals
                uv_wrapping  = 0    # keep default wrapping behavior
                app.ObjImport(path, group_name, import_hrc, import_mtl, import_uv, use_normals, uv_wrapping)
            except Exception as ex:
                app.LogMessage("DragDropFBXImport: ObjImport failed: %s" % ex, c.siError)

    return 1
