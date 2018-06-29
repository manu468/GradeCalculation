
import compute
id = []
a1 = []
a2 = []
test1 = []
test2 = []
project = []
lastName=[]
classData = open('class.txt', 'r')
ass1Data = open('a1.txt', 'r')
ass2Data = open('a2.txt', 'r')
test1Data = open('test1.txt', 'r')
test2Data = open('test2.txt', 'r')
projectData = open('project.txt', 'r')
maxass1 = ass1Data.readline().split("\n")[0]
maxass2 = ass2Data.readline().split("\n")[0]
maxtest1 = test1Data.readline().split("\n")[0]
maxtest2 = test2Data.readline().split("\n")[0]
maxproject = projectData.readline().split("\n")[0]
dictionaryLastName = {}
dictionaryName = {}
dictionaryA1 = {}
dictionaryA2 = {}
dictionaryTest1 = {}
dictionaryTest2 = {}
dictProject = {}
class grade(object):

    def ReadingValues(self):

        count = 0
        for line in classData:
            id.append(line.split("|")[0])
            aValue = grade.nameEdit(grade, str(line.split("|")[2]).replace("\n", ""))
            lastName.append(aValue)

            dictionaryLastName.update({line.split("|")[0]: aValue})

            dictionaryName.update({line.split("|")[0]: grade.nameEdit(grade, line.split("|")[1])})

        for ax in ass1Data:
            k = ax.split("|")[1]
            if ((k == "") | (k == "\n")):
                dictionaryA1.update({ax.split("|")[0]: " "})
            else:
                dictionaryA1.update({ax.split("|")[0]: int(k)})
        for ay in ass2Data:
            l = ay.split("|")[1]
            if ((l == "") | (l == "\n")):
                dictionaryA2.update({ay.split("|")[0]: " "})
            else:

                dictionaryA2.update({ay.split("|")[0]: int(l)})
        for az in test1Data:
            p = az.split("|")[1]
            if ((p == "") | (p == "\n")):
                dictionaryTest1.update({az.split("|")[0]: " "})
            else:

                dictionaryTest1.update({az.split("|")[0]: int(p)})

        for aa in test2Data:
            n = aa.split("|")[1]

            if ((n == "") | (n == "\n")):
                dictionaryTest2.update({aa.split("|")[0]: " "})
            else:

                dictionaryTest2.update({aa.split("|")[0]: int(n)})

        for ab in projectData:
            o = ab.split("|")[1]

            if ((o == "") | (o == "\n")):
                dictProject.update({ab.split("|")[0]: " "})
            else:

                dictProject.update({ab.split("|")[0]: int(o)})

        while (count < len(id)):
            a1.append(dictionaryA1.get(id[count]))
            a2.append(dictionaryA2.get(id[count]))
            test1.append(dictionaryTest1.get(id[count]))
            test2.append(dictionaryTest2.get(id[count]))
            project.append(dictProject.get(id[count]))
            count = count + 1


    def nameEdit(self,name):
        if (len(name) == 1):
            return (name + "     ")
        elif (len(name) == 2):
            return (name + "    ")
        elif (len(name) == 3):
            return (name + "   ")
        elif (len(name) == 4):
            return (name + "  ")
        elif (len(name) == 5):
            return (name + " ")
        else:
            return name

    def DisplayingMenu(self):


        print("1> Display individual component  \n"
              "2> Display component average \n"
              "3> Display Standard Report \n"
              "4> Sort by alternate column \n"
              "5> Change Pass/Fail point \n"
              "6> Exit")

        ini = input()

        if (ini == '1'):
            print("Choose the individual component")
            ini2 = input()
            if ((ini2 == 'a1') | (ini2 == 'A1')):
                l = 0
                print("A1 grades " + "(" + str(maxass1) + ") \n")
                while (l < len(id)):
                    print(id[l] + "\t\t" + str(dictionaryName.get(id[l])) + ", " + str(dictionaryLastName.get(id[l])) + "\t\t" + str(
                        dictionaryA1.get(id[l])))
                    l = l + 1
                print("\n")
                grade.DisplayingMenu(grade)

            elif ((ini2 == 'a2') | (ini2 == 'A2')):
                l = 0
                print("A2 grades " + "(" + str(maxass2) + ") \n")
                while (l < len(id)):
                    print(id[l] + "\t\t" + str(dictionaryName.get(id[l])) + ", " + str(dictionaryLastName.get(id[l])) + "\t\t" + str(
                        dictionaryA2.get(id[l])))
                    l = l + 1
                print("\n")
                grade.DisplayingMenu(grade)



            elif (ini2 == 'test1') | (ini2 == 'Test1'):
                l = 0
                print("Test1 grades " + "(" + str(maxtest1) + ") \n")
                while (l < len(id)):
                    print(id[l] + "\t\t" + str(dictionaryName.get(id[l])) + ", " + str(dictionaryLastName.get(id[l])) + "\t\t" + str(
                        dictionaryTest1.get(id[l])))
                    l = l + 1
                print("\n")
                grade.DisplayingMenu(grade)


            elif ((ini2 == "test2") | (ini2 == "Test2")):

                l = 0
                print("Test2 grades " + "(" + str(maxtest2) + ") \n")
                while (l < len(id)):
                    print(id[l] + "\t\t" + str(dictionaryName.get(id[l])) + ", " + str(dictionaryLastName.get(id[l])) + "\t\t" + str(
                        dictionaryTest2.get(id[l])))
                    l = l + 1
                print("\n")
                grade.DisplayingMenu(grade)


            elif ((ini2 == 'project') | (ini2 == 'Project')):
                l = 0
                print("Project grades " + "(" + str(maxproject) + ") \n")
                while (l < len(id)):
                    print(id[l] + "\t\t" + str(dictionaryName.get(id[l])) + ", " + str(dictionaryLastName.get(id[l])) + "\t\t" + str(
                        dictProject.get(id[l])))
                    l = l + 1
                print("\n")
                grade.DisplayingMenu(grade)


            else:
                print("select a valid option \n")
                grade.DisplayingMenu(grade)

        elif (ini == '2'):
            print("select the component to get average ")
            ini3 = input()
            if ((ini3 == 'a1') | (ini3 == 'A1')):
                compute.compute.A1average(compute.compute, a1, maxass1)
                grade.DisplayingMenu(grade)

            elif ((ini3 == 'a2') | (ini3 == 'A2')):
                compute.compute.A2average(compute.compute, a2, maxass2)
                grade.DisplayingMenu(grade)

            elif (ini3 == 'test1') | (ini3 == 'Test1'):
                compute.compute.Test1average(compute.compute, test1, maxtest1)
                grade.DisplayingMenu(grade)

            elif ((ini3 == 'test2') | (ini3 == 'Test2')):
                compute.compute.Test2average(compute.compute, test2, maxtest2)
                grade.DisplayingMenu(grade)

            elif ((ini3 == 'project') | (ini3 == 'Project')):
                compute.compute.Projectaverage(compute.compute, project, maxproject)
                grade.DisplayingMenu(grade)

            else:
                print("select a valid option")
                grade.DisplayingMenu(grade)

        elif (ini == '3'):
            compute.compute.FinalGrade(compute.compute, id, dictionaryName, dictionaryLastName, dictionaryA1, dictionaryA2, dictionaryTest1, dictionaryTest2, dictProject,
                          maxass1, maxass2, maxtest1, maxtest2, maxproject, 50)
            grade.DisplayingMenu(grade)

        elif (ini == '4'):
            print("choose the order of sorting ")
            ini4 = input()
            if ((ini4 == 'LT') | (ini4 == 'last name') | (ini4 == 'lt') | (
                    ini4 == 'Last Name') ):
                compute.compute.SortByLastName(compute.compute, id, dictionaryName, dictionaryLastName, dictionaryA1, dictionaryA2, dictProject, dictionaryTest1,
                                  dictionaryTest2, maxass1, maxass2, maxtest1, maxtest2, maxproject, lastName)
                grade.DisplayingMenu(grade)

            elif ((ini4 == 'GR')  | (ini4 == 'gr')  | (
                    ini4 == 'Numeric Grade') | (ini4 == 'numericgrade')):
                compute.compute.SortByGrade(compute.compute, id, dictionaryName, dictionaryLastName, dictionaryA1, dictionaryA2, dictProject, dictionaryTest1, dictionaryTest2,
                               maxass1, maxass2, maxtest1, maxtest2, maxproject)
                grade.DisplayingMenu(grade)
            else:
                print("select a valid option")
                grade.DisplayingMenu(grade)

        elif (ini == '5'):
            print("Enter the new Pass/Fail grade")
            default = input()
            compute.compute.FinalGrade(compute.compute, id, dictionaryName, dictionaryLastName, dictionaryA1, dictionaryA2, dictionaryTest1, dictionaryTest2, dictProject,
                          maxass1, maxass2, maxtest1, maxtest2, maxproject, default)
            grade.DisplayingMenu(grade)



        elif (ini == '6'):
            print("Good Bye")
            exit

        else:
            print("select a valid option")
            grade.DisplayingMenu(grade)

grade.ReadingValues(grade)
grade.DisplayingMenu(grade)
