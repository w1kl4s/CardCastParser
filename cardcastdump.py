import urllib.request
import json
import sys

def parseIdToJson(deckidlist):
	for deckid in deckidlist:
		api_url = "https://api.cardcastgame.com/v1/decks/" + deckid +  "/cards"
		try:
			with urllib.request.urlopen(api_url) as url:
				data = json.loads(url.read().decode())
		except urllib.error.HTTPError:
			print("Deck with ID \"" + deckid + "\" was not found!")
			return
		calls_data, calls, responses = [], [], []

		blank_delimiter = "%delimiter%"

		for i in data['calls']:
			calls_data.append(i['text'])
		for i in data['responses']:
			responses.append(i['text'][0])

		for x in calls_data:
			result = [blank_delimiter] * (len(x) * 2 - 1)
			result[0::2] = x
			temp = ""
			calls.append(temp.join(result))

		json_data = {'calls': calls, 'responses': responses}

		data_file = deckid + ".json"
		try:
			with open(data_file, 'w') as outputfile:
				json.dump(json_data, outputfile)
			print("Written file " + deckid + ".json!")
		except:
			print("Something went wrong!")
def help():
	print("Usage: cardcastdump.py [option] [ARG]... ")
	print("\nOptions:")
	print(" -i 		Dump decks to JSON files by ID")
	print(" -f 		Dump decks to JSON files from text file (multiple IDs in file, new id in new line)")
	print("\n\n Examples:\n cardcastdump.py -i ID1 ID2 ID3 ID4")
	print(" cardcastdump.py -f file1.txt file2.txt")

sys.argv.pop(0)
try:
	if sys.argv[0] == '-i':
		parseIdToJson(sys.argv[1:])
	elif sys.argv[0] == '-f':
		id_list = []
		for i in sys.argv[1:]:
			with open(i, 'r') as input:
				for line in input:
					id_list.append(line.replace('\n',''))
		parseIdToJson(id_list)
	else:
		help()
except:
	help()



	