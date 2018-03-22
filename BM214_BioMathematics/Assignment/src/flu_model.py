#!/usr/bin/python

def init(data_file_path, debug=False):
    df = get_data_frame(data_file_path)
    days     = df["Day"].values
    cases    = df["Cases"].values
    infected = df["Infected"].values
    #vertical differents between the cases and infected curves
    vert_diff = [c - i for c, i in zip(cases, infected)]
    new_vert_diff = [i + d for i, d in zip(infected, vert_diff))]



    #print new_infected


    plot_results(days, cases, infected, vert_diff, new_vert_diff)
    if debug is True:
        print "DEBUG MODE: [ON]\nColumns:",
        for i in xrange(0, len(df.columns) - 3):
            print df.columns[i],

def plot_results(days, cases, infected, vert_diff, new_vert_diff):
    plt.plot(days, cases, label="Cases")
    plt.plot(days, infected, label="Infetced")
    plt.plot(days, vert_diff, label="Vertical diff")
    plt.plot(days, new_vert_diff, label="New Infected")
    plt.title('The Graph of Days vs Cases and Infected')
    plt.ylabel('Cases and Infected')
    plt.xlabel('Days')
    plt.legend(bbox_to_anchor=(1.0, 1), loc=0, borderaxespad=0.)
    plt.show()

def get_data_frame(file_path):
    return pd.read_excel(file_path)

if __name__ == "__main__":
    from pandas import (ExcelWriter, ExcelFile)
    import matplotlib.pyplot as plt
    from sys import argv, exit
    import pandas as pd

    if len(argv) != 2:
        exit("Usage: flu_model.py <influenza.xlsx>")
    else:
        init(argv[1])


else:
    from sys import exit
    exit("Usage: flu_model.py <influenza.xlsx>")
