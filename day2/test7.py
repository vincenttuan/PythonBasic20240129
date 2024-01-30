data = "97,45,90"
# 請分別印出及格與不及格的分數

def printPass():
    global data
    scores = data.split(",")
    if int(scores[0]) >= 60:
        print("及格:", scores[0])
    if int(scores[1]) >= 60:
        print("及格:", scores[1])
    if int(scores[2]) >= 60:
        print("及格:", scores[2])

def printFail():
    global data
    scores = data.split(",")
    if int(scores[0]) < 60:
        print("不及格:", scores[0])
    if int(scores[1]) < 60:
        print("不及格:", scores[1])
    if int(scores[2]) < 60:
        print("不及格:", scores[2])

if __name__ == '__main__':
    printPass()
    printFail()