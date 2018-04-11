#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#########################################################################
## This Source Code Form is subject to the terms of the Mozilla Public  #
## License, v. 2.0. If a copy of the MPL was not distributed with this  #
## file, You can obtain one at http://mozilla.org/MPL/2.0/.             #
#########################################################################
## fontfix.py                                                           #
##                                                                      #
## Temporary tool for fixing the old font map list into the new config  #
##                                                                      #
#########################################################################


import random
import wx


# Convert Surrogate Form to UTF-16 escape sequence (Multi-escape to Single Escape)
def as_surrogates(str):
  return str.encode('utf-16', 'surrogatepass').decode('utf-16')
  

# MODIFIED Character sets convering a-z, A-Z and 0-9
fontMapList = [


  # 0 - Cursive Characters
  [
  u'\\uD835\\uDCB6', u'\\uD835\\uDCB7', u'\\uD835\\uDCB8', u'\\uD835\\uDCB9', u'\\uD835\\uDC52',
  u'\\uD835\\uDCBB', u'\\uD835\\uDC54', u'\\uD835\\uDCBD', u'\\uD835\\uDCBE', u'\\uD835\\uDCBF',
  u'\\uD835\\uDCC0', u'\\uD835\\uDCC1', u'\\uD835\\uDCC2', u'\\uD835\\uDCC3', u'\\uD835\\uDC5C',
  u'\\uD835\\uDCC5', u'\\uD835\\uDCC6', u'\\uD835\\uDCC7', u'\\uD835\\uDCC8', u'\\uD835\\uDCC9',
  u'\\uD835\\uDCCA', u'\\uD835\\uDCCB', u'\\uD835\\uDCCC', u'\\uD835\\uDCCD', u'\\uD835\\uDCCE',
  u'\\uD835\\uDCCF', u'\\uD835\\uDC9C', u'\\uD835\\uDC35', u'\\uD835\\uDC9E', u'\\uD835\\uDC9F',
  u'\\uD835\\uDC38', u'\\uD835\\uDC39', u'\\uD835\\uDCA2', u'\\uD835\\uDC3B', u'\\uD835\\uDC3C',
  u'\\uD835\\uDCA5', u'\\uD835\\uDCA6', u'\\uD835\\uDC3F', u'\\uD835\\uDC40', u'\\uD835\\uDCA9',
  u'\\uD835\\uDCAA', u'\\uD835\\uDCAB', u'\\uD835\\uDCAC', u'\\uD835\\uDC45', u'\\uD835\\uDCAE',
  u'\\uD835\\uDCAF', u'\\uD835\\uDCB0', u'\\uD835\\uDCB1', u'\\uD835\\uDCB2', u'\\uD835\\uDCB3',
  u'\\uD835\\uDCB4', u'\\uD835\\uDCB5', u'\\uD835\\uDFE2', u'\\uD835\\uDFE3', u'\\uD835\\uDFE4',
  u'\\uD835\\uDFE5', u'\\uD835\\uDFE6', u'\\uD835\\uDFE7', u'\\uD835\\uDFE8', u'\\uD835\\uDFE9',
  u'\\uD835\\uDFEA', u'\\uD835\\uDFEB'
  ],

  # 1 - Bold Cursive Characters
  [
  u'\\uD835\\uDCEA', u'\\uD835\\uDCEB', u'\\uD835\\uDCEC', u'\\uD835\\uDCED', u'\\uD835\\uDCEE',
  u'\\uD835\\uDCEF', u'\\uD835\\uDCF0', u'\\uD835\\uDCF1', u'\\uD835\\uDCF2', u'\\uD835\\uDCF3',
  u'\\uD835\\uDCF4', u'\\uD835\\uDCF5', u'\\uD835\\uDCF6', u'\\uD835\\uDCF7', u'\\uD835\\uDCF8',
  u'\\uD835\\uDCF9', u'\\uD835\\uDCFA', u'\\uD835\\uDCFB', u'\\uD835\\uDCFC', u'\\uD835\\uDCFD',
  u'\\uD835\\uDCFE', u'\\uD835\\uDCFF', u'\\uD835\\uDD00', u'\\uD835\\uDD01', u'\\uD835\\uDD02',
  u'\\uD835\\uDD03', u'\\uD835\\uDCD0', u'\\uD835\\uDCD1', u'\\uD835\\uDCD2', u'\\uD835\\uDCD3',
  u'\\uD835\\uDCD4', u'\\uD835\\uDCD5', u'\\uD835\\uDCD6', u'\\uD835\\uDCD7', u'\\uD835\\uDCD8',
  u'\\uD835\\uDCD9', u'\\uD835\\uDCDA', u'\\uD835\\uDCDB', u'\\uD835\\uDCDC', u'\\uD835\\uDCDD',
  u'\\uD835\\uDCDE', u'\\uD835\\uDCDF', u'\\uD835\\uDCE0', u'\\uD835\\uDCE1', u'\\uD835\\uDCE2',
  u'\\uD835\\uDCE3', u'\\uD835\\uDCE4', u'\\uD835\\uDCE5', u'\\uD835\\uDCE6', u'\\uD835\\uDCE7',
  u'\\uD835\\uDCE8', u'\\uD835\\uDCE9', u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9'
  ],

  # 2 - Hollow Characters
  [
  u'\\uD835\\uDD52', u'\\uD835\\uDD53', u'\\uD835\\uDD54', u'\\uD835\\uDD55', u'\\uD835\\uDD56',
  u'\\uD835\\uDD57', u'\\uD835\\uDD58', u'\\uD835\\uDD59', u'\\uD835\\uDD5A', u'\\uD835\\uDD5B',
  u'\\uD835\\uDD5C', u'\\uD835\\uDD5D', u'\\uD835\\uDD5E', u'\\uD835\\uDD5F', u'\\uD835\\uDD60',
  u'\\uD835\\uDD61', u'\\uD835\\uDD62', u'\\uD835\\uDD63', u'\\uD835\\uDD64', u'\\uD835\\uDD65',
  u'\\uD835\\uDD66', u'\\uD835\\uDD67', u'\\uD835\\uDD68', u'\\uD835\\uDD69', u'\\uD835\\uDD6A',
  u'\\uD835\\uDD6B', u'\\uD835\\uDD38', u'\\uD835\\uDD39', u'\\u2102', u'\\uD835\\uDD3B',
  u'\\uD835\\uDD3C', u'\\uD835\\uDD3D', u'\\uD835\\uDD3E', u'\\u210D', u'\\uD835\\uDD40',
  u'\\uD835\\uDD41', u'\\uD835\\uDD42', u'\\uD835\\uDD43', u'\\uD835\\uDD44', u'\\u2115',
  u'\\uD835\\uDD46', u'\\u2119', u'\\u211A', u'\\u211D', u'\\uD835\\uDD4A', u'\\uD835\\uDD4B',
  u'\\uD835\\uDD4C', u'\\uD835\\uDD4D', u'\\uD835\\uDD4E', u'\\uD835\\uDD4F', u'\\uD835\\uDD50',
  u'\\u2124', u'\\uD835\\uDFD8', u'\\uD835\\uDFD9', u'\\uD835\\uDFDA', u'\\uD835\\uDFDB',
  u'\\uD835\\uDFDC', u'\\uD835\\uDFDD', u'\\uD835\\uDFDE', u'\\uD835\\uDFDF', u'\\uD835\\uDFE0',
  u'\\uD835\\uDFE1'
  ],
  
  # 3 - Gothic Characters
  [
  u'\\uD835\\uDD1E', u'\\uD835\\uDD1F', u'\\uD835\\uDD20', u'\\uD835\\uDD21', u'\\uD835\\uDD22',
  u'\\uD835\\uDD23', u'\\uD835\\uDD24', u'\\uD835\\uDD25', u'\\uD835\\uDD26', u'\\uD835\\uDD27',
  u'\\uD835\\uDD28', u'\\uD835\\uDD29', u'\\uD835\\uDD2A', u'\\uD835\\uDD2B', u'\\uD835\\uDD2C',
  u'\\uD835\\uDD2D', u'\\uD835\\uDD2E', u'\\uD835\\uDD2F', u'\\uD835\\uDD30', u'\\uD835\\uDD31',
  u'\\uD835\\uDD32', u'\\uD835\\uDD33', u'\\uD835\\uDD34', u'\\uD835\\uDD35', u'\\uD835\\uDD36',
  u'\\uD835\\uDD37', u'\\uD835\\uDD04', u'\\uD835\\uDD05', u'\\u212D', u'\\uD835\\uDD07',
  u'\\uD835\\uDD08', u'\\uD835\\uDD09', u'\\uD835\\uDD0A', u'\\u210C', u'\\u2111',
  u'\\uD835\\uDD0D', u'\\uD835\\uDD0E', u'\\uD835\\uDD0F', u'\\uD835\\uDD10', u'\\uD835\\uDD11',
  u'\\uD835\\uDD12', u'\\uD835\\uDD13', u'\\uD835\\uDD14', u'\\u211C', u'\\uD835\\uDD16',
  u'\\uD835\\uDD17', u'\\uD835\\uDD18', u'\\uD835\\uDD19', u'\\uD835\\uDD1A', u'\\uD835\\uDD1B',
  u'\\uD835\\uDD1C', u'\\u2128',
  u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9'
  ],

  # 4 - Bold Gothic Characters
  [
  u'\\uD835\\uDD86', u'\\uD835\\uDD87', u'\\uD835\\uDD88', u'\\uD835\\uDD89', u'\\uD835\\uDD8A',
  u'\\uD835\\uDD8B', u'\\uD835\\uDD8C', u'\\uD835\\uDD8D', u'\\uD835\\uDD8E', u'\\uD835\\uDD8F',
  u'\\uD835\\uDD90', u'\\uD835\\uDD91', u'\\uD835\\uDD92', u'\\uD835\\uDD93', u'\\uD835\\uDD94',
  u'\\uD835\\uDD95', u'\\uD835\\uDD96', u'\\uD835\\uDD97', u'\\uD835\\uDD98', u'\\uD835\\uDD99',
  u'\\uD835\\uDD9A', u'\\uD835\\uDD9B', u'\\uD835\\uDD9C', u'\\uD835\\uDD9D', u'\\uD835\\uDD9E',
  u'\\uD835\\uDD9F', u'\\uD835\\uDD6C', u'\\uD835\\uDD6D', u'\\uD835\\uDD6E', u'\\uD835\\uDD6F',
  u'\\uD835\\uDD70', u'\\uD835\\uDD71', u'\\uD835\\uDD72', u'\\uD835\\uDD73', u'\\uD835\\uDD74',
  u'\\uD835\\uDD75', u'\\uD835\\uDD76', u'\\uD835\\uDD77', u'\\uD835\\uDD78', u'\\uD835\\uDD79',
  u'\\uD835\\uDD7A', u'\\uD835\\uDD7B', u'\\uD835\\uDD7C', u'\\uD835\\uDD7D', u'\\uD835\\uDD7E',
  u'\\uD835\\uDD7F', u'\\uD835\\uDD80', u'\\uD835\\uDD81', u'\\uD835\\uDD82', u'\\uD835\\uDD83',
  u'\\uD835\\uDD84', u'\\uD835\\uDD85',
  u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9'
  ],

  # 5 - Circled Characters
  [
  u'\\u24D0', u'\\u24D1', u'\\u24D2', u'\\u24D3', u'\\u24D4', u'\\u24D5', u'\\u24D6', u'\\u24D7',
  u'\\u24D8', u'\\u24D9', u'\\u24DA', u'\\u24DB', u'\\u24DC', u'\\u24DD', u'\\u24DE', u'\\u24DF',
  u'\\u24E0', u'\\u24E1', u'\\u24E2', u'\\u24E3', u'\\u24E4', u'\\u24E5', u'\\u24E6', u'\\u24E7',
  u'\\u24E8', u'\\u24E9', u'\\u24B6', u'\\u24B7', u'\\u24B8', u'\\u24B9', u'\\u24BA', u'\\u24BB',
  u'\\u24BC', u'\\u24BD', u'\\u24BE', u'\\u24BF', u'\\u24C0', u'\\u24C1', u'\\u24C2', u'\\u24C3',
  u'\\u24C4', u'\\u24C5', u'\\u24C6', u'\\u24C7', u'\\u24C8', u'\\u24C9', u'\\u24CA', u'\\u24CB',
  u'\\u24CC', u'\\u24CD', u'\\u24CE', u'\\u24CF', u'\\u24EA', u'\\u2460', u'\\u2461', u'\\u2462',
  u'\\u2463', u'\\u2464', u'\\u2465', u'\\u2466', u'\\u2467', u'\\u2468'
  ],
  
  
  # 6 - Negative Circled Characters (Only Uppercase)
  [
  u'\\uD83C\\uDD50', u'\\uD83C\\uDD51', u'\\uD83C\\uDD52', u'\\uD83C\\uDD53', u'\\uD83C\\uDD54',
  u'\\uD83C\\uDD55', u'\\uD83C\\uDD56', u'\\uD83C\\uDD57', u'\\uD83C\\uDD58', u'\\uD83C\\uDD59',
  u'\\uD83C\\uDD5A', u'\\uD83C\\uDD5B', u'\\uD83C\\uDD5C', u'\\uD83C\\uDD5D', u'\\uD83C\\uDD5E',
  u'\\uD83C\\uDD5F', u'\\uD83C\\uDD60', u'\\uD83C\\uDD61', u'\\uD83C\\uDD62', u'\\uD83C\\uDD63',
  u'\\uD83C\\uDD64', u'\\uD83C\\uDD65', u'\\uD83C\\uDD66', u'\\uD83C\\uDD67', u'\\uD83C\\uDD68',
  u'\\uD83C\\uDD69',
  u'\\uD83C\\uDD50', u'\\uD83C\\uDD51', u'\\uD83C\\uDD52', u'\\uD83C\\uDD53', u'\\uD83C\\uDD54',
  u'\\uD83C\\uDD55', u'\\uD83C\\uDD56', u'\\uD83C\\uDD57', u'\\uD83C\\uDD58', u'\\uD83C\\uDD59',
  u'\\uD83C\\uDD5A', u'\\uD83C\\uDD5B', u'\\uD83C\\uDD5C', u'\\uD83C\\uDD5D', u'\\uD83C\\uDD5E',
  u'\\uD83C\\uDD5F', u'\\uD83C\\uDD60', u'\\uD83C\\uDD61', u'\\uD83C\\uDD62', u'\\uD83C\\uDD63',
  u'\\uD83C\\uDD64', u'\\uD83C\\uDD65', u'\\uD83C\\uDD66', u'\\uD83C\\uDD67', u'\\uD83C\\uDD68',
  u'\\uD83C\\uDD69',
  u'\\u24FF', u'\\u2776', u'\\u2777', u'\\u2778', u'\\u2779', u'\\u277A', u'\\u277B',
  u'\\u277C', u'\\u277D', u'\\u277E'
  ],
  
  
  # 7 - Squared Characters (Only Uppercase)
  [
  u'\\uD83C\\uDD30', u'\\uD83C\\uDD31', u'\\uD83C\\uDD32', u'\\uD83C\\uDD33', u'\\uD83C\\uDD34',
  u'\\uD83C\\uDD35', u'\\uD83C\\uDD36', u'\\uD83C\\uDD37', u'\\uD83C\\uDD38', u'\\uD83C\\uDD39',
  u'\\uD83C\\uDD3A', u'\\uD83C\\uDD3B', u'\\uD83C\\uDD3C', u'\\uD83C\\uDD3D', u'\\uD83C\\uDD3E',
  u'\\uD83C\\uDD3F', u'\\uD83C\\uDD40', u'\\uD83C\\uDD41', u'\\uD83C\\uDD42', u'\\uD83C\\uDD43',
  u'\\uD83C\\uDD44', u'\\uD83C\\uDD45', u'\\uD83C\\uDD46', u'\\uD83C\\uDD47', u'\\uD83C\\uDD48',
  u'\\uD83C\\uDD49',
  u'\\uD83C\\uDD30', u'\\uD83C\\uDD31', u'\\uD83C\\uDD32', u'\\uD83C\\uDD33', u'\\uD83C\\uDD34',
  u'\\uD83C\\uDD35', u'\\uD83C\\uDD36', u'\\uD83C\\uDD37', u'\\uD83C\\uDD38', u'\\uD83C\\uDD39',
  u'\\uD83C\\uDD3A', u'\\uD83C\\uDD3B', u'\\uD83C\\uDD3C', u'\\uD83C\\uDD3D', u'\\uD83C\\uDD3E',
  u'\\uD83C\\uDD3F', u'\\uD83C\\uDD40', u'\\uD83C\\uDD41', u'\\uD83C\\uDD42', u'\\uD83C\\uDD43',
  u'\\uD83C\\uDD44', u'\\uD83C\\uDD45', u'\\uD83C\\uDD46', u'\\uD83C\\uDD47', u'\\uD83C\\uDD48',
  u'\\uD83C\\uDD49',
  u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9'
  ],
  
  
  # 8 - Negative Squared Characters (Only Uppercase)
  [
  u'\\uD83C\\uDD70', u'\\uD83C\\uDD71', u'\\uD83C\\uDD72', u'\\uD83C\\uDD73', u'\\uD83C\\uDD74',
  u'\\uD83C\\uDD75', u'\\uD83C\\uDD76', u'\\uD83C\\uDD77', u'\\uD83C\\uDD78', u'\\uD83C\\uDD79',
  u'\\uD83C\\uDD7A', u'\\uD83C\\uDD7B', u'\\uD83C\\uDD7C', u'\\uD83C\\uDD7D', u'\\uD83C\\uDD7E',
  u'\\uD83C\\uDD7F', u'\\uD83C\\uDD80', u'\\uD83C\\uDD81', u'\\uD83C\\uDD82', u'\\uD83C\\uDD83',
  u'\\uD83C\\uDD84', u'\\uD83C\\uDD85', u'\\uD83C\\uDD86', u'\\uD83C\\uDD87', u'\\uD83C\\uDD88',
  u'\\uD83C\\uDD89',
  u'\\uD83C\\uDD70', u'\\uD83C\\uDD71', u'\\uD83C\\uDD72', u'\\uD83C\\uDD73', u'\\uD83C\\uDD74',
  u'\\uD83C\\uDD75', u'\\uD83C\\uDD76', u'\\uD83C\\uDD77', u'\\uD83C\\uDD78', u'\\uD83C\\uDD79',
  u'\\uD83C\\uDD7A', u'\\uD83C\\uDD7B', u'\\uD83C\\uDD7C', u'\\uD83C\\uDD7D', u'\\uD83C\\uDD7E',
  u'\\uD83C\\uDD7F', u'\\uD83C\\uDD80', u'\\uD83C\\uDD81', u'\\uD83C\\uDD82', u'\\uD83C\\uDD83',
  u'\\uD83C\\uDD84', u'\\uD83C\\uDD85', u'\\uD83C\\uDD86', u'\\uD83C\\uDD87', u'\\uD83C\\uDD88',
  u'\\uD83C\\uDD89',
  u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9'
  ],
  
  
  # 9 - EXTRA THICC Characters (Only Uppercase)
  [
  u'\\u5342', u'\\u4E43', u'\\u531A', u'\\u5200', u'\\u4E47', u'\\u4E0B', u'\\u53B6', u'\\u5344',
  u'\\u5DE5', u'\\u4E01', u'\\u957F', u'\\u4E5A', u'\\u4ECE', u'\\uD841\\uDE28', u'\\u53E3', u'\\u5C38',
  u'\\u353F', u'\\u5C3A', u'\\u4E02', u'\\u4E05', u'\\u51F5', u'\\u30EA', u'\\u5C71', u'\\u4E42',
  u'\\u4E2B', u'\\u4E59',
  u'\\u5342', u'\\u4E43', u'\\u531A', u'\\u5200', u'\\u4E47', u'\\u4E0B', u'\\u53B6', u'\\u5344',
  u'\\u5DE5', u'\\u4E01', u'\\u957F', u'\\u4E5A', u'\\u4ECE', u'\\uD841\\uDE28', u'\\u53E3', u'\\u5C38',
  u'\\u353F', u'\\u5C3A', u'\\u4E02', u'\\u4E05', u'\\u51F5', u'\\u30EA', u'\\u5C71', u'\\u4E42',
  u'\\u4E2B', u'\\u4E59',
  u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9'
  ],
  
  
  # 10 - Emoji Characters (Only Uppercase)
  [
  u'\\uD83C\\uDDE6', u'\\uD83C\\uDDE7', u'\\uD83C\\uDDE8', u'\\uD83C\\uDDE9', u'\\uD83C\\uDDEA',
  u'\\uD83C\\uDDEB', u'\\uD83C\\uDDEC', u'\\uD83C\\uDDED', u'\\uD83C\\uDDEE', u'\\uD83C\\uDDEF',
  u'\\uD83C\\uDDF0', u'\\uD83C\\uDDF1', u'\\uD83C\\uDDF2', u'\\uD83C\\uDDF3', u'\\uD83C\\uDDF4',
  u'\\uD83C\\uDDF5', u'\\uD83C\\uDDF6', u'\\uD83C\\uDDF7', u'\\uD83C\\uDDF8', u'\\uD83C\\uDDF9',
  u'\\uD83C\\uDDFA', u'\\uD83C\\uDDFB', u'\\uD83C\\uDDFC', u'\\uD83C\\uDDFD', u'\\uD83C\\uDDFE',
  u'\\uD83C\\uDDFF',
  u'\\uD83C\\uDDE6', u'\\uD83C\\uDDE7', u'\\uD83C\\uDDE8', u'\\uD83C\\uDDE9', u'\\uD83C\\uDDEA',
  u'\\uD83C\\uDDEB', u'\\uD83C\\uDDEC', u'\\uD83C\\uDDED', u'\\uD83C\\uDDEE', u'\\uD83C\\uDDEF',
  u'\\uD83C\\uDDF0', u'\\uD83C\\uDDF1', u'\\uD83C\\uDDF2', u'\\uD83C\\uDDF3', u'\\uD83C\\uDDF4',
  u'\\uD83C\\uDDF5', u'\\uD83C\\uDDF6', u'\\uD83C\\uDDF7', u'\\uD83C\\uDDF8', u'\\uD83C\\uDDF9',
  u'\\uD83C\\uDDFA', u'\\uD83C\\uDDFB', u'\\uD83C\\uDDFC', u'\\uD83C\\uDDFD', u'\\uD83C\\uDDFE',
  u'\\uD83C\\uDDFF',
  u'0\\u20E3', u'1\\u20E3', u'2\\u20E3', u'3\\u20E3', u'4\\u20E3', u'5\\u20E3', u'6\\u20E3',
  u'7\\u20E3', u'8\\u20E3', u'9\\u20E3'
  ],
  
  
  # 11 - Fullwidth Characters
  [
  u'\\uFF41', u'\\uFF42', u'\\uFF43', u'\\uFF44', u'\\uFF45', u'\\uFF46', u'\\uFF47', u'\\uFF48',
  u'\\uFF49', u'\\uFF4A', u'\\uFF4B', u'\\uFF4C', u'\\uFF4D', u'\\uFF4E', u'\\uFF4F', u'\\uFF50',
  u'\\uFF51', u'\\uFF52', u'\\uFF53', u'\\uFF54', u'\\uFF55', u'\\uFF56', u'\\uFF57', u'\\uFF58',
  u'\\uFF59', u'\\uFF5A', u'\\uFF21', u'\\uFF22', u'\\uFF23', u'\\uFF24', u'\\uFF25', u'\\uFF26',
  u'\\uFF27', u'\\uFF28', u'\\uFF29', u'\\uFF2A', u'\\uFF2B', u'\\uFF2C', u'\\uFF2D', u'\\uFF2E',
  u'\\uFF2F', u'\\uFF30', u'\\uFF31', u'\\uFF32', u'\\uFF33', u'\\uFF34', u'\\uFF35', u'\\uFF36',
  u'\\uFF37', u'\\uFF38', u'\\uFF39', u'\\uFF3A', u'\\uFF10', u'\\uFF11', u'\\uFF12', u'\\uFF13',
  u'\\uFF14', u'\\uFF15', u'\\uFF16', u'\\uFF17', u'\\uFF18', u'\\uFF19'
  ],
  
  
  # 12 - Parenthesized Characters
  [
  u'\\u249C', u'\\u249D', u'\\u249E', u'\\u249F', u'\\u24A0', u'\\u24A1', u'\\u24A2', u'\\u24A3',
  u'\\u24A4', u'\\u24A5', u'\\u24A6', u'\\u24A7', u'\\u24A8', u'\\u24A9', u'\\u24AA', u'\\u24AB',
  u'\\u24AC', u'\\u24AD', u'\\u24AE', u'\\u24AF', u'\\u24B0', u'\\u24B1', u'\\u24B2', u'\\u24B3',
  u'\\u24B4', u'\\u24B5', u'\\u249C', u'\\u249D', u'\\u249E', u'\\u249F', u'\\u24A0', u'\\u24A1',
  u'\\u24A2', u'\\u24A3', u'\\u24A4', u'\\u24A5', u'\\u24A6', u'\\u24A7', u'\\u24A8', u'\\u24A9',
  u'\\u24AA', u'\\u24AB', u'\\u24AC', u'\\u24AD', u'\\u24AE', u'\\u24AF', u'\\u24B0', u'\\u24B1',
  u'\\u24B2', u'\\u24B3', u'\\u24B4', u'\\u24B5',
  u'0', u'\\u2474', u'\\u2475', u'\\u2476', u'\\u2477', u'\\u2478', u'\\u2479', u'\\u247A', u'\\u247B', u'\\u247C'
  ],
  
  
  # 13 - 'Curvy' Characters
  [
  u'\\u03B1', u'\\u0432', u'\\u00A2', u'\\u2202', u'\\u0454', u'\\u0192', u'\\uFEED', u'\\u043D',
  u'\\u03B9', u'\\u05E0', u'\\u043A', u'\\u2113', u'\\u043C', u'\\u03B7', u'\\u03C3', u'\\u03C1',
  u'\\u06F9', u'\\u044F', u'\\u0455', u'\\u0442', u'\\u03C5', u'\\u03BD', u'\\u03C9', u'\\u03C7',
  u'\\u0443', u'\\u0579', u'\\u03B1', u'\\u0432', u'\\u00A2', u'\\u2202', u'\\u0454', u'\\u0192',
  u'\\uFEED', u'\\u043D', u'\\u03B9', u'\\u05E0', u'\\u043A', u'\\u2113', u'\\u043C', u'\\u03B7',
  u'\\u03C3', u'\\u03C1', u'\\u06F9', u'\\u044F', u'\\u0455', u'\\u0442', u'\\u03C5', u'\\u03BD',
  u'\\u03C9', u'\\u03C7', u'\\u0443', u'\\u0579', u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9'
  ],
  
  
  # 14 - Faux Cyrllic Characters
  [
  u'\\u0430', u'\\u044A', u'\\u0441', u'\\u2181', u'\\u044D', u'f', u'\\u0411', u'\\u0402',
  u'\\u0456', u'\\u0458', u'\\u043A', u'l', u'\\u043C', u'\\u0438', u'\\u043E', u'\\u0440',
  u'q', u'\\u0453', u'\\u0455', u'\\u0442', u'\\u0446', u'v', u'\\u0448', u'\\u0445',
  u'\\u040E', u'z', u'\\u0414', u'\\u0411', u'\\u0480', u'\\u2181', u'\\u0404', u'F',
  u'\\u0411', u'\\u041D', u'\\u0406', u'\\u0408', u'\\u040C', u'L', u'\\u041C', u'\\u0418',
  u'\\u0424', u'\\u0420', u'Q', u'\\u042F', u'\\u0405', u'\\u0413', u'\\u0426', u'V',
  u'\\u0429', u'\\u0416', u'\\u0427', u'Z',
  u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9'
  ],
  
  
  # 15 - Faux Ethiopic Characters
  [
  u'\\u120D', u'\\u130C', u'\\u122D', u'\\u12D5', u'\\u127F', u'\\u127B', u'\\u1297', u'\\u12D8',
  u'\\u130E', u'\\u130B', u'\\u1315', u'\\u1228', u'\\u1320', u'\\u12AD', u'\\u12D0', u'\\u12E8',
  u'\\u12D2', u'\\u12EA', u'\\u1290', u'\\u1355', u'\\u1201', u'\\u1200', u'\\u1220', u'\\u1238',
  u'\\u1203', u'\\u130A', u'\\u120D', u'\\u130C', u'\\u122D', u'\\u12D5', u'\\u127F', u'\\u127B',
  u'\\u1297', u'\\u12D8', u'\\u130E', u'\\u130B', u'\\u1315', u'\\u1228', u'\\u1320', u'\\u12AD',
  u'\\u12D0', u'\\u12E8', u'\\u12D2', u'\\u12EA', u'\\u1290', u'\\u1355', u'\\u1201', u'\\u1200',
  u'\\u1220', u'\\u1238', u'\\u1203', u'\\u130A',
  u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9'
  ],
  
  
  # 16 - Superscript Characters
  [
  u'\\u1D43', u'\\u1D47', u'\\u1D9C', u'\\u1D48', u'\\u1D49', u'\\u1DA0', u'\\u1D4D', u'\\u02B0',
  u'\\u2071', u'\\u02B2', u'\\u1D4F', u'\\u02E1', u'\\u1D50', u'\\u207F', u'\\u1D52', u'\\u1D56',
  u'q', u'\\u02B3', u'\\u02E2', u'\\u1D57', u'\\u1D58', u'\\u1D5B', u'\\u02B7', u'\\u02E3',
  u'\\u02B8', u'\\u1DBB', u'\\u1D2C', u'\\u1D2E', u'\\u1D9C', u'\\u1D30', u'\\u1D31', u'\\u1DA0',
  u'\\u1D33', u'\\u1D34', u'\\u1D35', u'\\u1D36', u'\\u1D37', u'\\u1D38', u'\\u1D39', u'\\u1D3A',
  u'\\u1D3C', u'\\u1D3E', u'Q', u'\\u1D3F', u'\\u02E2', u'\\u1D40', u'\\u1D41', u'\\u2C7D',
  u'\\u1D42', u'\\u02E3', u'\\u02B8', u'\\u1DBB', u'\\u2070', u'\\u00B9', u'\\u00B2', u'\\u00B3',
  u'\\u2074', u'\\u2075', u'\\u2076', u'\\u2077', u'\\u2078', u'\\u2079'
  ],
  
  
  # 17 - Inverted Characters
  [
  u'\\u0250', u'q', u'\\u0254', u'p', u'\\u01DD', u'\\u025F', u'\\u0183', u'\\u0265',
  u'\\u0131', u'\\u027E', u'\\u029E', u'\\u05DF', u'\\u026F', u'u', u'o', u'd',
  u'b', u'\\u0279', u's', u'\\u0287', u'n', u'\\u028C', u'\\u028D', u'x',
  u'\\u028E', u'z', u'\\u0250', u'q', u'\\u0254', u'p', u'\\u01DD', u'\\u025F',
  u'\\u0183', u'\\u0265', u'\\u0131', u'\\u027E', u'\\u029E', u'\\u05DF', u'\\u026F', u'u',
  u'o', u'd', u'b', u'\\u0279', u's', u'\\u0287', u'n', u'\\uD800\\uDF21',
  u'\\u028D', u'x', u'\\u028E', u'z',
  u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9'
  ],
  
  
  # 18 - Dotted Characters
  [
  u'\\u00E4', u'\\u1E05', u'\\u010B', u'\\u1E0B', u'\\u00EB', u'\\u1E1F', u'\\u0121', u'\\u1E27',
  u'\\u00EF', u'j', u'\\u1E33', u'\\u1E37', u'\\u1E41', u'\\u1E45', u'\\u00F6', u'\\u1E57',
  u'q', u'\\u1E5B', u'\\u1E61', u'\\u1E97', u'\\u00FC', u'\\u1E7F', u'\\u1E85', u'\\u1E8D',
  u'\\u00FF', u'\\u017C', u'\\u00C4', u'\\u1E04', u'\\u010A', u'\\u1E0A', u'\\u0401', u'\\u1E1E',
  u'\\u0120', u'\\u1E26', u'\\u0407', u'J', u'\\u1E32', u'\\u1E36', u'\\u1E40', u'\\u1E44',
  u'\\u00D6', u'\\u1E56', u'Q', u'\\u1E5A', u'\\u1E60', u'\\u1E6A', u'\\u00DC', u'\\u1E7E',
  u'\\u1E84', u'\\u1E8C', u'\\u0178', u'\\u017B',
  u'0', u'1', u'2', u'\\u04DF', u'4', u'5', u'6', u'7', u'8', u'9'
  ],
  
  
  # 19 - Stroked Characters
  [
  u'\\u023A', u'\\u0180', u'\\u023C', u'\\u0111', u'\\u0247', u'f', u'\\u01E5', u'\\u0127',
  u'\\u0268', u'\\u0249', u'\\uA741', u'\\u0142', u'm', u'n', u'\\u00F8', u'\\u1D7D',
  u'\\uA757', u'\\u024D', u's', u'\\u0167', u'\\u1D7E', u'v', u'w', u'x',
  u'\\u024F', u'\\u01B6', u'\\u023A', u'\\u0243', u'\\u023B', u'\\u0110', u'\\u0246', u'F',
  u'\\u01E4', u'\\u0126', u'\\u0197', u'\\u0248', u'\\uA740', u'\\u0141', u'M', u'N',
  u'\\u00D8', u'\\u2C63', u'\\uA756', u'\\u024C', u'S', u'\\u0166', u'\\u1D7E', u'V',
  u'W', u'X', u'\\u024E', u'\\u01B5',
  u'0', u'1', u'\\u01BB', u'3', u'4', u'5', u'6', u'7', u'8', u'9'
  ],
  
  
  # 20 - Underlined Characters
  [
  u'a\\u035F', u'b\\u035F', u'c\\u035F', u'd\\u035F', u'e\\u035F', u'f\\u035F', u'g\\u035F', u'h\\u035F',
  u'i\\u035F', u'j\\u035F', u'k\\u035F', u'l\\u035F', u'm\\u035F', u'n\\u035F', u'o\\u035F', u'p\\u035F',
  u'q\\u035F', u'r\\u035F', u's\\u035F', u't\\u035F', u'u\\u035F', u'v\\u035F', u'w\\u035F', u'x\\u035F',
  u'y\\u035F', u'z\\u035F',
  u'A\\u035F', u'B\\u035F', u'C\\u035F', u'D\\u035F', u'E\\u035F', u'F\\u035F', u'G\\u035F', u'H\\u035F',
  u'I\\u035F', u'J\\u035F', u'K\\u035F', u'L\\u035F', u'M\\u035F', u'N\\u035F', u'O\\u035F', u'P\\u035F',
  u'Q\\u035F', u'R\\u035F', u'S\\u035F', u'T\\u035F', u'U\\u035F', u'V\\u035F', u'W\\u035F', u'X\\u035F',
  u'Y\\u035F', u'Z\\u035F',
  u'0\\u035F', u'1\\u035F', u'2\\u035F', u'3\\u035F', u'4\\u035F', u'5\\u035F', u'6\\u035F', u'7\\u035F', u'8\\u035F', u'9\\u035F'
  ],
  
  
  # 21 - Double Underlined Characters
  [
  u'a\\u0347', u'b\\u0347', u'c\\u0347', u'd\\u0347', u'e\\u0347', u'f\\u0347', u'g\\u0347', u'h\\u0347',
  u'i\\u0347', u'j\\u0347', u'k\\u0347', u'l\\u0347', u'm\\u0347', u'n\\u0347', u'o\\u0347', u'p\\u0347',
  u'q\\u0347', u'r\\u0347', u's\\u0347', u't\\u0347', u'u\\u0347', u'v\\u0347', u'w\\u0347', u'x\\u0347',
  u'y\\u0347', u'z\\u0347',
  u'A\\u0347', u'B\\u0347', u'C\\u0347', u'D\\u0347', u'E\\u0347', u'F\\u0347', u'G\\u0347', u'H\\u0347',
  u'I\\u0347', u'J\\u0347', u'K\\u0347', u'L\\u0347', u'M\\u0347', u'N\\u0347', u'O\\u0347', u'P\\u0347',
  u'Q\\u0347', u'R\\u0347', u'S\\u0347', u'T\\u0347', u'U\\u0347', u'V\\u0347', u'W\\u0347', u'X\\u0347',
  u'Y\\u0347', u'Z\\u0347',
  u'0\\u0347', u'1\\u0347', u'2\\u0347', u'3\\u0347', u'4\\u0347', u'5\\u0347', u'6\\u0347', u'7\\u0347', u'8\\u0347', u'9\\u0347'
  ]

  
] 




