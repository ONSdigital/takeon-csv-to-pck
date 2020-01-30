import csv
import sys
import os
from datetime import datetime

counter = 50
batch_max = 50
batch_start = 500000
batch_header = 'FBFV'
checkletter = 'F'
batch_date = datetime.now().strftime("%d/%m/%y")
batch_header_line = batch_header + str(batch_start) + batch_date + '\n'
form_separator = 'FV' + '\n'
survey_number = '0066'
survey_code = 'QSL'

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
    # Write new file, create new batch header
    if counter % batch_max == 0:
        batch_start += 1
        pck_file = open("store" + 'QSL' + str(counter), "w")
        batch_header_line = batch_header + str(batch_start) + batch_date + '\n'
        pck_file.write(batch_header_line)
    else:    
        pck_file.write(form_separator)
        reference_line = survey_number + ':' + row['responder_id'] + checkletter + ':' + row['period'][2:] + '\n'
        list_of_question_values = [(key, value) for key, value in row.items() if key.startswith("Q")]
        list_of_question_values.append(('Q0146','0'))
        list_of_question_values.append(('Q0147','0'))
        pck_file.writelines([reference_line])
        for question_tuple in list_of_question_values:
            if len(str(question_tuple[0])) == 5:
                question = str(question_tuple[0][1:5])
            else:
                question = str(question_tuple[0][1:4]).zfill(4)
            response = str(question_tuple[1]).zfill(11)
            response_line = question + ' ' + response + '\n'
            pck_file.write(response_line)
    counter += 1

pck_file.close()