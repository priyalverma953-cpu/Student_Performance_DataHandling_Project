import pandas as pd
# df = pd.read_csv("output/cleaned_data.csv")

def analyze_data(df):
    print("\nAverage Marks")
    print(df['Marks'].mean())

    print("\nMaximum Marks")
    print(df['Marks'].max())

    print("\nMinimum Marks\n",df['Marks'].min())


    print("\nAverage Attendance")
    print(df['Attendance'].mean())

    print("\nAverage Study Hours")
    print(df['StudyHours'].mean())

    print("\n Pass percentage")
    pass_percentage = (len(df[df["Result"]=="Pass"])/len(df)*100)
    print(pass_percentage)

    print("\n Failed Percentage")
    failed_percentage = (len(df[df["Result"]=="Fail"])/len(df)*100)
    print(failed_percentage)

    print("\nGrade Distribution")
    print(df["Grade"].value_counts())

#MODULE 7 : SORTING
    print("\n Students sorted by Mark")
    print(df.sort_values('Marks', ascending=False))

    print("\n Students sorted by Attendance")
    print(df.sort_values('Attendance', ascending=False))

    print("\n Students sorted by Study Hours")
    print(df.sort_values('StudyHours', ascending=False))

#MODULE 8:  GROUPING
    print("\n Average marks by grade")
    print(df.groupby('Grade').agg(
        Avg_Marks = ('Marks','mean')    
                     ))

    print("Number of students in each grade")
    print(df.groupby("Grade")["Grade"].count())


    print("\n Average attendance by grade")
    print(df.groupby('Grade').agg(
        Avg_Attendance = ('Attendance', 'mean')
        ))

#MODULE 9 : STATISTICAL ANALYSIS
    print("\n Mean")
    print(df.mean(numeric_only= True))

    print("\n Median")
    print(df.median(numeric_only = True))

    print("\n Mode")
    print(df.mode())

    print("\n Standard Deviation")
    print(df.std(numeric_only = True))

    print("\n Variance")
    print(df.var(numeric_only = True))

    print("\n Correlation Matrix")
    print(df.corr(numeric_only= True))

#MODULE 10 : REPORT GENERATION

    report = pd.DataFrame({
        "Total_Students" : [len(df)],
        "Passed_Student" : [len(df[df["Result"]=="Pass"])],
        "Failed_Student" : [len(df[df["Result"]=="Fail"])],
        "Highest_Marks"  : [df["Marks"].max()],
        "Lowest_Marks"   : [df["Marks"].min()],
        "Average_Marks"  : [df["Marks"].mean()],
        "Average_Attendance" : [df["Attendance"].mean()]
        })

    report.to_csv("output/report.csv", index = False)

    grade_report = df["Grade"].value_counts()

    print("\n Final Report")
    print(report)

    print("\n Grade distribution")
    print(grade_report)

    #BONUS TASKS
    #TASK 1: TOP 10 STUDENTS

    print("\n Top 10 Students by Performance Score")
    top_10 = df.nlargest(10, "Performance Score")
    print(top_10[["Name", "Marks", "Grade", "Performance Score"]])

    top_10.to_csv("output/top10_students.csv", index = False)

    #TASK 2 : EXPORT IN EXCEL FORMAT
    report.to_excel("output/report.xlsx", index = False)
    print("Report exported in Excel Format!")

    return df

