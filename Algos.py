import menu, subprocess, sys, os

def subprocess_cmd(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    print proc_stdout
    divider()

def Bagging(classpath, filename):
    command = classpath + ';'
    command += 'java weka.classifiers.meta.Bagging -P 100 -S 1 -num-slots 1 -I 10 -t '
    command += filename + ' -W weka.classifiers.trees.REPTree -- -M 2 -V 0.001 -N 3 -S 1 -L -1 -I 0.0'
    subprocess_cmd(command)
    divider()

def J48(classpath, filename):
    command = classpath + ';'
    command += 'java weka.classifiers.trees.J48 -C 0.25 -M 2 -t ' + filename
    subprocess_cmd(command)
    divider()

def MLP(classpath, filename):
    command = classpath + ';'
    command += 'java weka.classifiers.functions.MultilayerPerceptron -L 0.3 -M 0.2 -N 500 -V 0 -S 0 -E 20 -H a -t '
    command += filename
    subprocess_cmd(command)
    divider()

def RandomTree(classpath, filename):
    command = classpath + ';'
    command += 'java weka.classifiers.trees.RandomTree -K 0 -M 1.0 -V 0.001 -S 1 -t '
    command += filename
    subprocess_cmd(command)
    divider()

def RBFNetwork(classpath, filename):
    command = classpath + ';'
    command += 'java weka.classifiers.functions.RBFNetwork -B 2 -S 1 -R 1.0E-8 -M -1 -W 0.1 -t '
    command += filename + '-W weka.classifiers.trees.REPTree -- -M 2 -V 0.001 -N 3 -S 1 -L -1 -I 0.0'
    subprocess_cmd(command)
    divider()

def REPTree(classpath, filename):
    command = classpath + ';'
    command += 'java weka.classifiers.trees.REPTree -M 2 -V 0.001 -N 3 -S 1 -L -1 -I 0.0 -t '
    command += filename
    subprocess_cmd(command)

def divider():
    print '''
    ========================================================

    ========================================================

    '''
