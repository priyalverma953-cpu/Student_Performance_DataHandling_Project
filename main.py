import sys
sys.path.append("src")

from load_data import load_data
from clean_data import clean_data
from transform import transform_data
from data_filtering import data_filtering
from analyze import analyze_data

if __name__ == "__main__":
    print("="*50)
    print("Loading Data...")
    df = load_data("data/student_dataset_v2.csv")

    print("="*50)
    print("Cleaning Data...")
    df = clean_data(df)

    print("="*50)
    print("Transforming Data...")
    df = transform_data(df)

    print("="*50)
    print("Filtering Data...")
    df = data_filtering(df)

    print("="*50)
    print("Analyzing Data...")
    analyze_data(df)

    print("="*50)
    print("PIPELINE COMPLETE")



    



