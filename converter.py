import json

print('Select an option:')
print('(1) Key Value Pairs')
print('(2) Single Value Array')

option = input('Enter option #: ')

# value pairs
if option == "1":
    inputs = "input.txt"
    dict1 = {}
        
    with open(inputs) as f:
        for line in f:
            first, second = line.strip().split(None, 1)
            dict1[first] = second.strip()
                
    outputs = open("output.json", "w")
    json.dump(dict1, outputs, indent = 4, sort_keys = False)
    outputs.close()  
else:
    pass

# single values
if option == "2":
    inputs = "input.txt"
    dict2 = []
        
    with open(inputs) as fh:
        for line in fh:
            data = line.strip()
            dict2.append(data)
            

    outputs = open("output.json", "w")
    json.dump(dict2, outputs, indent = 4)
    outputs.close()  