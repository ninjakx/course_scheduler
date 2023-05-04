import bisect
from src.main.utils.utils import BisectData
    
class Course:
    def __init__(self, course_title, instructor, date, min_employees, max_employees):
        self.__course_title = course_title
        self.__course_id = ""
        self.__instructor = instructor
        self.__date = date
        self.__min_employees = min_employees
        self.__max_employees = max_employees
        self.__course_status = 0
        self.__registered_employees = []

    def _register_employee(self, employee)->str:
        reg_id = f"REG-COURSE-{employee._get_name()}-{self.__course_title}"
        bisect.insort(self.__registered_employees, BisectData(employee, reg_id))
                    #   , key=lambda r: r[0]._get_name())
        return reg_id

    def _remove_register_employee(self, regId):
        for reg in self.__registered_employees:
            if reg._get_reg_id() == regId:
                self.__registered_employees.remove(reg)

    def _match_course(self, course)->bool:
        if self.__course_title == course._get_course_title():
            return True
        else:
            return False    
        
    def _get_course_status(self)->str:
        return self.__course_status

    def _set_course_id(self, course_id):
        self.__course_id = course_id

    def _set_course_status(self, status)->str:
        # alloted or cancelled
        self.__course_status = status
    
    def _get_course_id(self)->str:
        return self.__course_id
    
    def _get_course_title(self)->str:
        return self.__course_title
    
    def _get_instructor(self)->str:
        return self.__instructor
    
    def _get_date(self)->str:
        return self.__date
    
    def _get_min_employees(self)->int:
        return self.__min_employees
    
    def _get_max_employees(self)->int:
        return self.__max_employees
    
    def _get_registered_employees(self)->list:
        return self.__registered_employees
        