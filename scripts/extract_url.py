from sys import argv
import json

# extract_url.py [SOURCE] [BEGIN_ID] [END_ID]
# extracts url from "imagePath" and outputs to image_paths.txt

OUTPUT = "image_paths.txt"
SOURCE = argv[1]
BEGIN_ID = int(argv[2])
END_ID = int(argv[3])

# load source
nodesJson = open(SOURCE, 'r')
nodesList = json.load(nodesJson)
nodesJson.close()

urlList = []

for node in nodesList:
	nodeId = node["id"]
	if (nodeId >= BEGIN_ID and nodeId <= END_ID):
		urlList.append(node["imagePath"])
		

outFile = open(OUTPUT, 'w')
for u in urlList:
	outFile.write(u + "\n")
	
outFile.close()
