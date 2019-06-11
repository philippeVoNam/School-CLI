import npyscreen

# if __name__ == "__main__":
#     App = ExamForm()
#     App.run()
#     info = App.get_form_info()
#     print(info["date"])

class ExamForm(npyscreen.NPSApp):
    def main(self):
        # These lines create the form and populate it with widgets.
        # A fairly complex screen in only 8 or so lines of code - a line for each control.
       self.F  = npyscreen.Form(name = "Exam Form",)
       self.classCode   = self.F.add(npyscreen.TitleText, name='Class Code :')
       self.date        = self.F.add(npyscreen.TitleDateCombo, name='Date :')
       self.type        = self.F.add(npyscreen.TitleSelectOne, max_height=4, value = [0,], name="Type",
                          values = ["Quiz","Midterm","Final Exam"], scroll_exit=True)
       self.description = self.F.add(npyscreen.MultiLineEdit,
                          value = """# Author : Philippe Vo \n# Date : 
                          """,
                          max_height=10, rely=8)

        # This lets the user interact with the Form.
       self.F.edit()

    def get_form_info(self) :
        info = {
            "classCode": self.classCode.value,
            "date": self.date.value,
            "type": self.type.get_selected_objects()[0],
            "description": self.description.value
        }

        return info

class AssignmentForm(npyscreen.NPSApp):
    def main(self):
        # These lines create the form and populate it with widgets.
        # A fairly complex screen in only 8 or so lines of code - a line for each control.
       self.F  = npyscreen.Form(name = "Assignment Form",)
       self.classCode   = self.F.add(npyscreen.TitleText, name='Class Code :')
       self.title   = self.F.add(npyscreen.TitleText, name='Title :')
       self.date        = self.F.add(npyscreen.TitleDateCombo, name='Date :')
       self.filePath = self.F.add(npyscreen.TitleFilenameCombo, name="Filepath :")
       self.totalNumbers2Do = self.F.add(npyscreen.TitleText, name='How many # :')
       self.description = self.F.add(npyscreen.MultiLineEdit,
                          value = """# Author : Philippe Vo \n# Date : 
                          """,
                          max_height=10, rely=9)

        # This lets the user interact with the Form.
       self.F.edit()

    def get_form_info(self) :
        info = {
            "classCode": self.classCode.value,
            "title": self.title.value,
            "filepath": self.filePath.value,
            "date": self.date.value,
            "description": self.description.value,
            "totalNumbers": self.totalNumbers2Do.value
        }

        return info

class LabReportForm(npyscreen.NPSApp):
    def main(self):
        # These lines create the form and populate it with widgets.
        # A fairly complex screen in only 8 or so lines of code - a line for each control.
       self.F  = npyscreen.Form(name = "Lab Report Form",)
       self.classCode   = self.F.add(npyscreen.TitleText, name='Class Code :')
       self.title   = self.F.add(npyscreen.TitleText, name='Title :')
       self.date        = self.F.add(npyscreen.TitleDateCombo, name='Date :')
       self.totalNumbers2Do = self.F.add(npyscreen.TitleText, name='How many # :')
       self.description = self.F.add(npyscreen.MultiLineEdit,
                          value = """# Author : Philippe Vo \n# Date : 
                          """,
                          max_height=10, rely=9)

        # This lets the user interact with the Form.
       self.F.edit()

    def get_form_info(self) :
        info = {
            "classCode": self.classCode.value,
            "title": self.title.value,
            "date": self.date.value,
            "description": self.description.value,
            "totalNumbers": self.totalNumbers2Do.value
        }

        return info
        
class HomeworkForm(npyscreen.NPSApp):
    def main(self):
        # These lines create the form and populate it with widgets.
        # A fairly complex screen in only 8 or so lines of code - a line for each control.
       self.F  = npyscreen.Form(name = "Homework Form",)
       self.classCode   = self.F.add(npyscreen.TitleText, name='Class Code :')
       self.title   = self.F.add(npyscreen.TitleText, name='Title :')
       self.date        = self.F.add(npyscreen.TitleDateCombo, name='Date :')
       self.filePath = self.F.add(npyscreen.TitleFilenameCombo, name="Filepath :")
       self.description = self.F.add(npyscreen.MultiLineEdit,
                          value = """# Author : Philippe Vo \n# Date : 
                          """,
                          max_height=10, rely=9)

        # This lets the user interact with the Form.
       self.F.edit()

    def get_form_info(self) :
        info = {
            "classCode": self.classCode.value,
            "title": self.title.value,
            "filepath": self.filePath.value,
            "date": self.date.value,
            "description": self.description.value
        }

        return info
        
class NoteForm(npyscreen.NPSApp):
    def main(self):
        # These lines create the form and populate it with widgets.
        # A fairly complex screen in only 8 or so lines of code - a line for each control.
       self.F  = npyscreen.Form(name = "Note Form",)
       self.classCode   = self.F.add(npyscreen.TitleText, name='Class Code :')
       self.title   = self.F.add(npyscreen.TitleText, name='Title :')
       self.date        = self.F.add(npyscreen.TitleDateCombo, name='Date :')
       self.filePath = self.F.add(npyscreen.TitleFilenameCombo, name="Filepath :")
       self.description = self.F.add(npyscreen.MultiLineEdit,
                          value = """# Author : Philippe Vo \n# Date : 
                          """,
                          max_height=10, rely=9)

        # This lets the user interact with the Form.
       self.F.edit()

    def get_form_info(self) :
        info = {
            "classCode": self.classCode.value,
            "title": self.title.value,
            "filepath": self.filePath.value,
            "date": self.date.value,
            "description": self.description.value
        }

        return info

if __name__ == "__main__":
    App = AssignmentForm()
    App.run()
    info = App.get_form_info()
    print(info["date"])