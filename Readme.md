# md5-checksum-sync
A self managed job to verify all unchecked md5_hashes in the record table.

Script to create / reset the database and fill it with data
```
pipenv run python create-db.py
```

Script to print the current database contents
```
pipenv run python print-db.py
```
Run the checksum syncer program
```
pipenv run python main.py
```
