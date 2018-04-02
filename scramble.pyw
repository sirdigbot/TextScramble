#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import random
import wx


EMOJISETIDX = 9
DISCORDSETIDX = 10


# Character sets convering a-z, A-Z and 0-9
charSets = [

  # 0 - Cursive Characters
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

  # 1- Bold Cursive Characters
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

  # 2 - Hollow Characters
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

  # 3 - Gothic Characters
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

  # 4 - Circled Characters
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
  
  
  # 5 - Negative Circled Characters (Only Uppercase)
  [
  u'\uD83C\uDD50', u'\uD83C\uDD51', u'\uD83C\uDD52', u'\uD83C\uDD53', u'\uD83C\uDD54',
  u'\uD83C\uDD55', u'\uD83C\uDD56', u'\uD83C\uDD57', u'\uD83C\uDD58', u'\uD83C\uDD59',
  u'\uD83C\uDD5A', u'\uD83C\uDD5B', u'\uD83C\uDD5C', u'\uD83C\uDD5D', u'\uD83C\uDD5E',
  u'\uD83C\uDD5F', u'\uD83C\uDD60', u'\uD83C\uDD61', u'\uD83C\uDD62', u'\uD83C\uDD63',
  u'\uD83C\uDD64', u'\uD83C\uDD65', u'\uD83C\uDD66', u'\uD83C\uDD67', u'\uD83C\uDD68',
  u'\uD83C\uDD69',
  u'\uD83C\uDD50', u'\uD83C\uDD51', u'\uD83C\uDD52', u'\uD83C\uDD53', u'\uD83C\uDD54',
  u'\uD83C\uDD55', u'\uD83C\uDD56', u'\uD83C\uDD57', u'\uD83C\uDD58', u'\uD83C\uDD59',
  u'\uD83C\uDD5A', u'\uD83C\uDD5B', u'\uD83C\uDD5C', u'\uD83C\uDD5D', u'\uD83C\uDD5E',
  u'\uD83C\uDD5F', u'\uD83C\uDD60', u'\uD83C\uDD61', u'\uD83C\uDD62', u'\uD83C\uDD63',
  u'\uD83C\uDD64', u'\uD83C\uDD65', u'\uD83C\uDD66', u'\uD83C\uDD67', u'\uD83C\uDD68',
  u'\uD83C\uDD69',
  u'\u24FF', u'\u2776', u'\u2777', u'\u2778', u'\u2779', u'\u277A', u'\u277B',
  u'\u277C', u'\u277D', u'\u277E'
  ],
  
  
  # 6 - Squared Characters (Only Uppercase)
  [
  u'\uD83C\uDD30', u'\uD83C\uDD31', u'\uD83C\uDD32', u'\uD83C\uDD33', u'\uD83C\uDD34',
  u'\uD83C\uDD35', u'\uD83C\uDD36', u'\uD83C\uDD37', u'\uD83C\uDD38', u'\uD83C\uDD39',
  u'\uD83C\uDD3A', u'\uD83C\uDD3B', u'\uD83C\uDD3C', u'\uD83C\uDD3D', u'\uD83C\uDD3E',
  u'\uD83C\uDD3F', u'\uD83C\uDD40', u'\uD83C\uDD41', u'\uD83C\uDD42', u'\uD83C\uDD43',
  u'\uD83C\uDD44', u'\uD83C\uDD45', u'\uD83C\uDD46', u'\uD83C\uDD47', u'\uD83C\uDD48',
  u'\uD83C\uDD49',
  u'\uD83C\uDD30', u'\uD83C\uDD31', u'\uD83C\uDD32', u'\uD83C\uDD33', u'\uD83C\uDD34',
  u'\uD83C\uDD35', u'\uD83C\uDD36', u'\uD83C\uDD37', u'\uD83C\uDD38', u'\uD83C\uDD39',
  u'\uD83C\uDD3A', u'\uD83C\uDD3B', u'\uD83C\uDD3C', u'\uD83C\uDD3D', u'\uD83C\uDD3E',
  u'\uD83C\uDD3F', u'\uD83C\uDD40', u'\uD83C\uDD41', u'\uD83C\uDD42', u'\uD83C\uDD43',
  u'\uD83C\uDD44', u'\uD83C\uDD45', u'\uD83C\uDD46', u'\uD83C\uDD47', u'\uD83C\uDD48',
  u'\uD83C\uDD49',
  u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9'
  ],
  
  
  # 7 - Negative Squared Characters (Only Uppercase)
  [
  u'\uD83C\uDD70', u'\uD83C\uDD71', u'\uD83C\uDD72', u'\uD83C\uDD73', u'\uD83C\uDD74',
  u'\uD83C\uDD75', u'\uD83C\uDD76', u'\uD83C\uDD77', u'\uD83C\uDD78', u'\uD83C\uDD79',
  u'\uD83C\uDD7A', u'\uD83C\uDD7B', u'\uD83C\uDD7C', u'\uD83C\uDD7D', u'\uD83C\uDD7E',
  u'\uD83C\uDD7F', u'\uD83C\uDD80', u'\uD83C\uDD81', u'\uD83C\uDD82', u'\uD83C\uDD83',
  u'\uD83C\uDD84', u'\uD83C\uDD85', u'\uD83C\uDD86', u'\uD83C\uDD87', u'\uD83C\uDD88',
  u'\uD83C\uDD89',
  u'\uD83C\uDD70', u'\uD83C\uDD71', u'\uD83C\uDD72', u'\uD83C\uDD73', u'\uD83C\uDD74',
  u'\uD83C\uDD75', u'\uD83C\uDD76', u'\uD83C\uDD77', u'\uD83C\uDD78', u'\uD83C\uDD79',
  u'\uD83C\uDD7A', u'\uD83C\uDD7B', u'\uD83C\uDD7C', u'\uD83C\uDD7D', u'\uD83C\uDD7E',
  u'\uD83C\uDD7F', u'\uD83C\uDD80', u'\uD83C\uDD81', u'\uD83C\uDD82', u'\uD83C\uDD83',
  u'\uD83C\uDD84', u'\uD83C\uDD85', u'\uD83C\uDD86', u'\uD83C\uDD87', u'\uD83C\uDD88',
  u'\uD83C\uDD89',
  u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9'
  ],
  
  
  # 8 - EXTRA THICC Characters (Only Uppercase)
  [
  u'\u5342', u'\u4E43', u'\u531A', u'\u5200', u'\u4E47', u'\u4E0B', u'\u53B6', u'\u5344',
  u'\u5DE5', u'\u4E01', u'\u957F', u'\u4E5A', u'\u4ECE', u'\uD841\uDE28', u'\u53E3', u'\u5C38',
  u'\u353F', u'\u5C3A', u'\u4E02', u'\u4E05', u'\u51F5', u'\u30EA', u'\u5C71', u'\u4E42',
  u'\u4E2B', u'\u4E59',
  u'\u5342', u'\u4E43', u'\u531A', u'\u5200', u'\u4E47', u'\u4E0B', u'\u53B6', u'\u5344',
  u'\u5DE5', u'\u4E01', u'\u957F', u'\u4E5A', u'\u4ECE', u'\uD841\uDE28', u'\u53E3', u'\u5C38',
  u'\u353F', u'\u5C3A', u'\u4E02', u'\u4E05', u'\u51F5', u'\u30EA', u'\u5C71', u'\u4E42',
  u'\u4E2B', u'\u4E59',
  u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9'
  ],
  
  # 9 - Emoji Characters (Only Uppercase)
  [
  u'\uD83C\uDDE6', u'\uD83C\uDDE7', u'\uD83C\uDDE8', u'\uD83C\uDDE9', u'\uD83C\uDDEA',
  u'\uD83C\uDDEB', u'\uD83C\uDDEC', u'\uD83C\uDDED', u'\uD83C\uDDEE', u'\uD83C\uDDEF',
  u'\uD83C\uDDF0', u'\uD83C\uDDF1', u'\uD83C\uDDF2', u'\uD83C\uDDF3', u'\uD83C\uDDF4',
  u'\uD83C\uDDF5', u'\uD83C\uDDF6', u'\uD83C\uDDF7', u'\uD83C\uDDF8', u'\uD83C\uDDF9',
  u'\uD83C\uDDFA', u'\uD83C\uDDFB', u'\uD83C\uDDFC', u'\uD83C\uDDFD', u'\uD83C\uDDFE',
  u'\uD83C\uDDFF',
  u'\uD83C\uDDE6', u'\uD83C\uDDE7', u'\uD83C\uDDE8', u'\uD83C\uDDE9', u'\uD83C\uDDEA',
  u'\uD83C\uDDEB', u'\uD83C\uDDEC', u'\uD83C\uDDED', u'\uD83C\uDDEE', u'\uD83C\uDDEF',
  u'\uD83C\uDDF0', u'\uD83C\uDDF1', u'\uD83C\uDDF2', u'\uD83C\uDDF3', u'\uD83C\uDDF4',
  u'\uD83C\uDDF5', u'\uD83C\uDDF6', u'\uD83C\uDDF7', u'\uD83C\uDDF8', u'\uD83C\uDDF9',
  u'\uD83C\uDDFA', u'\uD83C\uDDFB', u'\uD83C\uDDFC', u'\uD83C\uDDFD', u'\uD83C\uDDFE',
  u'\uD83C\uDDFF',
  u'0\u20E3', u'1\u20E3', u'2\u20E3', u'3\u20E3', u'4\u20E3', u'5\u20E3', u'6\u20E3',
  u'7\u20E3', u'8\u20E3', u'9\u20E3'
  ],
  
  # 10 - Discord-Friendly Emoji Characters (Emoji + Space). Prevents creation of flag emoji
  [
  u'\uD83C\uDDE6 ', u'\uD83C\uDDE7 ', u'\uD83C\uDDE8 ', u'\uD83C\uDDE9 ', u'\uD83C\uDDEA ',
  u'\uD83C\uDDEB ', u'\uD83C\uDDEC ', u'\uD83C\uDDED ', u'\uD83C\uDDEE ', u'\uD83C\uDDEF ',
  u'\uD83C\uDDF0 ', u'\uD83C\uDDF1 ', u'\uD83C\uDDF2 ', u'\uD83C\uDDF3 ', u'\uD83C\uDDF4 ',
  u'\uD83C\uDDF5 ', u'\uD83C\uDDF6 ', u'\uD83C\uDDF7 ', u'\uD83C\uDDF8 ', u'\uD83C\uDDF9 ',
  u'\uD83C\uDDFA ', u'\uD83C\uDDFB ', u'\uD83C\uDDFC ', u'\uD83C\uDDFD ', u'\uD83C\uDDFE ',
  u'\uD83C\uDDFF ',
  u'\uD83C\uDDE6 ', u'\uD83C\uDDE7 ', u'\uD83C\uDDE8 ', u'\uD83C\uDDE9 ', u'\uD83C\uDDEA ',
  u'\uD83C\uDDEB ', u'\uD83C\uDDEC ', u'\uD83C\uDDED ', u'\uD83C\uDDEE ', u'\uD83C\uDDEF ',
  u'\uD83C\uDDF0 ', u'\uD83C\uDDF1 ', u'\uD83C\uDDF2 ', u'\uD83C\uDDF3 ', u'\uD83C\uDDF4 ',
  u'\uD83C\uDDF5 ', u'\uD83C\uDDF6 ', u'\uD83C\uDDF7 ', u'\uD83C\uDDF8 ', u'\uD83C\uDDF9 ',
  u'\uD83C\uDDFA ', u'\uD83C\uDDFB ', u'\uD83C\uDDFC ', u'\uD83C\uDDFD ', u'\uD83C\uDDFE ',
  u'\uD83C\uDDFF ',
  u'0\u20E3 ', u'1\u20E3 ', u'2\u20E3 ', u'3\u20E3 ', u'4\u20E3 ', u'5\u20E3 ', u'6\u20E3 ',
  u'7\u20E3 ', u'8\u20E3 ', u'9\u20E3 '
  ]
  
]



