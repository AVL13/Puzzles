#!/usr/bin/env python3
# -*- coding: utf-8 -*-


TILESIZE = 60 # 30 - minimum, maximum определяется размером экрана


from PyQt4 import QtGui, QtCore



class Twelve(QtGui.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(self.__class__.__name__)
        dialog_size = (TILESIZE * 3 + 8, TILESIZE * 5 + 12)
        self.setMaximumSize(*dialog_size)
        self.setMinimumSize(*dialog_size)
        self.__empty = 7
        self.__tiles = [QtGui.QLabel('1', self),
                        QtGui.QLabel('2', self),
                        QtGui.QLabel('3', self),
                        QtGui.QLabel('12', self),
                        QtGui.QLabel(' ', self),
                        QtGui.QLabel('4', self),
                        QtGui.QLabel('11', self),
                        None,
                        QtGui.QLabel('5', self),
                        QtGui.QLabel('10', self),
                        QtGui.QLabel(' ', self),
                        QtGui.QLabel('6', self),
                        QtGui.QLabel('9', self),
                        QtGui.QLabel('8', self),
                        QtGui.QLabel('7', self)]
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtGui.QColor(190,190,190))
        font = QtGui.QFont('Arial', TILESIZE // 3.6)
        for i, tile in enumerate(self.__tiles):
            if not tile: continue
            tile.setAlignment(QtCore.Qt.AlignCenter)
            tile.setFont(font)
            tile.setAutoFillBackground(True)
            tile.setPalette(palette)
            tile.setFrameShape(QtGui.QFrame.StyledPanel)
            #tile.setFrameStyle(QtGui.QFrame.Raised)
            tile.setLineWidth(2)
            tile.setMidLineWidth(2)
            tile.resize(TILESIZE, TILESIZE)
            tile.move((i%3)*(TILESIZE+2) + 2, (i//3)*(TILESIZE+2) + 2)


    def keyReleaseEvent(self, event):
        super().keyReleaseEvent(event)
        key = event.key()
        if (key == QtCore.Qt.Key_Left and
                self.__empty % 3 != 0 and
                self.__empty not in (5, 11)):
            tile = self.__tiles[self.__empty - 1]
            self.__tiles[self.__empty] = tile
            self.__tiles[self.__empty - 1] = None
            tile.move(tile.x() + (TILESIZE+2), tile.y())
            self.__empty -= 1
        elif (key == QtCore.Qt.Key_Right and
                self.__empty % 3 != 2 and
                self.__empty not in (3, 9)):
            tile = self.__tiles[self.__empty + 1]
            self.__tiles[self.__empty] = tile
            self.__tiles[self.__empty + 1] = None
            tile.move(tile.x() - (TILESIZE+2), tile.y())
            self.__empty += 1
        elif (key == QtCore.Qt.Key_Up and
                self.__empty > 2 and
                self.__empty not in (7, 13)):
            tile = self.__tiles[self.__empty - 3]
            self.__tiles[self.__empty] = tile
            self.__tiles[self.__empty - 3] = None
            tile.move(tile.x(), tile.y() + (TILESIZE+2))
            self.__empty -= 3
        elif (key == QtCore.Qt.Key_Down and
                self.__empty < 12 and
                self.__empty not in (1, 7)):
            tile = self.__tiles[self.__empty + 3]
            self.__tiles[self.__empty] = tile
            self.__tiles[self.__empty + 3] = None
            tile.move(tile.x(), tile.y() - (TILESIZE+2))
            self.__empty += 3


##    def closeEvent(self, event):
##        msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Warning,
##                                   'Close the puzzle',
##                                   'Are you sure?',
##                                   QtGui.QMessageBox.Close |
##                                   QtGui.QMessageBox.Cancel,
##                                   self)
##        answer = msgBox.exec()
##        if answer == QtGui.QMessageBox.Close:
##            event.accept()
##            super().closeEvent(event)
##        else:
##            event.ignore()
##            #super().closeEvent(event)


    def done(self, r):
        msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Warning,
                                   'Close the puzzle',
                                   'Are you sure?',
                                   QtGui.QMessageBox.Close |
                                   QtGui.QMessageBox.Cancel,
                                   self)
        answer = msgBox.exec()
        if answer == QtGui.QMessageBox.Close:
            super().done(r)



class Fifteen(QtGui.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(self.__class__.__name__)
        dialog_size = (TILESIZE * 4 + 10, TILESIZE * 4 + 10)
        self.setMaximumSize(*dialog_size)
        self.setMinimumSize(*dialog_size)
        self.__empty = 15
        self.__tiles = [QtGui.QLabel('1', self),
                        QtGui.QLabel('2', self),
                        QtGui.QLabel('3', self),
                        QtGui.QLabel('4', self),
                        QtGui.QLabel('5', self),
                        QtGui.QLabel('6', self),
                        QtGui.QLabel('7', self),
                        QtGui.QLabel('8', self),
                        QtGui.QLabel('9', self),
                        QtGui.QLabel('10', self),
                        QtGui.QLabel('11', self),
                        QtGui.QLabel('12', self),
                        QtGui.QLabel('13', self),
                        QtGui.QLabel('14', self),
                        QtGui.QLabel('15', self),
                        None]
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtGui.QColor(190,190,190))
        font = QtGui.QFont('Arial', TILESIZE // 3.6)
        for i, tile in enumerate(self.__tiles[:-1]):
            tile.setAlignment(QtCore.Qt.AlignCenter)
            tile.setFont(font)
            tile.setAutoFillBackground(True)
            tile.setPalette(palette)
            tile.setFrameShape(QtGui.QFrame.StyledPanel)
            #tile.setFrameStyle(QtGui.QFrame.Raised)
            tile.setLineWidth(2)
            tile.setMidLineWidth(2)
            tile.resize(TILESIZE, TILESIZE)
            tile.move((i%4)*(TILESIZE+2) + 2, (i//4)*(TILESIZE+2) + 2)


    def keyReleaseEvent(self, event):
        super().keyReleaseEvent(event)
        key = event.key()
        if (key == QtCore.Qt.Key_Left and
                self.__empty % 4 != 0):
            tile = self.__tiles[self.__empty - 1]
            self.__tiles[self.__empty] = tile
            self.__tiles[self.__empty - 1] = None
            tile.move(tile.x() + (TILESIZE+2), tile.y())
            self.__empty -= 1
        elif (key == QtCore.Qt.Key_Right and
                self.__empty % 4 != 3):
            tile = self.__tiles[self.__empty + 1]
            self.__tiles[self.__empty] = tile
            self.__tiles[self.__empty + 1] = None
            tile.move(tile.x() - (TILESIZE+2), tile.y())
            self.__empty += 1
        elif (key == QtCore.Qt.Key_Up and
                self.__empty > 3):
            tile = self.__tiles[self.__empty - 4]
            self.__tiles[self.__empty] = tile
            self.__tiles[self.__empty - 4] = None
            tile.move(tile.x(), tile.y() + (TILESIZE+2))
            self.__empty -= 4
        elif (key == QtCore.Qt.Key_Down and
                self.__empty < 12):
            tile = self.__tiles[self.__empty + 4]
            self.__tiles[self.__empty] = tile
            self.__tiles[self.__empty + 4] = None
            tile.move(tile.x(), tile.y() - (TILESIZE+2))
            self.__empty += 4


    def done(self, r):
        msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Warning,
                                   'Close the puzzle',
                                   'Are you sure?',
                                   QtGui.QMessageBox.Close |
                                   QtGui.QMessageBox.Cancel,
                                   self)
        answer = msgBox.exec()
        if answer == QtGui.QMessageBox.Close:
            super().done(r)



if "__main__" == __name__:
    import sys

    app = QtGui.QApplication(sys.argv)

    twelve = Twelve()
    twelve.show()

    fifteen = Fifteen()
    fifteen.show()

    sys.exit(app.exec())
