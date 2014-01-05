from sys import argv
import json

# add_status.py [SOURCE] [STATUS] [BEGIN_ID] [END_ID]
# outputs to SOURCE_modified.json

SOURCE = argv[1] 
STATUS = argv[2] 
BEGIN_ID = int(argv[3])
END_ID = int(argv[4])

OUTPUT_FIX = "_modified.json"

# load source
nodesJson = open(SOURCE, 'r')
nodesList = json.load(nodesJson)
nodesJson.close()

for nn in nodesList:
	nnId = nn["id"]
	if (nnId >= BEGIN_ID and nnId <= END_ID):
		nn["tags"].append("status_" + STATUS)

outFile = open(SOURCE + OUTPUT_FIX, 'w')
json.dump(nodesList, outFile, False, True, True, True, None, 3)
outFile.close()



