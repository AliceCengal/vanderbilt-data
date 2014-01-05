from sys import argv
import json

# id_fixer.py [SOURCE] [ID_START] [ID_END]
# When deleting or adding objects in the middle of a large
# dataset, use this script to realign their id to be sequestial
# The result will be stored in [SOURCE]_fixed.json

# init
SOURCE = argv[1]
ID_START = int(argv[2])
ID_END = int(argv[3])

# open SOURCE
sourceJson = open(SOURCE, 'r')
sourceList = json.load(sourceJson)
sourceJson.close()

# init new data list
jsonId = len(sourceList)
newDataList = []

for dataObject in sourceList:
    if (dataObject["id"] >= ID_START and dataObject["id"] <= ID_END):
        dataObject["id"] = jsonId
        jsonId = jsonId - 1
        
    newDataList.append(dataObject)

# save
fixedJson = open(SOURCE + "_fixed.json", 'w')
json.dump(newDataList, fixedJson, False, True, True, True, None, 2)
