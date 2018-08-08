import json

with open("survey.json", "r") as read_file:
    survey = json.load(read_file)


def averageAge(survey):
    sum = []
    for x in range(len(survey)):
        n = survey[x]['age']
        sum.append(n)
    final = 0
    for x in range(len(sum)):
        final = final + sum[x]
    final = final / (len(sum))
    print("\n", final, "\n")


def names(survey):
    names = []
    for x in range(len(survey)):
        n = survey[x]['name']
        names.append(n)
    print("\n", names, "\n")


def dob(survey):
    dob = []
    for x in range(len(survey)):
        n = survey[x]['birthday']
        names.append(n)
    print("\n", dob, "\n")


def responses(survey):
    print("\n", len(survey), "\n")


#MAIN CODE
def main():
    responses(survey)

if __name__ == "__main__":
    main()