# Convert Surrogate Form to UTF-16 escape sequence (Multi-escape to Single Escape)
def as_surrogates(str):
  return str.encode('utf-16', 'surrogatepass').decode('utf-16')


def to_random_text(str, charSet=None, filterEmojiNums=True):
  outputText    = ""
  maxCharsetIdx = len(charSets) - 1
  
  for c in str:
    num         = ord(c)
    charType    = 0      # 0 = Invalid, 1 = Lowercase, 2 = Capital, 3 = Number
    selectedSet = 0
    
    # Allow a specific charset to be forced safely
    if charSet is None:
      selectedSet = random.randint(0, maxCharsetIdx)
    elif 0 <= charSet < len(charSets):
      selectedSet = charSet
    
    # Convert ASCII to match CharSet Lists
    if 97 <= num <= 122:
      num -= 97 # Offset to 0 to 25 range (a-z)
      charType = 1
    elif 65 <= num <= 90:
      num -= 39 # Offset to 26 to 51 range (A-Z)
      charType = 2
    elif 48 <= num <= 57:
      num += 4  # Offset to 52 to 61 range (0-9)
      charType = 3
    
    # Prevent Using Emoji Numbers
    if charType == 3 and (selectedSet == EMOJISETIDX or selectedSet == DISCORDSETIDX) and filterEmojiNums:
      if charSet is None: # If using random sets, select one that is non-emoji
        selectedSet = random.randint(0, maxCharsetIdx) % min(EMOJISETIDX, DISCORDSETIDX)
      else:               # If forced set, use regular numbers
        charType = 0
    
    # Add Character to output string
    if charType > 0:
      if num < len(charSets[selectedSet]):
        outputText += as_surrogates(charSets[selectedSet][num])
    else:
      outputText += c
    
  return outputText



