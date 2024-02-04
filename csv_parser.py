import csv
from algorithms import mds, hc, pca

# TODO: how to represent the data? numpy array? tuple of numpy arrays?
def parse(fn : str):
    pass

def main():
    is_valid = False

    while not is_valid:
        response = input("Please enter the filename of the data you want to evaluate, or type 'q' to quit.\n")
        # TODO: check if the filename is valid
        filename = response # if valid

    # TODO: parse the csv
    parse(filename)

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