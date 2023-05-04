"""
    Reads the content from the file.
    Validates if it is valid or not.
    Call command extractor for each line of the file.
"""
from src.main.controller.CommandExtractor import CommandExtractor

class FileReader:
    def __init__(self, filename):
        self.__filename = filename
        self.__file = open(filename)

    def check_extension(self, filePath)->bool:
        file_extension = filePath.split(".")[-1]
        if file_extension == "txt":
            return True
        else:
            return False
        
    def __iter__(self):
        return self
    
    def __next__(self):
        line = self.__file.readline()
        if line.strip()=="":
            self.__file.close()
            return None
        cExtr = CommandExtractor().extract_command(line.strip())
        return cExtr