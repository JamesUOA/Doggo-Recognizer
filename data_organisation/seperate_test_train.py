import random
import pandas as pd


def split_training_and_testing(csv_path, percentage):
    df = pd.read_csv(csv_path)
    headers = list(df.columns.values)
    training_df = pd.DataFrame(columns=headers)

    plates = df.filename.nunique()
    amount = round(plates * percentage)

    for i in range(amount):
        plates = df.filename.nunique()
        random_plate = random.randint(0, plates)
        chosen_plate = df.iloc[random_plate]
        filtered = df.loc[df.filename == chosen_plate.filename]

        training_df = training_df.append(filtered)

        df = df[df.filename != chosen_plate.filename]
        df = df.reset_index(drop=True)
        if(i%1000 == 0):
            print(i/amount*100 ,"% complete")
            print("currently on", i)

    df.to_csv("doggo_testing.csv", index=None)
    training_df.to_csv("doggo_training.csv", index=None)


split_training_and_testing("data/final_data.csv", 0.9)
