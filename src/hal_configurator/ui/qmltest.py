
from PySide import QtGui
from gen.qmltest import Ui_Form

class Form(QtGui.QWidget, Ui_Form):
  def __init__(self, *args, **kwargs):
    super(Form, self).__init__(*args, **kwargs)
    self.setupUi()
    self.bindUi()

  def setupUi(self):
    super(Form, self).setupUi(self)

  def bindUi(self):
    pass
