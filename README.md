#  Weka Categorization Commands
![logo](logo.png)

## Python project for running categorization experiments.
it's known that WEKA craches when the input dataset is too big. For this reason you have to run the algorithms from your terminal avoiding the GUI. Because the length of the commands is too big, I developed this programm which takes as input the installation directory of WEKA, the working directory and the filename of the dataset. Then a menu with available algorithms will appeared and you have to choose one. Finally when the algorithm has terminated the results is visible in the terminal.

---

## Built and run

```bash
$ git clone https://github.com/sp1thas/WEKACMDs.git && cd WEKACMDs
$ python WekaCommands.py
```

## Prerequirments
 - Python 2.7
  - termcolor

    Installation (run as root):

```bash
$ pip install -r requirements.txt
```

 - WEKA [link](http://www.cs.waikato.ac.nz/ml/weka/)
 - Your dataset

## Usage
```bash

$ python WekaCommands.py -i <inputfile> -o <outputfile> -w <wekadirectory>
```
```

  -i, --ifile

          This is the input dataset

  -o, --ofile
          This is the output file with classification results
          (model is not contained)

  -w, --wekadir
          Direction with WEKA software

  -h,
          Prints these options
```

## Algorithms Availability


 | Bayes | Availability |
 |---|---|
 | BayesNet | ok |
 | NaiveBayes |ok |
 | NaiveBayesMultinomial | ok |
 | NaiveBayesMultinomialText | ok |
 | NaiveBayesUpdateable | ok |  

 | Functions | Availability |
 |---|---|
 | Logistic | ok |
 | MultilayerPerceptron | ok |
 | SimpleLogistic | ok |
 | SMO | ok |

 | Lazy | Availability |
 |---|---|
 | IBk | ok |
 | KStar | ok |
 | LWL | ok |

 | Meta | Availability |
 |---|---|
 | AdaBoostM1 | - |
 | AdditiveRegression | - |
 | AttributeSelectedClassifier | - |
 | Bagging | ok |
 | ClassificationViaRegression | - |
 | CostSensitiveClassifier | - |
 | CVParameterSelection | - |
 | FilteredClassifier | - |
 | IterativeClassifierOptimizer | - |
 | LogitBoost | - |
 | MultiClassClassifier | - |
 | MultiClassClassifierUpdateable | - |
 | MultiScheme | - |
 | RandomCommittee | - |
 | RandomizableFilteredClassifier | - |
 | RandomSubSpace | - |
 | RegressionByDiscretization | - |
 | Stacking | - |
 | Vote | - |
 | WeightedistancesHandlerWrapper | - |

 | Misc | Availability |
 |---|---|
 | InputMappedClassifier | ok |
 | SerializedClaassifier | - |

 | Rules | Availability |
 |---|---|
 | DecisionTable | ok |
 | JRip | ok |
 | M5Rules | - |
 | OneR | ok |
 | PART | ok |
 | ZeroR | ok |

 | Trees | Availability |
 |---|---|
 | DecisionStump | ok |
 | HoeffdingTree | ok |
 | J48 | ok |
 | LMT | ok |
 | M5P | - |
 | RandomForest | ok |
 | RandomTree | ok |
 | REPTree | ok |

 | EXTRA |
 |---|
 | RBFNetwork |


## Running

run python script with necessery arguments
> ![alt text](https://github.com/sp1thas/WEKAcategorizationCMDs/raw/master/screenshots/1.png "run script")

press enter to continue
> ![alt text](https://github.com/sp1thas/WEKAcategorizationCMDs/raw/master/screenshots/2.png "enter to continue")

choose algorith
> ![alt text](https://github.com/sp1thas/WEKAcategorizationCMDs/raw/master/screenshots/3.png "choose algorithm")

check results
> ![alt text](https://github.com/sp1thas/WEKAcategorizationCMDs/raw/master/screenshots/4.png "see results")

and output file has been generated
## Authors

* **Simakis Panagiotis** - *Initial work*

## License

This project is licensed under the GNU General Public License version 3 - see the [LICENSE](LICENSE) file for details
