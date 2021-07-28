import pandas as pd
import json
import ast
import os

filename = r"D:\Desktop\IR_term_8\sample-1M.jsonl"
output_path = r"D:\Desktop\IR_term_8"

with open(filename) as json_file:      
    data = json_file.readlines()
    # this line below may take at least 8-10 minutes of processing for 4-5 million rows. It converts all strings in list to actual json objects. 
    data = list(map(json.loads, data)) 

df = pd.DataFrame(data)
for col in df.columns:
    print (col)

labels_to_drop = ["content", "media-type", "source", "published"]
df = df.drop(labels_to_drop, axis = 1)


df.head()

'''
count = len(df)

out_header = ["title"]

for idx, e in df.iterrows():
    print("Row ",idx," out of ",count)
    entry = e.values.tolist()
    print (entry)
    #for src in src_lst:
    #    print (src)

    #output.to_csv(output_path, sep='\t', header=is_first, index=False, mode='a')
    #is_first = False
'''
df.to_csv('article_titles.csv', index=False)
#print (path)