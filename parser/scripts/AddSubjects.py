import json

def AddSubjectNames():
    resultPath = '../result(parsedOnly).json'
    with open(resultPath, 'r') as file:
        data = json.load(file)
    
    subjectPath = 'subjects[1].json'
    with open(subjectPath, 'r') as file:
        subjects = json.load(file)
    
    for subgroup in data:
        data[subgroup] = Update(data[subgroup], subjects)

    with open(resultPath, 'w') as file:
        data = json.dump(data, file, indent=4, separators=(',', ': '))

def Update(schedule, subjects):
    for day in schedule:
        for time, details in schedule[day].items():
            subjectCode = details[0][:-1]
            type = details[0][-1]

            if subjectCode in subjects:
                details.append(subjects[subjectCode])
            
            if type == 'L':
                details.append('Lecture')
            elif type == 'T':
                details.append('Tutorial')
            elif type == 'P':
                details.append('Practical')
    return schedule


AddSubjectNames()

# import json

# File paths
# input_file = 'OldNew.json'  # Replace with your actual file path
# output_file = 'processed_data.json'
#
# # Read the old data from the JSON file
# with open(input_file, 'r') as file:
#     data = json.load(file)
#
# # Process the JSON data
# result = {}
# for category, items in data.items():
#     for key, value in items.items():
#         # Remove whitespaces
#         cleaned_key = key.replace(" ", "")
#         cleaned_value = value.replace(" ", "")
#         # Format the output
#         result[f"{cleaned_key}"] = f"{cleaned_value} / {cleaned_key}"
#
# # Write the result to a new file
# with open(output_file, 'w') as file:
#     json.dump(result, file, indent=4)
#
# print(f"Data has been processed and written to '{output_file}'")
