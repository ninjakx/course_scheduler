# course_scheduler
 
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fninjakx%2Fcourse_scheduler%2F&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

**Context**

The head of the Learning management system (LMS) has hired you as a consultant. The LMS team has the goal of upskilling the employees with the latest topics via courses. You need to help build a system to schedule and manage the courses. 

## Pre-requisites
* Python 3.8/3.9
* Pip

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


