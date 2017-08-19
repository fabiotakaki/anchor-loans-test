import re
class CreditCard:
  def __init__(self, number):
    self.number = number

  def get_number(self):
    return self.number

  # (?!.*([0-9])\1{3}) - Case 1: 111x-xxxx-xxxx-xxxx
  # (?!.*([0-9])\2{1,}-\2{1,}) - Case 2: xx11-11xx-xxxx-xxxx
  # (?!.*([0-9])\3{3}-\3{1}) - Case 3: x111-1xxx-xxxx-xxxx
  # (?!.*([0-9])-\4{3})(?!.*([0-9])-\4{3}) Case 4: xxx1-111x-xxxx-xxxx
  # ([456]\d{3}-?\d{4}-?\d{4}-?\d{4}) Final Case: verify 16 digits, - allowed, consists only digits (0-9)
  def validate(self):
    reg_exp = re.compile(r'^(?!.*([0-9])\1{3})(?!.*([0-9])\2{1,}-\2{1,})(?!.*([0-9])\3{3}-\3{1})(?!.*([0-9])-\4{3})(?!.*([0-9])-\4{3})([456]\d{3}-?\d{4}-?\d{4}-?\d{4})$')
    match = reg_exp.match(self.number)
    if match:
      return True
    else:
      return False
