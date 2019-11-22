import random
import math
import numpy as np
import pandas as pd

def insert(df, values):
    df1 = pd.DataFrame(data = [values], columns = ["T_val", "HR_val", "BP_val", "Problem_type"])
    df = pd.concat([df, df1], axis = 0)
    return df

def forT(iteration, values):
    if iteration == 0:
        values.append(random.uniform(2.0, 3.0))
        values.append(random.uniform(0.0, 10.0))
        values.append(random.uniform(0.0, 21.0))
        values.append("T")
    if iteration == 1:
        values.append(random.uniform(3.0, 4.0))
        values.append(random.uniform(0.0, 10.0))
        values.append(random.uniform(0.0, 21.0))
        values.append("T")
    if iteration == 2:
        values.append(random.uniform(3.0, 4.0))
        values.append(random.uniform(10.0, 25.0))
        values.append(random.uniform(0.0, 21.0))
        values.append("T")
    if iteration == 3:
        values.append(random.uniform(3.0, 4.0))
        values.append(random.uniform(0.0, 10.0))
        values.append(random.uniform(21.0, 50.0))
        values.append("T")
    if iteration == 4:
        values.append(random.uniform(4.0, 5.0))
        values.append(random.uniform(0.0, 10.0))
        values.append(random.uniform(0.0, 21.0))
        values.append("T")
    if iteration == 5:
        values.append(random.uniform(4.0, 5.0))
        values.append(random.uniform(10.0, 25.0))
        values.append(random.uniform(0.0, 21.0))
        values.append("T")
    if iteration == 6:
        values.append(random.uniform(4.0, 5.0))
        values.append(random.uniform(0.0, 10.0))
        values.append(random.uniform(21.0, 50.0))
        values.append("T")

def forHR(iteration, values):
    if iteration == 0:
        values.append(random.uniform(0.0, 2.0))
        values.append(random.uniform(10.0, 25.0))
        values.append(random.uniform(0.0, 21.0))
        values.append("HR")
    if iteration == 1:
        values.append(random.uniform(0.0, 2.0))
        values.append(random.uniform(25.0, 35.0))
        values.append(random.uniform(0.0, 21.0))
        values.append("HR")
    if iteration == 2:
        values.append(random.uniform(2.0, 3.0))
        values.append(random.uniform(25.0, 35.0))
        values.append(random.uniform(0.0, 21.0))
        values.append("HR")
    if iteration == 3:
        values.append(random.uniform(0.0, 2.0))
        values.append(random.uniform(25.0, 35.0))
        values.append(random.uniform(21.0, 50.0))
        values.append("HR")
    if iteration == 4:
        values.append(random.uniform(0.0, 2.0))
        values.append(random.uniform(35.0, 50.0))
        values.append(random.uniform(0.0, 21.0))
        values.append("HR")
    if iteration == 5:
        values.append(random.uniform(2.0, 3.0))
        values.append(random.uniform(35.0, 50.0))
        values.append(random.uniform(0.0, 21.0))
        values.append("HR")
    if iteration == 6:
        values.append(random.uniform(0.0, 2.0))
        values.append(random.uniform(35.0, 50.0))
        values.append(random.uniform(21.0, 50.0))
        values.append("HR")

def forBP(iteration, values):
    if iteration == 0:
        values.append(random.uniform(0.0, 2.0))
        values.append(random.uniform(0.0, 10.0))
        values.append(random.uniform(21.0, 50.0))
        values.append("BP")
    if iteration == 1:
        values.append(random.uniform(0.0, 2.0))
        values.append(random.uniform(0.0, 10.0))
        values.append(random.uniform(50.0, 80.0))
        values.append("BP")
    if iteration == 2:
        values.append(random.uniform(0.0, 2.0))
        values.append(random.uniform(10.0, 25.0))
        values.append(random.uniform(50.0, 80.0))
        values.append("BP")
    if iteration == 3:
        values.append(random.uniform(2.0, 3.0))
        values.append(random.uniform(0.0, 10.0))
        values.append(random.uniform(50.0, 80.0))
        values.append("BP")
    if iteration == 4:
        values.append(random.uniform(0.0, 2.0))
        values.append(random.uniform(0.0, 10.0))
        values.append(random.uniform(80.0, 110.0))
        values.append("BP")
    if iteration == 5:
        values.append(random.uniform(0.0, 2.0))
        values.append(random.uniform(10.0, 25.0))
        values.append(random.uniform(80.0, 110.0))
        values.append("BP")
    if iteration == 6:
        values.append(random.uniform(2.0, 3.0))
        values.append(random.uniform(0.0, 10.0))
        values.append(random.uniform(80.0, 110.0))
        values.append("BP")

