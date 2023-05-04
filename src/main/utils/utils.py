import functools
@functools.total_ordering
class BisectData:
    def __init__(self, employee, reg_id):
        self.__employee = employee
        self.__reg_id = reg_id
    def __lt__(self, empOther):
        return self.__employee._get_name() < empOther.__employee._get_name()
    def _get_employee(self):
        return self.__employee
    def _get_reg_id(self):
        return self.__reg_id