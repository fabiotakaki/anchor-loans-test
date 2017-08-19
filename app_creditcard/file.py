import os
from werkzeug import secure_filename
from creditcard import CreditCard
from collections import deque

class File:
  def __init__(self, file):
    self.allowed_extensions = set(['txt'])
    self.upload_folder = 'app_creditcard/uploads/'
    self.file = file

  def allowed_file(self):
    return '.' in self.file.filename and self.file.filename.rsplit('.', 1)[1] in self.allowed_extensions

  def upload(self):
    if self.file and self.allowed_file():
      filename = secure_filename(self.file.filename)
      self.filename = filename
      self.file.save(os.path.join(self.upload_folder, filename))
      return True
    else:
      return False

  def validate_credit_cards(self):
    with open(self.upload_folder+self.filename, "r") as file:
      lines = deque(file.readlines())
      quantity_cc = int(lines.popleft())
      if(quantity_cc < 0 or quantity_cc > 100):
        return None
      else:
        result = []
        while(lines):
          line = lines.popleft()
          cc = CreditCard(line)
          if(cc.validate()):
            creditcard = dict([('creditcard', line), ('valid', True)])
          else:
            creditcard = dict([('creditcard', line), ('valid', False)])

          result.append(creditcard)

        return result