import csv


#Deal with Parent
ParentStartKB = []
ParentEndKB = []
Parent = []
with open('Parent.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        Parent.append((row[1], row[2]))
        # Parent.append(row[2])
        ParentStartKB.append(row[1])
        ParentEndKB.append(row[2])
        line_count += 1


# We need to fill up all the lacking numbers in Parent so it will
# be easier for us to check in future
Whole_Parent = []
for i in Parent:
    check = i[0]
    Sub_Parent = []
    while check != i[1]:
        Sub_Parent.append(check)
        check = int(check)
        check += 1
        check = str(check)
    Sub_Parent.append(i[1])
    Whole_Parent.append(Sub_Parent)


#Deak with Mutation
Mutation = []
Mutation_Start_KB = []
Mutation_End_KB = []
with open('CNV.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if row[3].isnumeric():
            Mutation.append((row[3], row[10]))
            Mutation_Start_KB.append(row[3])
            Mutation_End_KB.append(row[10])
        line_count += 1

# We need to fill up all the lacking numbers in Mutation so it will
# be easier for us to check in future
Whole_Mutation = []
for i in Mutation:
    check = i[0]
    Sub_Mutation= []
    while check != i[1]:
        Sub_Mutation.append(check)
        check = int(check)
        check += 1
        check = str(check)
    Sub_Mutation.append(i[1])
    Whole_Mutation.append(Sub_Mutation)




StartKB = 0
EndKB = 0

# for interface
# display text
def displayText():
    print("Please Enter StartKB and EndKB Seperatly in the following functions")
    print("EX : if you have 1374 as start KB then please enter the string format, 1374 with double quotes")


def StartOverlap(StartKB): 
    print("Is the Start KB", StartKB, "in The Mutation File?")
    print("The Answer Is")
    StartOverlap = []
    import collections
    StartOverlap = [item for item, count in collections.Counter(Mutation_Start_KB).items() if count > 1]
    if(StartKB in StartOverlap):
        print("TRUE")
    else:
        print("FALSE")



def EndOverlap(EndKB): 
    print("Is the End KB", StartKB, "in The Mutation File?")
    print("The Answer Is")
    EndOverlap = []
    import collections
    EndOverlap = [item for item, count in collections.Counter(Mutation_End_KB).items() if count > 1]
    if(EndKB in EndOverlap):
        print("TRUE")
    else:
        print("FALSE")


def in_Between_Parents(StartKB, EndKB):
    print("Is This In Between Parents?")
    print("The Answer is")

    find = False

    for i in Whole_Parent:
        if StartKB in i:
            find = True
            if EndKB in i:
                print("TRUE")
                break
            else:
                print("FALSE")
                break
        else:
            find = False
    
    if find == False:
        print("FALSE")
        

def parent_in_betaween_mutation(StartKB, EndKB):
    print("Is The Parent In Between Parents?")
    print("The Answer is")
    find = False

    for i in Whole_Mutation:
        if StartKB in i:
            find = True
            if EndKB in i:
                print("TRUE")
                break
            else:
                print("FALSE")
                break
        else:
            find = False
    
    if find == False:
        print("FALSE")
    










        
        






