# -*- coding: utf-8 -*-
import subprocess, sys, os, pprint

def subprocess_cmd(command, output):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    print(proc_stdout.decode('utf-8', 'ignore'))
    file = open(output,'w')
    file.write(proc_stdout.decode('utf-8', 'ignore'))
    file.close()

############## BAYES #################
######################################

def BayesNet(classpath, filename, output):
    command = ( classpath + ';' +
                'java weka.classifiers.bayes.BayesNet -t ' + filename +
                ' -D -Q weka.classifiers.bayes.net.search.local.K2 -- -P 1 -S BAYES -E weka.classifiers.bayes.net.estimate.SimpleEstimator -- -A 0.5' )
    subprocess_cmd(command, output)

def NaiveBayes(classpath, filename, output):
    command = ( classpath + ';' +
                'java weka.classifiers.bayes.NaiveBayes -t ' +
                filename )
    subprocess_cmd(command, output)

def NaiveBayesMultinomial(classpath, filename, output):
    command = ( classpath + ';' +
                'java weka.classifiers.bayes.NaiveBayesMultinomial -t ' +
                filename )
    subprocess_cmd(command, output)

def NaiveBayesMultinomialText(classpath, filename, output):
    command = ( classpath + ';' +
                'java weka.classifiers.bayes.NaiveBayesMultinomialText -t ' +
                filename + ' -P 0 -M 3.0 -norm 1.0 -lnorm 2.0 -stopwords-handler weka.core.stopwords.Null -tokenizer "weka.core.tokenizers.WordTokenizer -delimiters \" \\r\\n\\t.,;:\\\'\\\"()?!\"" -stemmer weka.core.stemmers.NullStemmer' +
                output )
    subprocess_cmd(command, output)

def NaiveBayesUpdateable(classpath, filename, output):
    command = ( classpath + ';' +
                'java weka.classifiers.bayes.NaiveBayesMultinomialUpdateable -t ' +
                filename )
    subprocess_cmd(command, output)


############# META ###################
######################################
def Bagging(classpath, filename, output):
    command = ( classpath + ';' +
                'java weka.classifiers.meta.Bagging -P 100 -S 1 -num-slots 1 -I 10 -t ' +
                filename + ' -W weka.classifiers.trees.REPTree -- -M 2 -V 0.001 -N 3 -S 1 -L -1 -I 0.0' )
    subprocess_cmd(command, output)
################ MISC ################
######################################
def InputMappedClassifier(classpath, filename, output):
    command = ( classpath + ';' +
                'java weka.classifiers.misc.InputMappedClassifier -t ' +
                filename + ' -I -trim -W weka.classifiers.rules.ZeroR' )
    subprocess_cmd(command, output)

########### RULES ####################
######################################
def DecisionTable(classpath, filename, output):
    command = ( classpath + ';' +
                'java weka.classifiers.rules.DecisionTable -t ' +
                filename + ' -X 1 -S "weka.attributeSelection.BestFirst -D 1 -N 5"' )
    subprocess_cmd(command, output)

def JRip(classpath, filename, output):
    command = ( classpath + ';' +
                'java weka.classifiers.rules.JRip -F 3 -N 2.0 -O 2 -S 1 -t ' +
                filename )
    subprocess_cmd(command, output)

def OneR(classpath, filename, output):
    command = ( classpath + ';' +
                'java weka.classifiers.rules.ZeroR -t ' +
                filename )
    subprocess_cmd(command, output)

def PART(classpath, filename, output):
    command = ( classpath + ';' +
                'java weka.classifiers.rules.PART -M 2 -C 0.25 -Q 1 -t ' +
                filename )
    subprocess_cmd(command, output)


def ZeroR(classpath, filename, output):
    command = ( classpath + ';' +
                'java weka.classifiers.rules.OneR -B 6 -t ' +
                filename )
    subprocess_cmd(command, output)


###########FUNCTIONS##################
######################################

def Logistic(classpath, filename, output):
    command = ( classpath + ';' +
                'java weka.classifiers.functions.Logistic -t ' +
                filename + ' -R 1.0E-8 -M -1 -num-decimal-places 4' )
    subprocess_cmd(command, output)

