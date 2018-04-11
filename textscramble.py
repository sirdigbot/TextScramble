#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#########################################################################
## This Source Code Form is subject to the terms of the Mozilla Public  #
## License, v. 2.0. If a copy of the MPL was not distributed with this  #
## file, You can obtain one at http://mozilla.org/MPL/2.0/.             #
#########################################################################
## textscramble.py                                                      #
##                                                                      #
##  An ASCII to Unicode Text Scrambler                                  #
##                                                                      #
#########################################################################


import random
import wx
from images import PNG_CROSS, PNG_OPEN


from config import FontMapConfig # The config file handle class



# Convert Surrogate Form to UTF-16 escape sequence (Multi-escape to Single Escape)
def as_surrogates(str):
  return str.encode('utf-16', 'surrogatepass').decode('utf-16')
  

  
class MainWindow(wx.Frame):
  
  def __init__(self, parent, title):
    super(MainWindow, self).__init__(parent, title=title, size=(720, 400))
    
    if not self.IsDoubleBuffered():
      self.SetDoubleBuffered(True) # Prevent weird display glitches
    self.SetMinSize((660, 224))
    self.config = FontMapConfig('fontmaps')
    
    self.initUI()
    self.Centre()
    self.Show()

    
    
  ####################
  ## UI Setup
  ####################
  
  def initUI(self):
    panel = wx.Panel(self)
    
    rootLayout        = wx.BoxSizer(wx.VERTICAL)  # Holds notebook
    notebook          = wx.Notebook(panel)
    inputPage         = wx.Panel(notebook)
    inputPageLayout   = wx.BoxSizer(wx.VERTICAL)
    configPage        = wx.Panel(notebook)
    configPageLayout  = wx.BoxSizer(wx.VERTICAL)

    
    # --- Scrambler Page ---
    # Text I/O
    ioLayout        = wx.BoxSizer(wx.VERTICAL)
    ioToolbarLayout = wx.BoxSizer(wx.HORIZONTAL)
    # wx.TE_RICH (Only affects MSW) Allows >64kb data in field, Native Ctrl+A and faster processing
    self.inputText  = wx.TextCtrl(inputPage, style=wx.TE_MULTILINE | wx.TE_RICH) 
    self.outputText = wx.TextCtrl(inputPage, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH)
    self.outputText.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))
    self.clearInput = wx.BitmapButton(inputPage, -1, wx.Bitmap.NewFromPNGData(PNG_CROSS, len(PNG_CROSS)))
    self.readFile   = wx.BitmapButton(inputPage, -1, wx.Bitmap.NewFromPNGData(PNG_CROSS, len(PNG_OPEN)))
    
    # LAST HERE
    # Bitmap buttons aren't dispalying properly
    # also the cross mark looks bad, I want to use ART_DELETE but it doesnt display right either
    
    
    ioToolbarLayout.Add(self.clearInput, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, 0)
    ioToolbarLayout.Add(self.readFile, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, 0)
    ioLayout.Add(ioToolbarLayout, 0, wx.EXPAND | wx.TOP | wx.LEFT, 6)
    ioLayout.Add(self.inputText, 1, wx.EXPAND | wx.TOP | wx.LEFT, 6)
    ioLayout.Add(self.outputText, 1, wx.EXPAND | wx.TOP | wx.LEFT, 6)
    
    
    # Font Selection Header
    selectHeaderLayout  = wx.FlexGridSizer(2, 2, 0, 0)
    fontModeLabel       = wx.StaticText(inputPage, -1, 'Font Mode')
    self.randomFont     = wx.CheckBox(inputPage, -1, 'Random')
    self.selectAll      = wx.Button(inputPage, -1, 'Select All')
    self.deselectAll    = wx.Button(inputPage, -1, 'Deselect All')
    
    selectHeaderLayout.Add(fontModeLabel, 0, wx.TOP | wx.LEFT, 6)
    selectHeaderLayout.Add(self.randomFont, 0,  wx.TOP | wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER, 6)
    selectHeaderLayout.Add(self.selectAll, 0,  wx.TOP | wx.LEFT | wx.BOTTOM, 6)
    selectHeaderLayout.Add(self.deselectAll, 0,  wx.TOP | wx.LEFT | wx.RIGHT| wx.BOTTOM, 6)
    
    # Font Selection
    self.selectedFonts  = wx.CheckListBox(inputPage)
    selectLayout        = wx.BoxSizer(wx.VERTICAL)
    selectLayout.Add(selectHeaderLayout, 0, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER, 0)
    selectLayout.Add(self.selectedFonts, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER, 6)
    
    
    # Global Font Config Bar
    fontCfgLayout           = wx.BoxSizer(wx.HORIZONTAL)
    self.charCount          = wx.StaticText(inputPage, -1, 'Characters: 0')
    self.filterEmoji = wx.CheckBox(inputPage, -1, 'Filter Emoji Digits')
    self.filterEmoji.SetToolTip(wx.ToolTip('Emoji Numbers can display weirdly in some text fields.'))
    paddingLabel            = wx.StaticText(inputPage, -1, 'Padding')
    paddingLabel.SetToolTip(wx.ToolTip('Add spaces between each character.'))
    self.paddingSpaces      = wx.SpinCtrl(inputPage, value='0', min=0, max=1000, size=wx.Size(64,-1))
    self.paddingSpaces.SetToolTip(wx.ToolTip('Add spaces between each character.'))
    zalgoLabel              = wx.StaticText(inputPage, -1, 'Zalgo')
    self.zalgoMode          = wx.Choice(inputPage, size=wx.Size(64,-1))
    self.zalgoUpCheck       = wx.CheckBox(inputPage, -1, 'Up')
    self.zalgoMidCheck      = wx.CheckBox(inputPage, -1, 'Middle')
    self.zalgoDownCheck     = wx.CheckBox(inputPage, -1, 'Down')
    
    fontCfgLayout.Add(self.charCount, 1, wx.ALIGN_CENTER_VERTICAL, 0)
    fontCfgLayout.Add(zalgoLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0)
    fontCfgLayout.Add(self.zalgoMode, 0, wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 6)
    fontCfgLayout.Add(self.zalgoUpCheck, 0, wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 0)
    fontCfgLayout.Add(self.zalgoMidCheck, 0, wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 0)
    fontCfgLayout.Add(self.zalgoDownCheck, 0, wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 6) 
    fontCfgLayout.Add(self.filterEmoji, 0, wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 8) # +2 for better sectioning
    fontCfgLayout.Add(paddingLabel, 0, wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 6)
    fontCfgLayout.Add(self.paddingSpaces, 0, wx.ALIGN_CENTER_VERTICAL, 0)
    

    # Combine Input Page Layouts
    upperInputLayout = wx.BoxSizer(wx.HORIZONTAL)
    upperInputLayout.Add(ioLayout, 1, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER, 0)
    upperInputLayout.Add(selectLayout, 0, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER, 0)
    
    inputPageLayout.Add(upperInputLayout, 1, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER, 0)
    inputPageLayout.Add(fontCfgLayout, 0, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER, 6)
    
    
    
    # --- Config Page ---
    
    
    
    
    # Combine Top-level Layouts
    notebook.AddPage(inputPage, 'Scrambler', select=True)
    notebook.AddPage(configPage, 'Settings')
    
    inputPage.SetSizer(inputPageLayout)
    configPage.SetSizer(configPageLayout)
    rootLayout.Add(notebook, 1, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER, 6)
    panel.SetSizer(rootLayout)
    
    self.configUI()
  

  # Configure UI and UI Events
  def configUI(self):
    
    # Initial Values
    for name in self.config.fontMapNames:
      self.selectedFonts.Append(name)
    
    self.filterEmoji.SetValue(True)
    self.randomFont.SetValue(True)
    
    self.zalgoMode.Append('None')
    self.zalgoMode.Append('Low')
    self.zalgoMode.Append('Medium')
    self.zalgoMode.Append('High')
    self.zalgoMode.Append('Very High')
    self.zalgoMode.Append('Spam')
    self.zalgoMode.SetSelection(0)
    self.zalgoUpCheck.SetValue(True)
    self.zalgoMidCheck.SetValue(True)
    self.zalgoDownCheck.SetValue(True)
    
    
    # Font Mode Selection Data
    #  - If not using random, only 1 index will be selected at a time
    #  - If using random, the bool states from randomFontIndexStates will determine each check
    self.singleFontIndex        = 0
    self.randomFontIndexStates  = []
    for i in range(0, self.config.fontCount):
      self.randomFontIndexStates.append(True) # Random by default
    self.ApplyFontSelection()
    
    
    # Events
    self.selectedFonts.Bind(wx.EVT_CHECKLISTBOX, self.OnFontSelected)
    self.selectAll.Bind(wx.EVT_BUTTON, self.OnFontSelectAll)
    self.deselectAll.Bind(wx.EVT_BUTTON, self.OnFontDeselectAll)
    self.randomFont.Bind(wx.EVT_CHECKBOX, self.OnFontModeChanged)
    self.inputText.Bind(wx.EVT_TEXT, self.OnTextInput)
    
    
    
  ####################
  ## UI Functions
  ####################
    
  def UpdateCharCount(self):
    count = len(self.outputText.GetValue())
    self.charCount.SetLabel('Characters: ' + str(count))
    
    if count < 15000:
      self.charCount.SetForegroundColour(wx.NullColour)
    elif 15000 <= count < 50000:
      self.charCount.SetForegroundColour('#c9b42a')
    elif 50000 <= count < 100000:
      self.charCount.SetForegroundColour('#e58c20')
    else:
      self.charCount.SetForegroundColour('#ee0000')
    
    
      
      
  def UpdateOutput(self):
    outString = self.inputText.GetValue()
    
    if self.filterEmoji.IsChecked():
      outString = self.FilterEmojiDigits(outString)
    
    idx = self.zalgoMode.GetSelection()
    if idx > 0:
      upCharMax   = 0
      midCharMax  = 0
      downCharMax = 0
      if self.zalgoUpCheck.IsChecked:
        upCharMax   = (idx * 6) + idx # The higher the index, the more zalgo
      if self.zalgoMidCheck.IsChecked:
        midCharMax  = (idx * 6) + idx
      if self.zalgoDownCheck.IsChecked:
        downCharMax = (idx * 6) + idx
      outString = self.ZalgoifyText(outString, upCharMax, midCharMax, downCharMax)
      
    self.outputText.SetValue(self.inputText.GetValue())
    self.UpdateCharCount()

  
  # Apply font selection to checkboxes based on random mode
  def ApplyFontSelection(self):
    for i in range(0, self.config.fontCount):
      if self.randomFont.IsChecked():
        self.selectedFonts.Check(i, self.randomFontIndexStates[i])
      else:
        self.selectedFonts.Check(i, True if i == self.singleFontIndex else False)
    
    
    
  ####################
  ## Core/Misc Functions
  ####################
  
  def FilterEmojiDigits(self, str):
    pass
    
  # Return a string with randomly inserted 'Zalgo' characters, specifying the maximum amount of each type
  def ZalgoifyText(self, str, upCharMax=0, midCharMax=0, downCharMax=0):
    pass
    
    

  ####################
  ## Events
  ####################
  
  def OnFontSelectAll(self, event):
    if self.randomFont.IsChecked():
      for i in range(0, len(self.randomFontIndexStates)):
        self.randomFontIndexStates[i] = True
      self.ApplyFontSelection()
    # Do nothing if not random mode
  
  
  def OnFontDeselectAll(self, event):
    if self.randomFont.IsChecked():
      for i in range(0, len(self.randomFontIndexStates)):
        self.randomFontIndexStates[i] = False
      self.ApplyFontSelection()
    # Do nothing if not random mode
    
    
  def OnFontSelected(self, event):
    index = event.GetInt()
    if self.randomFont.IsChecked():
      self.randomFontIndexStates[index] = self.selectedFonts.IsChecked(index)
    else:
      self.singleFontIndex = index
    self.ApplyFontSelection()
    
  
  def OnFontModeChanged(self, event):
    if self.randomFont.IsChecked():
      self.selectAll.Enable()
      self.deselectAll.Enable()
    else:
      self.selectAll.Disable()
      self.deselectAll.Disable()
    self.ApplyFontSelection() # Mode is changed, selection will too
    self.UpdateOutput()
    
    
  def OnTextInput(self, event):
    self.UpdateOutput()
    

def main():
  app = wx.App()
  wx.InitAllImageHandlers()
  MainWindow(None, 'Text Scrambler')
  app.MainLoop()
  
  
  
if __name__ == "__main__":
  main()
  