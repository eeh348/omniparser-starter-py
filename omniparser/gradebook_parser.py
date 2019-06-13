
import pandas

import statistics

import os


def calculate_average_grade_from_csv(my_csv_filepth):

    df = pandas.read_csv(my_csv_filepth)

    rows = df.to_dict("records")
    grades = [r["final_grade"] for r in rows]
    avg_grade = statistics.mean(grades)

    #breakpoint()

    #grade

    return avg_grade

if __name__ == "__main__":

    print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE...")

    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2019.csv")

    avg = calculate_average_grade_from_csv(gradebook_filepath)

    print(avg)



