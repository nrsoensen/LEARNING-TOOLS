import json

#important functions
def takeSurvey():
    start = "\n" + "Would you like to participate in a survey? Yes or no?" + "\n\n"

    survey = []

    while True:
        user_input = input(start)

        if user_input == "yes":
            print("\n" + "Okay...bye" + "\n")
            break

        elif user_input == "no":
            s1 = {}
            name = input("\n" + "Question 1: What is your name? " + "\n\n")
            s1['name'] = name
            while True:
                try:
                    age = eval(input("\n" + "Question 2: How old are you? " + "\n\n"))
                    s1['age'] = age
                    break
                except NameError:
                    print("That's not a number!")
                    continue
            birthplace = input("\n" + "Question 3: Where were you born? " + "\n\n")
            s1['birthplace'] = birthplace
            hometown = input("\n" + "Question 4: Where do you live? " + "\n\n")
            s1['hometown'] = hometown
            color = input("\n" + "Question 5: What is your favorite color? " + "\n\n")
            s1['color'] = color
            birthday = input("\n" + "Question 6: When were you born? (MM/DD/YYYY)" + "\n\n")
            s1['birthday'] = birthday
            print("\n" + "Thank you for your input! Here were your responses:")
            printResponses(s1)
            survey.append(s1)

            while True:
                edit = input("Would you like to edit your responses? Yes or no" + "\n\n")
                if edit == "no":
                    break
                elif edit == "yes":
                    edit2 = input("\n" + "What do you want to edit?" + "\n" + "Name" + "\n" + "Age" + "\n" + "Birthplace" +
                        "\n" + "Hometown" + "\n" + "Fav Color" + "\n" + "Birthday" + "\n\n")
                    edit2 = edit2.lower()
                    editSurvey(edit2, s1)

            saveData(survey)

        else:
            print("\n" + "I'm sorry, I didn't catch that.")


def saveData(survey):
    file = open("survey.json", "r")
    try:
        existingData = json.load(file)
        survey.extend(existingData)
    except ValueError:
        print("")
    file.close()

    file = open("survey.json", "w")
    file.write("[\n")
    count = 0
    for i in survey:
        json.dump(i, file)
        if (count < len(survey)-1):
            file.write(',\n')
        else:
            file.write('\n]')
        count += 1
    file.close()

    #my og JSON writer thing -- only thing different
#    f = open("survey.json", "a")
#    json.dump(survey, f)
#    f.close()


def printResponses(s1):
    print("Name:", s1['name'], ", Age:", s1['age'], ", Birthplace:", s1['birthplace'],
        ", Hometown:", s1['hometown'], ", Fav Color:", s1['color'], ", Birthday:", s1['birthday'], "\n")



def averageAge(survey):
    sum = []
    for x in range(len(survey)):
        n = survey[x]['age']
        sum.append(n)
    final = 0
    for x in range(len(sum)):
        final = final + sum[x]
    final = final / (len(sum))



def editSurvey(edit2, s1):
    if edit2 == "name":
        name = input("\n" + "Edit name" + "\n\n")
        s1['name'] = name
        printResponses(s1)
    elif edit2 == "age":
        age = eval(input("\n" + "Edit age" + "\n\n"))
        s1['age'] = age
        printResponses(s1)
    elif edit2 == "birthplace":
        birthplace = input("\n" + "Edit birthplace" + "\n\n")
        s1['birthplace'] = birthplace
        printResponses(s1)
    elif edit2 == "hometown":
        hometown = input("\n" + "Edit hometown" + "\n\n")
        s1['hometown'] = hometown
        printResponses(s1)
    elif edit2 == "fav color":
        color = input("\n" + "Edit fav color" + "\n\n")
        s1['color'] = color
        printResponses(s1)
    elif edit2 == "birthday":
        birthday = input("\n" + "Edit birthday" + "\n\n")
        s1['birthday'] = birthday
        printResponses(s1)



#with open("survey.json", "r") as read_file:
#    survey = json.load(read_file)


#MAIN CODE
def main():
    takeSurvey()

if __name__ == "__main__":
    main()
