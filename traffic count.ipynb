import pandas as pd
from google.colab import files

uploaded = files.upload() #upload 'filtered_yesterday' and 'filtered_today' separately

file_name = next(iter(uploaded))
df = pd.read_csv(file_name)

def map_terminal_to_code(terminal):
    if terminal in ['P01', 'P02']:
        return 'T1'
    elif terminal == 'P03':
        return 'T2'
    elif terminal in ['C01', 'C02']:
        return 'CGO'
    else:
        return 'Unknown'

df['Terminal Code'] = df['dep_arr_tmnl_cd'].apply(map_terminal_to_code)
terminal_counts = df.groupby('Terminal Code').size().reset_index(name='Count')

total_flights = terminal_counts['Count'].sum()
total_row = pd.DataFrame([{'Terminal Code': 'Total', 'Count': total_flights}])
terminal_counts = pd.concat([terminal_counts, total_row], ignore_index=True)

print(terminal_counts)
