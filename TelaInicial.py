# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaInicial.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(919, 559)
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frameVideo = QtWidgets.QFrame(self.groupBox_2)
        self.frameVideo.setMinimumSize(QtCore.QSize(301, 211))
        self.frameVideo.setFrameShape(QtWidgets.QFrame.Box)
        self.frameVideo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameVideo.setObjectName("frameVideo")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frameVideo)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.imagemMidia = QtWidgets.QLabel(self.frameVideo)
        self.imagemMidia.setText("")
        self.imagemMidia.setPixmap(QtGui.QPixmap("icones/play.png"))
        self.imagemMidia.setScaledContents(False)
        self.imagemMidia.setAlignment(QtCore.Qt.AlignCenter)
        self.imagemMidia.setWordWrap(False)
        self.imagemMidia.setOpenExternalLinks(False)
        self.imagemMidia.setObjectName("imagemMidia")
        self.verticalLayout_3.addWidget(self.imagemMidia)
        self.verticalLayout_6.addWidget(self.frameVideo)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.slideMusica = QtWidgets.QSlider(self.groupBox_2)
        self.slideMusica.setMinimumSize(QtCore.QSize(314, 22))
        self.slideMusica.setPageStep(1)
        self.slideMusica.setOrientation(QtCore.Qt.Horizontal)
        self.slideMusica.setObjectName("slideMusica")
        self.verticalLayout_5.addWidget(self.slideMusica)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.botaoAnterior = QtWidgets.QPushButton(self.groupBox_2)
        self.botaoAnterior.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icones/previus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botaoAnterior.setIcon(icon)
        self.botaoAnterior.setIconSize(QtCore.QSize(18, 18))
        self.botaoAnterior.setAutoRepeat(False)
        self.botaoAnterior.setObjectName("botaoAnterior")
        self.horizontalLayout.addWidget(self.botaoAnterior)
        self.botaoPlay = QtWidgets.QPushButton(self.groupBox_2)
        self.botaoPlay.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icones/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botaoPlay.setIcon(icon1)
        self.botaoPlay.setIconSize(QtCore.QSize(18, 18))
        self.botaoPlay.setAutoRepeat(False)
        self.botaoPlay.setObjectName("botaoPlay")
        self.horizontalLayout.addWidget(self.botaoPlay)
        self.botaoProximo = QtWidgets.QPushButton(self.groupBox_2)
        self.botaoProximo.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icones/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botaoProximo.setIcon(icon2)
        self.botaoProximo.setIconSize(QtCore.QSize(18, 18))
        self.botaoProximo.setAutoRepeat(False)
        self.botaoProximo.setObjectName("botaoProximo")
        self.horizontalLayout.addWidget(self.botaoProximo)
        self.botaoStop = QtWidgets.QPushButton(self.groupBox_2)
        self.botaoStop.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icones/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botaoStop.setIcon(icon3)
        self.botaoStop.setIconSize(QtCore.QSize(18, 18))
        self.botaoStop.setAutoRepeat(False)
        self.botaoStop.setObjectName("botaoStop")
        self.horizontalLayout.addWidget(self.botaoStop)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setMaximumSize(QtCore.QSize(21, 21))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icones/note-beam.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.comboMusica = QtWidgets.QComboBox(self.groupBox_2)
        self.comboMusica.setFrame(True)
        self.comboMusica.setObjectName("comboMusica")
        self.comboMusica.addItem("")
        self.comboMusica.addItem("")
        self.horizontalLayout_3.addWidget(self.comboMusica)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setMaximumSize(QtCore.QSize(21, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("icones/legendas.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.comboLegenda = QtWidgets.QComboBox(self.groupBox_2)
        self.comboLegenda.setFrame(True)
        self.comboLegenda.setObjectName("comboLegenda")
        self.comboLegenda.addItem("")
        self.comboLegenda.addItem("")
        self.horizontalLayout_4.addWidget(self.comboLegenda)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.botaoVolume = QtWidgets.QPushButton(self.groupBox_2)
        self.botaoVolume.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icones/iconfinder-volume-max-sound-speaker-audio-4593170_122277.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botaoVolume.setIcon(icon4)
        self.botaoVolume.setIconSize(QtCore.QSize(18, 18))
        self.botaoVolume.setAutoRepeat(False)
        self.botaoVolume.setObjectName("botaoVolume")
        self.horizontalLayout_7.addWidget(self.botaoVolume)
        self.slideVolume = QtWidgets.QSlider(self.groupBox_2)
        self.slideVolume.setProperty("value", 99)
        self.slideVolume.setOrientation(QtCore.Qt.Horizontal)
        self.slideVolume.setObjectName("slideVolume")
        self.horizontalLayout_7.addWidget(self.slideVolume)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        self.listaTrecho = QtWidgets.QListWidget(self.groupBox_2)
        self.listaTrecho.setMinimumSize(QtCore.QSize(251, 320))
        self.listaTrecho.setObjectName("listaTrecho")
        self.horizontalLayout_6.addWidget(self.listaTrecho)
        self.verticalLayout_9.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.botaoAdicionar = QtWidgets.QToolButton(self.groupBox_3)
        self.botaoAdicionar.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icones/add-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botaoAdicionar.setIcon(icon5)
        self.botaoAdicionar.setObjectName("botaoAdicionar")
        self.horizontalLayout_8.addWidget(self.botaoAdicionar)
        self.botaoRemover = QtWidgets.QToolButton(self.groupBox_3)
        self.botaoRemover.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icones/remove-symbol_icon-icons.com_73439.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botaoRemover.setIcon(icon6)
        self.botaoRemover.setObjectName("botaoRemover")
        self.horizontalLayout_8.addWidget(self.botaoRemover)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.listaPlaylist = QtWidgets.QListWidget(self.groupBox_3)
        self.listaPlaylist.setObjectName("listaPlaylist")
        self.verticalLayout_8.addWidget(self.listaPlaylist)
        self.horizontalLayout_9.addLayout(self.verticalLayout_8)
        self.verticalLayout_9.addWidget(self.groupBox_3)
        self.horizontalLayout_12.addLayout(self.verticalLayout_9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_2 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_2.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidget_2.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.dockWidgetContents_2)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.groupBox = QtWidgets.QGroupBox(self.dockWidgetContents_2)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.areaBusca = QtWidgets.QLineEdit(self.groupBox)
        self.areaBusca.setObjectName("areaBusca")
        self.horizontalLayout_2.addWidget(self.areaBusca)
        self.comboBanco = QtWidgets.QComboBox(self.groupBox)
        self.comboBanco.setObjectName("comboBanco")
        self.comboBanco.addItem("")
        self.comboBanco.addItem("")
        self.comboBanco.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBanco)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.botaoAdicionar_2 = QtWidgets.QToolButton(self.groupBox)
        self.botaoAdicionar_2.setText("")
        self.botaoAdicionar_2.setIcon(icon5)
        self.botaoAdicionar_2.setObjectName("botaoAdicionar_2")
        self.verticalLayout_2.addWidget(self.botaoAdicionar_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.listaBanco = QtWidgets.QListWidget(self.groupBox)
        self.listaBanco.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.listaBanco.setAcceptDrops(True)
        self.listaBanco.setObjectName("listaBanco")
        self.verticalLayout.addWidget(self.listaBanco)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_11.addLayout(self.verticalLayout_2)
        self.horizontalLayout_10.addWidget(self.groupBox)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_2)

        self.retranslateUi(MainWindow)
        self.comboMusica.setCurrentIndex(0)
        self.comboLegenda.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Player"))
        self.comboMusica.setItemText(0, _translate("MainWindow", "Cantada", "654"))
        self.comboMusica.setItemText(1, _translate("MainWindow", "Playback"))
        self.comboLegenda.setCurrentText(_translate("MainWindow", "Normal"))
        self.comboLegenda.setItemText(0, _translate("MainWindow", "Normal"))
        self.comboLegenda.setItemText(1, _translate("MainWindow", "Sem Legenda"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Playlist"))
        self.botaoAdicionar.setToolTip(_translate("MainWindow", "<html><head/><body><p>Adicionar midia externa</p></body></html>"))
        self.botaoRemover.setToolTip(_translate("MainWindow", "<html><head/><body><p>Remover item da lista</p></body></html>"))
        self.dockWidget_2.setWindowTitle(_translate("MainWindow", "Sonoplastia"))
        self.groupBox.setTitle(_translate("MainWindow", "Banco:"))
        self.areaBusca.setToolTip(_translate("MainWindow", "<html><head/><body><p>Clique Enter para procurar</p></body></html>"))
        self.comboBanco.setItemText(0, _translate("MainWindow", "Musica"))
        self.comboBanco.setItemText(1, _translate("MainWindow", "Trecho"))
        self.comboBanco.setItemText(2, _translate("MainWindow", "Album"))
        self.botaoAdicionar_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>Adicionar a playList</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
