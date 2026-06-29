import pandas as pd
# df = pd.read_csv("data/student_dataset_v2.csv")

def clean_data(df):
    #MODULE 3: DATA CLEANING
    df = df.drop_duplicates()
    df['StudyHours'] = df['StudyHours'].fillna(df['StudyHours'].mean())

    df['Attendance'] = df['Attendance'].fillna(df['Attendance'].mean())


    df['Marks'] = df['Marks'].fillna(df['Marks'].mean())

    df = df[(df['Attendance'] >= 0) & (df['Attendance'] <= 100)]
    df = df[(df['StudyHours'] >= 0) & (df['StudyHours'] <= 100)]

    df.to_csv("output/cleaned_data.csv", index = False)

    print(f"Rows after cleaning : {len(df)}")
    print(df.head())

    return df
