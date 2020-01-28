import csv
import sys
import os
from datetime import datetime



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
with open('pck.txt', 'w') as pck_file:
    counter = 1
    batch_start = 500000
    batch_header = 'FBFV'
    batch_date = datetime.now().strftime("%d/%m/%y")
    batch_header_line = batch_header + str(batch_start) + batch_date + '\n'
    form_separator = 'FV' + '\n'
    survey_code = '0066' 
    pck_file.write(batch_header_line)
    for row in dictionary_list:
        if counter % 10 == 0:
            #pck_file.write(form_separator)
            batch_header_line = batch_header + str(batch_start) + batch_date + '\n'
            pck_file.write(batch_header_line)
        elif counter == 1:
            pck_file.write(form_separator)
            reference_line = survey_code + ':' + row['responder_id'] + 'F' + ':' + row['period'][2:] + '\n'
            list_of_lines = [(key, value) for key, value in row.items() if key.startswith("Q")]
            pck_file.writelines([reference_line])
            for question_tuple in list_of_lines:
                question = str(question_tuple[0][1:4]).zfill(4)
                response = str(question_tuple[1]).zfill(11)
                response_line = question + ' ' + response + '\n'
                pck_file.write(response_line)
        else:    
            pck_file.write(form_separator)
            reference_line = survey_code + ':' + row['responder_id'] + 'F' + ':' + row['period'][2:] + '\n'
            list_of_lines = [(key, value) for key, value in row.items() if key.startswith("Q")]
            pck_file.writelines([reference_line])
            for question_tuple in list_of_lines:
                question = str(question_tuple[0][1:4]).zfill(4)
                response = str(question_tuple[1]).zfill(11)
                response_line = question + ' ' + response + '\n'
                pck_file.write(response_line)
        counter += 1
        batch_start += 1