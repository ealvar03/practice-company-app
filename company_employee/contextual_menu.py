from datetime import date
import os

from company_employee.company import Company


class ContextualMenu:
    my_company = None

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
        option_selected = str(input('SELECT A NUMBER OPTION: '))
        self.match_options(option_selected)

    # Regarding the selected option this method will select a particular case
    def match_options(self, option_selected):
        match option_selected:
            case '11':
                self.option_11()
            case '12':
                self.my_company.display_employee_data()
            case '13':

            case '14':
            case '15':
            case '16':
            case '21':
            case '22':
            case '23':

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