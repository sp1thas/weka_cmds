# -*- coding: utf-8 -*-
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


choise = ''

while not choise == '0':
    print 'Choise algorithm:'
    print '''
    bayes
    ━━━━┓
        ┠── "b1": BayesNet
        ┠── "b2": NaiveBayes
        ┠── "b3": NaiveBayesMultinomial
        ┠── "b4": NaiveBayesMultinomialText
        ┖── "b5": NaiveBayesUpdateable
    functions
    ━━━━┳━━━━
        ┠── "f1": Logistic
        ┠── "f2": MultilayerPerceptron
        ┠── "f3": SimpleLogistic
        ┖── "f4": SMO
    lazy
    ━━━━┓
        ┠── "l1": IBk
        ┠── "l2": KStar
        ┖── "l3": LWL
    meta
    ━━━━┓
        ┃   "m1": AdaBoostM1
        ┃   "m2": AdditiveRegression
        ┃   "m3": AttributeSelectedClassifier
        ┠── "m4": Bagging
        ┃   "m5": ClassificationViaRegression
        ┃   "m6": CostSensitiveClassifier
        ┃   "m7": CVParameterSelection
        ┃   "m8": FilteredClassifier
        ┃   "m9": IterativeClassifierOptimizer
        ┃   "m10": LogitBoost
        ┃   "m11": MultiClassClassifier
        ┃   "m12": MultiClassClassifierUpdateable
        ┃   "m13": MultiScheme
        ┃   "m14": RandomCommittee
        ┃   "m14": RandomizableFilteredClassifier
        ┃   "m15": RandomSubSpace
        ┃   "m16": RegressionByDiscretization
        ┃   "m17": Stacking
        ┃   "m18": Vote
        ┃   "m19": WeightedistancesHandlerWrapper
    misc
    ━━━━┓
        ┃   "mi1": InputMappedClassifier
        ┃   "mi2": SerializedClaassifier
    rules
    ━━━━┓
        ┃   "r1": DecisionTable
        ┃   "r2": JRip
        ┃   "r3": M5Rules
        ┃   "r4": OneR
        ┃   "r5": PART
        ┖── "r6": ZeroR
    trees
    ━━━━┓
        ┃ "t1": DecisionStump
        ┃ "t2": HoeffdingTree
        ┠── "t3": J48
        ┃ "t4": LMT
        ┃ "t5": M5P
        ┃ "t6": RandomForest
        ┠── "t7": RandomTree
        ┖── "t8": REPTree
    extra
    ━━━━┓
        ┖── "e1": RBFNetwork
    EXIT
    ━━━━┓
        ┖── "0"
    '''
    choise = raw_input('>>> ')

    # bayes codeblock
    if choise[0]  == 'b':
        if choise[1]  == 1: BayesNet(ClassPath, FileName)
        elif choise[1]  == 2: NaiveBayes(ClassPath, FileName)
        elif choise[1]  == 3: NaiveBayesMultinomial(ClassPath, FileName)
        elif choise[1]  == 4: NaiveBayesMultinomialText(ClassPath, FileName)
        elif choise[1]  == 5: NaiveBayesUpdateable(ClassPath, FileName)

    # fuctions codeblock
    elif choise[0]  == 'f':
        if choise[1]  == '1': Logistic(ClassPath, FileName)
        elif choise[1]  == '2': MLP(ClassPath, FileName)
        elif choise[1]  == '3': SimpleLogistic(ClassPath, FileName)
        elif choise[1]  == '4': SMO(ClassPath, FileName)

    # lazy codeblock
    elif choise[0]  == 'l':
        if choise[1]  == '1': IBk(ClassPath, FileName)
        elif choise[1]  == '2': KStar(ClassPath, FileName)
        elif choise[1]  == '3': LWL(ClassPath, FileName)

    # meta codeblock
    elif choise[0]  == 'm' and len(a)>2:
        if choise[1:]  == '1': pass
        elif choise[1:]  == '2': pass
        elif choise[1:]  == '3': pass
        elif choise[1:]  == '4': Bagging(ClassPath, FileName)
        elif choise[1:]  == '5': pass
        elif choise[1:]  == '6': pass
        elif choise[1:]  == '7': pass
        elif choise[1:]  == '8': pass
        elif choise[1:]  == '9': pass
        elif choise[1:]  == '10': pass
        elif choise[1:]  == '11': pass
        elif choise[1:]  == '12': pass
        elif choise[1:]  == '13': pass
        elif choise[1:]  == '14': pass
        elif choise[1:]  == '15': pass
        elif choise[1:]  == '16': pass
        elif choise[1:]  == '17': pass
        elif choise[1:]  == '18': pass
        elif choise[1:]  == '19': pass

    # misc codeblock
    elif choise[0:2] == 'mi':
        if choise[2] == '1': pass
        elif choise[2] == '2': pass

    # rules codeblock
    elif choise[0]  == 'r':
        if choise[1]  == 1: pass
        elif choise[1]  == 2: pass
        elif choise[1]  == 3: pass
        elif choise[1]  == 4: pass
        elif choise[1]  == 5: pass
        elif choise[1]  == 6: ZeroR(ClassPath, FileName)

    # trees codeblock
    elif choise[0]  == 't':
        if choise[1] == '1': pass
        elif choise[1] == '2': pass
        elif choise[1] == '3': J48(ClassPath, FileName)
        elif choise[1] == '4': pass
        elif choise[1] == '5': pass
        elif choise[1] == '6': RandomForest(ClassPath, FileName)
        elif choise[1] == '7': RandomTree(ClassPath, FileName)
        elif choise[1] == '8': REPTree(ClassPath, FileName)

    elif choise  == 'e':
        if choise[1] == '1': RBFNetwork(ClassPath, FileName)


print 'bye!'
