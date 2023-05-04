from aenum import Enum, NoAlias
class CommandType(Enum, settings=NoAlias): # and no of parameters they have
    ADD_COURSE_OFFERING = 5
    REGISTER = 2
    ALLOT = 1
    CANCEL = 1
    ALLOT_COURSE = 1