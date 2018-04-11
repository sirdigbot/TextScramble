#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#########################################################################
## This Source Code Form is subject to the terms of the Mozilla Public  #
## License, v. 2.0. If a copy of the MPL was not distributed with this  #
## file, You can obtain one at http://mozilla.org/MPL/2.0/.             #
#########################################################################
## config.py                                                            #
##                                                                      #
## Config contains a list of all the font maps and their default settings
## All fontmaps have the same default settings except for their asciimap arrays
## with the exception of the Emoji font which has a default padding of 1 (emoji letters make emoji flags)
##
##
## 
##  {
##    "name": "Cursive",     # The font's display name
##    "padding": "0",        # Spaces put before/between each character
##    "asciimapoffs": "48",  # Starting index offset (0 based) for the ASCII map
##                           # The end index will be either 127 or the last index in the asciimap (lowest)
##
##    "asciimap": [          # An array of unicode characters mapped to ASCII indexes (1:1 mapping)
##        ["A", true],       # Contains an array with a unicode character and a bool value (for toggling chars)
##        ...
##     ],                  
##
##    "miscmap": {},         # An object/dictionary/hashmap of non-ASCII characters and their font mapping.
##                           # This is always empty by default, but allows for users to customise the mappings
##                           # asciimap array will always be searched first so this doesn't override it.
##  }
##                                                                      #
#########################################################################


import json
import os
import wx




