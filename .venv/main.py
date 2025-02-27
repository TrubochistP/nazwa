#1

# class car:
#  def __init__(self,year,mark,model):
#   self.year = year
#   self.mark = mark
#   self.model = model
#
#  def get_info(self):
#   return f"{self.year}, {self.mark}, {self.model}"

#2

# class employee:
#  def __init__(self,name,level,salary):
#   self.name = name
#   self.level = level
#   self.salary = salary
#
#
# class department:
#  def __init__(self, name):
#   self.name = name
#   self.employees = []
#
#  def add_employees(self, employee):
#   self.employees.append(employee)
#
#   def remove_employee(self, employee_name):
#    for employee in self.employees:
#     if employee.name == employee_name:
#      self.employees.remove(employee)
#      break
#
#   def all_salaries(self):
#    all_salaries = 0
#    for employee in self.employees:
#     all_salaries += employee.salary
#    return all_salaries
#
#   def list_of_employees(self):
#    return self.employees

#3

# class device:
#  def __init__(self, name):
#   self.name = name
#   self.is_on = False
#
#  def turn_on(self):
#   self.is_on = True
#
#  def turn_off(self):
#   self.is_on = False
#
# class Tv(device):
#  def __init__(self, name, screen_size):
#   self.screen_size = screen_size
#
# class fridge(device):
#  def __init__(self, name, volume):
#   self.temperature = temperature

#4
#
# import random
#
# def random_litera():
#     alphabet = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']
#     yield random.choice(alphabet)
#
# litera = next(random_litera())
# print(litera)
#
#
