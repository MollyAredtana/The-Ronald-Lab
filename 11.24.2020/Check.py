import csv


#Deal with Parent
ParentStartKB = []
ParentEndKB = []
with open('Parent.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        ParentStartKB.append(row[1])
        ParentEndKB.append(row[2])



#Deal with Mutation File
M_Start_KB = []
M_End_KB = []

# MAP = collections.ChainMap(M_Start_KBwithPOS, M_End_KBwithPOS)

with open('CNV.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if row[3].isnumeric() & row[2].isnumeric():
            M_Start_KB.append(row[3])
            M_End_KB.append(row[10])




StartKB = 0
EndKB = 0

# for interface
# display text
def displayText():
    print("Please Enter StartKB and EndKB Seperatly in the following functions")

# Enter the startKB 
# def InputStartKB():

#Check Start Overlap
count = 1
i = 0
NoOverlapKB = []
StartOverlap = {}
def StartOverlap(): 
    while i < len(M_Start_KB):
        if M_Start_KB[i] == M_Start_KB[count]:
            StartOverlap.update({str(i), "TRUE"})
            count = 0 # recheck from begining
            if M_Start_KB[i + 1] in NoOverlapKB:
                i + 1 + 1 # move on to the next one
            else:
                i + 1 # moving on and not in nooverlap list
        elif count == len(M_Start_KB) - 1: # reach the end and find no overlapping
            NoOverlapKB.append[M_Start_KB[i]] # a checker to avoid repeating check of the no overlapping number
            count = 0 # recheck from begining
            if M_Start_KB[i + 1] in NoOverlapKB:
                i + 1 + 1 # move on to the next one
            else:
                i + 1 # moving on and not in nooverlap list
        else:
            count += 1

        if i == len(M_Start_KB) - 1: # finished checking
            break

        
        






