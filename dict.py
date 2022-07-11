import json
import sys




def open_dict():
	global data
	with open("dictionary.json") as f:
		data = json.load(f)



def use_dict():
	open_dict()
	print("=========================================================================================")
	print("*********************welcome to python dictionary by aalekh*********************")
	print("=========================================================================================")
	if len(sys.argv) < 2:
		print("use it like this : python dict.py [word_to_search]")

	else:
		try:
			ans = data[sys.argv[1]]
			print(ans)
		
		except KeyError:
			print("Information isn't available")




use_dict()