#Clase para cada competidor individual

class Competitor:
  """
  Clase Competidor 

  Metodos Get,Set y clasificacion basica para el almacenamiento de datos de un competidor especifico
  """

  def __init__(self, cedula, last_name, last_name_2, name, initial, gender, age, hours, minutes, seconds ):
    self.age_group = self.get_age_group(age)
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

  """
  get_data() 

  Retorna el competidor con formato de diccionario
  """
  def get_data(self):
    competitor_dictionary = {
      "cedula" : self.cedula,
      "last_name" : self.last_name,
      "last_name_2" : self.last_name_2,
      "name" : self.name,
      "initial" : self.initial,
      "gender" : self.gender,
      "age" : self.age,
      "hours" : self.hours,
      "minutes" : self.minutes,
      "seconds" : self.seconds,
      "age_group": self.age_group
    }
    return competitor_dictionary 
    
  def get_cedula(self):
    return self.cedula

  def get_age(self):
    return self.age

  def get_gender(self):
    return self.gender

  def get_name(self):
    return self.name

  def get_last_name(self):
    return self.last_name

  def get_last_name_2(self):
    return self.last_name_2

  def get_initial(self):
    return self.initial

  def get_hours(self):
    return self.hours

  def get_minutes(self):
    return self.minutes

  def get_seconds(self):
    return self.seconds

  """
  get_age_group(self, age) 

  Retorna el grupo etario al que pertenece
  """
  def get_age_group(self, age):
    if int(age) <= 25:
      return 'junior'
    elif int(age) <= 40: 
      return 'senior'
    elif int(age) > 40:
      return 'master'

