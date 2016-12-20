import os
from Setup import *
from Algos import *



# setup weka's directory
WekaDirectory = WekaDir()
# setup the working directory
WorkingDir = WorkingDir()
# setup the file name
FileName = FileName(WorkingDir)

ClassPath = ClassPath(WekaDirectory)


choise = 1

while choise:
    print 'Choise algorithm:'
    print '1. Bagging\n2. J48\n3. MLP\n4. RandomTree\n5. RBFNetwork\n6. REPTree'
    choise = int(raw_input('>>> '))
    if choise == 1:
        Bagging(ClassPath, FileName)
    elif choise == 2:
        J48(ClassPath, FileName)
    elif choise == 3:
        MLP(ClassPath, FileName)
    elif choise == 4:
        RandomTree(ClassPath, FileName)
    elif choise == 5:
        RBFNetwork(ClassPath, FileName)
    elif choise == 6:
        REPTree(ClassPath, FileName)
print 'bye!'
