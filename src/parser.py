import sys
import csv

debug = True

def main(args):
    numArgs = len(args)
    inputFileName = ''
    outputFileName = ''
    classMapFileName = ''
    if(numArgs) == 0:
        print("No arguments = no generation!")
        print("1 arg (input file name) - generate output with same file name")
        print("2 args (input file name, output file name) - generate output with given file name")
        print("3 args (input file name, output file name, class map file name) - generate output with given file name finding class stylings in given class map file")
        return
    elif numArgs == 1:
        inputFileName = args[0]
        outputFileName = inputFileName
        print("Attempting to create output file with same name as input file with name {input}".format(input = inputFileName))
    elif numArgs == 2:
        inputFileName = args[0]
        outputFileName = args[1]
        print("Attempting to create output file with name {output} from input file with name {input}".format(output = outputFileName, input = inputFileName))
    elif numArgs == 3:
        inputFileName = args[0]
        outputFileName = args[1]
        classMapFileName = args[2]
        print("Attempting to create output file with name {output} from input file with name {input} with class defs found in {classMap}".format(output = outputFileName, input = inputFileName, classMap = classMapFileName))
    else:
        print("Only using first three arguments.")
        inputFileName = args[0]
        outputFileName = args[1]
        classMapFileName = args[2]
        print("Attempting to create output file with name {output} from input file with name {input} with class defs found in {classMap}".format(output = outputFileName, input = inputFileName, classMap = classMapFileName))

    tagSet = loadTagSet()
    classMap = None
    if not tagSet:
        print("Tag csv not found or is empty! Generated file will be badly misformatted. A copy of the csv can be found on Github.")
    print("Loaded tags.")
    if debug:
        print(tagSet)
    if classMapFileName != '':
        classMap = loadClassMap(classMapFileName)
        if not classMap:
            print("Class definitions not found or is empty.")
        else:
            print("Loaded class definitions.")
            if debug:
                print(classMap)
    



def loadClassMap(fileName):
    classMapPath = 'resources/classes/'
    classMapFileName = fileName + '.csv'
    classMap = {}
    print("loading class definitions from {path}".format(path = classMapPath + classMapFileName))
    with open(classMapPath + classMapFileName) as file:
        reader = csv.reader(file)
        for row in reader:
            classMap[row[0]] = row[1]
    if not classMap:
        return None
    return classMap

def loadTagSet():
    tagMapPath = 'resources/tags/'
    tagMapFileName = 'tags.csv'
    tagSet = set()
    print("loading standard tags from {path}".format(path = tagMapPath + tagMapFileName))
    with open(tagMapPath + tagMapFileName) as file:
        reader = csv.reader(file)
        for row in reader:
            for tag in row:
                tagSet.add(tag)
    if not tagSet:
        return None
    return tagSet
    

if __name__ == "__main__":
    main(sys.argv[1:])