class MainWindow(wx.Frame):
  
  def __init__(self, parent, title):
    super(MainWindow, self).__init__(parent, title=title, size=(720, 400))
    
    self.SetMinSize((500, 192))
    self.initUI()
    self.Centre()
    self.Show()
  
  
  def initUI(self):
    mainPanel = wx.Panel(self)
    
    mainLayout = wx.BoxSizer(wx.VERTICAL)
    
    # Text I/O
    self.textInput = wx.TextCtrl(mainPanel, style=wx.TE_MULTILINE)
    self.textOutput = wx.TextCtrl(mainPanel, style=wx.TE_MULTILINE | wx.TE_READONLY)
    self.textOutput.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))
    
    # Setup Windows-Only Select All (Ctrl+A) Handler For Text Fields
    randomId = wx.NewId()
    self.Bind(wx.EVT_MENU, self.OnSelectAllShortcut, id=randomId)
    accel_tbl = wx.AcceleratorTable([(wx.ACCEL_CTRL,  ord('A'), randomId)])
    self.SetAcceleratorTable(accel_tbl)
    
    # Setup Scrambler
    self.textInput.Bind(wx.EVT_TEXT, self.UpdateOutputText)
    
    
    # Font Mode Selection
    modeLayout = wx.BoxSizer(wx.HORIZONTAL)
    self.modeSelect = wx.ComboBox(mainPanel, style=wx.CB_READONLY)
    self.modeSelect.Append('Cursive')
    self.modeSelect.Append('Bold Cursive')
    self.modeSelect.Append('Hollow')
    self.modeSelect.Append('Gothic')
    self.modeSelect.Append('Circled')
    self.modeSelect.Append('Negative Circled')
    self.modeSelect.Append('Squared')
    self.modeSelect.Append('Negative Squared')
    self.modeSelect.Append(u'乇乂丅尺卂 丅卄工匚匚')
    self.modeSelect.Append('Emoji')
    self.modeSelect.Append('Discord-Friendly Emoji') # Emoji Characters with 1-space either side
    self.modeSelect.Append('Random')
    
    # Set Default Font Mode to randomModeIndex
    self.randomModeIndex = self.modeSelect.GetCount()-1
    self.modeSelect.Select(self.randomModeIndex) # Random by default
    self.modeSelect.Bind(wx.EVT_COMBOBOX, self.UpdateOutputText) # Update on change
    
    modeLabel               = wx.StaticText(mainPanel, -1, 'Font Mode')
    self.charCountLabel     = wx.StaticText(mainPanel, -1, 'Characters: 0')
    self.filterEmojiNumbers = wx.CheckBox(mainPanel, -1, 'Filter Emoji Numbers')
    self.filterEmojiNumbers.SetValue(True)
    self.filterEmojiNumbers.Bind(wx.EVT_CHECKBOX, self.UpdateOutputText)
    self.filterEmojiNumbers.SetToolTip(wx.ToolTip('Emoji Numbers can display weirdly in some text fields.'))
    
    modeLayout.Add(self.charCountLabel, 1, wx.ALIGN_CENTER_VERTICAL, 0)
    modeLayout.Add(self.filterEmojiNumbers, 0, wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 6)
    modeLayout.Add(modeLabel, 0, wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 6)
    modeLayout.Add(self.modeSelect, 0, wx.ALIGN_CENTER_VERTICAL, 0)
    
    
    # Add to Main Layout
    mainLayout.Add(self.textInput, 1, wx.EXPAND | wx.TOP | wx.RIGHT | wx.LEFT, 6)
    mainLayout.Add(self.textOutput, 1, wx.EXPAND | wx.TOP | wx.RIGHT | wx.LEFT, 6)
    mainLayout.Add(modeLayout, 0, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER, 6)
    
    mainPanel.SetSizer(mainLayout)
  
  
  def OnSelectAllShortcut(self, event):
    if MainWindow.FindFocus() == self.textInput:
      self.textInput.SetSelection(-1, -1)
    elif MainWindow.FindFocus() == self.textOutput:
      self.textOutput.SetSelection(-1, -1)
 
 
  def GetFontMode(self):
    return self.modeSelect.GetCurrentSelection()
    
    
  def UpdateCharCount(self):
    count = len(self.textOutput.GetValue())
    self.charCountLabel.SetLabel('Characters: ' + str(count))
    if count < 7000:
      self.charCountLabel.SetForegroundColour(wx.NullColour)
    elif 7000 <= count < 14000:
      self.charCountLabel.SetForegroundColour((229, 160, 32))
    elif count >= 14000:
      self.charCountLabel.SetForegroundColour((204, 0, 0))
  
  
  def UpdateOutputText(self, event):
    mode = None if self.GetFontMode() == self.randomModeIndex else self.GetFontMode()
    self.textOutput.SetValue(to_random_text(self.textInput.GetValue(), mode, self.filterEmojiNumbers.IsChecked()))
    self.UpdateCharCount()


    
def main():
  app = wx.App()
  MainWindow(None, 'Text Scrambler')
  app.MainLoop()
  
  
if __name__ == "__main__":
  main()
 