config_default = r'''

[


  {
    "name": "Cursive",
    "padding": "0",
    "asciimapoffs": "48",
    "asciimap": [
      ["\uD835\uDFE2", true], ["\uD835\uDFE3", true], ["\uD835\uDFE4", true], ["\uD835\uDFE5", true], ["\uD835\uDFE6", true], 
      ["\uD835\uDFE7", true], ["\uD835\uDFE8", true], ["\uD835\uDFE9", true], ["\uD835\uDFEA", true], ["\uD835\uDFEB", true], 
      [":", true], [";", true], ["<", true], ["=", true], [">", true],
      ["?", true], ["@", true],
      ["\uD835\uDC9C", true], ["\uD835\uDC35", true], ["\uD835\uDC9E", true], ["\uD835\uDC9F", true], ["\uD835\uDC38", true], 
      ["\uD835\uDC39", true], ["\uD835\uDCA2", true], ["\uD835\uDC3B", true], ["\uD835\uDC3C", true], ["\uD835\uDCA5", true], 
      ["\uD835\uDCA6", true], ["\uD835\uDC3F", true], ["\uD835\uDC40", true], ["\uD835\uDCA9", true], ["\uD835\uDCAA", true], 
      ["\uD835\uDCAB", true], ["\uD835\uDCAC", true], ["\uD835\uDC45", true], ["\uD835\uDCAE", true], ["\uD835\uDCAF", true], 
      ["\uD835\uDCB0", true], ["\uD835\uDCB1", true], ["\uD835\uDCB2", true], ["\uD835\uDCB3", true], ["\uD835\uDCB4", true], 
      ["\uD835\uDCB5", true], 
      ["[", true], ["\\", true], ["]", true], ["^", true], ["_", true], ["`", true],
      ["\uD835\uDCB6", true], ["\uD835\uDCB7", true], ["\uD835\uDCB8", true], ["\uD835\uDCB9", true], ["\uD835\uDC52", true], 
      ["\uD835\uDCBB", true], ["\uD835\uDC54", true], ["\uD835\uDCBD", true], ["\uD835\uDCBE", true], ["\uD835\uDCBF", true], 
      ["\uD835\uDCC0", true], ["\uD835\uDCC1", true], ["\uD835\uDCC2", true], ["\uD835\uDCC3", true], ["\uD835\uDC5C", true], 
      ["\uD835\uDCC5", true], ["\uD835\uDCC6", true], ["\uD835\uDCC7", true], ["\uD835\uDCC8", true], ["\uD835\uDCC9", true], 
      ["\uD835\uDCCA", true], ["\uD835\uDCCB", true], ["\uD835\uDCCC", true], ["\uD835\uDCCD", true], ["\uD835\uDCCE", true], 
      ["\uD835\uDCCF", true]
    ],
    
    "miscmap": {}
  },


  {
    "name": "Bold Cursive",
    "padding": "0",
    "asciimapoffs": "48",
    "asciimap": [
      ["0", true], ["1", true], ["2", true], ["3", true], ["4", true], 
      ["5", true], ["6", true], ["7", true], ["8", true], ["9", true], 
      [":", true], [";", true], ["<", true], ["=", true], [">", true],
      ["?", true], ["@", true],
      ["\uD835\uDCD0", true], ["\uD835\uDCD1", true], ["\uD835\uDCD2", true], ["\uD835\uDCD3", true], ["\uD835\uDCD4", true], 
      ["\uD835\uDCD5", true], ["\uD835\uDCD6", true], ["\uD835\uDCD7", true], ["\uD835\uDCD8", true], ["\uD835\uDCD9", true], 
      ["\uD835\uDCDA", true], ["\uD835\uDCDB", true], ["\uD835\uDCDC", true], ["\uD835\uDCDD", true], ["\uD835\uDCDE", true], 
      ["\uD835\uDCDF", true], ["\uD835\uDCE0", true], ["\uD835\uDCE1", true], ["\uD835\uDCE2", true], ["\uD835\uDCE3", true], 
      ["\uD835\uDCE4", true], ["\uD835\uDCE5", true], ["\uD835\uDCE6", true], ["\uD835\uDCE7", true], ["\uD835\uDCE8", true], 
      ["\uD835\uDCE9", true], 
      ["[", true], ["\\", true], ["]", true], ["^", true], ["_", true], ["`", true],
      ["\uD835\uDCEA", true], ["\uD835\uDCEB", true], ["\uD835\uDCEC", true], ["\uD835\uDCED", true], ["\uD835\uDCEE", true], 
      ["\uD835\uDCEF", true], ["\uD835\uDCF0", true], ["\uD835\uDCF1", true], ["\uD835\uDCF2", true], ["\uD835\uDCF3", true], 
      ["\uD835\uDCF4", true], ["\uD835\uDCF5", true], ["\uD835\uDCF6", true], ["\uD835\uDCF7", true], ["\uD835\uDCF8", true], 
      ["\uD835\uDCF9", true], ["\uD835\uDCFA", true], ["\uD835\uDCFB", true], ["\uD835\uDCFC", true], ["\uD835\uDCFD", true], 
      ["\uD835\uDCFE", true], ["\uD835\uDCFF", true], ["\uD835\uDD00", true], ["\uD835\uDD01", true], ["\uD835\uDD02", true], 
      ["\uD835\uDD03", true]
    ],
    
    "miscmap": {}
  },


  {
    "name": "Hollow",
    "padding": "0",
    "asciimapoffs": "48",
    "asciimap": [
      ["\uD835\uDFD8", true], ["\uD835\uDFD9", true], ["\uD835\uDFDA", true], ["\uD835\uDFDB", true], ["\uD835\uDFDC", true], 
      ["\uD835\uDFDD", true], ["\uD835\uDFDE", true], ["\uD835\uDFDF", true], ["\uD835\uDFE0", true], ["\uD835\uDFE1", true], 
      [":", true], [";", true], ["<", true], ["=", true], [">", true],
      ["?", true], ["@", true],
      ["\uD835\uDD38", true], ["\uD835\uDD39", true], ["\u2102", true], ["\uD835\uDD3B", true], ["\uD835\uDD3C", true], 
      ["\uD835\uDD3D", true], ["\uD835\uDD3E", true], ["\u210D", true], ["\uD835\uDD40", true], ["\uD835\uDD41", true], 
      ["\uD835\uDD42", true], ["\uD835\uDD43", true], ["\uD835\uDD44", true], ["\u2115", true], ["\uD835\uDD46", true], 
      ["\u2119", true], ["\u211A", true], ["\u211D", true], ["\uD835\uDD4A", true], ["\uD835\uDD4B", true], 
      ["\uD835\uDD4C", true], ["\uD835\uDD4D", true], ["\uD835\uDD4E", true], ["\uD835\uDD4F", true], ["\uD835\uDD50", true], 
      ["\u2124", true], 
      ["[", true], ["\\", true], ["]", true], ["^", true], ["_", true], ["`", true],
      ["\uD835\uDD52", true], ["\uD835\uDD53", true], ["\uD835\uDD54", true], ["\uD835\uDD55", true], ["\uD835\uDD56", true], 
      ["\uD835\uDD57", true], ["\uD835\uDD58", true], ["\uD835\uDD59", true], ["\uD835\uDD5A", true], ["\uD835\uDD5B", true], 
      ["\uD835\uDD5C", true], ["\uD835\uDD5D", true], ["\uD835\uDD5E", true], ["\uD835\uDD5F", true], ["\uD835\uDD60", true], 
      ["\uD835\uDD61", true], ["\uD835\uDD62", true], ["\uD835\uDD63", true], ["\uD835\uDD64", true], ["\uD835\uDD65", true], 
      ["\uD835\uDD66", true], ["\uD835\uDD67", true], ["\uD835\uDD68", true], ["\uD835\uDD69", true], ["\uD835\uDD6A", true], 
      ["\uD835\uDD6B", true]
    ],
    
    "miscmap": {}
  },


  {
    "name": "Gothic",
    "padding": "0",
    "asciimapoffs": "48",
    "asciimap": [
      ["0", true], ["1", true], ["2", true], ["3", true], ["4", true], 
      ["5", true], ["6", true], ["7", true], ["8", true], ["9", true], 
      [":", true], [";", true], ["<", true], ["=", true], [">", true],
      ["?", true], ["@", true],
      ["\uD835\uDD04", true], ["\uD835\uDD05", true], ["\u212D", true], ["\uD835\uDD07", true], ["\uD835\uDD08", true], 
      ["\uD835\uDD09", true], ["\uD835\uDD0A", true], ["\u210C", true], ["\u2111", true], ["\uD835\uDD0D", true], 
      ["\uD835\uDD0E", true], ["\uD835\uDD0F", true], ["\uD835\uDD10", true], ["\uD835\uDD11", true], ["\uD835\uDD12", true], 
      ["\uD835\uDD13", true], ["\uD835\uDD14", true], ["\u211C", true], ["\uD835\uDD16", true], ["\uD835\uDD17", true], 
      ["\uD835\uDD18", true], ["\uD835\uDD19", true], ["\uD835\uDD1A", true], ["\uD835\uDD1B", true], ["\uD835\uDD1C", true], 
      ["\u2128", true], 
      ["[", true], ["\\", true], ["]", true], ["^", true], ["_", true], ["`", true],
      ["\uD835\uDD1E", true], ["\uD835\uDD1F", true], ["\uD835\uDD20", true], ["\uD835\uDD21", true], ["\uD835\uDD22", true], 
      ["\uD835\uDD23", true], ["\uD835\uDD24", true], ["\uD835\uDD25", true], ["\uD835\uDD26", true], ["\uD835\uDD27", true], 
      ["\uD835\uDD28", true], ["\uD835\uDD29", true], ["\uD835\uDD2A", true], ["\uD835\uDD2B", true], ["\uD835\uDD2C", true], 
      ["\uD835\uDD2D", true], ["\uD835\uDD2E", true], ["\uD835\uDD2F", true], ["\uD835\uDD30", true], ["\uD835\uDD31", true], 
      ["\uD835\uDD32", true], ["\uD835\uDD33", true], ["\uD835\uDD34", true], ["\uD835\uDD35", true], ["\uD835\uDD36", true], 
      ["\uD835\uDD37", true]
    ],
    
    "miscmap": {}
  },


  {
    "name": "Bold Gothic",
    "padding": "0",
    "asciimapoffs": "48",
    "asciimap": [
      ["0", true], ["1", true], ["2", true], ["3", true], ["4", true], 
      ["5", true], ["6", true], ["7", true], ["8", true], ["9", true], 
      [":", true], [";", true], ["<", true], ["=", true], [">", true],
      ["?", true], ["@", true],
      ["\uD835\uDD6C", true], ["\uD835\uDD6D", true], ["\uD835\uDD6E", true], ["\uD835\uDD6F", true], ["\uD835\uDD70", true], 
      ["\uD835\uDD71", true], ["\uD835\uDD72", true], ["\uD835\uDD73", true], ["\uD835\uDD74", true], ["\uD835\uDD75", true], 
      ["\uD835\uDD76", true], ["\uD835\uDD77", true], ["\uD835\uDD78", true], ["\uD835\uDD79", true], ["\uD835\uDD7A", true], 
      ["\uD835\uDD7B", true], ["\uD835\uDD7C", true], ["\uD835\uDD7D", true], ["\uD835\uDD7E", true], ["\uD835\uDD7F", true], 
      ["\uD835\uDD80", true], ["\uD835\uDD81", true], ["\uD835\uDD82", true], ["\uD835\uDD83", true], ["\uD835\uDD84", true], 
      ["\uD835\uDD85", true], 
      ["[", true], ["\\", true], ["]", true], ["^", true], ["_", true], ["`", true],
      ["\uD835\uDD86", true], ["\uD835\uDD87", true], ["\uD835\uDD88", true], ["\uD835\uDD89", true], ["\uD835\uDD8A", true], 
      ["\uD835\uDD8B", true], ["\uD835\uDD8C", true], ["\uD835\uDD8D", true], ["\uD835\uDD8E", true], ["\uD835\uDD8F", true], 
      ["\uD835\uDD90", true], ["\uD835\uDD91", true], ["\uD835\uDD92", true], ["\uD835\uDD93", true], ["\uD835\uDD94", true], 
      ["\uD835\uDD95", true], ["\uD835\uDD96", true], ["\uD835\uDD97", true], ["\uD835\uDD98", true], ["\uD835\uDD99", true], 
      ["\uD835\uDD9A", true], ["\uD835\uDD9B", true], ["\uD835\uDD9C", true], ["\uD835\uDD9D", true], ["\uD835\uDD9E", true], 
      ["\uD835\uDD9F", true]
    ],
    
    "miscmap": {}
  },


  {
    "name": "Circled",
    "padding": "0",
    "asciimapoffs": "48",
    "asciimap": [
      ["\u24EA", true], ["\u2460", true], ["\u2461", true], ["\u2462", true], ["\u2463", true], 
      ["\u2464", true], ["\u2465", true], ["\u2466", true], ["\u2467", true], ["\u2468", true], 
      [":", true], [";", true], ["<", true], ["=", true], [">", true],
      ["?", true], ["@", true],
      ["\u24B6", true], ["\u24B7", true], ["\u24B8", true], ["\u24B9", true], ["\u24BA", true], 
      ["\u24BB", true], ["\u24BC", true], ["\u24BD", true], ["\u24BE", true], ["\u24BF", true], 
      ["\u24C0", true], ["\u24C1", true], ["\u24C2", true], ["\u24C3", true], ["\u24C4", true], 
      ["\u24C5", true], ["\u24C6", true], ["\u24C7", true], ["\u24C8", true], ["\u24C9", true], 
      ["\u24CA", true], ["\u24CB", true], ["\u24CC", true], ["\u24CD", true], ["\u24CE", true], 
      ["\u24CF", true], 
      ["[", true], ["\\", true], ["]", true], ["^", true], ["_", true], ["`", true],
      ["\u24D0", true], ["\u24D1", true], ["\u24D2", true], ["\u24D3", true], ["\u24D4", true], 
      ["\u24D5", true], ["\u24D6", true], ["\u24D7", true], ["\u24D8", true], ["\u24D9", true], 
      ["\u24DA", true], ["\u24DB", true], ["\u24DC", true], ["\u24DD", true], ["\u24DE", true], 
      ["\u24DF", true], ["\u24E0", true], ["\u24E1", true], ["\u24E2", true], ["\u24E3", true], 
      ["\u24E4", true], ["\u24E5", true], ["\u24E6", true], ["\u24E7", true], ["\u24E8", true], 
      ["\u24E9", true]
    ],
    
    "miscmap": {}
  },


  {
    "name": "Negative Circled",
    "padding": "0",
    "asciimapoffs": "48",
    "asciimap": [
      ["\u24FF", true], ["\u2776", true], ["\u2777", true], ["\u2778", true], ["\u2779", true], 
      ["\u277A", true], ["\u277B", true], ["\u277C", true], ["\u277D", true], ["\u277E", true], 
      [":", true], [";", true], ["<", true], ["=", true], [">", true],
      ["?", true], ["@", true],
      ["\uD83C\uDD50", true], ["\uD83C\uDD51", true], ["\uD83C\uDD52", true], ["\uD83C\uDD53", true], ["\uD83C\uDD54", true], 
      ["\uD83C\uDD55", true], ["\uD83C\uDD56", true], ["\uD83C\uDD57", true], ["\uD83C\uDD58", true], ["\uD83C\uDD59", true], 
      ["\uD83C\uDD5A", true], ["\uD83C\uDD5B", true], ["\uD83C\uDD5C", true], ["\uD83C\uDD5D", true], ["\uD83C\uDD5E", true], 
      ["\uD83C\uDD5F", true], ["\uD83C\uDD60", true], ["\uD83C\uDD61", true], ["\uD83C\uDD62", true], ["\uD83C\uDD63", true], 
      ["\uD83C\uDD64", true], ["\uD83C\uDD65", true], ["\uD83C\uDD66", true], ["\uD83C\uDD67", true], ["\uD83C\uDD68", true], 
      ["\uD83C\uDD69", true], 
      ["[", true], ["\\", true], ["]", true], ["^", true], ["_", true], ["`", true],
      ["\uD83C\uDD50", true], ["\uD83C\uDD51", true], ["\uD83C\uDD52", true], ["\uD83C\uDD53", true], ["\uD83C\uDD54", true], 
      ["\uD83C\uDD55", true], ["\uD83C\uDD56", true], ["\uD83C\uDD57", true], ["\uD83C\uDD58", true], ["\uD83C\uDD59", true], 
      ["\uD83C\uDD5A", true], ["\uD83C\uDD5B", true], ["\uD83C\uDD5C", true], ["\uD83C\uDD5D", true], ["\uD83C\uDD5E", true], 
      ["\uD83C\uDD5F", true], ["\uD83C\uDD60", true], ["\uD83C\uDD61", true], ["\uD83C\uDD62", true], ["\uD83C\uDD63", true], 
      ["\uD83C\uDD64", true], ["\uD83C\uDD65", true], ["\uD83C\uDD66", true], ["\uD83C\uDD67", true], ["\uD83C\uDD68", true], 
      ["\uD83C\uDD69", true]
    ],
    
    "miscmap": {}
  },


  {
    "name": "Squared",
    "padding": "0",
    "asciimapoffs": "48",
    "asciimap": [
      ["0", true], ["1", true], ["2", true], ["3", true], ["4", true], 
      ["5", true], ["6", true], ["7", true], ["8", true], ["9", true], 
      [":", true], [";", true], ["<", true], ["=", true], [">", true],
      ["?", true], ["@", true],
      ["\uD83C\uDD30", true], ["\uD83C\uDD31", true], ["\uD83C\uDD32", true], ["\uD83C\uDD33", true], ["\uD83C\uDD34", true], 
      ["\uD83C\uDD35", true], ["\uD83C\uDD36", true], ["\uD83C\uDD37", true], ["\uD83C\uDD38", true], ["\uD83C\uDD39", true], 
      ["\uD83C\uDD3A", true], ["\uD83C\uDD3B", true], ["\uD83C\uDD3C", true], ["\uD83C\uDD3D", true], ["\uD83C\uDD3E", true], 
      ["\uD83C\uDD3F", true], ["\uD83C\uDD40", true], ["\uD83C\uDD41", true], ["\uD83C\uDD42", true], ["\uD83C\uDD43", true], 
      ["\uD83C\uDD44", true], ["\uD83C\uDD45", true], ["\uD83C\uDD46", true], ["\uD83C\uDD47", true], ["\uD83C\uDD48", true], 
      ["\uD83C\uDD49", true], 
      ["[", true], ["\\", true], ["]", true], ["^", true], ["_", true], ["`", true],
      ["\uD83C\uDD30", true], ["\uD83C\uDD31", true], ["\uD83C\uDD32", true], ["\uD83C\uDD33", true], ["\uD83C\uDD34", true], 
      ["\uD83C\uDD35", true], ["\uD83C\uDD36", true], ["\uD83C\uDD37", true], ["\uD83C\uDD38", true], ["\uD83C\uDD39", true], 
      ["\uD83C\uDD3A", true], ["\uD83C\uDD3B", true], ["\uD83C\uDD3C", true], ["\uD83C\uDD3D", true], ["\uD83C\uDD3E", true], 
      ["\uD83C\uDD3F", true], ["\uD83C\uDD40", true], ["\uD83C\uDD41", true], ["\uD83C\uDD42", true], ["\uD83C\uDD43", true], 
      ["\uD83C\uDD44", true], ["\uD83C\uDD45", true], ["\uD83C\uDD46", true], ["\uD83C\uDD47", true], ["\uD83C\uDD48", true], 
      ["\uD83C\uDD49", true]
    ],
    
    "miscmap": {}
  },


  {
    "name": "Negative Squared",
    "padding": "0",
    "asciimapoffs": "48",
    "asciimap": [
      ["0", true], ["1", true], ["2", true], ["3", true], ["4", true], 
      ["5", true], ["6", true], ["7", true], ["8", true], ["9", true], 
      [":", true], [";", true], ["<", true], ["=", true], [">", true],
      ["?", true], ["@", true],
      ["\uD83C\uDD70", true], ["\uD83C\uDD71", true], ["\uD83C\uDD72", true], ["\uD83C\uDD73", true], ["\uD83C\uDD74", true], 
      ["\uD83C\uDD75", true], ["\uD83C\uDD76", true], ["\uD83C\uDD77", true], ["\uD83C\uDD78", true], ["\uD83C\uDD79", true], 
      ["\uD83C\uDD7A", true], ["\uD83C\uDD7B", true], ["\uD83C\uDD7C", true], ["\uD83C\uDD7D", true], ["\uD83C\uDD7E", true], 
      ["\uD83C\uDD7F", true], ["\uD83C\uDD80", true], ["\uD83C\uDD81", true], ["\uD83C\uDD82", true], ["\uD83C\uDD83", true], 
      ["\uD83C\uDD84", true], ["\uD83C\uDD85", true], ["\uD83C\uDD86", true], ["\uD83C\uDD87", true], ["\uD83C\uDD88", true], 
      ["\uD83C\uDD89", true], 
      ["[", true], ["\\", true], ["]", true], ["^", true], ["_", true], ["`", true],
      ["\uD83C\uDD70", true], ["\uD83C\uDD71", true], ["\uD83C\uDD72", true], ["\uD83C\uDD73", true], ["\uD83C\uDD74", true], 
      ["\uD83C\uDD75", true], ["\uD83C\uDD76", true], ["\uD83C\uDD77", true], ["\uD83C\uDD78", true], ["\uD83C\uDD79", true], 
      ["\uD83C\uDD7A", true], ["\uD83C\uDD7B", true], ["\uD83C\uDD7C", true], ["\uD83C\uDD7D", true], ["\uD83C\uDD7E", true], 
      ["\uD83C\uDD7F", true], ["\uD83C\uDD80", true], ["\uD83C\uDD81", true], ["\uD83C\uDD82", true], ["\uD83C\uDD83", true], 
      ["\uD83C\uDD84", true], ["\uD83C\uDD85", true], ["\uD83C\uDD86", true], ["\uD83C\uDD87", true], ["\uD83C\uDD88", true], 
      ["\uD83C\uDD89", true]
    ],
    
    "miscmap": {}
  },


  {
    "name": "EXTRA THICC",
    "padding": "0",
    "asciimapoffs": "48",
    "asciimap": [
      ["0", true], ["1", true], ["2", true], ["3", true], ["4", true], 
      ["5", true], ["6", true], ["7", true], ["8", true], ["9", true], 
      [":", true], [";", true], ["<", true], ["=", true], [">", true],
      ["?", true], ["@", true],
      ["\u5342", true], ["\u4E43", true], ["\u531A", true], ["\u5200", true], ["\u4E47", true], 
      ["\u4E0B", true], ["\u53B6", true], ["\u5344", true], ["\u5DE5", true], ["\u4E01", true], 
      ["\u957F", true], ["\u4E5A", true], ["\u4ECE", true], ["\uD841\uDE28", true], ["\u53E3", true], 
      ["\u5C38", true], ["\u353F", true], ["\u5C3A", true], ["\u4E02", true], ["\u4E05", true], 
      ["\u51F5", true], ["\u30EA", true], ["\u5C71", true], ["\u4E42", true], ["\u4E2B", true], 
      ["\u4E59", true], 
      ["[", true], ["\\", true], ["]", true], ["^", true], ["_", true], ["`", true],
      ["\u5342", true], ["\u4E43", true], ["\u531A", true], ["\u5200", true], ["\u4E47", true], 
      ["\u4E0B", true], ["\u53B6", true], ["\u5344", true], ["\u5DE5", true], ["\u4E01", true], 
      ["\u957F", true], ["\u4E5A", true], ["\u4ECE", true], ["\uD841\uDE28", true], ["\u53E3", true], 
      ["\u5C38", true], ["\u353F", true], ["\u5C3A", true], ["\u4E02", true], ["\u4E05", true], 
      ["\u51F5", true], ["\u30EA", true], ["\u5C71", true], ["\u4E42", true], ["\u4E2B", true], 
      ["\u4E59", true]
    ],
    
    "miscmap": {}
  },


  {
    "name": "Emoji",
    "padding": "1",
    "asciimapoffs": "48",
    "asciimap": [
      ["0\u20E3", true], ["1\u20E3", true], ["2\u20E3", true], ["3\u20E3", true], ["4\u20E3", true], 
      ["5\u20E3", true], ["6\u20E3", true], ["7\u20E3", true], ["8\u20E3", true], ["9\u20E3", true], 
      [":", true], [";", true], ["<", true], ["=", true], [">", true],
      ["?", true], ["@", true],
      ["\uD83C\uDDE6", true], ["\uD83C\uDDE7", true], ["\uD83C\uDDE8", true], ["\uD83C\uDDE9", true], ["\uD83C\uDDEA", true], 
      ["\uD83C\uDDEB", true], ["\uD83C\uDDEC", true], ["\uD83C\uDDED", true], ["\uD83C\uDDEE", true], ["\uD83C\uDDEF", true], 
      ["\uD83C\uDDF0", true], ["\uD83C\uDDF1", true], ["\uD83C\uDDF2", true], ["\uD83C\uDDF3", true], ["\uD83C\uDDF4", true], 
      ["\uD83C\uDDF5", true], ["\uD83C\uDDF6", true], ["\uD83C\uDDF7", true], ["\uD83C\uDDF8", true], ["\uD83C\uDDF9", true], 
      ["\uD83C\uDDFA", true], ["\uD83C\uDDFB", true], ["\uD83C\uDDFC", true], ["\uD83C\uDDFD", true], ["\uD83C\uDDFE", true], 
      ["\uD83C\uDDFF", true], 
      ["[", true], ["\\", true], ["]", true], ["^", true], ["_", true], ["`", true],
      ["\uD83C\uDDE6", true], ["\uD83C\uDDE7", true], ["\uD83C\uDDE8", true], ["\uD83C\uDDE9", true], ["\uD83C\uDDEA", true], 
      ["\uD83C\uDDEB", true], ["\uD83C\uDDEC", true], ["\uD83C\uDDED", true], ["\uD83C\uDDEE", true], ["\uD83C\uDDEF", true], 
      ["\uD83C\uDDF0", true], ["\uD83C\uDDF1", true], ["\uD83C\uDDF2", true], ["\uD83C\uDDF3", true], ["\uD83C\uDDF4", true], 
      ["\uD83C\uDDF5", true], ["\uD83C\uDDF6", true], ["\uD83C\uDDF7", true], ["\uD83C\uDDF8", true], ["\uD83C\uDDF9", true], 
      ["\uD83C\uDDFA", true], ["\uD83C\uDDFB", true], ["\uD83C\uDDFC", true], ["\uD83C\uDDFD", true], ["\uD83C\uDDFE", true], 
      ["\uD83C\uDDFF", true]
    ],
    
    "miscmap": {}
  },


  {
    "name": "Fullwidth",
    "padding": "0",
    "asciimapoffs": "48",
    "asciimap": [
      ["\uFF10", true], ["\uFF11", true], ["\uFF12", true], ["\uFF13", true], ["\uFF14", true], 
      ["\uFF15", true], ["\uFF16", true], ["\uFF17", true], ["\uFF18", true], ["\uFF19", true], 
      [":", true], [";", true], ["<", true], ["=", true], [">", true],
      ["?", true], ["@", true],
      ["\uFF21", true], ["\uFF22", true], ["\uFF23", true], ["\uFF24", true], ["\uFF25", true], 
      ["\uFF26", true], ["\uFF27", true], ["\uFF28", true], ["\uFF29", true], ["\uFF2A", true], 
      ["\uFF2B", true], ["\uFF2C", true], ["\uFF2D", true], ["\uFF2E", true], ["\uFF2F", true], 
      ["\uFF30", true], ["\uFF31", true], ["\uFF32", true], ["\uFF33", true], ["\uFF34", true], 
      ["\uFF35", true], ["\uFF36", true], ["\uFF37", true], ["\uFF38", true], ["\uFF39", true], 
      ["\uFF3A", true], 
      ["[", true], ["\\", true], ["]", true], ["^", true], ["_", true], ["`", true],
      ["\uFF41", true], ["\uFF42", true], ["\uFF43", true], ["\uFF44", true], ["\uFF45", true], 
      ["\uFF46", true], ["\uFF47", true], ["\uFF48", true], ["\uFF49", true], ["\uFF4A", true], 
      ["\uFF4B", true], ["\uFF4C", true], ["\uFF4D", true], ["\uFF4E", true], ["\uFF4F", true], 
      ["\uFF50", true], ["\uFF51", true], ["\uFF52", true], ["\uFF53", true], ["\uFF54", true], 
      ["\uFF55", true], ["\uFF56", true], ["\uFF57", true], ["\uFF58", true], ["\uFF59", true], 
      ["\uFF5A", true]
    ],
    
    "miscmap": {}
  },


  {
    "name": "Parenthesized",
    "padding": "0",
    "asciimapoffs": "48",
    "asciimap": [
      ["0", true], ["\u2474", true], ["\u2475", true], ["\u2476", true], ["\u2477", true], 
      ["\u2478", true], ["\u2479", true], ["\u247A", true], ["\u247B", true], ["\u247C", true], 
      [":", true], [";", true], ["<", true], ["=", true], [">", true],
      ["?", true], ["@", true],
      ["\u249C", true], ["\u249D", true], ["\u249E", true], ["\u249F", true], ["\u24A0", true], 
      ["\u24A1", true], ["\u24A2", true], ["\u24A3", true], ["\u24A4", true], ["\u24A5", true], 
      ["\u24A6", true], ["\u24A7", true], ["\u24A8", true], ["\u24A9", true], ["\u24AA", true], 
      ["\u24AB", true], ["\u24AC", true], ["\u24AD", true], ["\u24AE", true], ["\u24AF", true], 
      ["\u24B0", true], ["\u24B1", true], ["\u24B2", true], ["\u24B3", true], ["\u24B4", true], 
      ["\u24B5", true], 
      ["[", true], ["\\", true], ["]", true], ["^", true], ["_", true], ["`", true],
      ["\u249C", true], ["\u249D", true], ["\u249E", true], ["\u249F", true], ["\u24A0", true], 
      ["\u24A1", true], ["\u24A2", true], ["\u24A3", true], ["\u24A4", true], ["\u24A5", true], 
      ["\u24A6", true], ["\u24A7", true], ["\u24A8", true], ["\u24A9", true], ["\u24AA", true], 
      ["\u24AB", true], ["\u24AC", true], ["\u24AD", true], ["\u24AE", true], ["\u24AF", true], 
      ["\u24B0", true], ["\u24B1", true], ["\u24B2", true], ["\u24B3", true], ["\u24B4", true], 
      ["\u24B5", true]
    ],
    
    "miscmap": {}
  },


  {
    "name": "'Curvy'",
    "padding": "0",
    "asciimapoffs": "48",
    "asciimap": [
      ["0", true], ["1", true], ["2", true], ["3", true], ["4", true], 
      ["5", true], ["6", true], ["7", true], ["8", true], ["9", true], 
      [":", true], [";", true], ["<", true], ["=", true], [">", true],
      ["?", true], ["@", true],
      ["\u03B1", true], ["\u0432", true], ["\u00A2", true], ["\u2202", true], ["\u0454", true], 
      ["\u0192", true], ["\uFEED", true], ["\u043D", true], ["\u03B9", true], ["\u05E0", true], 
      ["\u043A", true], ["\u2113", true], ["\u043C", true], ["\u03B7", true], ["\u03C3", true], 
      ["\u03C1", true], ["\u06F9", true], ["\u044F", true], ["\u0455", true], ["\u0442", true], 
      ["\u03C5", true], ["\u03BD", true], ["\u03C9", true], ["\u03C7", true], ["\u0443", true], 
      ["\u0579", true], 
      ["[", true], ["\\", true], ["]", true], ["^", true], ["_", true], ["`", true],
      ["\u03B1", true], ["\u0432", true], ["\u00A2", true], ["\u2202", true], ["\u0454", true], 
      ["\u0192", true], ["\uFEED", true], ["\u043D", true], ["\u03B9", true], ["\u05E0", true], 
      ["\u043A", true], ["\u2113", true], ["\u043C", true], ["\u03B7", true], ["\u03C3", true], 
      ["\u03C1", true], ["\u06F9", true], ["\u044F", true], ["\u0455", true], ["\u0442", true], 
      ["\u03C5", true], ["\u03BD", true], ["\u03C9", true], ["\u03C7", true], ["\u0443", true], 
      ["\u0579", true]
    ],
    
    "miscmap": {}
  },


  {
    "name": "Faux Cyrllic",
    "padding": "0",
    "asciimapoffs": "48",
    "asciimap": [
      ["0", true], ["1", true], ["2", true], ["3", true], ["4", true], 
      ["5", true], ["6", true], ["7", true], ["8", true], ["9", true], 
      [":", true], [";", true], ["<", true], ["=", true], [">", true],
      ["?", true], ["@", true],
      ["\u0414", true], ["\u0411", true], ["\u0480", true], ["\u2181", true], ["\u0404", true], 
      ["F", true], ["\u0411", true], ["\u041D", true], ["\u0406", true], ["\u0408", true], 
      ["\u040C", true], ["L", true], ["\u041C", true], ["\u0418", true], ["\u0424", true], 
      ["\u0420", true], ["Q", true], ["\u042F", true], ["\u0405", true], ["\u0413", true], 
      ["\u0426", true], ["V", true], ["\u0429", true], ["\u0416", true], ["\u0427", true], 
      ["Z", true], 
      ["[", true], ["\\", true], ["]", true], ["^", true], ["_", true], ["`", true],
      ["\u0430", true], ["\u044A", true], ["\u0441", true], ["\u2181", true], ["\u044D", true], 
      ["f", true], ["\u0411", true], ["\u0402", true], ["\u0456", true], ["\u0458", true], 
      ["\u043A", true], ["l", true], ["\u043C", true], ["\u0438", true], ["\u043E", true], 
      ["\u0440", true], ["q", true], ["\u0453", true], ["\u0455", true], ["\u0442", true], 
      ["\u0446", true], ["v", true], ["\u0448", true], ["\u0445", true], ["\u040E", true], 
      ["z", true]
    ],
    
    "miscmap": {}
  },


  {
    "name": "Faux Ethiopic",
    "padding": "0",
    "asciimapoffs": "48",
    "asciimap": [
      ["0", true], ["1", true], ["2", true], ["3", true], ["4", true], 
      ["5", true], ["6", true], ["7", true], ["8", true], ["9", true], 
      [":", true], [";", true], ["<", true], ["=", true], [">", true],
      ["?", true], ["@", true],
      ["\u120D", true], ["\u130C", true], ["\u122D", true], ["\u12D5", true], ["\u127F", true], 
      ["\u127B", true], ["\u1297", true], ["\u12D8", true], ["\u130E", true], ["\u130B", true], 
      ["\u1315", true], ["\u1228", true], ["\u1320", true], ["\u12AD", true], ["\u12D0", true], 
      ["\u12E8", true], ["\u12D2", true], ["\u12EA", true], ["\u1290", true], ["\u1355", true], 
      ["\u1201", true], ["\u1200", true], ["\u1220", true], ["\u1238", true], ["\u1203", true], 
      ["\u130A", true], 
      ["[", true], ["\\", true], ["]", true], ["^", true], ["_", true], ["`", true],
      ["\u120D", true], ["\u130C", true], ["\u122D", true], ["\u12D5", true], ["\u127F", true], 
      ["\u127B", true], ["\u1297", true], ["\u12D8", true], ["\u130E", true], ["\u130B", true], 
      ["\u1315", true], ["\u1228", true], ["\u1320", true], ["\u12AD", true], ["\u12D0", true], 
      ["\u12E8", true], ["\u12D2", true], ["\u12EA", true], ["\u1290", true], ["\u1355", true], 
      ["\u1201", true], ["\u1200", true], ["\u1220", true], ["\u1238", true], ["\u1203", true], 
      ["\u130A", true]
    ],
    
    "miscmap": {}
  },


  {
    "name": "Superscript",
    "padding": "0",
    "asciimapoffs": "48",
    "asciimap": [
      ["\u2070", true], ["\u00B9", true], ["\u00B2", true], ["\u00B3", true], ["\u2074", true], 
      ["\u2075", true], ["\u2076", true], ["\u2077", true], ["\u2078", true], ["\u2079", true], 
      [":", true], [";", true], ["<", true], ["=", true], [">", true],
      ["?", true], ["@", true],
      ["\u1D2C", true], ["\u1D2E", true], ["\u1D9C", true], ["\u1D30", true], ["\u1D31", true], 
      ["\u1DA0", true], ["\u1D33", true], ["\u1D34", true], ["\u1D35", true], ["\u1D36", true], 
      ["\u1D37", true], ["\u1D38", true], ["\u1D39", true], ["\u1D3A", true], ["\u1D3C", true], 
      ["\u1D3E", true], ["Q", true], ["\u1D3F", true], ["\u02E2", true], ["\u1D40", true], 
      ["\u1D41", true], ["\u2C7D", true], ["\u1D42", true], ["\u02E3", true], ["\u02B8", true], 
      ["\u1DBB", true], 
      ["[", true], ["\\", true], ["]", true], ["^", true], ["_", true], ["`", true],
      ["\u1D43", true], ["\u1D47", true], ["\u1D9C", true], ["\u1D48", true], ["\u1D49", true], 
      ["\u1DA0", true], ["\u1D4D", true], ["\u02B0", true], ["\u2071", true], ["\u02B2", true], 
      ["\u1D4F", true], ["\u02E1", true], ["\u1D50", true], ["\u207F", true], ["\u1D52", true], 
      ["\u1D56", true], ["q", true], ["\u02B3", true], ["\u02E2", true], ["\u1D57", true], 
      ["\u1D58", true], ["\u1D5B", true], ["\u02B7", true], ["\u02E3", true], ["\u02B8", true], 
      ["\u1DBB", true]
    ],
    
    "miscmap": {}
  },


  {
    "name": "Inverted",
    "padding": "0",
    "asciimapoffs": "48",
    "asciimap": [
      ["0", true], ["1", true], ["2", true], ["3", true], ["4", true], 
      ["5", true], ["6", true], ["7", true], ["8", true], ["9", true], 
      [":", true], [";", true], ["<", true], ["=", true], [">", true],
      ["?", true], ["@", true],
      ["\u0250", true], ["q", true], ["\u0254", true], ["p", true], ["\u01DD", true], 
      ["\u025F", true], ["\u0183", true], ["\u0265", true], ["\u0131", true], ["\u027E", true], 
      ["\u029E", true], ["\u05DF", true], ["\u026F", true], ["u", true], ["o", true], 
      ["d", true], ["b", true], ["\u0279", true], ["s", true], ["\u0287", true], 
      ["n", true], ["\uD800\uDF21", true], ["\u028D", true], ["x", true], ["\u028E", true], 
      ["z", true], 
      ["[", true], ["\\", true], ["]", true], ["^", true], ["_", true], ["`", true],
      ["\u0250", true], ["q", true], ["\u0254", true], ["p", true], ["\u01DD", true], 
      ["\u025F", true], ["\u0183", true], ["\u0265", true], ["\u0131", true], ["\u027E", true], 
      ["\u029E", true], ["\u05DF", true], ["\u026F", true], ["u", true], ["o", true], 
      ["d", true], ["b", true], ["\u0279", true], ["s", true], ["\u0287", true], 
      ["n", true], ["\u028C", true], ["\u028D", true], ["x", true], ["\u028E", true], 
      ["z", true]
    ],
    
    "miscmap": {}
  },


  {
    "name": "Dotted",
    "padding": "0",
    "asciimapoffs": "48",
    "asciimap": [
      ["0", true], ["1", true], ["2", true], ["\u04DF", true], ["4", true], 
      ["5", true], ["6", true], ["7", true], ["8", true], ["9", true], 
      [":", true], [";", true], ["<", true], ["=", true], [">", true],
      ["?", true], ["@", true],
      ["\u00C4", true], ["\u1E04", true], ["\u010A", true], ["\u1E0A", true], ["\u0401", true], 
      ["\u1E1E", true], ["\u0120", true], ["\u1E26", true], ["\u0407", true], ["J", true], 
      ["\u1E32", true], ["\u1E36", true], ["\u1E40", true], ["\u1E44", true], ["\u00D6", true], 
      ["\u1E56", true], ["Q", true], ["\u1E5A", true], ["\u1E60", true], ["\u1E6A", true], 
      ["\u00DC", true], ["\u1E7E", true], ["\u1E84", true], ["\u1E8C", true], ["\u0178", true], 
      ["\u017B", true], 
      ["[", true], ["\\", true], ["]", true], ["^", true], ["_", true], ["`", true],
      ["\u00E4", true], ["\u1E05", true], ["\u010B", true], ["\u1E0B", true], ["\u00EB", true], 
      ["\u1E1F", true], ["\u0121", true], ["\u1E27", true], ["\u00EF", true], ["j", true], 
      ["\u1E33", true], ["\u1E37", true], ["\u1E41", true], ["\u1E45", true], ["\u00F6", true], 
      ["\u1E57", true], ["q", true], ["\u1E5B", true], ["\u1E61", true], ["\u1E97", true], 
      ["\u00FC", true], ["\u1E7F", true], ["\u1E85", true], ["\u1E8D", true], ["\u00FF", true], 
      ["\u017C", true]
    ],
    
    "miscmap": {}
  },


  {
    "name": "Stroked",
    "padding": "0",
    "asciimapoffs": "48",
    "asciimap": [
      ["0", true], ["1", true], ["\u01BB", true], ["3", true], ["4", true], 
      ["5", true], ["6", true], ["7", true], ["8", true], ["9", true], 
      [":", true], [";", true], ["<", true], ["=", true], [">", true],
      ["?", true], ["@", true],
      ["\u023A", true], ["\u0243", true], ["\u023B", true], ["\u0110", true], ["\u0246", true], 
      ["F", true], ["\u01E4", true], ["\u0126", true], ["\u0197", true], ["\u0248", true], 
      ["\uA740", true], ["\u0141", true], ["M", true], ["N", true], ["\u00D8", true], 
      ["\u2C63", true], ["\uA756", true], ["\u024C", true], ["S", true], ["\u0166", true], 
      ["\u1D7E", true], ["V", true], ["W", true], ["X", true], ["\u024E", true], 
      ["\u01B5", true], 
      ["[", true], ["\\", true], ["]", true], ["^", true], ["_", true], ["`", true],
      ["\u023A", true], ["\u0180", true], ["\u023C", true], ["\u0111", true], ["\u0247", true], 
      ["f", true], ["\u01E5", true], ["\u0127", true], ["\u0268", true], ["\u0249", true], 
      ["\uA741", true], ["\u0142", true], ["m", true], ["n", true], ["\u00F8", true], 
      ["\u1D7D", true], ["\uA757", true], ["\u024D", true], ["s", true], ["\u0167", true], 
      ["\u1D7E", true], ["v", true], ["w", true], ["x", true], ["\u024F", true], 
      ["\u01B6", true]
    ],
    
    "miscmap": {}
  },


  {
    "name": "Underlined",
    "padding": "0",
    "asciimapoffs": "48",
    "asciimap": [
      ["0\u035F", true], ["1\u035F", true], ["2\u035F", true], ["3\u035F", true], ["4\u035F", true], 
      ["5\u035F", true], ["6\u035F", true], ["7\u035F", true], ["8\u035F", true], ["9\u035F", true], 
      [":", true], [";", true], ["<", true], ["=", true], [">", true],
      ["?", true], ["@", true],
      ["A\u035F", true], ["B\u035F", true], ["C\u035F", true], ["D\u035F", true], ["E\u035F", true], 
      ["F\u035F", true], ["G\u035F", true], ["H\u035F", true], ["I\u035F", true], ["J\u035F", true], 
      ["K\u035F", true], ["L\u035F", true], ["M\u035F", true], ["N\u035F", true], ["O\u035F", true], 
      ["P\u035F", true], ["Q\u035F", true], ["R\u035F", true], ["S\u035F", true], ["T\u035F", true], 
      ["U\u035F", true], ["V\u035F", true], ["W\u035F", true], ["X\u035F", true], ["Y\u035F", true], 
      ["Z\u035F", true], 
      ["[", true], ["\\", true], ["]", true], ["^", true], ["_", true], ["`", true],
      ["a\u035F", true], ["b\u035F", true], ["c\u035F", true], ["d\u035F", true], ["e\u035F", true], 
      ["f\u035F", true], ["g\u035F", true], ["h\u035F", true], ["i\u035F", true], ["j\u035F", true], 
      ["k\u035F", true], ["l\u035F", true], ["m\u035F", true], ["n\u035F", true], ["o\u035F", true], 
      ["p\u035F", true], ["q\u035F", true], ["r\u035F", true], ["s\u035F", true], ["t\u035F", true], 
      ["u\u035F", true], ["v\u035F", true], ["w\u035F", true], ["x\u035F", true], ["y\u035F", true], 
      ["z\u035F", true]
    ],
    
    "miscmap": {}
  },


  {
    "name": "Double Underlined",
    "padding": "0",
    "asciimapoffs": "48",
    "asciimap": [
      ["0\u0347", true], ["1\u0347", true], ["2\u0347", true], ["3\u0347", true], ["4\u0347", true], 
      ["5\u0347", true], ["6\u0347", true], ["7\u0347", true], ["8\u0347", true], ["9\u0347", true], 
      [":", true], [";", true], ["<", true], ["=", true], [">", true],
      ["?", true], ["@", true],
      ["A\u0347", true], ["B\u0347", true], ["C\u0347", true], ["D\u0347", true], ["E\u0347", true], 
      ["F\u0347", true], ["G\u0347", true], ["H\u0347", true], ["I\u0347", true], ["J\u0347", true], 
      ["K\u0347", true], ["L\u0347", true], ["M\u0347", true], ["N\u0347", true], ["O\u0347", true], 
      ["P\u0347", true], ["Q\u0347", true], ["R\u0347", true], ["S\u0347", true], ["T\u0347", true], 
      ["U\u0347", true], ["V\u0347", true], ["W\u0347", true], ["X\u0347", true], ["Y\u0347", true], 
      ["Z\u0347", true], 
      ["[", true], ["\\", true], ["]", true], ["^", true], ["_", true], ["`", true],
      ["a\u0347", true], ["b\u0347", true], ["c\u0347", true], ["d\u0347", true], ["e\u0347", true], 
      ["f\u0347", true], ["g\u0347", true], ["h\u0347", true], ["i\u0347", true], ["j\u0347", true], 
      ["k\u0347", true], ["l\u0347", true], ["m\u0347", true], ["n\u0347", true], ["o\u0347", true], 
      ["p\u0347", true], ["q\u0347", true], ["r\u0347", true], ["s\u0347", true], ["t\u0347", true], 
      ["u\u0347", true], ["v\u0347", true], ["w\u0347", true], ["x\u0347", true], ["y\u0347", true], 
      ["z\u0347", true]
    ],
    
    "miscmap": {}
  }


]

'''







