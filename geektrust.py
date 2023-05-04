from src.main.controller.FileReader import FileReader
from src.main.LMS.LearningManagementSystem import LearningManagementSystem
import sys

def main():
    lms = LearningManagementSystem()
    filename = sys.argv[-1]
    fileReader = FileReader(filename=filename)
    curCmd = fileReader.__next__()
    while (curCmd!=None):
        if (curCmd._get_command_type()!=None):
            lms.runCommand(curCmd)
        curCmd = fileReader.__next__()

if __name__ == "__main__":
    main()
