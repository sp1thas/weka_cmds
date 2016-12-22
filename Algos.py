import menu, subprocess, sys, os

def subprocess_cmd(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    print proc_stdout
    divider()

############## BAYES #################
######################################

def BayesNet(classpath, filename):
    command = classpath + ';'
    command += 'java weka.classifiers.bayes.BayesNet -t '
    command += filename + ' -D -Q weka.classifiers.bayes.net.search.local.K2 -- -P 1 -S BAYES -E weka.classifiers.bayes.net.estimate.SimpleEstimator -- -A 0.5'
    subprocess_cmd(command)
    divider()

def NaiveBayes(classpath, filename):
    command = classpath + ';'
    command += 'java weka.classifiers.bayes.NaiveBayes -t '
    command += filename
    subprocess_cmd(command)

def NaiveBayesMultinomial(classpath, filename):
    command = classpath + ';'
    command += 'java weka.classifiers.bayes.NaiveBayesMultinomial -t '
    command += filename
    subprocess_cmd(command)

def NaiveBayesMultinomialText(classpath, filename):
    command = classpath + ';'
    command += 'java weka.classifiers.bayes.NaiveBayesMultinomialText -t '
    command += filename + ' -P 0 -M 3.0 -norm 1.0 -lnorm 2.0 -stopwords-handler weka.core.stopwords.Null -tokenizer "weka.core.tokenizers.WordTokenizer -delimiters \" \\r\\n\\t.,;:\\\'\\\"()?!\"" -stemmer weka.core.stemmers.NullStemmer'
    subprocess_cmd(command)
    divider()

def NaiveBayesUpdateable(classpath, filename):
    command = classpath + ';'
    command += 'weka.classifiers.bayes.NaiveBayesMultinomialUpdateable -t '
    command += filename
    subprocess_cmd(command)


############# META ###################
######################################
def Bagging(classpath, filename):
    command = classpath + ';'
    command += 'java weka.classifiers.meta.Bagging -P 100 -S 1 -num-slots 1 -I 10 -t '
    command += filename + ' -W weka.classifiers.trees.REPTree -- -M 2 -V 0.001 -N 3 -S 1 -L -1 -I 0.0'
    subprocess_cmd(command)
    divider()


########### RULES ####################
######################################

def ZeroR(classpath, filename):
    command = classpath + ';'
    command += 'java weka.classifiers.rules.ZeroR -t '
    command += filename
    subprocess_cmd(command)


###########FUNCTIONS##################
######################################

def Logistic(classpath, filename):
    command = classpath + ';'
    command += 'java weka.classifiers.functions.Logistic -t '
    command += filename + ' -R 1.0E-8 -M -1 -num-decimal-places 4'
    subprocess_cmd(command)
    divider()

def MLP(classpath, filename):
    command = classpath + ';'
    command += 'java weka.classifiers.functions.MultilayerPerceptron -L 0.3 -M 0.2 -N 500 -V 0 -S 0 -E 20 -H a -t '
    command += filename
    subprocess_cmd(command)
    divider()

def SimpleLogistic(classpath, filename):
    command = classpath + ';'
    command += 'java weka.classifiers.functions.SimpleLogistic -I 0 -M 500 -H 50 -W 0.0 -t '
    command += filename
    subprocess_cmd(command)
    divider()

def SMO(classpath, filename):
    command = classpath + ';'
    command += 'java weka.classifiers.functions.SMO -t '
    command += filename + ' -C 1.0 -L 0.001 -P 1.0E-12 -N 0 -V -1 -W 1 -K "weka.classifiers.functions.supportVector.PolyKernel -E 1.0 -C 250007" -calibrator "weka.classifiers.functions.Logistic -R 1.0E-8 -M -1 -num-decimal-places 4"'
    subprocess_cmd(command)
    divider()


############# LAZY ###################
######################################

def IBk(classpath, filename):
    command = classpath + ';'
    command += 'java weka.classifiers.lazy.IBk -t '
    command += filename + ' -K 1 -W 0 -A "weka.core.neighboursearch.LinearNNSearch -A \"weka.core.EuclideanDistance -R first-last\""'
    subprocess_cmd(command)
    divider()

def KStar(classpath, filename):
    command = classpath + ';'
    command += 'java weka.classifiers.lazy.KStar -B 20 -M a -t '
    command += filename
    subprocess_cmd(command)
    divider()

def LWL(classpath, filename):
    command = classpath + ';'
    command += 'java weka.classifiers.lazy.LWL -t '
    command += filename + ' -U 0 -K -1 -A "weka.core.neighboursearch.LinearNNSearch -A \"weka.core.EuclideanDistance -R first-last\"" -W weka.classifiers.trees.DecisionStump'
    subprocess_cmd(command)
    divider()


############ TREES ###################
######################################

def J48(classpath, filename):
    command = classpath + ';'
    command += 'java weka.classifiers.trees.J48 -C 0.25 -M 2 -t ' + filename
    subprocess_cmd(command)
    divider()

def RandomTree(classpath, filename):
    command = classpath + ';'
    command += 'java weka.classifiers.trees.RandomTree -K 0 -M 1.0 -V 0.001 -S 1 -t '
    command += filename
    subprocess_cmd(command)
    divider()

def REPTree(classpath, filename):
    command = classpath + ';'
    command += 'java weka.classifiers.trees.REPTree -M 2 -V 0.001 -N 3 -S 1 -L -1 -I 0.0 -t '
    command += filename
    subprocess_cmd(command)


############ EXTRA ###################
######################################
def RBFNetwork(classpath, filename):
    command = classpath + ';'
    command += 'java weka.classifiers.functions.RBFNetwork -B 2 -S 1 -R 1.0E-8 -M -1 -W 0.1 -t '
    command += filename + '-W weka.classifiers.trees.REPTree -- -M 2 -V 0.001 -N 3 -S 1 -L -1 -I 0.0'
    subprocess_cmd(command)
    divider()


######################################

def divider():
    print '''
    ========================================================

    ========================================================

    '''
