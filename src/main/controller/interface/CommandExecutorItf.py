# interface will be defined here
import zope.interface
  
class CommandExecutorItf(zope.interface.Interface):
    # x = zope.interface.Attribute("foo")
    # def method1(self, x):
    #     pass
    def executeCommand(self, coursesDet, regIDvsCourse, command_attributes):
        pass
    #   void executeCommand(TreeMap<String, Course> courses, Map<String, Course> registrationIdCourseMap, Command command) throws InvalidInputException, CourseFullException;
