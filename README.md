#  Weka Categorization Commands
![logo](logo.png)

## Python project for running categorization experiments.
it's known that WEKA craches when the input dataset is too big. For this reason you have to run the algorithms from your terminal avoiding the GUI. Because the length of the commands is too big, I developed this programm which takes as input the installation directory of WEKA, the working directory and the filename of the dataset. Then a menu with available algorithms will appeared and you have to choose one. Finally when the algorithm has terminated the results is visible in the terminal.

---

## Built and run

```bash
git clone https://github.com/sp1thas/Weka-Categorization-Commands.git && cd Weka-Categorization-Commands
python WekaCommands.py
```

## Prerequirments
 - Python 2.7
  - termcolor

    Installation (run as root):
    ```bash
    
      $ pip install termcolor
      
      ```
 - WEKA [link](http://www.cs.waikato.ac.nz/ml/weka/)
 - Your dataset


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

run python script. First insert the installation directory of Weka.

> ![alt text](https://github.com/sp1thas/WEKAcategorizationCMDs/raw/master/screenshots/1.png "Run script...")

then insert the directory of the dataset

> ![alt text](https://github.com/sp1thas/WEKAcategorizationCMDs/raw/master/screenshots/2.png "Run script...")

.. the filename of dataset

> ![alt text](https://github.com/sp1thas/WEKAcategorizationCMDs/raw/master/screenshots/3.png "Run script...")

and finally choose the algorithm of your choise

> ![alt text](https://github.com/sp1thas/WEKAcategorizationCMDs/raw/master/screenshots/4.png "Run script...")

and get the output

> ![alt text](https://github.com/sp1thas/WEKAcategorizationCMDs/raw/master/screenshots/5.png "Run script...")

## Authors

* **Simakis Panagiotis** - *Initial work*

## License

This project is licensed under the GNU General Public License version 3 - see the [LICENSE](LICENSE) file for details