def MLP(classpath, filename, output):
    command = ( classpath + ';' +
                'java weka.classifiers.functions.MultilayerPerceptron -L 0.3 -M 0.2 -N 500 -V 0 -S 0 -E 20 -H a -t ' +
                filename )
    subprocess_cmd(command, output)

def SimpleLogistic(classpath, filename, output):
    command = ( classpath + ';' +
                'java weka.classifiers.functions.SimpleLogistic -I 0 -M 500 -H 50 -W 0.0 -t ' +
                filename )
    subprocess_cmd(command, output)

def SMO(classpath, filename, output):
    command = ( classpath + ';' +
                'java weka.classifiers.functions.SMO -t ' +
                ' -C 1.0 -L 0.001 -P 1.0E-12 -N 0 -V -1 -W 1 -K "weka.classifiers.functions.supportVector.PolyKernel -E 1.0 -C 250007" -calibrator "weka.classifiers.functions.Logistic -R 1.0E-8 -M -1 -num-decimal-places 4"' )
    subprocess_cmd(command, output)


############# LAZY ###################
######################################

def IBk(classpath, filename, output):
    command = ( classpath + ';' +
                'java weka.classifiers.lazy.IBk -t ' +
                filename + ' -K 1 -W 0 -A "weka.core.neighboursearch.LinearNNSearch -A \\"weka.core.EuclideanDistance -R first-last\\""' )
    subprocess_cmd(command, output)

def KStar(classpath, filename, output):
    command = ( classpath + ';' +
                'java weka.classifiers.lazy.KStar -B 20 -M a -t ' +
                filename )
    subprocess_cmd(command, output)

def LWL(classpath, filename, output):
    command = ( classpath + ';' +
                'java weka.classifiers.lazy.LWL -t ' +
                filename + ' -U 0 -K -1 -A "weka.core.neighboursearch.LinearNNSearch -A \\"weka.core.EuclideanDistance -R first-last\\"" -W weka.classifiers.trees.DecisionStump' )
    subprocess_cmd(command, output)


############ TREES ###################
######################################

def DecisionStump(classpath, filename, output):
    command = ( classpath + ';' +
                'java weka.classifiers.trees.DecisionStump -t ' +
                filename )
    subprocess_cmd(command, output)

def HoeffdingTree(classpath, filename, output):
    command = ( classpath + ';' +
                'java weka.classifiers.trees.HoeffdingTree -L 2 -S 1 -E 1.0E-7 -H 0.05 -M 0.01 -G 200.0 -N 0.0 -t ' +
                filename )
    subprocess_cmd(command, output)

def J48(classpath, filename, output):
    command = ( classpath + ';' +
                'java weka.classifiers.trees.J48 -C 0.25 -M 2 -t ' +
                filename )
    subprocess_cmd(command, output)

def LMT(classpath, filename, output):
    command = ( classpath + ';' +
                'java weka.classifiers.trees.LMT -I -1 -M 15 -W 0.0 -t ' +
                filename )
    subprocess_cmd(command, output)

def RandomForest(classpath, filename, output):
    command = ( classpath + ';' +
                'java weka.classifiers.trees.RandomForest -P 100 -I 100 -num-slots 1 -K 0 -M 1.0 -V 0.001 -S 1 -t ' +
                filename )
    subprocess_cmd(command, output)


def RandomTree(classpath, filename, output):
    command = ( classpath + ';' +
                'java weka.classifiers.trees.RandomTree -K 0 -M 1.0 -V 0.001 -S 1 -t ' +
                filename )
    subprocess_cmd(command, output)

def REPTree(classpath, filename, output):
    command = ( classpath + ';' +
                'java weka.classifiers.trees.REPTree -M 2 -V 0.001 -N 3 -S 1 -L -1 -I 0.0 -t ' +
                filename )
    subprocess_cmd(command, output)


############ EXTRA ###################
######################################
def RBFNetwork(classpath, filename):
    command = ( classpath + ';' +
                'java weka.classifiers.functions.RBFNetwork -B 2 -S 1 -R 1.0E-8 -M -1 -W 0.1 -t ' +
                filename + '-W weka.classifiers.trees.REPTree -- -M 2 -V 0.001 -N 3 -S 1 -L -1 -I 0.0' )
    subprocess_cmd(command, output)


######################################

def divider():
    print ('''
    ========================================================''')
