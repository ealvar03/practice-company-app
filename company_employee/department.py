class Department:
    department_name = ''
    dep_id = ''
    location = ''
    company = ''

    # Method to store all the data in department class (name, id, location,
    # company and employee)
    def __init__(self, department_name, department_id, location, company):
        self.department_name = department_name
        self.dep_id = department_id
        self.location = location
        self.company = company
