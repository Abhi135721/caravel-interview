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

question = {}	#dict to store each question 
options = {}	#to store options for each question
opt = []	# to store options in a list

final_json_array = []	#each question dict is pushed to the list

def convert_to_json(test_str):
    # find pattern in the above test string
    # and generate data.json
    # clarify yourself properly before proceding
    # use python 3.6.4 only
    # good luck
	count = 0	#to count for every 4 options to push to options dict
	for i in test_str:
		#regular expression to evaluate every string
		for k , v in re.findall(r'([^\s]+)\s+(.+?)$', i, re.M):
			#if key is 'question' add question to value
			if(k == "question"):
				question[""+k] = v[:-2].rstrip()
				opt = []
			#if key is option add that to options dict then to opt array
			else:
				count += 1
				k1 = "text"
				k2 = "is_correct"
				#to check if the option is true or not
				if v[-1:] == "+":
					v = v[:-1].rstrip()
					v1 = "true"
				else:
					v1 = "false"
				options[k1] = v
				options[k2] = v1
				opt.append(options.copy())
			#for every four options there is a question push opt to question dict
			if(count%4 == 3):
				question["options"] = opt
				final_json_array.append(question.copy())
	final_obj = json.dumps(final_json_array,indent = 4)
	return final_obj

#to write to a data1.json file in some location : specify path to save json file
json_to_be_written_to_file = convert_to_json(test_str)
with open("C:\\Users\\abhia\\Desktop\\New folder\\caravel-interview\\Task2\\data1.json","w") as json_file:
	print("writing to file")
	print(json_to_be_written_to_file)
	json_file.write(json_to_be_written_to_file)

