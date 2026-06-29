import pandas as pd
# df = pd.read_csv("output/cleaned_data.csv")

def data_filtering(df):
    toppers = df[df["Marks"] >= 90]
    print(toppers)
    failed_students = df[df["Result"] == "Fail"]
    print(failed_students)
    low_attendance = df[df["Attendance"] < 75]
    print(low_attendance)
    study_more = df[df["StudyHours"] > 8]
    print(study_more)

    toppers.to_csv("output/toppers.csv", index = False)
    failed_students.to_csv("output/failed_students.csv", index = False)

    return df