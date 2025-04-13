import json
import pandas as pd

with open("035_signup_data.json", "r") as file:
    data = json.load(file)

    df = pd.DataFrame(data)

    excel_filename = "038_first_exam_result.xlsx"
    df.to_excel(excel_filename, index=False)
    print("excel_filename has been created successfully.")
