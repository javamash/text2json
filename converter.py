import json

print('Select an option:')
print('(1) Key Value Pairs')
print('(2) Single Value Array')

option = input('Enter option #: ')

inputs = "input.txt"
outputs = open("output.json", "w")

# value pairs
if option == "1":
    
    dict1 = {}
        
    with open(inputs) as f:
        for line in f:
            first, second = line.strip().split(None, 1)
            dict1[first] = second.strip()
                
    json.dump(dict1, outputs, indent = 4)
    outputs.close()  
else:
    pass

# single values
if option == "2":
    
    dict2 = []
        
    with open(inputs) as s:
        for line in s:
            data = line.strip()
            dict2.append(data)
            
    json.dump(dict2, outputs, indent = 4)
    outputs.close()
