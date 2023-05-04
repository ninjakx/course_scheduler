from src.main.controller.implementation.AddCourseCmdExecutor import AddCourseCmdExecutor
from src.main.controller.implementation.RegisterCourseCmdExecutor import RegisterCourseCmdExecutor
from src.main.controller.implementation.AllotCourseCmdExecutor import AllotCourseCmdExecutor
from src.main.controller.implementation.CancelCourseCmdExecutor import CancelCourseCmdExecutor
from src.main.enums.CommandType import CommandType

class CommandExecutorFactory:
    def create_command(self, name):
        name = name.replace('-', '_')
        if name == CommandType.ADD_COURSE_OFFERING.name:
            executor = AddCourseCmdExecutor()
            return executor

        elif name == CommandType.REGISTER.name:
            executor = RegisterCourseCmdExecutor()
            return executor

        elif name == CommandType.ALLOT.name or name == CommandType.ALLOT_COURSE.name:
            executor = AllotCourseCmdExecutor()
            return executor

        elif name == CommandType.CANCEL.name:
            executor = CancelCourseCmdExecutor()
            return executor
        
        else:
            return None