def forTandHR(iteration, values):
    if iteration == 0:
        values.append(random.uniform(2.0, 3.0))
        values.append(random.uniform(10.0, 25.0))
        values.append(random.uniform(0.0, 21.0))
        values.append("T and HR")
    if iteration == 1:
        values.append(random.uniform(3.0, 4.0))
        values.append(random.uniform(10.0, 25.0))
        values.append(random.uniform(0.0, 21.0))
        values.append("T and HR")
    if iteration == 2:
        values.append(random.uniform(2.0, 3.0))
        values.append(random.uniform(25.0, 35.0))
        values.append(random.uniform(0.0, 21.0))
        values.append("T and HR")
    if iteration == 3:
        values.append(random.uniform(3.0, 4.0))
        values.append(random.uniform(25.0, 35.0))
        values.append(random.uniform(0.0, 21.0))
        values.append("T and HR")
    if iteration == 4:
        values.append(random.uniform(3.0, 4.0))
        values.append(random.uniform(25.0, 35.0))
        values.append(random.uniform(21.0, 50.0))
        values.append("T and HR")
    if iteration == 5:
        values.append(random.uniform(4.0, 5.0))
        values.append(random.uniform(25.0, 35.0))
        values.append(random.uniform(0.0, 21.0))
        values.append("T and HR")
    if iteration == 6:
        values.append(random.uniform(3.0, 4.0))
        values.append(random.uniform(35.0, 50.0))
        values.append(random.uniform(0.0, 21.0))
        values.append("T and HR")
    if iteration == 7:
        values.append(random.uniform(4.0, 5.0))
        values.append(random.uniform(25.0, 35.0))
        values.append(random.uniform(21.0, 50.0))
        values.append("T and HR")
    if iteration == 8:
        values.append(random.uniform(3.0, 4.0))
        values.append(random.uniform(35.0, 50.0))
        values.append(random.uniform(21.0, 50.0))
        values.append("T and HR")
    if iteration == 9:
        values.append(random.uniform(4.0, 5.0))
        values.append(random.uniform(35.0, 50.0))
        values.append(random.uniform(0.0, 21.0))
        values.append("T and HR")
    if iteration == 10:
        values.append(random.uniform(4.0, 5.0))
        values.append(random.uniform(35.0, 50.0))
        values.append(random.uniform(21.0, 50.0))
        values.append("T and HR")

def forHRandBP(iteration, values):
    if iteration == 0:
        values.append(random.uniform(0.0, 2.0))
        values.append(random.uniform(10.0, 25.0))
        values.append(random.uniform(21.0, 50.0))
        values.append("HR and BP")
    if iteration == 1:
        values.append(random.uniform(0.0, 2.0))
        values.append(random.uniform(10.0, 25.0))
        values.append(random.uniform(50.0, 80.0))
        values.append("HR and BP")
    if iteration == 2:
        values.append(random.uniform(0.0, 2.0))
        values.append(random.uniform(25.0, 35.0))
        values.append(random.uniform(21.0, 50.0))
        values.append("HR and BP")
    if iteration == 3:
        values.append(random.uniform(0.0, 2.0))
        values.append(random.uniform(25.0, 35.0))
        values.append(random.uniform(50.0, 80.0))
        values.append("HR and BP")
    if iteration == 4:
        values.append(random.uniform(2.0, 3.0))
        values.append(random.uniform(25.0, 35.0))
        values.append(random.uniform(50.0, 80.0))
        values.append("HR and BP")
    if iteration == 5:
        values.append(random.uniform(0.0, 2.0))
        values.append(random.uniform(25.0, 35.0))
        values.append(random.uniform(80.0, 110.0))
        values.append("HR and BP")
    if iteration == 6:
        values.append(random.uniform(0.0, 2.0))
        values.append(random.uniform(35.0, 50.0))
        values.append(random.uniform(50.0, 80.0))
        values.append("HR and BP")
    if iteration == 7:
        values.append(random.uniform(2.0, 3.0))
        values.append(random.uniform(25.0, 35.0))
        values.append(random.uniform(80.0, 110.0))
        values.append("HR and BP")
    if iteration == 8:
        values.append(random.uniform(2.0, 3.0))
        values.append(random.uniform(35.0, 50.0))
        values.append(random.uniform(50.0, 80.0))
        values.append("HR and BP")
    if iteration == 9:
        values.append(random.uniform(0.0, 2.0))
        values.append(random.uniform(35.0, 50.0))
        values.append(random.uniform(80.0, 110.0))
        values.append("HR and BP")
    if iteration == 10:
        values.append(random.uniform(2.0, 3.0))
        values.append(random.uniform(35.0, 50.0))
        values.append(random.uniform(80.0, 110.0))
        values.append("HR and BP")

