# takeon-csv-to-pck
Scripts to convert csv file provided by Results team into the PCK format, ready for ingestion and validation

## Scripts & steps
### To be run in order
1. convert-to-pck.py: [input: csv file] [output: storeINQ file]
 `python3 convert-to-pck.py`
2. sql-insert-csv.py: [input: csv file] [output: SQL Insert statement to be run in PGAdmin]
`python3 sql-insert-csv.py`
3. Put Store file(s) produced from first step into takeon-ingestion-landing-zone-bucket which will trigger data ingestion pipeline
4. Wait for outputs in takeon-ingestion-ingest-zone-bucket
5. Execute takeon-combine-json-ingest lambda function which will ingest the data into the Postgres Database
6. If needed - `python3 validate-many.py` to validate all references once ingested

