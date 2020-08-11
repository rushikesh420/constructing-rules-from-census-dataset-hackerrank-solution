#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'arrangingRules' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY rules as parameter.
#
import pandas as pd
import numpy as np
#df = pd.DataFrame(["age", "sex", "education","native-country", "race", "#"])

def arrangingRules(rules):
    # Write your code here
    confidence =[]
    col_names=["age", "sex", "education","native-country", "race", "marital-status", "workclass", "occupation", "hours-per-week", "income", "capital-gain", "capital-loss"]
    df = pd.read_csv("census.csv",header =None, names= col_names)
    list_part1 = []
    for rule in rules:
        part1= rule.split("=>")[0][1:-1]
        #list_part1 = part1.split(",")
        a = part1.split(",")[0]
        b = part1.split(",")[1]
        c = rule.split("=>")[1][1:-1]

        new_df= df[[a.split('=')[0], b.split('=')[0], c.split('=')[0]]]
        #new_df[c.split('=')[0]] = df[c.split('=')[0]]
        cols = new_df.columns.tolist()
        temp = new_df.groupby(cols).size().reset_index().rename(columns={0:'count'})

        #temp = temp.reset_index().rename(columns={0:'count'})
        #print(temp)
        #list_part2=[]

        count1 = 0
        count2 = 0
        for index, row in temp.iterrows():
            #for i in range(len(list_part1)):
             #   list_part2.append(row[list_part1[i].split('=')[0]])
            x = row[a.split('=')[0]]    
            y = row[b.split('=')[0]]
            z = row[c.split('=')[0]]
            m = row['count']
            
            #print(z ,m, list_part1, list_part2)
            #if(list_part2 == list_part1 and z == c):  

            if(x ==a and y==b and z ==c):                    
                count1 = m
            if(x ==a and y==b):
                count2 = count2+m
           

        support = count1/temp.shape[0]
        confidence.append(count1/count2)
    #print(confidence)
    confidence, rules = zip(*sorted(zip(confidence, rules)))
    #print(rules)
    #print(confidence)
    return(rules[::-1])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rules_count = int(input().strip())

    rules = []

    for _ in range(rules_count):
        rules_item = input()
        rules.append(rules_item)

    result = arrangingRules(rules)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
