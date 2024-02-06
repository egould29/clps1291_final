# CLPS 1291 Final Project

**Authors:** Ephraim Gould and Diana Olmos Gonzalez

## How to Use
The source code for the behavior of this application is all located in the `src` folder. Running the `csv_parser.py` file will prompt the user to entire a filename they would like to see a dimensionality reduction visualization for. All data files are stored in the 'data' folder.

If the user enters a valid filename, they will be prompted to select if they would like to see a multi-dimensional scaling (MDS) plot, a hierarchical clustering (HC) dendrogram, or the principal components plotted in the eigenvector space (PCA).

## Data

The 'customers-100.csv' file was downloaded from [here](https://www.datablist.com/learn/csv/download-sample-csv-files) to test parsing. The 'colors' and 'traitData' files were downloaded from assignments 1 and 2 and converted into CSV files with the `pkl_to_csv.py` script.