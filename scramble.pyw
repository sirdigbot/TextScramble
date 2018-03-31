#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
import random
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QPlainTextEdit, QLabel


# Character sets convering a-z, A-Z and 0-9
charSets = [

  # Cursive Characters
  [
  u'\uD835\uDCB6', u'\uD835\uDCB7', u'\uD835\uDCB8', u'\uD835\uDCB9', u'\uD835\uDC52',
  u'\uD835\uDCBB', u'\uD835\uDC54', u'\uD835\uDCBD', u'\uD835\uDCBE', u'\uD835\uDCBF',
  u'\uD835\uDCC0', u'\uD835\uDCC1', u'\uD835\uDCC2', u'\uD835\uDCC3', u'\uD835\uDC5C',
  u'\uD835\uDCC5', u'\uD835\uDCC6', u'\uD835\uDCC7', u'\uD835\uDCC8', u'\uD835\uDCC9',
  u'\uD835\uDCCA', u'\uD835\uDCCB', u'\uD835\uDCCC', u'\uD835\uDCCD', u'\uD835\uDCCE',
  u'\uD835\uDCCF', u'\uD835\uDC9C', u'\uD835\uDC35', u'\uD835\uDC9E', u'\uD835\uDC9F',
  u'\uD835\uDC38', u'\uD835\uDC39', u'\uD835\uDCA2', u'\uD835\uDC3B', u'\uD835\uDC3C',
  u'\uD835\uDCA5', u'\uD835\uDCA6', u'\uD835\uDC3F', u'\uD835\uDC40', u'\uD835\uDCA9',
  u'\uD835\uDCAA', u'\uD835\uDCAB', u'\uD835\uDCAC', u'\uD835\uDC45', u'\uD835\uDCAE',
  u'\uD835\uDCAF', u'\uD835\uDCB0', u'\uD835\uDCB1', u'\uD835\uDCB2', u'\uD835\uDCB3',
  u'\uD835\uDCB4', u'\uD835\uDCB5', u'\uD835\uDFE2', u'\uD835\uDFE3', u'\uD835\uDFE4',
  u'\uD835\uDFE5', u'\uD835\uDFE6', u'\uD835\uDFE7', u'\uD835\uDFE8', u'\uD835\uDFE9',
  u'\uD835\uDFEA', u'\uD835\uDFEB'
  ],

  # Bold Cursive Characters
  [
  u'\uD835\uDCEA', u'\uD835\uDCEB', u'\uD835\uDCEC', u'\uD835\uDCED', u'\uD835\uDCEE',
  u'\uD835\uDCEF', u'\uD835\uDCF0', u'\uD835\uDCF1', u'\uD835\uDCF2', u'\uD835\uDCF3',
  u'\uD835\uDCF4', u'\uD835\uDCF5', u'\uD835\uDCF6', u'\uD835\uDCF7', u'\uD835\uDCF8',
  u'\uD835\uDCF9', u'\uD835\uDCFA', u'\uD835\uDCFB', u'\uD835\uDCFC', u'\uD835\uDCFD',
  u'\uD835\uDCFE', u'\uD835\uDCFF', u'\uD835\uDD00', u'\uD835\uDD01', u'\uD835\uDD02',
  u'\uD835\uDD03', u'\uD835\uDCD0', u'\uD835\uDCD1', u'\uD835\uDCD2', u'\uD835\uDCD3',
  u'\uD835\uDCD4', u'\uD835\uDCD5', u'\uD835\uDCD6', u'\uD835\uDCD7', u'\uD835\uDCD8',
  u'\uD835\uDCD9', u'\uD835\uDCDA', u'\uD835\uDCDB', u'\uD835\uDCDC', u'\uD835\uDCDD',
  u'\uD835\uDCDE', u'\uD835\uDCDF', u'\uD835\uDCE0', u'\uD835\uDCE1', u'\uD835\uDCE2',
  u'\uD835\uDCE3', u'\uD835\uDCE4', u'\uD835\uDCE5', u'\uD835\uDCE6', u'\uD835\uDCE7',
  u'\uD835\uDCE8', u'\uD835\uDCE9', u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9'
  ],

  # Hollow Characters
  [
  u'\uD835\uDD52', u'\uD835\uDD53', u'\uD835\uDD54', u'\uD835\uDD55', u'\uD835\uDD56',
  u'\uD835\uDD57', u'\uD835\uDD58', u'\uD835\uDD59', u'\uD835\uDD5A', u'\uD835\uDD5B',
  u'\uD835\uDD5C', u'\uD835\uDD5D', u'\uD835\uDD5E', u'\uD835\uDD5F', u'\uD835\uDD60',
  u'\uD835\uDD61', u'\uD835\uDD62', u'\uD835\uDD63', u'\uD835\uDD64', u'\uD835\uDD65',
  u'\uD835\uDD66', u'\uD835\uDD67', u'\uD835\uDD68', u'\uD835\uDD69', u'\uD835\uDD6A',
  u'\uD835\uDD6B', u'\uD835\uDD38', u'\uD835\uDD39', u'\u2102', u'\uD835\uDD3B',
  u'\uD835\uDD3C', u'\uD835\uDD3D', u'\uD835\uDD3E', u'\u210D', u'\uD835\uDD40',
  u'\uD835\uDD41', u'\uD835\uDD42', u'\uD835\uDD43', u'\uD835\uDD44', u'\u2115',
  u'\uD835\uDD46', u'\u2119', u'\u211A', u'\u211D', u'\uD835\uDD4A', u'\uD835\uDD4B',
  u'\uD835\uDD4C', u'\uD835\uDD4D', u'\uD835\uDD4E', u'\uD835\uDD4F', u'\uD835\uDD50',
  u'\u2124', u'\uD835\uDFD8', u'\uD835\uDFD9', u'\uD835\uDFDA', u'\uD835\uDFDB',
  u'\uD835\uDFDC', u'\uD835\uDFDD', u'\uD835\uDFDE', u'\uD835\uDFDF', u'\uD835\uDFE0',
  u'\uD835\uDFE1'
  ],

  # Gothic Characters
  [
  u'\uD835\uDD86', u'\uD835\uDD87', u'\uD835\uDD88', u'\uD835\uDD89', u'\uD835\uDD8A',
  u'\uD835\uDD8B', u'\uD835\uDD8C', u'\uD835\uDD8D', u'\uD835\uDD8E', u'\uD835\uDD8F',
  u'\uD835\uDD90', u'\uD835\uDD91', u'\uD835\uDD92', u'\uD835\uDD93', u'\uD835\uDD94',
  u'\uD835\uDD95', u'\uD835\uDD96', u'\uD835\uDD97', u'\uD835\uDD98', u'\uD835\uDD99',
  u'\uD835\uDD9A', u'\uD835\uDD9B', u'\uD835\uDD9C', u'\uD835\uDD9D', u'\uD835\uDD9E',
  u'\uD835\uDD9F', u'\uD835\uDD6C', u'\uD835\uDD6D', u'\uD835\uDD6E', u'\uD835\uDD6F',
  u'\uD835\uDD70', u'\uD835\uDD71', u'\uD835\uDD72', u'\uD835\uDD73', u'\uD835\uDD74',
  u'\uD835\uDD75', u'\uD835\uDD76', u'\uD835\uDD77', u'\uD835\uDD78', u'\uD835\uDD79',
  u'\uD835\uDD7A', u'\uD835\uDD7B', u'\uD835\uDD7C', u'\uD835\uDD7D', u'\uD835\uDD7E',
  u'\uD835\uDD7F', u'\uD835\uDD80', u'\uD835\uDD81', u'\uD835\uDD82', u'\uD835\uDD83',
  u'\uD835\uDD84', u'\uD835\uDD85', u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9'
  ],

  # Encircled Characters
  [
  u'\u24D0', u'\u24D1', u'\u24D2', u'\u24D3', u'\u24D4', u'\u24D5', u'\u24D6', u'\u24D7',
  u'\u24D8', u'\u24D9', u'\u24DA', u'\u24DB', u'\u24DC', u'\u24DD', u'\u24DE', u'\u24DF',
  u'\u24E0', u'\u24E1', u'\u24E2', u'\u24E3', u'\u24E4', u'\u24E5', u'\u24E6', u'\u24E7',
  u'\u24E8', u'\u24E9', u'\u24B6', u'\u24B7', u'\u24B8', u'\u24B9', u'\u24BA', u'\u24BB',
  u'\u24BC', u'\u24BD', u'\u24BE', u'\u24BF', u'\u24C0', u'\u24C1', u'\u24C2', u'\u24C3',
  u'\u24C4', u'\u24C5', u'\u24C6', u'\u24C7', u'\u24C8', u'\u24C9', u'\u24CA', u'\u24CB',
  u'\u24CC', u'\u24CD', u'\u24CE', u'\u24CF', u'\u24EA', u'\u2460', u'\u2461', u'\u2462',
  u'\u2463', u'\u2464', u'\u2465', u'\u2466', u'\u2467', u'\u2468'
  ],
  
  # EXTRA THICC Characters (Only Uppercase)
  [
  u'\u5342', u'\u4E43', u'\u531A', u'\u5200', u'\u4E47', u'\u4E0B', u'\u53B6', u'\u5344',
  u'\u5DE5', u'\u4E01', u'\u957F', u'\u4E5A', u'\u4ECE', u'\uD841\uDE28', u'\u53E3', u'\u5C38',
  u'\u353F', u'\u5C3A', u'\u4E02', u'\u4E05', u'\u51F5', u'\u30EA', u'\u5C71', u'\u4E42',
  u'\u4E2B', u'\u4E59', u'\u5342', u'\u4E43', u'\u531A', u'\u5200', u'\u4E47', u'\u4E0B',
  u'\u53B6', u'\u5344', u'\u5DE5', u'\u4E01', u'\u957F', u'\u4E5A', u'\u4ECE', u'\uD841\uDE28',
  u'\u53E3', u'\u5C38', u'\u353F', u'\u5C3A', u'\u4E02', u'\u4E05', u'\u51F5', u'\u30EA',
  u'\u5C71', u'\u4E42', u'\u4E2B', u'\u4E59', u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9'
  ]
]

