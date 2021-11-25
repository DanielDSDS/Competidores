#Clase para cada competidor individual

class Competitor:

  def __init__(self, cedula, last_name, last_name_2, name, initial, gender, age, hours, minutes, seconds ):
    self.cedula = cedula
    self.last_name = last_name
    self.last_name_2 = last_name_2
    self.name = name
    self.initial = initial
    self.gender = gender
    self.age = age
    self.hours = hours
    self.minutes = minutes
    self.seconds = seconds

  def get_cedula():
    return self.cedula

  def get_age():
    return self.age

  def get_gender():
    return self.gender

  def get_name():
    return self.name

  def get_last_name():
    return self.last_name

  def get_last_name_2():
    return self.last_name_2

  def get_initial():
    return self.initial

  def get_hours():
    return self.hours

  def get_minutes():
    return self.minutes

  def get_seconds():
    return self.seconds

