class TemplateReader:
    def __init__(self):
        pass

    @staticmethod
    def read_course_template(course_name):
        global email_message
        try:
            if course_name== 'report':
                email_file = open("sendEmail/graphs.html", "r")
                email_message = email_file.read()

            elif course_name == 'country':
                email_file = open("sendEmail/DLM_Template.html", "r")
                email_message = email_file.read()
            elif course_name == 'simple':
                email_file = open("sendEmail/simple.html", "r")
                email_message = email_file.read()
            return email_message
        except Exception as e:
            #print("Exception====>>>")
            print('The exception is '+str(e))
