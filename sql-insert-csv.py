import csv
import sys
import os
from datetime import datetime

survey = '0066'
form_id = 1
status = 'Form Sent Out'
esc = "\'"

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

insert_statement = """Insert Into dev01.Contributor
(
    Reference                  ,
    Period                     ,
    Survey                     ,
    FormID                     ,
    Status                     ,
    ReceiptDate                ,
    FormType                   ,
    Checkletter                ,
    FrozenSicOutdated          ,
    RuSicOutdated              ,
    FrozenSic                  ,
    RuSic                      ,
    FrozenEmployees            ,
    Employees                  ,
    FrozenEmployment           ,
    Employment                 ,
    FrozenFteEmployment        ,
    FteEmployment              ,
    FrozenTurnover             ,
    Turnover                   ,
    EnterpriseReference        ,
    WowEnterpriseReference     ,
    CellNumber                 ,
    Currency                   ,
    VatReference               ,
    PayeReference              ,
    CompanyRegistrationNumber  ,
    NumberLiveLocalUnits       ,
    NumberLiveVat              ,
    NumberLivePaye             ,
    LegalStatus                ,
    ReportingUnitMarker        ,
    Region                     ,
    BirthDate                  ,
    EnterpriseName             ,
    ReferenceName              ,
    ReferenceAddress           ,
    ReferencePostcode          ,
    TradingStyle               ,
    Contact                    ,
    Telephone                  ,
    Fax                        ,
    SelectionType              ,
    InclusionExclusion         ,
    CreatedBy                  ,
    CreatedDate                ,
	LastUpdatedBy              ,
    LastUpdatedDate  
) VALUES """
insert_row = ''

for row in dictionary_list:
    insert_row += '(' + esc + row['responder_id'] + esc + ',' + esc + row['period'] + esc 
    insert_row += ',' + esc + survey + esc + ',' + str(form_id) + ',' + esc + status + esc + ',' + 'now()'
    insert_row += ',' + esc + '0004' + esc + ',' + esc + 'T' + esc + ',' + esc + '70110' + esc + ',' + esc + '70110' + esc + ',' + esc + '41100' + esc
    insert_row += ',' + esc + '41100' + esc + ',' + str(750) + ',' + str(748) + ',' + str(100) + ',' + str(100) + ',' + str(100) + ',' + str(100) + ',' + str(99999)
    insert_row += ',' + str(99999) + ',' + esc + row['enterprise_ref'] + esc + ',' + esc + '2906948169' + esc + ',' + str(1) + ',' + esc + 'S' + esc 
    insert_row += ',' + esc + '326935020502' + esc + ',' + esc + '2135632144542' + esc
    insert_row += ',' + esc + '97395797' + esc + ',' + str(178) + ',' + str(0) + ',' + str(0) + ',' + esc + '1' + esc + ',' + esc + 'E' + esc 
    insert_row += ',' + esc + row['gor_code'] + esc + ',' + esc + '06/06/1975' + esc
    insert_row += ',' + esc + row['enterprise_name'] + esc + ',' + esc + row['enterprise_name'] + esc + ',' + esc + '9 Brenda falls,East Harry, Wales' + esc 
    insert_row += ',' + esc + 'L2T 0PR' + esc + ',' + esc + 'Sole Trader' + esc + ',' + esc + 'Heather Griffiths' + esc
    insert_row += ',' + esc + '01633 5551234' + esc + ',' + esc + '54321' + esc + ',' + esc + 'P' + esc + ',' + esc + ' ' + esc
    insert_row += ',' + esc + 'fisdba' + esc + ',' + 'now()' + ',' + esc + 'fisdba' + esc + ',' + 'now()' + '),' + '\n'
    
sql_file = open('insert-into-contributor.sql', 'w')
sql_file.writelines([insert_statement, insert_row[:-2], ';'])
