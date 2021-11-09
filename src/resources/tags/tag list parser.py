import re
def main():
    tagList = []
    with open("raw tag list.txt") as file:
        for line in file:
            if "REMOVE" in line:
                continue
            else:
                tag = re.split("<(.*)>", line, 1)
                if len(tag) > 1:
                    print(tag)
                    tag = re.split("([a-zA-Z]*)", tag[1])
                    tagList.append(tag[1].strip())
    writeToTagFile(tagList)

def writeToTagFile(tagList):
    with open("tags.csv", "w") as file:
        for tag in tagList:
            file.write(tag+",")
            print(tag, end=",")


if __name__ == "__main__":
    main()