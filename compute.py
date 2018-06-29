
dictionaryGrades = {}
percent = []
dictionaryPercentage = {}
class compute(object):

    maxAss1=0
    id=[]
    def __init__(self):
        print(" ")


    def A1average(self, a1, maxass1):
        l = len(a1)
        s = 0
        for m in a1:
            s = s + int(compute.SpaceRemove(self, m))
        print( "A1 average: " + str(s / l) + "/" + str(maxass1) + "\n")

    def A2average(self, a2, maxass2):
        l = len(a2)
        s = 0
        for m in a2:
            s = s + int(compute.SpaceRemove(self,m))
        print("A2 average: " + str(s / l) + "/" + str(maxass2) + "\n")


    def Test1average(self, test1, maxtest1):
        l = len(test1)
        s = 0
        for m in test1:
            s = s + int(compute.SpaceRemove(self,m))
        print("Test1 average: " + str(s / l) + "/" + str(maxtest1) + "\n")


    def Test2average(self, test2, maxtest2):
        l = len(test2)
        s = 0
        for m in test2:
            s = s + int(compute.SpaceRemove(self,m))
        print("Test2 average: " + str(s / l) + "/" + str(maxtest2) + "\n")


    def Projectaverage(self, project, maxproject):
        l = len(project)
        s = 0
        for m in project:
            s = s + int(compute.SpaceRemove(self,m))
        print("Project average: " + str(s / l) + "/" + str(maxproject) + "\n")

    def calculatePercentage(self, id, dictionaryA1, dictionaryA2, dictionaryTest1, dictionaryTest2, dictionaryProject, maxass1, maxass2, maxtest1, maxtest2, maxproject, dummy):
        k = 0
        while (k < len(id)):

            percentage = ((int(compute.SpaceRemove(self, dictionaryA1.get(id[k]))) / int(maxass1)) * 7.5) + ((int(compute.SpaceRemove(self, dictionaryA2.get(id[k]))) / int(maxass2)) * 7.5) + ((int(compute.SpaceRemove(self, dictionaryTest1.get(id[k]))) / int(maxtest1)) * 30) + ((int(compute.SpaceRemove(self, dictionaryTest2.get(id[k]))) / int(maxtest2)) * 30) + ((int(compute.SpaceRemove(self, dictionaryProject.get(id[k]))) / int(maxproject)) * 25)
            percent.append(percentage)
            dictionaryPercentage.update({id[k]: int(percentage)})
            if ((percentage >= int(dummy) + 42)):
                dictionaryGrades.update({id[k]: "A+"})

            elif ((percentage >= int(dummy) + 35) & (percentage < int(dummy) + 42)):
                dictionaryGrades.update({id[k]: "A"})

            elif ((percentage >= int(dummy) + 28) & (percentage < int(dummy) + 35)):
                dictionaryGrades.update({id[k]: "A-"})

            elif ((percentage >= int(dummy) + 21) & (percentage < int(dummy) + 28)):
                dictionaryGrades.update({id[k]: "B+"})

            elif ((percentage >= int(dummy) + 14) & (percentage < int(dummy) + 21)):
                dictionaryGrades.update({id[k]: "B"})

            elif ((percentage >= int(dummy) + 7) & (percentage < int(dummy) + 14)):
                dictionaryGrades.update({id[k]: "B-"})

            elif ((percentage >= int(dummy)) & (percentage < int(dummy) + 7)):
                dictionaryGrades.update({id[k]: "C"})

            else:
                dictionaryGrades.update({id[k]: "F"})

            k = k + 1



    def FinalGrade(self, id, dictionaryName, dictionaryLastName, dictionaryA1, dictionaryA2, dictionaryTest1, dictionaryTest2, dictionaryProject, maxass1, maxass2, maxtest1, maxtest2, maxproject, default_value):

        compute.calculatePercentage(self, id, dictionaryA1, dictionaryA2, dictionaryTest1, dictionaryTest2, dictionaryProject, maxass1, maxass2, maxtest1, maxtest2, maxproject, default_value)

        print("ID \t\tLN  \t\t FN \t\tA1 \t    A2 \t\tPR \t\tT1 \t\tT2 \t\tGR \t\t  FL \n")
        j=0
        while(j<len(id)):

           print(str(id[j]) + " \t" + str(dictionaryLastName.get(id[j])) + "\t\t" + str(dictionaryName.get(id[j])) +
                 "\t\t" + str(dictionaryA1.get(id[j])) + "\t\t" + str(dictionaryA2.get(id[j])) + "\t\t" +
                 str(dictionaryProject.get(id[j])) + "\t\t" + str(dictionaryTest1.get(id[j])) + "\t\t" +
                 str(dictionaryTest2.get(id[j])) + "\t\t" + str(dictionaryPercentage.get(id[j])) + "\t\t  " + str(dictionaryGrades.get(id[j])) + "\n")

           j=j+1

    def SortByLastName(self, id, dictionaryName, dictionaryLastName, dictionaryA1, dictionaryA2, dictionaryProject, dictionaryTest1, dictionaryTest2, maxass1, maxass2, maxtest1, maxtest2, maxproject, lastName):

        compute.calculatePercentage(self, id, dictionaryA1, dictionaryA2, dictionaryTest1, dictionaryTest2, dictionaryProject, maxass1, maxass2, maxtest1, maxtest2, maxproject, 50)
        newid=[]
        a=0
        while(a<len(id)):
            for i, na in dictionaryLastName.items():
                search = sorted(lastName)[a]
                if(na == str(search)):
                    newid.append(i)

            a=a+1

        print("ID \t\tLN  \t\t FN \t\tA1 \t    A2 \t\tPR \t\tT1 \t\tT2 \t\tGR \t\t  FL \n")
        j = 0
        while (j < len(newid)):

            print(str(newid[j]) + " \t" + str(dictionaryLastName.get(newid[j])) + "\t\t" + str(dictionaryName.get(newid[j])) +
                  "\t\t" + str(dictionaryA1.get(newid[j])) + "\t\t" + str(dictionaryA2.get(newid[j])) + "\t\t" +
                  str(dictionaryProject.get(newid[j])) + "\t\t" + str(dictionaryTest1.get(newid[j])) + "\t\t" +
                  str(dictionaryTest2.get(newid[j])) + "\t\t" + str(dictionaryPercentage.get(newid[j])) + "\t\t  " + str(dictionaryGrades.get(newid[j])) + "\n")

            j = j + 1

        newid.clear()
        percent.clear()




    def SpaceRemove(self, field):
        if(field == " "):
            return 0
        else:
            return field


    def SortByGrade(self, id, dictionaryName, dictionaryLastName, dictionaryA1, dictionaryA2, dictionaryProject, dictionaryTest1, dictionaryTest2, maxass1, maxass2, maxtest1, maxtest2, maxproject):

        compute.calculatePercentage(self, id, dictionaryA1, dictionaryA2, dictionaryTest1, dictionaryTest2, dictionaryProject, maxass1, maxass2, maxtest1, maxtest2, maxproject, 50)
        newid1 = []
        a = 0
        while (a < len(percent)):
            for i, na in dictionaryPercentage.items():
                search = sorted(percent, reverse = True)[a]
                if (na == int(search)):
                    newid1.append(i)

            a = a + 1



        print("ID \t\tLN  \t\t FN \t\tA1 \t    A2 \t\tPR \t\tT1 \t\tT2 \t\tGR \t\t  FL \n")
        i = 0
        while (i < len(newid1)):
            print(str(newid1[i]) + " \t" + str(dictionaryLastName.get(newid1[i])) + "\t\t" + str(
                dictionaryName.get(newid1[i])) + "\t\t" + str(dictionaryA1.get(newid1[i])) + "\t\t" + str(
                dictionaryA2.get(newid1[i])) + "\t\t" + str(dictionaryProject.get(newid1[i])) + "\t\t" + str(
                dictionaryTest1.get(newid1[i])) + "\t\t" + str(dictionaryTest2.get(newid1[i])) + "\t\t" + str(dictionaryPercentage.get(newid1[i])) + "\t\t  " + str(dictionaryGrades.get(newid1[i])) + "\n")

            i = i + 1
        percent.clear()
        newid1.clear()


