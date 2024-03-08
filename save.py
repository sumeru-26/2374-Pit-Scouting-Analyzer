import csv

# fields = ['Team Number', 'Drive Train', 'Intake Type', 'Indexing Type', '# of Notes in Auto', 'Notes about Auto', 'Endgame', 'Alliance Criteria']

def add(coded_str : str, file_name : str):
    with open(file_name, 'a') as file:
        writer = csv.writer(file)
        row = coded_str.split('^')
        writer.writerow(row)