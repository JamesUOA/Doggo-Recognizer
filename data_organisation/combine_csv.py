import glob
import pandas as pd


def combine_csv():
    dog_df = pd.read_csv("data/n02085620-Chihuahua.csv")
    headers = list(dog_df.columns.values)
    output_df = pd.DataFrame(columns=headers)

    for file in glob.glob('data/*'):

        print(file)
        name = file.split("\\")[1]
        current_csv = pd.read_csv(file)
        output_df = output_df.append(current_csv)
        print(name)
    output_df.to_csv("data/combined.csv.csv",index=None)

    print('Successfully combined csv.')


def alter_filename():
    df = pd.read_csv("data/combined.csv")
    headers = list(df.columns.values)
    output_df = pd.DataFrame(columns=headers)

    for index, row in df.iterrows():
        row.filename = row.filename + '.jpg'
        output_df = output_df.append(row, ignore_index=True)
        print(row.filename)
    output_df.to_csv('data/final_data.csv', index=None)

alter_filename()