# Config contains a list of all the font maps and their default settings
# All fontmaps have the same default settings except for their asciimap arrays
# with the exception of the Emoji font which has a default padding of 1 (emoji letters make emoji flags)
#
# 
#  {
#    "name": "Cursive",     # The font's display name
#    "padding": "0",        # Spaces put before/between each character
#    "asciimapoffs": "48"   # Starting index offset (0 based) for the ASCII map
#                           # The end index will be either 127 or the last index in the asciimap (lowest)
#
#    "asciimap": [          # An array of unicode characters mapped to ASCII indexes (1:1 mapping)
#        ["A", true],       # Contains an array with a unicode character and a bool value (for toggling chars)
#        ...
#     ],                  
#
#    "miscmap": {},         # An object/dictionary/hashmap of non-ASCII characters and their font mapping.
#                           # This is always empty by default, but allows for users to customise the mappings
#                           # asciimap array will always be searched first so this doesn't override it.
#  },
config_default = r'''

"fontmaps": [


  {
    "name": "Cursive",
    "padding": "0",
    "asciimapoffs": "48"
    "asciimap": [
      "\uD835\uDFE2", "\uD835\uDFE3", "\uD835\uDFE4", "\uD835\uDFE5", "\uD835\uDFE6",
      "\uD835\uDFE7", "\uD835\uDFE8", "\uD835\uDFE9", "\uD835\uDFEA", "\uD835\uDFEB",
      ":", ";", "<", "=", ">",
      "?", "@",
      "\uD835\uDC9C", "\uD835\uDC35", "\uD835\uDC9E", "\uD835\uDC9F", "\uD835\uDC38",
      "\uD835\uDC39", "\uD835\uDCA2", "\uD835\uDC3B", "\uD835\uDC3C", "\uD835\uDCA5",
      "\uD835\uDCA6", "\uD835\uDC3F", "\uD835\uDC40", "\uD835\uDCA9", "\uD835\uDCAA",
      "\uD835\uDCAB", "\uD835\uDCAC", "\uD835\uDC45", "\uD835\uDCAE", "\uD835\uDCAF",
      "\uD835\uDCB0", "\uD835\uDCB1", "\uD835\uDCB2", "\uD835\uDCB3", "\uD835\uDCB4",
      "\uD835\uDCB5",
      "[", "\\", "]", "^", "_", "`",
      "\uD835\uDCB6", "\uD835\uDCB7", "\uD835\uDCB8", "\uD835\uDCB9", "\uD835\uDC52",
      "\uD835\uDCBB", "\uD835\uDC54", "\uD835\uDCBD", "\uD835\uDCBE", "\uD835\uDCBF",
      "\uD835\uDCC0", "\uD835\uDCC1", "\uD835\uDCC2", "\uD835\uDCC3", "\uD835\uDC5C",
      "\uD835\uDCC5", "\uD835\uDCC6", "\uD835\uDCC7", "\uD835\uDCC8", "\uD835\uDCC9",
      "\uD835\uDCCA", "\uD835\uDCCB", "\uD835\uDCCC", "\uD835\uDCCD", "\uD835\uDCCE",
      "\uD835\uDCCF"
    ],
    
    "miscmap": {}
  },
  
  
  {
    "name": "Bold Cursive",
    "padding": "0",
    "asciimapoffs": "48"
    "asciimap": [
      "0", "1", "2", "3", "4",
      "5", "6", "7", "8", "9",
      ":", ";", "<", "=", ">",
      "?", "@",
      "\uD835\uDCD0", "\uD835\uDCD1", "\uD835\uDCD2", "\uD835\uDCD3", "\uD835\uDCD4",
      "\uD835\uDCD5", "\uD835\uDCD6", "\uD835\uDCD7", "\uD835\uDCD8", "\uD835\uDCD9",
      "\uD835\uDCDA", "\uD835\uDCDB", "\uD835\uDCDC", "\uD835\uDCDD", "\uD835\uDCDE",
      "\uD835\uDCDF", "\uD835\uDCE0", "\uD835\uDCE1", "\uD835\uDCE2", "\uD835\uDCE3",
      "\uD835\uDCE4", "\uD835\uDCE5", "\uD835\uDCE6", "\uD835\uDCE7", "\uD835\uDCE8",
      "\uD835\uDCE9",
      "[", "\\", "]", "^", "_", "`",
      "\uD835\uDCEA", "\uD835\uDCEB", "\uD835\uDCEC", "\uD835\uDCED", "\uD835\uDCEE",
      "\uD835\uDCEF", "\uD835\uDCF0", "\uD835\uDCF1", "\uD835\uDCF2", "\uD835\uDCF3",
      "\uD835\uDCF4", "\uD835\uDCF5", "\uD835\uDCF6", "\uD835\uDCF7", "\uD835\uDCF8",
      "\uD835\uDCF9", "\uD835\uDCFA", "\uD835\uDCFB", "\uD835\uDCFC", "\uD835\uDCFD",
      "\uD835\uDCFE", "\uD835\uDCFF", "\uD835\uDD00", "\uD835\uDD01", "\uD835\uDD02",
      "\uD835\uDD03"
    ],

    "miscmap": {}
  },


  {
    "name": "Hollow",
    "padding": "0",
    "asciimapoffs": "48"
    "asciimap": [
      "\uD835\uDFD8", "\uD835\uDFD9", "\uD835\uDFDA", "\uD835\uDFDB", "\uD835\uDFDC",
      "\uD835\uDFDD", "\uD835\uDFDE", "\uD835\uDFDF", "\uD835\uDFE0", "\uD835\uDFE1",
      ":", ";", "<", "=", ">",
      "?", "@",
      "\uD835\uDD38", "\uD835\uDD39", "\u2102", "\uD835\uDD3B", "\uD835\uDD3C",
      "\uD835\uDD3D", "\uD835\uDD3E", "\u210D", "\uD835\uDD40", "\uD835\uDD41",
      "\uD835\uDD42", "\uD835\uDD43", "\uD835\uDD44", "\u2115", "\uD835\uDD46",
      "\u2119", "\u211A", "\u211D", "\uD835\uDD4A", "\uD835\uDD4B",
      "\uD835\uDD4C", "\uD835\uDD4D", "\uD835\uDD4E", "\uD835\uDD4F", "\uD835\uDD50",
      "\u2124",
      "[", "\\", "]", "^", "_", "`",
      "\uD835\uDD52", "\uD835\uDD53", "\uD835\uDD54", "\uD835\uDD55", "\uD835\uDD56",
      "\uD835\uDD57", "\uD835\uDD58", "\uD835\uDD59", "\uD835\uDD5A", "\uD835\uDD5B",
      "\uD835\uDD5C", "\uD835\uDD5D", "\uD835\uDD5E", "\uD835\uDD5F", "\uD835\uDD60",
      "\uD835\uDD61", "\uD835\uDD62", "\uD835\uDD63", "\uD835\uDD64", "\uD835\uDD65",
      "\uD835\uDD66", "\uD835\uDD67", "\uD835\uDD68", "\uD835\uDD69", "\uD835\uDD6A",
      "\uD835\uDD6B"
    ],

    "miscmap": {}
  },


  {
    "name": "Gothic",
    "padding": "0",
    "asciimapoffs": "48"
    "asciimap": [
      "0", "1", "2", "3", "4",
      "5", "6", "7", "8", "9",
      ":", ";", "<", "=", ">",
      "?", "@",
      "\uD835\uDD04", "\uD835\uDD05", "\u212D", "\uD835\uDD07", "\uD835\uDD08",
      "\uD835\uDD09", "\uD835\uDD0A", "\u210C", "\u2111", "\uD835\uDD0D",
      "\uD835\uDD0E", "\uD835\uDD0F", "\uD835\uDD10", "\uD835\uDD11", "\uD835\uDD12",
      "\uD835\uDD13", "\uD835\uDD14", "\u211C", "\uD835\uDD16", "\uD835\uDD17",
      "\uD835\uDD18", "\uD835\uDD19", "\uD835\uDD1A", "\uD835\uDD1B", "\uD835\uDD1C",
      "\u2128",
      "[", "\\", "]", "^", "_", "`",
      "\uD835\uDD1E", "\uD835\uDD1F", "\uD835\uDD20", "\uD835\uDD21", "\uD835\uDD22",
      "\uD835\uDD23", "\uD835\uDD24", "\uD835\uDD25", "\uD835\uDD26", "\uD835\uDD27",
      "\uD835\uDD28", "\uD835\uDD29", "\uD835\uDD2A", "\uD835\uDD2B", "\uD835\uDD2C",
      "\uD835\uDD2D", "\uD835\uDD2E", "\uD835\uDD2F", "\uD835\uDD30", "\uD835\uDD31",
      "\uD835\uDD32", "\uD835\uDD33", "\uD835\uDD34", "\uD835\uDD35", "\uD835\uDD36",
      "\uD835\uDD37"
    ],

    "miscmap": {}
  },


  {
    "name": "Bold Gothic",
    "padding": "0",
    "asciimapoffs": "48"
    "asciimap": [
      "0", "1", "2", "3", "4",
      "5", "6", "7", "8", "9",
      ":", ";", "<", "=", ">",
      "?", "@",
      "\uD835\uDD6C", "\uD835\uDD6D", "\uD835\uDD6E", "\uD835\uDD6F", "\uD835\uDD70",
      "\uD835\uDD71", "\uD835\uDD72", "\uD835\uDD73", "\uD835\uDD74", "\uD835\uDD75",
      "\uD835\uDD76", "\uD835\uDD77", "\uD835\uDD78", "\uD835\uDD79", "\uD835\uDD7A",
      "\uD835\uDD7B", "\uD835\uDD7C", "\uD835\uDD7D", "\uD835\uDD7E", "\uD835\uDD7F",
      "\uD835\uDD80", "\uD835\uDD81", "\uD835\uDD82", "\uD835\uDD83", "\uD835\uDD84",
      "\uD835\uDD85",
      "[", "\\", "]", "^", "_", "`",
      "\uD835\uDD86", "\uD835\uDD87", "\uD835\uDD88", "\uD835\uDD89", "\uD835\uDD8A",
      "\uD835\uDD8B", "\uD835\uDD8C", "\uD835\uDD8D", "\uD835\uDD8E", "\uD835\uDD8F",
      "\uD835\uDD90", "\uD835\uDD91", "\uD835\uDD92", "\uD835\uDD93", "\uD835\uDD94",
      "\uD835\uDD95", "\uD835\uDD96", "\uD835\uDD97", "\uD835\uDD98", "\uD835\uDD99",
      "\uD835\uDD9A", "\uD835\uDD9B", "\uD835\uDD9C", "\uD835\uDD9D", "\uD835\uDD9E",
      "\uD835\uDD9F"
    ],

    "miscmap": {}
  },


  {
    "name": "Circled",
    "padding": "0",
    "asciimapoffs": "48"
    "asciimap": [
      "\u24EA", "\u2460", "\u2461", "\u2462", "\u2463",
      "\u2464", "\u2465", "\u2466", "\u2467", "\u2468",
      ":", ";", "<", "=", ">",
      "?", "@",
      "\u24B6", "\u24B7", "\u24B8", "\u24B9", "\u24BA",
      "\u24BB", "\u24BC", "\u24BD", "\u24BE", "\u24BF",
      "\u24C0", "\u24C1", "\u24C2", "\u24C3", "\u24C4",
      "\u24C5", "\u24C6", "\u24C7", "\u24C8", "\u24C9",
      "\u24CA", "\u24CB", "\u24CC", "\u24CD", "\u24CE",
      "\u24CF",
      "[", "\\", "]", "^", "_", "`",
      "\u24D0", "\u24D1", "\u24D2", "\u24D3", "\u24D4",
      "\u24D5", "\u24D6", "\u24D7", "\u24D8", "\u24D9",
      "\u24DA", "\u24DB", "\u24DC", "\u24DD", "\u24DE",
      "\u24DF", "\u24E0", "\u24E1", "\u24E2", "\u24E3",
      "\u24E4", "\u24E5", "\u24E6", "\u24E7", "\u24E8",
      "\u24E9"
    ],

    "miscmap": {}
  },


  {
    "name": "Negative Circled",
    "padding": "0",
    "asciimapoffs": "48"
    "asciimap": [
      "\u24FF", "\u2776", "\u2777", "\u2778", "\u2779",
      "\u277A", "\u277B", "\u277C", "\u277D", "\u277E",
      ":", ";", "<", "=", ">",
      "?", "@",
      "\uD83C\uDD50", "\uD83C\uDD51", "\uD83C\uDD52", "\uD83C\uDD53", "\uD83C\uDD54",
      "\uD83C\uDD55", "\uD83C\uDD56", "\uD83C\uDD57", "\uD83C\uDD58", "\uD83C\uDD59",
      "\uD83C\uDD5A", "\uD83C\uDD5B", "\uD83C\uDD5C", "\uD83C\uDD5D", "\uD83C\uDD5E",
      "\uD83C\uDD5F", "\uD83C\uDD60", "\uD83C\uDD61", "\uD83C\uDD62", "\uD83C\uDD63",
      "\uD83C\uDD64", "\uD83C\uDD65", "\uD83C\uDD66", "\uD83C\uDD67", "\uD83C\uDD68",
      "\uD83C\uDD69",
      "[", "\\", "]", "^", "_", "`",
      "\uD83C\uDD50", "\uD83C\uDD51", "\uD83C\uDD52", "\uD83C\uDD53", "\uD83C\uDD54",
      "\uD83C\uDD55", "\uD83C\uDD56", "\uD83C\uDD57", "\uD83C\uDD58", "\uD83C\uDD59",
      "\uD83C\uDD5A", "\uD83C\uDD5B", "\uD83C\uDD5C", "\uD83C\uDD5D", "\uD83C\uDD5E",
      "\uD83C\uDD5F", "\uD83C\uDD60", "\uD83C\uDD61", "\uD83C\uDD62", "\uD83C\uDD63",
      "\uD83C\uDD64", "\uD83C\uDD65", "\uD83C\uDD66", "\uD83C\uDD67", "\uD83C\uDD68",
      "\uD83C\uDD69"
    ],

    "miscmap": {}
  },


  {
    "name": "Squared Characters",
    "padding": "0",
    "asciimapoffs": "48"
    "asciimap": [
      "0", "1", "2", "3", "4",
      "5", "6", "7", "8", "9",
      ":", ";", "<", "=", ">",
      "?", "@",
      "\uD83C\uDD30", "\uD83C\uDD31", "\uD83C\uDD32", "\uD83C\uDD33", "\uD83C\uDD34",
      "\uD83C\uDD35", "\uD83C\uDD36", "\uD83C\uDD37", "\uD83C\uDD38", "\uD83C\uDD39",
      "\uD83C\uDD3A", "\uD83C\uDD3B", "\uD83C\uDD3C", "\uD83C\uDD3D", "\uD83C\uDD3E",
      "\uD83C\uDD3F", "\uD83C\uDD40", "\uD83C\uDD41", "\uD83C\uDD42", "\uD83C\uDD43",
      "\uD83C\uDD44", "\uD83C\uDD45", "\uD83C\uDD46", "\uD83C\uDD47", "\uD83C\uDD48",
      "\uD83C\uDD49",
      "[", "\\", "]", "^", "_", "`",
      "\uD83C\uDD30", "\uD83C\uDD31", "\uD83C\uDD32", "\uD83C\uDD33", "\uD83C\uDD34",
      "\uD83C\uDD35", "\uD83C\uDD36", "\uD83C\uDD37", "\uD83C\uDD38", "\uD83C\uDD39",
      "\uD83C\uDD3A", "\uD83C\uDD3B", "\uD83C\uDD3C", "\uD83C\uDD3D", "\uD83C\uDD3E",
      "\uD83C\uDD3F", "\uD83C\uDD40", "\uD83C\uDD41", "\uD83C\uDD42", "\uD83C\uDD43",
      "\uD83C\uDD44", "\uD83C\uDD45", "\uD83C\uDD46", "\uD83C\uDD47", "\uD83C\uDD48",
      "\uD83C\uDD49"
    ],

    "miscmap": {}
  },


  {
    "name": "Negative Squared",
    "padding": "0",
    "asciimapoffs": "48"
    "asciimap": [
      "0", "1", "2", "3", "4",
      "5", "6", "7", "8", "9",
      ":", ";", "<", "=", ">",
      "?", "@",
      "\uD83C\uDD70", "\uD83C\uDD71", "\uD83C\uDD72", "\uD83C\uDD73", "\uD83C\uDD74",
      "\uD83C\uDD75", "\uD83C\uDD76", "\uD83C\uDD77", "\uD83C\uDD78", "\uD83C\uDD79",
      "\uD83C\uDD7A", "\uD83C\uDD7B", "\uD83C\uDD7C", "\uD83C\uDD7D", "\uD83C\uDD7E",
      "\uD83C\uDD7F", "\uD83C\uDD80", "\uD83C\uDD81", "\uD83C\uDD82", "\uD83C\uDD83",
      "\uD83C\uDD84", "\uD83C\uDD85", "\uD83C\uDD86", "\uD83C\uDD87", "\uD83C\uDD88",
      "\uD83C\uDD89",
      "[", "\\", "]", "^", "_", "`",
      "\uD83C\uDD70", "\uD83C\uDD71", "\uD83C\uDD72", "\uD83C\uDD73", "\uD83C\uDD74",
      "\uD83C\uDD75", "\uD83C\uDD76", "\uD83C\uDD77", "\uD83C\uDD78", "\uD83C\uDD79",
      "\uD83C\uDD7A", "\uD83C\uDD7B", "\uD83C\uDD7C", "\uD83C\uDD7D", "\uD83C\uDD7E",
      "\uD83C\uDD7F", "\uD83C\uDD80", "\uD83C\uDD81", "\uD83C\uDD82", "\uD83C\uDD83",
      "\uD83C\uDD84", "\uD83C\uDD85", "\uD83C\uDD86", "\uD83C\uDD87", "\uD83C\uDD88",
      "\uD83C\uDD89"
    ],

    "miscmap": {}
  },


  {
    "name": "EXTRA THICC",
    "padding": "0",
    "asciimapoffs": "48"
    "asciimap": [
      "0", "1", "2", "3", "4",
      "5", "6", "7", "8", "9",
      ":", ";", "<", "=", ">",
      "?", "@",
      "\u5342", "\u4E43", "\u531A", "\u5200", "\u4E47",
      "\u4E0B", "\u53B6", "\u5344", "\u5DE5", "\u4E01",
      "\u957F", "\u4E5A", "\u4ECE", "\uD841\uDE28", "\u53E3",
      "\u5C38", "\u353F", "\u5C3A", "\u4E02", "\u4E05",
      "\u51F5", "\u30EA", "\u5C71", "\u4E42", "\u4E2B",
      "\u4E59",
      "[", "\\", "]", "^", "_", "`",
      "\u5342", "\u4E43", "\u531A", "\u5200", "\u4E47",
      "\u4E0B", "\u53B6", "\u5344", "\u5DE5", "\u4E01",
      "\u957F", "\u4E5A", "\u4ECE", "\uD841\uDE28", "\u53E3",
      "\u5C38", "\u353F", "\u5C3A", "\u4E02", "\u4E05",
      "\u51F5", "\u30EA", "\u5C71", "\u4E42", "\u4E2B",
      "\u4E59"
    ],

    "miscmap": {}
  },


  {
    "name": "Emoji",
    "padding": "1",
    "asciimapoffs": "48"
    "asciimap": [
      "0\u20E3", "1\u20E3", "2\u20E3", "3\u20E3", "4\u20E3",
      "5\u20E3", "6\u20E3", "7\u20E3", "8\u20E3", "9\u20E3",
      ":", ";", "<", "=", ">",
      "?", "@",
      "\uD83C\uDDE6", "\uD83C\uDDE7", "\uD83C\uDDE8", "\uD83C\uDDE9", "\uD83C\uDDEA",
      "\uD83C\uDDEB", "\uD83C\uDDEC", "\uD83C\uDDED", "\uD83C\uDDEE", "\uD83C\uDDEF",
      "\uD83C\uDDF0", "\uD83C\uDDF1", "\uD83C\uDDF2", "\uD83C\uDDF3", "\uD83C\uDDF4",
      "\uD83C\uDDF5", "\uD83C\uDDF6", "\uD83C\uDDF7", "\uD83C\uDDF8", "\uD83C\uDDF9",
      "\uD83C\uDDFA", "\uD83C\uDDFB", "\uD83C\uDDFC", "\uD83C\uDDFD", "\uD83C\uDDFE",
      "\uD83C\uDDFF",
      "[", "\\", "]", "^", "_", "`",
      "\uD83C\uDDE6", "\uD83C\uDDE7", "\uD83C\uDDE8", "\uD83C\uDDE9", "\uD83C\uDDEA",
      "\uD83C\uDDEB", "\uD83C\uDDEC", "\uD83C\uDDED", "\uD83C\uDDEE", "\uD83C\uDDEF",
      "\uD83C\uDDF0", "\uD83C\uDDF1", "\uD83C\uDDF2", "\uD83C\uDDF3", "\uD83C\uDDF4",
      "\uD83C\uDDF5", "\uD83C\uDDF6", "\uD83C\uDDF7", "\uD83C\uDDF8", "\uD83C\uDDF9",
      "\uD83C\uDDFA", "\uD83C\uDDFB", "\uD83C\uDDFC", "\uD83C\uDDFD", "\uD83C\uDDFE",
      "\uD83C\uDDFF"
    ],

    "miscmap": {}
  },


  {
    "name": "Fullwidth",
    "padding": "0",
    "asciimapoffs": "48"
    "asciimap": [
      "\uFF10", "\uFF11", "\uFF12", "\uFF13", "\uFF14",
      "\uFF15", "\uFF16", "\uFF17", "\uFF18", "\uFF19",
      ":", ";", "<", "=", ">",
      "?", "@",
      "\uFF21", "\uFF22", "\uFF23", "\uFF24", "\uFF25",
      "\uFF26", "\uFF27", "\uFF28", "\uFF29", "\uFF2A",
      "\uFF2B", "\uFF2C", "\uFF2D", "\uFF2E", "\uFF2F",
      "\uFF30", "\uFF31", "\uFF32", "\uFF33", "\uFF34",
      "\uFF35", "\uFF36", "\uFF37", "\uFF38", "\uFF39",
      "\uFF3A",
      "[", "\\", "]", "^", "_", "`",
      "\uFF41", "\uFF42", "\uFF43", "\uFF44", "\uFF45",
      "\uFF46", "\uFF47", "\uFF48", "\uFF49", "\uFF4A",
      "\uFF4B", "\uFF4C", "\uFF4D", "\uFF4E", "\uFF4F",
      "\uFF50", "\uFF51", "\uFF52", "\uFF53", "\uFF54",
      "\uFF55", "\uFF56", "\uFF57", "\uFF58", "\uFF59",
      "\uFF5A"
    ],

    "miscmap": {}
  },


  {
    "name": "Parenthesized",
    "padding": "0",
    "asciimapoffs": "48"
    "asciimap": [
      "0", "\u2474", "\u2475", "\u2476", "\u2477",
      "\u2478", "\u2479", "\u247A", "\u247B", "\u247C",
      ":", ";", "<", "=", ">",
      "?", "@",
      "\u249C", "\u249D", "\u249E", "\u249F", "\u24A0",
      "\u24A1", "\u24A2", "\u24A3", "\u24A4", "\u24A5",
      "\u24A6", "\u24A7", "\u24A8", "\u24A9", "\u24AA",
      "\u24AB", "\u24AC", "\u24AD", "\u24AE", "\u24AF",
      "\u24B0", "\u24B1", "\u24B2", "\u24B3", "\u24B4",
      "\u24B5",
      "[", "\\", "]", "^", "_", "`",
      "\u249C", "\u249D", "\u249E", "\u249F", "\u24A0",
      "\u24A1", "\u24A2", "\u24A3", "\u24A4", "\u24A5",
      "\u24A6", "\u24A7", "\u24A8", "\u24A9", "\u24AA",
      "\u24AB", "\u24AC", "\u24AD", "\u24AE", "\u24AF",
      "\u24B0", "\u24B1", "\u24B2", "\u24B3", "\u24B4",
      "\u24B5"
    ],

    "miscmap": {}
  },


  {
    "name": "'Curvy'",
    "padding": "0",
    "asciimapoffs": "48"
    "asciimap": [
      "0", "1", "2", "3", "4",
      "5", "6", "7", "8", "9",
      ":", ";", "<", "=", ">",
      "?", "@",
      "\u03B1", "\u0432", "\u00A2", "\u2202", "\u0454",
      "\u0192", "\uFEED", "\u043D", "\u03B9", "\u05E0",
      "\u043A", "\u2113", "\u043C", "\u03B7", "\u03C3",
      "\u03C1", "\u06F9", "\u044F", "\u0455", "\u0442",
      "\u03C5", "\u03BD", "\u03C9", "\u03C7", "\u0443",
      "\u0579",
      "[", "\\", "]", "^", "_", "`",
      "\u03B1", "\u0432", "\u00A2", "\u2202", "\u0454",
      "\u0192", "\uFEED", "\u043D", "\u03B9", "\u05E0",
      "\u043A", "\u2113", "\u043C", "\u03B7", "\u03C3",
      "\u03C1", "\u06F9", "\u044F", "\u0455", "\u0442",
      "\u03C5", "\u03BD", "\u03C9", "\u03C7", "\u0443",
      "\u0579"
    ],

    "miscmap": {}
  },


  {
    "name": "Faux Cyrillic",
    "padding": "0",
    "asciimapoffs": "48"
    "asciimap": [
      "0", "1", "2", "3", "4",
      "5", "6", "7", "8", "9",
      ":", ";", "<", "=", ">",
      "?", "@",
      "\u0414", "\u0411", "\u0480", "\u2181", "\u0404",
      "F", "\u0411", "\u041D", "\u0406", "\u0408",
      "\u040C", "L", "\u041C", "\u0418", "\u0424",
      "\u0420", "Q", "\u042F", "\u0405", "\u0413",
      "\u0426", "V", "\u0429", "\u0416", "\u0427",
      "Z",
      "[", "\\", "]", "^", "_", "`",
      "\u0430", "\u044A", "\u0441", "\u2181", "\u044D",
      "f", "\u0411", "\u0402", "\u0456", "\u0458",
      "\u043A", "l", "\u043C", "\u0438", "\u043E",
      "\u0440", "q", "\u0453", "\u0455", "\u0442",
      "\u0446", "v", "\u0448", "\u0445", "\u040E",
      "z"
    ],

    "miscmap": {}
  },


  {
    "name": "Faux Ethiopic",
    "padding": "0",
    "asciimapoffs": "48"
    "asciimap": [
      "0", "1", "2", "3", "4",
      "5", "6", "7", "8", "9",
      ":", ";", "<", "=", ">",
      "?", "@",
      "\u120D", "\u130C", "\u122D", "\u12D5", "\u127F",
      "\u127B", "\u1297", "\u12D8", "\u130E", "\u130B",
      "\u1315", "\u1228", "\u1320", "\u12AD", "\u12D0",
      "\u12E8", "\u12D2", "\u12EA", "\u1290", "\u1355",
      "\u1201", "\u1200", "\u1220", "\u1238", "\u1203",
      "\u130A",
      "[", "\\", "]", "^", "_", "`",
      "\u120D", "\u130C", "\u122D", "\u12D5", "\u127F",
      "\u127B", "\u1297", "\u12D8", "\u130E", "\u130B",
      "\u1315", "\u1228", "\u1320", "\u12AD", "\u12D0",
      "\u12E8", "\u12D2", "\u12EA", "\u1290", "\u1355",
      "\u1201", "\u1200", "\u1220", "\u1238", "\u1203",
      "\u130A"
    ],

    "miscmap": {}
  },


  {
    "name": "Superscript",
    "padding": "0",
    "asciimapoffs": "48"
    "asciimap": [
      "\u2070", "\u00B9", "\u00B2", "\u00B3", "\u2074",
      "\u2075", "\u2076", "\u2077", "\u2078", "\u2079",
      ":", ";", "<", "=", ">",
      "?", "@",
      "\u1D2C", "\u1D2E", "\u1D9C", "\u1D30", "\u1D31",
      "\u1DA0", "\u1D33", "\u1D34", "\u1D35", "\u1D36",
      "\u1D37", "\u1D38", "\u1D39", "\u1D3A", "\u1D3C",
      "\u1D3E", "Q", "\u1D3F", "\u02E2", "\u1D40",
      "\u1D41", "\u2C7D", "\u1D42", "\u02E3", "\u02B8",
      "\u1DBB",
      "[", "\\", "]", "^", "_", "`",
      "\u1D43", "\u1D47", "\u1D9C", "\u1D48", "\u1D49",
      "\u1DA0", "\u1D4D", "\u02B0", "\u2071", "\u02B2",
      "\u1D4F", "\u02E1", "\u1D50", "\u207F", "\u1D52",
      "\u1D56", "q", "\u02B3", "\u02E2", "\u1D57",
      "\u1D58", "\u1D5B", "\u02B7", "\u02E3", "\u02B8",
      "\u1DBB"
    ],

    "miscmap": {}
  },


  {
    "name": "Inverted",
    "padding": "0",
    "asciimapoffs": "48"
    "asciimap": [
      "0", "1", "2", "3", "4",
      "5", "6", "7", "8", "9",
      ":", ";", "<", "=", ">",
      "?", "@",
      "\u0250", "q", "\u0254", "p", "\u01DD",
      "\u025F", "\u0183", "\u0265", "\u0131", "\u027E",
      "\u029E", "\u05DF", "\u026F", "u", "o",
      "d", "b", "\u0279", "s", "\u0287",
      "n", "\uD800\uDF21", "\u028D", "x", "\u028E",
      "z",
      "[", "\\", "]", "^", "_", "`",
      "\u0250", "q", "\u0254", "p", "\u01DD",
      "\u025F", "\u0183", "\u0265", "\u0131", "\u027E",
      "\u029E", "\u05DF", "\u026F", "u", "o",
      "d", "b", "\u0279", "s", "\u0287",
      "n", "\u028C", "\u028D", "x", "\u028E",
      "z"
    ],

    "miscmap": {}
  },


  {
    "name": "Dotted",
    "padding": "0",
    "asciimapoffs": "48"
    "asciimap": [
      "0", "1", "2", "\u04DF", "4",
      "5", "6", "7", "8", "9",
      ":", ";", "<", "=", ">",
      "?", "@",
      "\u00C4", "\u1E04", "\u010A", "\u1E0A", "\u0401",
      "\u1E1E", "\u0120", "\u1E26", "\u0407", "J",
      "\u1E32", "\u1E36", "\u1E40", "\u1E44", "\u00D6",
      "\u1E56", "Q", "\u1E5A", "\u1E60", "\u1E6A",
      "\u00DC", "\u1E7E", "\u1E84", "\u1E8C", "\u0178",
      "\u017B",
      "[", "\\", "]", "^", "_", "`",
      "\u00E4", "\u1E05", "\u010B", "\u1E0B", "\u00EB",
      "\u1E1F", "\u0121", "\u1E27", "\u00EF", "j",
      "\u1E33", "\u1E37", "\u1E41", "\u1E45", "\u00F6",
      "\u1E57", "q", "\u1E5B", "\u1E61", "\u1E97",
      "\u00FC", "\u1E7F", "\u1E85", "\u1E8D", "\u00FF",
      "\u017C"
    ],

    "miscmap": {}
  },


  {
    "name": "Stroked",
    "padding": "0",
    "asciimapoffs": "48"
    "asciimap": [
      "0", "1", "\u01BB", "3", "4",
      "5", "6", "7", "8", "9",
      ":", ";", "<", "=", ">",
      "?", "@",
      "\u023A", "\u0243", "\u023B", "\u0110", "\u0246",
      "F", "\u01E4", "\u0126", "\u0197", "\u0248",
      "\uA740", "\u0141", "M", "N", "\u00D8",
      "\u2C63", "\uA756", "\u024C", "S", "\u0166",
      "\u1D7E", "V", "W", "X", "\u024E",
      "\u01B5",
      "[", "\\", "]", "^", "_", "`",
      "\u023A", "\u0180", "\u023C", "\u0111", "\u0247",
      "f", "\u01E5", "\u0127", "\u0268", "\u0249",
      "\uA741", "\u0142", "m", "n", "\u00F8",
      "\u1D7D", "\uA757", "\u024D", "s", "\u0167",
      "\u1D7E", "v", "w", "x", "\u024F",
      "\u01B6"
    ],

    "miscmap": {}
  },


  {
    "name": "Underlined",
    "padding": "0",
    "asciimapoffs": "48"
    "asciimap": [
      "0\u035F", "1\u035F", "2\u035F", "3\u035F", "4\u035F",
      "5\u035F", "6\u035F", "7\u035F", "8\u035F", "9\u035F",
      ":", ";", "<", "=", ">",
      "?", "@",
      "A\u035F", "B\u035F", "C\u035F", "D\u035F", "E\u035F",
      "F\u035F", "G\u035F", "H\u035F", "I\u035F", "J\u035F",
      "K\u035F", "L\u035F", "M\u035F", "N\u035F", "O\u035F",
      "P\u035F", "Q\u035F", "R\u035F", "S\u035F", "T\u035F",
      "U\u035F", "V\u035F", "W\u035F", "X\u035F", "Y\u035F",
      "Z\u035F",
      "[", "\\", "]", "^", "_", "`",
      "a\u035F", "b\u035F", "c\u035F", "d\u035F", "e\u035F",
      "f\u035F", "g\u035F", "h\u035F", "i\u035F", "j\u035F",
      "k\u035F", "l\u035F", "m\u035F", "n\u035F", "o\u035F",
      "p\u035F", "q\u035F", "r\u035F", "s\u035F", "t\u035F",
      "u\u035F", "v\u035F", "w\u035F", "x\u035F", "y\u035F",
      "z\u035F"
    ],

    "miscmap": {}
  },


  {
    "name": "Double Underlined",
    "padding": "0",
    "asciimapoffs": "48"
    "asciimap": [
      "0\u0347", "1\u0347", "2\u0347", "3\u0347", "4\u0347",
      "5\u0347", "6\u0347", "7\u0347", "8\u0347", "9\u0347",
      ":", ";", "<", "=", ">",
      "?", "@",
      "A\u0347", "B\u0347", "C\u0347", "D\u0347", "E\u0347",
      "F\u0347", "G\u0347", "H\u0347", "I\u0347", "J\u0347",
      "K\u0347", "L\u0347", "M\u0347", "N\u0347", "O\u0347",
      "P\u0347", "Q\u0347", "R\u0347", "S\u0347", "T\u0347",
      "U\u0347", "V\u0347", "W\u0347", "X\u0347", "Y\u0347",
      "Z\u0347",
      "[", "\\", "]", "^", "_", "`",
      "a\u0347", "b\u0347", "c\u0347", "d\u0347", "e\u0347",
      "f\u0347", "g\u0347", "h\u0347", "i\u0347", "j\u0347",
      "k\u0347", "l\u0347", "m\u0347", "n\u0347", "o\u0347",
      "p\u0347", "q\u0347", "r\u0347", "s\u0347", "t\u0347",
      "u\u0347", "v\u0347", "w\u0347", "x\u0347", "y\u0347",
      "z\u0347"
    ],

    "miscmap": {}
  }

  
]

'''

