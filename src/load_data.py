import pandas as pd
df = pd.read_csv("data/student_dataset_v2.csv")

def load_data(path):
    df = pd.read_csv(path)

    print("\n First 5 records")
    print(df.head())

    print("\n last 5 records")
    print(df.tail())

    print("\n Shape:",df.shape)

    print("\n columns:",df.columns)

    print("\nData Types")
    print(df.dtypes)

#MODULE 2 : DATA INSPECTION
    print("\nMissing values")
    print(df.isnull().sum())

    print("\nDuplicate Records")
    print(df.duplicated().sum())

    print("\nStatistics")
    print(df.describe())

    print("\nMemory usuages")
    print(df.memory_usage())

    print("\nSummary")
    df.info()

    return df


