import os
from shutil import copyfile
import sys


def copyFile(filename, newName):
    result = None
    try:
        copyfile(filename, newName)
        result = True
    except:
        result = False
    finally:
        return result


def getIputsFiles(path):
    def mtime(f): return os.stat(os.path.join(path, f)).st_mtime
    return list(sorted(os.listdir(path), key=mtime))


def getModulesFolder(path):
    fList = []
    for f in os.listdir(path):
        fullPath = os.path.join(path, f)
        if(os.path.isdir(fullPath)):
            fList.append(os.path.join(fullPath, "joystick"))

    return fList


def getNewConfigName(lastConfigFile, newId):
    auxStr1 = lastConfigFile[:lastConfigFile.find('{')]
    auxStr2 = lastConfigFile[lastConfigFile.find('}')+1:]
    return auxStr1+newId+auxStr2


def checkNewIdInConfigs(newId, configList):
    result = False
    for config in configList:
        if(newId in config):
            result = True
            break
    return result


mainPath = str(sys.argv[1])+"\\Config\\Input"
newHWId = "{"+str(sys.argv[2]+"}")
modules = getModulesFolder(mainPath)

for m in modules:
    inputsList = getIputsFiles(m)
    if(len(inputsList) == 0 or checkNewIdInConfigs(newHWId, inputsList)):
        continue

    lastConfig = inputsList[len(inputsList)-1]
    lastConfigPath = os.path.join(m, lastConfig)
    newConfig = getNewConfigName(lastConfig, newHWId)
    newConfigPath = os.path.join(m, newConfig)

    print("Pegando a ultima configuração "+lastConfig)

    copyFile(lastConfigPath, newConfigPath)
    print("Copiando " + lastConfigPath)
    print("Para " + newConfigPath)

print("Pronto!")
