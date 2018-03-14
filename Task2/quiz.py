import re
import json

test_str = """
<< Which one of these is not a programming language >>

-  c
-  English +
-  python
-  java


<< Elixir is built upon the VM of  >>


- Java
- Python
- Ruby
- Erlang +

<< Which one of these is an equation for sigmoid  >>


- 1/1+e-x +
- 1/1-e-x
- 1/e-x
- None
"""

test_str = test_str.replace("<<","question")
test_str = test_str.partition("\n\n")

question = {}
options = {}
opt = []
final_json = {}

final_json_array = []

def convert_to_json(test_str):
    # find pattern in the above test string
    # and generate data.json
    # clarify yourself properly before proceding
    # use python 3.6.4 only
    # good luck
	count = 0
	for i in test_str:
		for k , v in re.findall(r'([^\s]+)\s+(.+?)$', i, re.M):
			if(k == "question"):
				question[""+k] = v[:-2].rstrip()
				opt = []
			else:
				count += 1
				k1 = "text"
				k2 = "is_correct"
				if v[-1:] == "+":
					v = v[:-1].rstrip()
					v1 = "true"
				else:
					v1 = "false"
				options[k1] = v
				options[k2] = v1
				opt.append(options.copy())
			if(count%4 == 3):
				question["options"] = opt
				final_json_array.append(question.copy())
	final_obj = json.dumps(final_json_array,indent = 4)
	return final_obj


json_to_be_written_to_file = convert_to_json(test_str)
with open("C:\\Users\\abhia\\Desktop\\New folder\\caravel-interview\\Task2\\data1.json","w") as json_file:
	print("writing to file")
	print(json_to_be_written_to_file)
	json_file.write(json_to_be_written_to_file)

