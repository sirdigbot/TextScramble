#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import random
import wx


EMOJISETIDX = 10
DISCORDSETIDX = 11


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
  u'\uD835\uDD1E', u'\uD835\uDD1F', u'\uD835\uDD20', u'\uD835\uDD21', u'\uD835\uDD22',
  u'\uD835\uDD23', u'\uD835\uDD24', u'\uD835\uDD25', u'\uD835\uDD26', u'\uD835\uDD27',
  u'\uD835\uDD28', u'\uD835\uDD29', u'\uD835\uDD2A', u'\uD835\uDD2B', u'\uD835\uDD2C',
  u'\uD835\uDD2D', u'\uD835\uDD2E', u'\uD835\uDD2F', u'\uD835\uDD30', u'\uD835\uDD31',
  u'\uD835\uDD32', u'\uD835\uDD33', u'\uD835\uDD34', u'\uD835\uDD35', u'\uD835\uDD36',
  u'\uD835\uDD37', u'\uD835\uDD04', u'\uD835\uDD05', u'\u212D', u'\uD835\uDD07',
  u'\uD835\uDD08', u'\uD835\uDD09', u'\uD835\uDD0A', u'\u210C', u'\u2111',
  u'\uD835\uDD0D', u'\uD835\uDD0E', u'\uD835\uDD0F', u'\uD835\uDD10', u'\uD835\uDD11',
  u'\uD835\uDD12', u'\uD835\uDD13', u'\uD835\uDD14', u'\u211C', u'\uD835\uDD16',
  u'\uD835\uDD17', u'\uD835\uDD18', u'\uD835\uDD19', u'\uD835\uDD1A', u'\uD835\uDD1B',
  u'\uD835\uDD1C', u'\u2128',
  u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9'
  ],

  # 4 - Bold Gothic Characters
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
  u'\uD835\uDD84', u'\uD835\uDD85',
  u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9'
  ],

  # 5 - Circled Characters
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
  
  
  # 6 - Negative Circled Characters (Only Uppercase)
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
  
  
  # 7 - Squared Characters (Only Uppercase)
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
  
  
  # 8 - Negative Squared Characters (Only Uppercase)
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
  
  
  # 9 - EXTRA THICC Characters (Only Uppercase)
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
  
  
  # 10 - Emoji Characters (Only Uppercase)
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
  
  
  # 11 - Discord-Friendly Emoji Characters (Emoji + Space). Prevents creation of flag emoji
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
  ],
  
  
  # 12 - Fullwidth Characters
  [
  u'\uFF41', u'\uFF42', u'\uFF43', u'\uFF44', u'\uFF45', u'\uFF46', u'\uFF47', u'\uFF48',
  u'\uFF49', u'\uFF4A', u'\uFF4B', u'\uFF4C', u'\uFF4D', u'\uFF4E', u'\uFF4F', u'\uFF50',
  u'\uFF51', u'\uFF52', u'\uFF53', u'\uFF54', u'\uFF55', u'\uFF56', u'\uFF57', u'\uFF58',
  u'\uFF59', u'\uFF5A', u'\uFF21', u'\uFF22', u'\uFF23', u'\uFF24', u'\uFF25', u'\uFF26',
  u'\uFF27', u'\uFF28', u'\uFF29', u'\uFF2A', u'\uFF2B', u'\uFF2C', u'\uFF2D', u'\uFF2E',
  u'\uFF2F', u'\uFF30', u'\uFF31', u'\uFF32', u'\uFF33', u'\uFF34', u'\uFF35', u'\uFF36',
  u'\uFF37', u'\uFF38', u'\uFF39', u'\uFF3A', u'\uFF10', u'\uFF11', u'\uFF12', u'\uFF13',
  u'\uFF14', u'\uFF15', u'\uFF16', u'\uFF17', u'\uFF18', u'\uFF19'
  ],
  
  
  # 13 - Parenthesized Characters
  [
  u'\u249C', u'\u249D', u'\u249E', u'\u249F', u'\u24A0', u'\u24A1', u'\u24A2', u'\u24A3',
  u'\u24A4', u'\u24A5', u'\u24A6', u'\u24A7', u'\u24A8', u'\u24A9', u'\u24AA', u'\u24AB',
  u'\u24AC', u'\u24AD', u'\u24AE', u'\u24AF', u'\u24B0', u'\u24B1', u'\u24B2', u'\u24B3',
  u'\u24B4', u'\u24B5', u'\u249C', u'\u249D', u'\u249E', u'\u249F', u'\u24A0', u'\u24A1',
  u'\u24A2', u'\u24A3', u'\u24A4', u'\u24A5', u'\u24A6', u'\u24A7', u'\u24A8', u'\u24A9',
  u'\u24AA', u'\u24AB', u'\u24AC', u'\u24AD', u'\u24AE', u'\u24AF', u'\u24B0', u'\u24B1',
  u'\u24B2', u'\u24B3', u'\u24B4', u'\u24B5',
  u'0', u'\u2474', u'\u2475', u'\u2476', u'\u2477', u'\u2478', u'\u2479', u'\u247A', u'\u247B', u'\u247C'
  ],
  
  
  # 14 - 'Curvy' Characters
  [
  u'\u03B1', u'\u0432', u'\u00A2', u'\u2202', u'\u0454', u'\u0192', u'\uFEED', u'\u043D',
  u'\u03B9', u'\u05E0', u'\u043A', u'\u2113', u'\u043C', u'\u03B7', u'\u03C3', u'\u03C1',
  u'\u06F9', u'\u044F', u'\u0455', u'\u0442', u'\u03C5', u'\u03BD', u'\u03C9', u'\u03C7',
  u'\u0443', u'\u0579', u'\u03B1', u'\u0432', u'\u00A2', u'\u2202', u'\u0454', u'\u0192',
  u'\uFEED', u'\u043D', u'\u03B9', u'\u05E0', u'\u043A', u'\u2113', u'\u043C', u'\u03B7',
  u'\u03C3', u'\u03C1', u'\u06F9', u'\u044F', u'\u0455', u'\u0442', u'\u03C5', u'\u03BD',
  u'\u03C9', u'\u03C7', u'\u0443', u'\u0579', u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9'
  ],
  
  
  # 15 - Faux Cyrllic Characters
  [
  u'\u0430', u'\u044A', u'\u0441', u'\u2181', u'\u044D', u'f', u'\u0411', u'\u0402',
  u'\u0456', u'\u0458', u'\u043A', u'l', u'\u043C', u'\u0438', u'\u043E', u'\u0440',
  u'q', u'\u0453', u'\u0455', u'\u0442', u'\u0446', u'v', u'\u0448', u'\u0445',
  u'\u040E', u'z', u'\u0414', u'\u0411', u'\u0480', u'\u2181', u'\u0404', u'F',
  u'\u0411', u'\u041D', u'\u0406', u'\u0408', u'\u040C', u'L', u'\u041C', u'\u0418',
  u'\u0424', u'\u0420', u'Q', u'\u042F', u'\u0405', u'\u0413', u'\u0426', u'V',
  u'\u0429', u'\u0416', u'\u0427', u'Z',
  u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9'
  ],
  
  
  # 16 - Faux Ethiopic Characters
  [
  u'\u120D', u'\u130C', u'\u122D', u'\u12D5', u'\u127F', u'\u127B', u'\u1297', u'\u12D8',
  u'\u130E', u'\u130B', u'\u1315', u'\u1228', u'\u1320', u'\u12AD', u'\u12D0', u'\u12E8',
  u'\u12D2', u'\u12EA', u'\u1290', u'\u1355', u'\u1201', u'\u1200', u'\u1220', u'\u1238',
  u'\u1203', u'\u130A', u'\u120D', u'\u130C', u'\u122D', u'\u12D5', u'\u127F', u'\u127B',
  u'\u1297', u'\u12D8', u'\u130E', u'\u130B', u'\u1315', u'\u1228', u'\u1320', u'\u12AD',
  u'\u12D0', u'\u12E8', u'\u12D2', u'\u12EA', u'\u1290', u'\u1355', u'\u1201', u'\u1200',
  u'\u1220', u'\u1238', u'\u1203', u'\u130A',
  u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9'
  ],
  
  
  # 17 - Superscript Characters
  [
  u'\u1D43', u'\u1D47', u'\u1D9C', u'\u1D48', u'\u1D49', u'\u1DA0', u'\u1D4D', u'\u02B0',
  u'\u2071', u'\u02B2', u'\u1D4F', u'\u02E1', u'\u1D50', u'\u207F', u'\u1D52', u'\u1D56',
  u'q', u'\u02B3', u'\u02E2', u'\u1D57', u'\u1D58', u'\u1D5B', u'\u02B7', u'\u02E3',
  u'\u02B8', u'\u1DBB', u'\u1D2C', u'\u1D2E', u'\u1D9C', u'\u1D30', u'\u1D31', u'\u1DA0',
  u'\u1D33', u'\u1D34', u'\u1D35', u'\u1D36', u'\u1D37', u'\u1D38', u'\u1D39', u'\u1D3A',
  u'\u1D3C', u'\u1D3E', u'Q', u'\u1D3F', u'\u02E2', u'\u1D40', u'\u1D41', u'\u2C7D',
  u'\u1D42', u'\u02E3', u'\u02B8', u'\u1DBB', u'\u2070', u'\u00B9', u'\u00B2', u'\u00B3',
  u'\u2074', u'\u2075', u'\u2076', u'\u2077', u'\u2078', u'\u2079'
  ],
  
  
  # 18 - Inverted Characters
  [
  u'\u0250', u'q', u'\u0254', u'p', u'\u01DD', u'\u025F', u'\u0183', u'\u0265',
  u'\u0131', u'\u027E', u'\u029E', u'\u05DF', u'\u026F', u'u', u'o', u'd',
  u'b', u'\u0279', u's', u'\u0287', u'n', u'\u028C', u'\u028D', u'x',
  u'\u028E', u'z', u'\u0250', u'q', u'\u0254', u'p', u'\u01DD', u'\u025F',
  u'\u0183', u'\u0265', u'\u0131', u'\u027E', u'\u029E', u'\u05DF', u'\u026F', u'u',
  u'o', u'd', u'b', u'\u0279', u's', u'\u0287', u'n', u'\uD800\uDF21',
  u'\u028D', u'x', u'\u028E', u'z',
  u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9'
  ],
  
  
  # 19 - Dotted Characters
  [
  u'\u00E4', u'\u1E05', u'\u010B', u'\u1E0B', u'\u00EB', u'\u1E1F', u'\u0121', u'\u1E27',
  u'\u00EF', u'j', u'\u1E33', u'\u1E37', u'\u1E41', u'\u1E45', u'\u00F6', u'\u1E57',
  u'q', u'\u1E5B', u'\u1E61', u'\u1E97', u'\u00FC', u'\u1E7F', u'\u1E85', u'\u1E8D',
  u'\u00FF', u'\u017C', u'\u00C4', u'\u1E04', u'\u010A', u'\u1E0A', u'\u0401', u'\u1E1E',
  u'\u0120', u'\u1E26', u'\u0407', u'J', u'\u1E32', u'\u1E36', u'\u1E40', u'\u1E44',
  u'\u00D6', u'\u1E56', u'Q', u'\u1E5A', u'\u1E60', u'\u1E6A', u'\u00DC', u'\u1E7E',
  u'\u1E84', u'\u1E8C', u'\u0178', u'\u017B',
  u'0', u'1', u'2', u'\u04DF', u'4', u'5', u'6', u'7', u'8', u'9'
  ],
  
  
  # 20 - Stroked Characters
  [
  u'\u023A', u'\u0180', u'\u023C', u'\u0111', u'\u0247', u'f', u'\u01E5', u'\u0127',
  u'\u0268', u'\u0249', u'\uA741', u'\u0142', u'm', u'n', u'\u00F8', u'\u1D7D',
  u'\uA757', u'\u024D', u's', u'\u0167', u'\u1D7E', u'v', u'w', u'x',
  u'\u024F', u'\u01B6', u'\u023A', u'\u0243', u'\u023B', u'\u0110', u'\u0246', u'F',
  u'\u01E4', u'\u0126', u'\u0197', u'\u0248', u'\uA740', u'\u0141', u'M', u'N',
  u'\u00D8', u'\u2C63', u'\uA756', u'\u024C', u'S', u'\u0166', u'\u1D7E', u'V',
  u'W', u'X', u'\u024E', u'\u01B5',
  u'0', u'1', u'\u01BB', u'3', u'4', u'5', u'6', u'7', u'8', u'9'
  ],
  
  
  # 21 - Underlined Characters
  [
  u'a\u035F', u'b\u035F', u'c\u035F', u'd\u035F', u'e\u035F', u'f\u035F', u'g\u035F', u'h\u035F',
  u'i\u035F', u'j\u035F', u'k\u035F', u'l\u035F', u'm\u035F', u'n\u035F', u'o\u035F', u'p\u035F',
  u'q\u035F', u'r\u035F', u's\u035F', u't\u035F', u'u\u035F', u'v\u035F', u'w\u035F', u'x\u035F',
  u'y\u035F', u'z\u035F',
  u'A\u035F', u'B\u035F', u'C\u035F', u'D\u035F', u'E\u035F', u'F\u035F', u'G\u035F', u'H\u035F',
  u'I\u035F', u'J\u035F', u'K\u035F', u'L\u035F', u'M\u035F', u'N\u035F', u'O\u035F', u'P\u035F',
  u'Q\u035F', u'R\u035F', u'S\u035F', u'T\u035F', u'U\u035F', u'V\u035F', u'W\u035F', u'X\u035F',
  u'Y\u035F', u'Z\u035F',
  u'0\u035F', u'1\u035F', u'2\u035F', u'3\u035F', u'4\u035F', u'5\u035F', u'6\u035F', u'7\u035F', u'8\u035F', u'9\u035F'
  ],
  
  
  # 22 - Double Underlined Characters
  [
  u'a\u0347', u'b\u0347', u'c\u0347', u'd\u0347', u'e\u0347', u'f\u0347', u'g\u0347', u'h\u0347',
  u'i\u0347', u'j\u0347', u'k\u0347', u'l\u0347', u'm\u0347', u'n\u0347', u'o\u0347', u'p\u0347',
  u'q\u0347', u'r\u0347', u's\u0347', u't\u0347', u'u\u0347', u'v\u0347', u'w\u0347', u'x\u0347',
  u'y\u0347', u'z\u0347',
  u'A\u0347', u'B\u0347', u'C\u0347', u'D\u0347', u'E\u0347', u'F\u0347', u'G\u0347', u'H\u0347',
  u'I\u0347', u'J\u0347', u'K\u0347', u'L\u0347', u'M\u0347', u'N\u0347', u'O\u0347', u'P\u0347',
  u'Q\u0347', u'R\u0347', u'S\u0347', u'T\u0347', u'U\u0347', u'V\u0347', u'W\u0347', u'X\u0347',
  u'Y\u0347', u'Z\u0347',
  u'0\u0347', u'1\u0347', u'2\u0347', u'3\u0347', u'4\u0347', u'5\u0347', u'6\u0347', u'7\u0347', u'8\u0347', u'9\u0347'
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
    self.modeSelect.Append('Bold Gothic')
    self.modeSelect.Append('Circled')
    self.modeSelect.Append('Negative Circled')
    self.modeSelect.Append('Squared')
    self.modeSelect.Append('Negative Squared')
    self.modeSelect.Append(u'乇乂丅尺卂 丅卄工匚匚')
    self.modeSelect.Append('Emoji')
    self.modeSelect.Append('Discord-Friendly Emoji') # Emoji Characters with 1-space either side
    self.modeSelect.Append('Fullwidth')
    self.modeSelect.Append('Parenthesized')
    self.modeSelect.Append('\'Curvy\'')
    self.modeSelect.Append('Faux Cyrllic')
    self.modeSelect.Append('Faux Ethiopic')
    self.modeSelect.Append('Superscript')
    self.modeSelect.Append('Inverted')
    self.modeSelect.Append('Dotted')
    self.modeSelect.Append('Stroked')
    self.modeSelect.Append('Underlined')
    self.modeSelect.Append('Double Underlined')
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
 