fontNameList = [
'Cursive',
'Bold Cursive',
'Hollow',
'Gothic',
'Bold Gothic',
'Circled',
'Negative Circled',
'Squared',
'Negative Squared',
u'EXTRA THICC',
'Emoji',
'Fullwidth',
'Parenthesized',
'\'Curvy\'',
'Faux Cyrllic',
'Faux Ethiopic',
'Superscript',
'Inverted',
'Dotted',
'Stroked',
'Underlined',
'Double Underlined',
]
  
def main():
  outstr = ''
  for map in range(0, len(fontMapList)):
    teststr = r'''


    {
      "name": "''' + fontNameList[map] + r'''",
      "padding": "0",
      "asciimapoffs": "48",
      "asciimap": [
        '''
    
    newlinecount = 0
    for i in range(52, 62):
      teststr += ('["' + fontMapList[map][i] + '", true], ')
      newlinecount += 1
      if newlinecount % 5 == 0:
        teststr += '\n        '
      
    newlinecount = 0
      
    teststr += r'''[":", true], [";", true], ["<", true], ["=", true], [">", true],
        ["?", true], ["@", true],
        '''
    
    for i in range(26, 52):
      teststr += ('["' + fontMapList[map][i] + '", true], ')
      newlinecount += 1
      if newlinecount % 5 == 0:
        teststr += '\n        '
      
    newlinecount = 0
    
    teststr += r'''
        ["[", true], ["\\", true], ["]", true], ["^", true], ["_", true], ["`", true],
        '''
    
    for i in range(0, 26):
      teststr += ('["' + fontMapList[map][i] + '", true], ')
      newlinecount += 1
      if newlinecount % 5 == 0:
        teststr += '\n        '
      
    newlinecount = 0
    
    teststr = teststr[:-2] # remove ", " from end
    
    teststr += r'''
      ],
      
      "miscmap": {}
    },'''
    
    outstr += teststr
    
  f = open('output.txt', 'w')
  f.write(outstr)
  
if __name__ == "__main__":
  main()
  
  