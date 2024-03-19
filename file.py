import csv
import pandas as pd

fields = ['Drive Train', 'Intake', 'Shooter', 'Climber', 'Team Number', 'Auto Notes #', 'Notes About Auto', 'What They Want On Alliance', 'Other Notes']
ordered_fields = ['Team Number', 'Drive Train', 'Intake', 'Shooter', 'Climber', 'Auto Notes #', 'Notes About Auto', 'What They Want On Alliance', 'Other Notes']

filters = {
    'drivetrain' : {
        1 : 'swerve',
        2 : 'tank',
        3 : 'mecanum',
        4 : 'other'
    },
    'intake' : {
        1 : 'otb',
        2 : 'utb',
        3 : 'both' 
    },
    'shooting' : {
        1 : 'amp',
        2 : 'speaker',
        3 : 'both',
        4 : 'none'
    },
    'climb' : {
        1 : 'trap',
        2 : 'climb',
        3 : 'none'
    }
}

def add(coded_str : str, file_name : str):
    with open(file_name, 'a') as file:
        writer = csv.writer(file)
        row = decode_str(coded_str)
        writer.writerow(row)

def read(file_name : str):
    df = pd.read_csv(file_name)
    return df[ordered_fields]

def update(df : pd.DataFrame, file_name : str):
    df.to_csv(file_name)

def decode_str(str : str) -> list[str]:
    str = str.lower()
    re = str.split('$')
    radios = list(re[0])
    del re[0]
    radios[0] = filters['drivetrain'][int(radios[0])]
    radios[1] = filters['intake'][int(radios[1])]
    radios[2] = filters['shooting'][int(radios[2])]
    radios[3] = filters['climb'][int(radios[3])]
    return radios + re

# NOTE: WILL DELETE ALL SAVED DATA
def rewrite_header(fields : list[str], file_name : str):
    with open(file_name, 'w') as file:
        pass
    with open(file_name, 'a') as file:
        csv.writer(file).writerow(fields)