def forBPandT(iteration, values):
    if iteration == 0:
        values.append(random.uniform(2.0, 3.0))
        values.append(random.uniform(0.0, 10.0))
        values.append(random.uniform(21.0, 50.0))
        values.append("T and BP")
    if iteration == 1:
        values.append(random.uniform(3.0, 4.0))
        values.append(random.uniform(0.0, 10.0))
        values.append(random.uniform(21.0, 50.0))
        values.append("T and BP")
    if iteration == 2:
        values.append(random.uniform(2.0, 3.0))
        values.append(random.uniform(0.0, 10.0))
        values.append(random.uniform(50.0, 80.0))
        values.append("T and BP")
    if iteration == 3:
        values.append(random.uniform(3.0, 4.0))
        values.append(random.uniform(0.0, 10.0))
        values.append(random.uniform(50.0, 80.0))
        values.append("T and BP")
    if iteration == 4:
        values.append(random.uniform(3.0, 4.0))
        values.append(random.uniform(10.0, 25.0))
        values.append(random.uniform(50.0, 80.0))
        values.append("T and BP")
    if iteration == 5:
        values.append(random.uniform(4.0, 5.0))
        values.append(random.uniform(0.0, 10.0))
        values.append(random.uniform(50.0, 80.0))
        values.append("T and BP")
    if iteration == 6:
        values.append(random.uniform(3.0, 4.0))
        values.append(random.uniform(0.0, 10.0))
        values.append(random.uniform(80.0, 110.0))
        values.append("T and BP")
    if iteration == 7:
        values.append(random.uniform(3.0, 4.0))
        values.append(random.uniform(10.0, 25.0))
        values.append(random.uniform(80.0, 110.0))
        values.append("T and BP")
    if iteration == 8:
        values.append(random.uniform(4.0, 5.0))
        values.append(random.uniform(10.0, 25.0))
        values.append(random.uniform(50.0, 80.0))
        values.append("T and BP")
    if iteration == 9:
        values.append(random.uniform(4.0, 5.0))
        values.append(random.uniform(0.0, 10.0))
        values.append(random.uniform(80.0, 110.0))
        values.append("T and BP")
    if iteration == 10:
        values.append(random.uniform(4.0, 5.0))
        values.append(random.uniform(10.0, 25.0))
        values.append(random.uniform(80.0, 110.0))
        values.append("T and BP")

def forTandHRandBP(iteration, values):
    if iteration == 0:
        values.append(random.uniform(2.0, 3.0))
        values.append(random.uniform(10.0, 25.0))
        values.append(random.uniform(21.0, 50.0))
        values.append("T and HR and BP")
    if iteration == 1:
        values.append(random.uniform(3.0, 4.0))
        values.append(random.uniform(25.0, 35.0))
        values.append(random.uniform(50.0, 80.0))
        values.append("T and HR and BP")
    if iteration == 2:
        values.append(random.uniform(4.0, 5.0))
        values.append(random.uniform(25.0, 35.0))
        values.append(random.uniform(50.0, 80.0))
        values.append("T and HR and BP")
    if iteration == 3:
        values.append(random.uniform(3.0, 4.0))
        values.append(random.uniform(35.0, 50.0))
        values.append(random.uniform(50.0, 80.0))
        values.append("T and HR and BP")
    if iteration == 4:
        values.append(random.uniform(3.0, 4.0))
        values.append(random.uniform(25.0, 35.0))
        values.append(random.uniform(80.0, 110.0))
        values.append("T and HR and BP")
    if iteration == 5:
        values.append(random.uniform(4.0, 5.0))
        values.append(random.uniform(35.0, 50.0))
        values.append(random.uniform(50.0, 80.0))
        values.append("T and HR and BP")
    if iteration == 6:
        values.append(random.uniform(4.0, 5.0))
        values.append(random.uniform(25.0, 35.0))
        values.append(random.uniform(80.0, 110.0))
        values.append("T and HR and BP")
    if iteration == 7:
        values.append(random.uniform(3.0, 4.0))
        values.append(random.uniform(35.0, 50.0))
        values.append(random.uniform(80.0, 110.0))
        values.append("T and HR and BP")
    if iteration == 8:
        values.append(random.uniform(4.0, 5.0))
        values.append(random.uniform(35.0, 50.0))
        values.append(random.uniform(80.0, 110.0))
        values.append("T and HR and BP")

def get_values(df, branch):
    values = []
    for iteration in range(7):
        forT(iteration, values)
        if branch == 0:
            df = insert(df, values)
        values = []
        forHR(iteration, values)
        if branch == 0:
            df = insert(df, values)
        values = []
        forBP(iteration, values)
        if branch == 0:
            df = insert(df, values)
        values = []

    for iteration in range(11):
        forTandHR(iteration, values)
        if branch == 0:
            df = insert(df, values)
        values = []
        forHRandBP(iteration, values)
        if branch == 0:
            df = insert(df, values)
        values = []
        forBPandT(iteration, values)
        if branch == 0:
            df = insert(df, values)
        values = []

    for iteration in range(9):
        forTandHRandBP(iteration, values)
        if branch == 0:
            df = insert(df, values)
        values = []

    return df

####################################

def get_data(branch):
    df = pd.DataFrame(columns = ["T_val", "HR_val", "BP_val", "Problem_type"])

    for repetition in range(10):
        df = get_values(df, branch)

    df.index = range(len(df.index))
    return df


#print(df, '\n')
