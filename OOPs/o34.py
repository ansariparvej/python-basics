# Method overriding:

class ineuron:
    def student(self):
        print("Print the details of all the students: ")
    def achievers(self):
        print("List of all the achiever: ")
    def hall_of_fame(self):
        print("List of hall of fame: ")

class ineuron_vision(ineuron):
    def student(self):
        print("Filters students list: ")

iv = ineuron_vision()
iv.student()

list()