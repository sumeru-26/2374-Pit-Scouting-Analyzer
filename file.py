import csv
import pandas as pd

fields = ['Drive Train', 'Intake', 'Shooter', 'Climber', 'Team Number', 'Auto Notes #', 'Notes About Auto', 'What They Want On Alliance', 'Other Notes'] 

def add(coded_str : str, file_name : str):
    with open(file_name, 'a') as file:
        writer = csv.writer(file)
        row = decode_str(coded_str)
        writer.writerow(row)

def read(file_name : str):
    return pd.read_csv(file_name)

def update(df : pd.DataFrame, file_name : str):
    df.to_csv(file_name)

def decode_str(str : str) -> list[str]:
    str = str.lower()
    re = str.split('$')
    radios = list(re[0])
    del re[0]
    return radios + re

# NOTE: WILL DELETE ALL SAVED DATA
def rewrite_header(fields : list[str], file_name : str):
    with open(file_name, 'w') as file:
        pass
    with open(file_name, 'a') as file:
        csv.writer(file).writerow(fields)

test = '1133$2374$4$VERY CONSISTENT ON BOTH SIDES$A FAST SPEAKER BOT$SINGLE ARM MECHANISM, FAST AMP CYCLES, AUTO SHOOTING'
add(test,'backup.csv')    