def clamp(value, smallest, largest):
  return max(smallest, min(value, largest))


  

# Font Map Config File Handle
#   Opens JSON config file and loads into variables
#   Allows manipulation of config data through variables
#   Writes those variables to the config file as JSON data
class FontMapConfig():
  
  def __init__(self, filename, extension='.json'):
    self.valid      = True
    self.directory  = wx.StandardPaths.Get().GetUserDataDir()
    self.path       = os.path.join(self.directory, filename + extension)
    
    # Get File Handle
    try:
      if not os.path.exists(self.directory):
        os.mkdir(self.directory)
      if not os.path.isfile(self.path):
        f = open(self.path, 'w')      # Create file if not exist
        f.close()
      self.file = open(self.path, 'r+') # Read/Write, No truncate
    except IOError:
      self.valid = False # When invalid, default config is used and saving is disabled
      
    # Create and variables to fill with JSON data
    self.fontMapNames     = []  # Arbitrary String
    self.fontMapPaddings  = []  # Padding Integer
    self.fontMapOffsets   = []  # Offset Integer
    self.fontMapASCII     = []  # Typeable ASCII Range (32 to 126 incl)
    self.fontMapMisc      = []  # Array of Hashmaps of characters/strings and strings to replace them with
    
    # Get JSON string (either from file or default)
    jsonString = ''
    if self.valid:
      jsonString = self.file.read()
      if not jsonString:
        jsonString = config_default
    else:
      jsonString = config_default
    
    try:
      jsonData = json.loads(jsonString)
      if not hasattr(jsonData, '__iter__'):   # Check that data is array
        self.valid = False
        jsonData = json.loads(config_default) # config_default is guaranteed valid
        print('[WARNING] Config is invalid format: Using Default in Read-only mode')
    except ValueError:
      self.valid = False
      jsonData = json.loads(config_default)
      print('[ERROR] Failed to load JSON data from config file. Using default in Read-only mode')
  
    # Parse JSON data into variables
    for map in range(0, len(jsonData)):
      # Buffer values so we only add font map if everything is valid
      try:
        name            = jsonData[map]['name']
      except KeyError:
        name            = 'UNNAMED'
        
      try:
        padding         = int(jsonData[map]['padding'])
      except ValueError:
        padding         = 0
        
      try:
        offset          = int(jsonData[map]['asciimapoffs']) 
      except ValueError:
        offset          = 32
      offset = clamp(offset, 32, 127) # Offsets out of typeable ASCII range break the logic
        
      asciiBoolMap  = []  # TYPEABLE ASCII map (32 to 126 incl)
                          # Each element is a character and its toggle state: ['C', True]

      # Fill asciiBoolMap with entire typeable ASCII table (defaulting where needed)
      # Account for starting offset and possible early map end
      for character in range(32, offset): # Offset <=32 will do nothing
        asciiBoolMap.append([chr(character), True])
      
      mapEnd = offset + len(jsonData[map]['asciimap'])
      for character in range(offset, min(mapEnd, 127)):
        asciiBoolMap.append(jsonData[map]['asciimap'][character-offset])
      
      # If map is not enough to cover typeable range entirely, add remaining characters
      if mapEnd < 126:
        for character in range(mapEnd, 127):
          asciiBoolMap.append([chr(character), True])
        
      # Check asciiMap is valid size
      if len(asciiBoolMap) == 127 - 32:
        # Add Font Map
        self.fontMapNames.append(name)
        self.fontMapPaddings.append(padding)
        self.fontMapOffsets.append(offset)
        self.fontMapASCII.append(asciiBoolMap)
        self.fontMapMisc.append(jsonData[map]['miscmap'])
          
          
    self.fontCount = len(self.fontMapNames)
    
    
  def __del__(self):
    if self.file and self.valid:
      self.file.close()
      
      
  def save_file(self):
    if self.file and self.valid:
      jsonBuffer = []
      
      # Parse variables into JSON data
      for map in range(0, len(self.fontMapNames)):
        mapBuffer = {}
        mapBuffer['name']         = self.fontMapNames[map]
        mapBuffer['padding']      = str(self.fontMapPaddings[map]) # Ints must be string
        offs = self.fontMapOffsets[map]
        mapBuffer['asciimapoffs'] = str(offs)
        # To keep asciimapoffs value valid, trim the starting-offseted ASCII from asciimap
        mapBuffer['asciimap']     = self.fontMapASCII[map][max(offs-32, 0):]
        mapBuffer['miscmap']      = self.fontMapMisc[map]
        jsonBuffer.append(mapBuffer)
      
      # Empty file and write new contents
      self.file.seek(0)
      self.file.truncate()
      self.file.write(json.dumps(jsonBuffer, indent=2, separators=(',', ': ')))
      
      
  def debug_print(self):
    for map in range(0, len(self.fontMapNames)):
      print('Name: ' + self.fontMapNames[map])
      print('Indx: ' + str(map))
      print('Padd: ' + str(self.fontMapPaddings[map]))
      print('Offs: ' + str(self.fontMapOffsets[map]))
      print('Font: ')
      print(self.fontMapASCII[map])
      print('Misc: ')
      print(self.fontMapMisc[map])
      print('\n')