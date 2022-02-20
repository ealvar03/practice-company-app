class Employee:
    employee_name = ''
    employee_age = ''
    employee_id = ''
    status = ''
    department = ''
    salary = ''
    category = ''
    street = ''
    st_number = ''
    postcode = ''
    city = ''

    # Method that stores all the employee data such as name, age, DNI and status
    def __init__(self, name, age, dni, status, department, salary, category, street, st_number, postcode, city):
        self.employee_name = name
        self.employee_age = age
        self.employee_id = dni
        self.status = status
        self.department = department
        self.salary = salary
        self.category = category
        self.street = street
        self.st_number = st_number
        self.postcode = postcode
        self.city = city

    # Create a method that will generate the net salary
    def get_salary(self, gross_salary, retention_percentage):
        net_salary = gross_salary - (gross_salary * retention_percentage)
        return net_salary

    # Create a method to generate the address information for the employee
    def get_employee_address(self):
        return str(self.street) + ' ' + str(self.st_number) + ' ' + str(self.postcode) + ' ' + str(self.city)

