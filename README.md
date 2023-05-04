# course_scheduler

## Pre-requisites
* Python 3.8/3.9
* Pip

# How to run the code

We have provided scripts to execute the code. 

Use `run.sh` if you are Linux/Unix/macOS Operating systems and `run.bat` if you are on Windows.  Both the files run the commands silently and prints only output from the input file `sample_input/input1.txt`. You are supposed to add the input commands in the file from the appropriate problem statement. 

Internally both the scripts run the following commands 

 * `pip install -r requirements.txt` - This will install the dependencies mentioned in the requirement.file
 * `python -m geektrust sample_input/input1.txt` - This will run the solution passing in the sample input file as the command line argument

If you are providing a solution without using the build file, we want you to name your Main file as geektrust.py. This is the file that will contain your main method.

 We expect your program to take the location to the text file as parameter. Input needs to be read from a text file, and output should be printed to the console. The text file will contain only commands in the format prescribed by the respective problem.

 ## Running the code for multiple test cases

 Please fill `input1.txt` and `input2.txt` with the input commands and use those files in `run.bat` or `run.sh`. Replace `python -m geektrust sample_input/input1.txt` with `python -m geektrust sample_input/input2.txt` to run the test case from the second file. 

 ## How to execute the unit tests

 `python -m unittest discover` will execute the unit test cases.

 The unit test coverage is found by the command :
`coverage run -m unittest discover`

This covers Design patterns like singleton, also uses interfaces and following:

**Object Modelling (OOPS)** 
- Solution follows some modelling principles. 
- Code maintains encapsulation. No encapsulation breakages were found. 

**Readability**
- Solution follows clean code principles and is well readable.
- Code follows the single responsibility principle.
- Code is structured and split across multiple files thereby improving its readability.
- Code is written with compact methods. Shorter, compact methods help in improving readability.
- Code has good usage of easily understandable names for methods, classes, and variables. This makes code easy to understand.
- Submission has very few magic numbers, making it easy to read and maintain. 

**Unit Tests** 
- Contains all the unit tests for every methods.

**Build**
- Not getting build there :/ but works fine in the local environment.


**Maintainability** 
- Code is maintainable. It doesn’t contain complex methods. Code is spread evenly across methods.
- Code had minimal code duplication. The submission follows DRY principles. This helps in increasing readability and helps in maintaining code. 

**Correctness( I/O)**
Some issue in the portal side not running there. 

### To run the app:

```bash
bash run.sh
```

**Output:**
```
OFFERING-PYTHON-JOHN
REG-COURSE-WOO-PYTHON ACCEPTED
REG-COURSE-ANDY-PYTHON ACCEPTED
REG-COURSE-BOBY-PYTHON ACCEPTED
REG-COURSE-BOBY-PYTHON CANCEL_ACCEPTED
REG-COURSE-ANDY-PYTHON ANDY@GMAIL.COM OFFERING-PYTHON-JOHN PYTHON JOHN 05062022 CONFIRMED
REG-COURSE-WOO-PYTHON WOO@GMAIL.COM OFFERING-PYTHON-JOHN PYTHON JOHN 05062022 CONFIRMED
```

### To see the coverage:

```bash
coverage run -m unittest discover
```
OR
```python3
python3 -m unittest 
```

**Output:**

```
.OFFERING-JAVA-JAMES
...REG-COURSE-WOO-JAVA CANCEL_REJECTED
..REG-COURSE-WOO-JAVA CANCEL_ACCEPTED
................INPUT_DATA_ERROR
......
----------------------------------------------------------------------
Ran 28 tests in 0.013s

OK
```

### To run particular test:

```python3
python3 -m unittest src/tests/CmdExecutorTest/test_CancelCourseCmdExecutor.py
```

**Output:**

```
REG-COURSE-WOO-JAVA CANCEL_REJECTED
..REG-COURSE-WOO-JAVA CANCEL_ACCEPTED
.
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

### To remove pycache:

```bash
find . -type d -name __pycache__ -exec rm -r {} \+
```


