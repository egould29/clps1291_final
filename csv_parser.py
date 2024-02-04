import csv
import pandas as pd
from algorithms import mds, hc, pca

# TODO: how to represent the data? numpy array? tuple of numpy arrays?
def parse(fn : str):
    try:
        df = pd.read_csv(f"data/{fn}")
        # print(df)
        return (True, df)
    except FileNotFoundError:
        return (False, None)

def main():
    is_valid = False
    intro_msg = "Please enter the filename of the data you want to evaluate, or type 'q' to quit.\n"
    response = input(intro_msg)

    while not is_valid and not response.lower() == 'q':
        is_valid, data = parse(response)
        if not is_valid:
            print("Invalid filename.")
            response = input(intro_msg)

    print(data)

    while not response.lower() == "q":
        prompt = "Would you like to test another algorithm on this data? Hit 'enter' to continue, or 'q' to quit.\n"

        response = input("Which linearity reduction algorithm would you like to employ (MDS/HC/PCA)?\n")
        if response.lower() == "mds":
            mds()
            response = input(prompt)
        elif response.lower() == "hc":
            hc()
            response = input(prompt)
        elif response.lower() == "pca":
            pca()
            response = input(prompt)
        else:
            print(f"I don't recognize that method")
            response = ''

if __name__ == "__main__":
    main()