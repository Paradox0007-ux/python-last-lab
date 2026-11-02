
import pandas as pd
import os

def inspect_csv(filename):
    if not os.path.exists(filename):
        print("File not found!")
        return

    try:
        df = pd.read_csv(filename)

        print("\n========== CSV FILE INSPECTOR ==========")

        print("\n1. First 5 Rows:")
        print(df.head())

        print("\n2. Dataset Information:")
        print(df.info())

        print("\n3. Number of Rows and Columns:")
        print(df.shape)

        print("\n4. Column Names:")
        print(df.columns.tolist())

        print("\n5. Missing Values:")
        print(df.isnull().sum())

        print("\n6. Duplicate Rows:")
        print(df.duplicated().sum())

        print("\n7. Statistical Summary:")
        print(df.describe(include="all"))

        print("\n========== DATA EXPORTER ==========")

        print("1. Export as CSV")
        print("2. Export as Excel")
        print("3. Export as JSON")

        choice = input("Enter your choice: ")

        if choice == "1":
            df.to_csv("exported_data.csv", index=False)
            print("CSV file exported successfully!")

        elif choice == "2":
            df.to_excel("exported_data.xlsx", index=False)
            print("Excel file exported successfully!")

        elif choice == "3":
            df.to_json("exported_data.json", orient="records", indent=4)
            print("JSON file exported successfully!")

        else:
            print("Invalid choice!")

    except Exception as e:
        print("Error:", e)


print("AUTOMATED CSV FILE INSPECTOR AND DATA EXPORTER")

filename = input("Enter CSV file name: ")

inspect_csv(filename)
