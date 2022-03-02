import os
import getch
from datetime import date
from company_employee.company import Company
from company_employee.department import Department


class ContextualMenu:
    my_department = None
    my_company = None
    exit_program = True

    def __init__(self):
        self.my_company = Company()

        if self.company_information_exists():
            self.get_company_information()
        else:
            self.my_company.company_name = str(input('Name of the company: '))
            self.my_company.company_cif = str(input('Company cif: '))
            self.my_company.street = str(input('Street: '))
            self.my_company.st_number = str(input('Street number: '))
            self.my_company.postcode = str(input('Postcode: '))
            self.my_company.city = str(input('City: '))

            today = date.today()
            self.my_company.creation_date = today.strftime("%d/%m/%Y")

            file = open("/Users/elenaalvarezortega/PycharmProjects/OOP_exercises/company_employee/company.dat", "w+")
            file.write(self.my_company.company_name + os.linesep)
            file.write(self.my_company.company_cif + os.linesep)
            file.write(self.my_company.street + os.linesep)
            file.write(self.my_company.st_number + os.linesep)
            file.write(self.my_company.postcode + os.linesep)
            file.write(self.my_company.city)
            file.close()

        # dummy data
        # **************************************************************************
        self.my_company.create_department('HR', '1234', 'London', 'Axa')
        self.my_company.create_department('IT', '1111', 'London', 'Axa')
        # **************************************************************************

    # Method to know if the file created exists (.dat)
    def company_information_exists(self):
        file = r"/Users/elenaalvarezortega/PycharmProjects/OOP_exercises/company_employee/company.dat"
        return os.path.isfile(file)

    # Method to modify data information from the file .dat
    def get_company_information(self):
        file = open("/Users/elenaalvarezortega/PycharmProjects/OOP_exercises/company_employee/company.dat", "r")
        self.my_company.company_name = file.readline().rstrip('\n')
        self.my_company.company_cif = file.readline().rstrip('\n')
        self.my_company.street = file.readline().rstrip('\n')
        self.my_company.st_number = file.readline().rstrip('\n')
        self.my_company.postcode = file.readline().rstrip('\n')
        self.my_company.city = file.readline().rstrip('\n')
        file.close()

    # Method to display the menu options (employee details, department details and company details)
    def show_menu(self):
        while self.exit_program:
            print(30 * '*')
            print((10 * '*') + ' ' + self.my_company.company_name + ' ' + (10 * '*'))
            print((8 * '*') + ' ' + 'Cif: ' + self.my_company.company_cif + ' ' + (8 * '*'))
            print(30 * '*')
            print(' ')
            print(30 * '*')
            print('1. Employee')
            print(30 * '*')
            print('11. Hire new employee')
            print('12. Show employee details')
            print('13. Show employee salary information')
            print('14. Show employees per department')
            print('15. Show all employees')
            print('16. Delete employee')
            print(30 * '*')
            print('2. Department')
            print(30 * '*')
            print('21. Create new department')
            print('22. Change department name')
            print('23. Delete department')
            print(30 * '*')
            print('50. Exit program')
            option_selected = str(input('SELECT A NUMBER OPTION: '))
            self.match_options(option_selected)

    # Regarding the selected option this method will select a particular case
    def match_options(self, option_selected):
        match option_selected:
            case '11':
                self.option_11()
            case '12':
                self.option_12()
            case '13':
                self.option_13()
            case '14':
                self.option_14()
            case '15':
                self.option_15()
            case '16':
                self.option_16()
            case '21':
                self.option_21()
            case '22':
                self.option_22()
            case '23':
                self.option_23()
            case '50':
                self.exit_program = False

    # Method to create new employee and then hire it, it will be used in match_options
    def option_11(self):
        employee_name = str(input('Introduce employee name: '))
        self.my_company.create_employee(employee_name,
                                           str(input('Introduce employee age: ')),
                                           str(input('Introduce employee dni: ')),
                                           str(input('Introduce employee status: ')),
                                           str(input('Introduce employee department: ')),
                                           str(input('Introduce employee salary: ')),
                                           str(input('Introduce employee category: ')),
                                           str(input('Introduce employee street: ')),
                                           str(input('Introduce employee street number: ')),
                                           str(input('Introduce employee postcode: ')),
                                           str(input('Introduce employee city: ')))
        self.my_company.hire_employee(employee_name)

    # This method will display the employee details
    def option_12(self):
        employee_name = str(input('Introduce employee name: '))
        self.my_company.get_employee(employee_name)
        getch.getch()

    # This method will show the employee salary information
    def option_13(self):
        employee_name = str(input('Introduce employee name: '))
        employee_details = self.my_company.get_employee(employee_name)
        print(employee_details.get_salary(2000, 0.05))
        getch.getch()

    # This method will show the employees per department
    def option_14(self):
        department_name = str(input('Introduce department name: '))
        employees_in_department = self.my_company.get_employees_department(department_name)
        count = 0
        while count < len(employees_in_department):
            item = employees_in_department[count]
            print(item.employee_name)
            count += 1
        getch.getch()

    # This method will show all the employees
    def option_15(self):
        self.my_company.display_employee_data()
        getch.getch()

    # This method will delete the data from a specific employee
    def option_16(self):
        employee_name = str(input('Introduce employee name: '))
        self.my_company.delete_employee(employee_name)
        getch.getch()

    # This method will create and store a new department information
    def option_21(self):
        self.my_department = Department(str(input('Introduce department name: ')),
                                        str(input('Introduce department id: ')),
                                        str(input('Introduce department location: ')),
                                        str(input('Introduce company: ')))

        if self.department_information_exists():
            self.get_department_information()
        else:
            self.my_department.department_name = str(input('Introduce department name: '))
            self.my_department.dep_id = str(input('Introduce department id: '))
            self.my_department.location = str(input('Introduce department location: '))
            self.my_department.company = str(input('Introduce company: '))

            dep_file = open("/Users/elenaalvarezortega/PycharmProjects/OOP_exercises/company_employee/department.dat",
                            "w+")
            dep_file.write(self.my_department.department_name + os.linesep)
            dep_file.write(self.my_department.dep_id + os.linesep)
            dep_file.write(self.my_department.location + os.linesep)
            dep_file.write(self.my_department.company)
            dep_file.close()

    # This method will provide the data for department information and will allow it to be modified
    def get_department_information(self):
        dep_file = open("/Users/elenaalvarezortega/PycharmProjects/OOP_exercises/company_employee/company.dat", "r")
        self.my_department.department_name = dep_file.readline().rstrip('\n')
        self.my_department.dep_id = dep_file.readline().rstrip('\n')
        self.my_department.location = dep_file.readline().rstrip('\n')
        self.my_department.company = dep_file.readline().rstrip('\n')
        dep_file.close()

    # Method to check if the department file exists
    def department_information_exists(self):
        dep_file = r"/Users/elenaalvarezortega/PycharmProjects/OOP_exercises/company_employee/department.dat"
        return os.path.isfile(dep_file)

    # This method will change the name of an existing department
    def option_22(self):
        department_name = str(input('Introduce department name: '))
        self.my_company.change_department_name(department_name)
        print(self.my_company.department_list[0].department_name)
        print(self.my_company.department_list[1].department_name)
        getch.getch()

    # This method will delete an existing department data
    def option_23(self):
        department_name = str(input('Introduce department name: '))
        self.my_company.delete_department(department_name)
        getch.getch()
