from company_employee.contract import Contract
from company_employee.department import Department
from company_employee.employee import Employee
from company_employee.utilities import Utilities


class Company:
    company_name = ''
    company_cif = ''
    street = ''
    st_number = ''
    postcode = ''
    city = ''
    employees_list = []
    department_list = []
    contract_list = []
    program_creation_date = ''
    creation_date = ''

    # Method to store company information
    def store_company_inf(self, company_name, cif, street, st_number, postcode, city):
        self.company_name = company_name
        self.company_cif = cif
        self.street = street
        self.st_number = st_number
        self.postcode = postcode
        self.city = city

    # Method to create a list of all the employees in the company
    def create_employee(self, employee_name, age, dni, status, department, salary, category, street, st_number,
                        postcode, city):
        self.employees_list.append(Employee(employee_name, age, dni, status, department, salary, category, street,
                                            st_number, postcode, city))

    # Method to show all the employees information
    def display_employee_data(self):
        count = 0
        while count < len(self.employees_list):
            item = self.employees_list[count]
            print(str(item.employee_name) + ' ' + str(item.employee_age) + ' ' + str(item.employee_id)
                  + ' ' + str(item.status) + ' ' + str(item.department) + ' ' + str(item.salary)
                  + ' ' + str(item.category) + ' ' + str(item.street) + ' ' + str(item.st_number)
                  + ' ' + str(item.postcode) + ' ' + str(item.city))
            count += 1

    # Method to create a list with all the departments information
    def create_department(self, department_name, department_id, location, company):
        self.department_list.append(Department(department_name, department_id, location, company))

    # # Method to show an employee who belongs to a specific department
    # def show_employee_department(self, department_name):
    #     count = 0
    #     while count < len(self.employees_list):
    #         item = self.employees_list[count]
    #         if department_name == item.department:
    #             print(item.employee_name)
    #         count += 1

    # Method to show all the department within a company
    def show_departments(self, company_name):
        new_department_list = []
        count = 0
        while count < len(self.department_list):
            item = self.department_list[count]
            if company_name == item.company:
                new_department_list.append(item)
            count += 1
        return new_department_list

    # Method to get employee
    def get_employee(self, employee_name):
        count = 0
        while count < len(self.employees_list):
            item = self.employees_list[count]
            if employee_name == item.employee_name:
                return item
            count += 1
        return None

    # Create a method to generate the address information for the company
    def get_company_address(self):
        return str(self.street) + ' ' + str(self.st_number) + ' ' + str(self.postcode) + ' ' + str(self.city)

    # Method to get all the employees who work in a particular department
    def get_employees_department(self, department_name):
        new_list = []
        count = 0
        while count < len(self.employees_list):
            item = self.employees_list[count]
            if department_name == item.department:
                new_list.append(item)
            count += 1
        return new_list

    # Method to store company contracts (creation date, employee information and company information)
    def hire_employee(self, employee_name):
        employee_inf = self.get_employee(employee_name)
        new_contract = Contract(employee_inf, self.company_name, self.company_cif)
        self.contract_list.append(new_contract)

    # Method to delete a contract
    # Falta eliminar empleado de la compañia (employees_list)
    def delete_contract(self, employee_name):
        count = 0
        while count < len(self.contract_list):
            item = self.contract_list[count]
            if employee_name == item.employee.employee_name:
                self.contract_list.pop(count)
            count += 1

    # Method to delete an employee
    def delete_employee(self, employee_name):
        count = 0
        while count < len(self.employees_list):
            item = self.employees_list[count]
            if employee_name == item.employee_name:
                self.employees_list.pop(count)
            count += 1

    # Private method to check if the department that is asked to be deleted is emptied or not
    def __is_department_empty(self, department_name):
        count = 0
        while count < len(self.employees_list):
            item = self.employees_list[count]
            if department_name == item.department:
                return False
            count += 1
        return True

    # Method that allows to change the department name
    def change_department_name(self, department_name):
        values_check = Utilities()
        new_name = str(input('new name: '))
        count = 0
        count2 = 0
        if self.__is_department_empty(department_name):
            while count < len(self.department_list):
                item = self.department_list[count]
                if values_check.check_values(department_name, item.department_name):
                    item.department_name = new_name
                count += 1
            return self.department_list
        else:
            while count < len(self.employees_list):
                if values_check.check_values(department_name, self.employees_list[count].department):
                    self.employees_list[count].department = new_name
                count += 1

            while count2 < len(self.department_list):
                if values_check.check_values(department_name, self.department_list[count2].department_name):
                    self.department_list[count2].department_name = new_name
                count2 += 1
            return self.department_list

    # Method to delete a department
    def delete_department(self, department_name):
        count = 0
        if self.__is_department_empty(department_name):
            while count < len(self.department_list):
                item = self.department_list[count]
                if department_name == item.department_name:
                    self.department_list.pop(count)
                count += 1
        else:
            print('Department cannot be deleted because it contains employees information')
