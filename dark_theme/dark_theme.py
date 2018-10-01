#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#
# PyQt dark palette from hdrpano
# Enter the palette code into you main windows class in init

# **** => copy this line ****
from PyQt5.QtGui import QPalette, QColor

class dark_theme:
    def __init__(self, app):

        # **** => copy this code ****
        app.setStyle("Fusion")
        dark_palette = QPalette()

        dark_palette.setColor(QPalette.Window, QColor(46, 47, 48))
        dark_palette.setColor(QPalette.WindowText, QColor(208, 208, 208))
        dark_palette.setColor(QPalette.Light, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Midlight, QColor(227, 227, 227))
        dark_palette.setColor(QPalette.Dark, QColor(64, 66, 68))
        dark_palette.setColor(QPalette.Mid, QColor(160, 160, 160))
        dark_palette.setColor(QPalette.Text, QColor(208, 208, 208))
        dark_palette.setColor(QPalette.BrightText, QColor(255, 51, 51))
        dark_palette.setColor(QPalette.Button, QColor(64, 66, 68))
        dark_palette.setColor(QPalette.ButtonText, QColor(208, 208, 208))  
        dark_palette.setColor(QPalette.Base, QColor(46, 47, 48))
        dark_palette.setColor(QPalette.Shadow, QColor(105, 105, 105))
        dark_palette.setColor(QPalette.Highlight, QColor(0, 0, 0, 102))
        dark_palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Link, QColor(0, 122, 244))
        dark_palette.setColor(QPalette.LinkVisited, QColor(165, 122, 255))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 54, 55))
        dark_palette.setColor(QPalette.NoRole, QColor(0, 0, 0))
        dark_palette.setColor(QPalette.ToolTipBase, QColor(0, 0, 0, 102))
        dark_palette.setColor(QPalette.ToolTipText, QColor(208, 208, 208))
        dark_palette.setColor(QPalette.Disabled, QPalette.Window, QColor(68, 68, 68, 255))
        dark_palette.setColor(QPalette.Disabled, QPalette.WindowText, QColor(164, 166, 168, 96))
        dark_palette.setColor(QPalette.Disabled, QPalette.Text, QColor(164, 166, 168, 96))
        dark_palette.setColor(QPalette.Disabled, QPalette.ButtonText, QColor(164, 166, 168, 96))
        dark_palette.setColor(QPalette.Disabled, QPalette.Base, QColor(68, 68, 68, 255))
        dark_palette.setColor(QPalette.Disabled, QPalette.Shadow, QColor(0, 0, 0, 255))

        app.setPalette(dark_palette)
        app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
