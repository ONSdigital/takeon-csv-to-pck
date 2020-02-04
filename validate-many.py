import json
import requests
import csv

survey = '0066'
validation_endpoint = ''
api_key = ''
request_header = dict({"x-api-key": api_key})

with open('Example_Results_Land_Input_Data_SAS.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    # Use Python Next built in
    # Returns the next row of the reader’s iterable object as a list
    header = next(reader)
    batch_list = []
    for column in reader:
        row = ",".join(column)
        # Add elements to individual lists by Whitespace
        row_list = row.split(",")
        batch_list.append(row_list)

dictionary_list = []
for list in batch_list:
    dictionary = dict(zip(header, list))
    dictionary_list.append(dictionary)

for row in dictionary_list:
    json_data = json.dumps({"reference" : row['responder_id'],
                            "period" : row['period'],
                            "survey" : survey,
                            "bpmId" : "0"})
    response = requests.post(validation_endpoint, data=json_data, headers=request_header)
    print(response.text)
