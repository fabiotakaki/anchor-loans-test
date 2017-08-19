import re
class CreditCard:
  def __init__(self, number):
    self.number = number

  def get_number(self):
    return self.number

  def validate(self):
    reg_exp = re.compile(r'^(?!.*([0-9])\1{3})([456]\d{3}-?\d{4}-?\d{4}-?\d{4})$')
    aux = self.number.replace('-', '')
    match = reg_exp.match(aux)
    if match:
      return True
    else:
      return False
