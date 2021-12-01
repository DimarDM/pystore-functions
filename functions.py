import os
import fnmatch
import pystore
import pandas as pd

store = pystore.store('mydatastore')

collection = None
#mypath = '/Users/dimitrisaristeidopoulos/Projects/coinapi/Results/20First_GREATER_ThanStrikePrice/'
mypath = input("Path  (Please don't give as an input nested folders):")

temp = mypath.split('/')
folder = temp[len(temp)-2]

collection = store.collection(folder,overwrite=True)

for path,dirs,files in os.walk(mypath):
    
    for file in fnmatch.filter(files,'*.csv'):
        data = pd.read_csv(mypath+file)
        print(data.head())
        collection.write(file, data)

        #fullname = os.path.abspath(os.path.join(path,f))


