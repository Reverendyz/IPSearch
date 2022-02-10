from os import listdir
from os.path import isfile, join
import re

def main():
    mypath = "."
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    
    for file in onlyfiles:
        with open(file) as f:
            for line in f.readlines():
                if re.search('10\.10\.*', line):
                    print(file)
                    print(line)
                

if __name__ == "__main__":
    main()

