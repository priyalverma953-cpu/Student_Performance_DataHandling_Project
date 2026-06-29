import pandas as pd
# df = pd.read_csv("data/student_dataset_v2.csv")

def transform_data(df):
    def grade(mark):
        if mark >= 90:
            return "A"
        elif mark >= 75:
            return "B"
        elif mark >= 60:
             "C"
        elif mark >= 40:
            return "D"
        else:
         return "F"
    
    df["Grade"] = df["Marks"].apply(grade)

    df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")

    df["Performance Score"] = (
        df["Marks"]*0.6 + df["Attendance"]*0.2 + df["StudyHours"]*0.2
    )

    df.to_csv("output/cleaned_data.csv", index = False)
    print(df[["Marks", "Grade", "Result", "Performance Score"]].head())
    print(f"Grades : {df['Grade'].value_counts().to_dict()}")

    return df