# this file setups the working directory, weka, and filename
import os

def WekaDir():
    # insert weka directory
    weka_dir = raw_input("First of all insert the installation path of Weka:\n>>> ")
    if not weka_dir.endswith('/'):
        weka_dir += '/weka.jar'
    else:
        weka_dir += 'weka.jar'
    # check weka directory
    while not os.path.exists(weka_dir):
        weka_dir = raw_input("*** WRONG PATH *** try again:\n>>> ")
        if not weka_dir.endswith('/'):
            weka_dir += '/weka.jar'
        else:
            weka_dir += 'weka.jar'
    return weka_dir
    print 'I \'ve got the path of weka'
    return weka_dir


def WorkingDir():
    working_dir = raw_input("Insert the working directory:\n>>> ")
    while not os.path.isdir(working_dir):
        working_dir = raw_input("*** WRONG DIRECTRORY *** try again:\n>>> ")
    return working_dir


def FileName(working_dir):
    if working_dir.endswith('/'):
        file_name = working_dir + raw_input("Insert the file name of dataset:\n>>> ")
    else:
        file_name = working_dir + '/' + raw_input("Insert the file name of dataset:\n>>> ")

    while not os.path.exists(file_name):
        file_name = raw_input("*** WRONG FILENAME *** try again\n>>> ")
    return file_name


def ClassPath(working_dir):
    return 'export CLASSPATH=$CLASSPATH:'+ working_dir
