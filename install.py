import os
import shutil
import maya.cmds as mc


def Run():
    projDir = os.path.dirname(os.path.abspath(__file__))
    mayaScriptpath = os.path.join(mc.internalVar(uad=True), "scripts")
    pluginName = os.path.split(projDir)[-1]

    pluginDestPath = os.path.join(mayaScriptpath, pluginName)

    if os.path.exists(pluginDestPath):
        shutil.rmtree(pluginDestPath)

    os.makedirs(pluginDestPath, exist_ok=True)

    srcdirName = "src"

    assetsDirName = "assets"

    shutil.copytree(os.path.join(projDir, srcdirName), os.path.join(pluginDestPath,srcdirName))
    shutil.copytree(os.path.join(projDir, assetsDirName), os.path.join(pluginDestPath,assetsDirName))

    def CreateShelfBtnForScript(scriptName):
        currentShelf = mc.tabLayout("ShelfLayout",q=True, selectTab=True)
        mc.setParent(currentShelf)
        iconImage = os.path.join(pluginDestPath,assetsDirName, scriptName + ".png")
        mc.shelfButton(c=f"from {pluginName}.src import {scriptName}; {scriptName}.Run()", image = iconImage)

    CreateShelfBtnForScript("LimbRigger")
    CreateShelfBtnForScript("TrimSheetUVBuilder")