# Convert Surrogate Form to UTF-16 escape sequence (Multi-escape to Single Escape)
def as_surrogates(str):
  return str.encode('utf-16', 'surrogatepass').decode('utf-16')


def to_random_text(str, charSet=None):
  outputText = ""
  for c in str:
    num = ord(c)
    usedSpecialChar = True
    selectedSet = 0
    
    # Allow a specific charset to be forced safely
    if charSet is None:
      selectedSet = random.randint(0, len(charSets)-1)
    elif 0 <= charSet < len(charSets):
      selectedSet = charSet
    
    # Convert ASCII to match CharSet Lists
    if 97 <= num <= 122:
      num -= 97 # Offset to 0 to 25 range (a-z)
    elif 65 <= num <= 90:
      num -= 39 # Offset to 26 to 51 range (A-Z)
    elif 48 <= num <= 57:
      num += 4  # Offset to 52 to 61 range (0-9)
    else:
      usedSpecialChar = False
    
    # Add Character to output string
    if usedSpecialChar:
      if num < len(charSets[selectedSet]):
        outputText += as_surrogates(charSets[selectedSet][num])
    else:
      outputText += c
    
  return outputText

  
  
class MainWindow(QWidget):

  def __init__(self):
    super().__init__()
    self.initUI()
    self.show()
  
  def initUI(self):
    self.title = 'Text Scrambler'
    self.setWindowTitle('Text Scrambler')
    self.resize(QSize(720, 360))
    
    mainLayout = QVBoxLayout(self)
    
    
    # Text Input
    self.textField = QPlainTextEdit(self)
    self.textField.setPlaceholderText('Enter Text Here..')
    
    # Text Output
    self.displayField = QPlainTextEdit(self)
    self.displayField.setReadOnly(True)
    
    # Connect I/O
    self.textField.textChanged.connect(self.UpdateOutputText)
    
  
    # Font Mode Selection
    modeLayout = QHBoxLayout(self)
    self.modeSelect = QComboBox(self)
    self.modeSelect.addItem('Cursive Characters')
    self.modeSelect.addItem('Bold Cursive Characters')
    self.modeSelect.addItem('Hollow Characters')
    self.modeSelect.addItem('Gothic Characters')
    self.modeSelect.addItem('Encircled Characters')
    self.modeSelect.addItem(u'乇乂丅尺卂 丅卄工匚匚 Characters')
    self.modeSelect.addItem('Random')
    self.randomModeIndex = self.modeSelect.count()-1
    self.modeSelect.setCurrentIndex(self.randomModeIndex) # Random by default
    
    self.modeSelect.currentIndexChanged.connect(self.UpdateOutputText)
    
    modeLabel = QLabel('Font Mode', self)
    self.charCountLabel = QLabel('Characters: 0', self)
    
    modeLayout.addWidget(self.charCountLabel, 1) # Stretch
    modeLayout.addWidget(modeLabel)
    modeLayout.addWidget(self.modeSelect)
    
    
    # Add to main layout
    mainLayout.addWidget(self.textField)
    mainLayout.addWidget(self.displayField)
    mainLayout.addLayout(modeLayout)
    
    self.setLayout(mainLayout)
    
    
  def GetFontMode(self):
    return self.modeSelect.currentIndex()
    
  def UpdateCharCount(self):
    count = len(self.displayField.toPlainText())
    self.charCountLabel.setText('Characters: ' + str(count))
    if count < 8000:
      self.charCountLabel.setStyleSheet('')
    elif 8000 <= count < 16000:
      self.charCountLabel.setStyleSheet('QLabel {color:#e5a020}')
    elif count >= 16000:
      self.charCountLabel.setStyleSheet('QLabel {color:#cc0000}')
    
  def UpdateOutputText(self):
    mode = None if self.GetFontMode() == self.randomModeIndex else self.GetFontMode();
    self.displayField.setPlainText(to_random_text(self.textField.toPlainText(), mode))
    self.UpdateCharCount()
  
    

def main():
  app = QApplication(sys.argv)
  wnd = MainWindow()
  sys.exit(app.exec())
  
  
if __name__ == "__main__":
  main()
  