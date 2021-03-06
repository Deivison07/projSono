#=======================================================================#

        self.horizontalLayout_2Coletanea = QtWidgets.QHBoxLayout(self.tabColetaneas)
        self.horizontalLayout_2Coletanea.setObjectName("horizontalLayout_2Coletanea")
        self.boxColetanea = QtWidgets.QGroupBox(self.tabColetaneas)
        self.boxColetanea.setTitle("")
        self.boxColetanea.setObjectName("boxColetanea")
        self.boxColetanea.setMinimumSize(QtCore.QSize(603, 524))
        self.boxColetanea.setMaximumSize(QtCore.QSize(603, 524))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.boxColetanea)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.boxColetanea)
        self.groupBox.setTabletTracking(False)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText('<- Voltar')
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayoutColetanea = QtWidgets.QHBoxLayout()
        self.horizontalLayoutColetanea.setObjectName("horizontalLayoutColetanea")
        self.horizontalLayoutColetanea_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayoutColetanea_2.setObjectName("horizontalLayoutColetanea_2")
        self.imagemColetanea = QtWidgets.QLabel(self.boxColetanea)
        self.imagemColetanea.setMinimumSize(QtCore.QSize(301, 421))
        self.imagemColetanea.setMaximumSize(QtCore.QSize(301, 421))
        self.imagemColetanea.setFrameShape(QtWidgets.QFrame.Box)
        self.imagemColetanea.setText("")
        self.imagemColetanea.setPixmap(QtGui.QPixmap("iconesColetanea/adoradores.jpg"))
        self.imagemColetanea.setScaledContents(True)
        self.imagemColetanea.setObjectName("imagemColetanea")
        self.horizontalLayoutColetanea_2.addWidget(self.imagemColetanea)
        self.horizontalLayoutColetanea.addLayout(self.horizontalLayoutColetanea_2)
        self.verticalLayoutColetanea = QtWidgets.QVBoxLayout()
        self.verticalLayoutColetanea.setObjectName("verticalLayoutColetanea")
        self.boatoColetanea = QtWidgets.QToolButton(self.boxColetanea)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icones/add-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boatoColetanea.setIcon(icon)
        self.boatoColetanea.setObjectName("boatoColetanea")
        self.verticalLayoutColetanea.addWidget(self.boatoColetanea, 0, QtCore.Qt.AlignRight)
        self.listaColetanea = QtWidgets.QListWidget(self.boxColetanea)
        self.listaColetanea.setMinimumSize(QtCore.QSize(256, 421))
        self.listaColetanea.setMaximumSize(QtCore.QSize(256, 421))
        self.listaColetanea.setStyleSheet("")
        self.listaColetanea.setObjectName("listaColetanea")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.listaColetanea.addItem(item)
        self.verticalLayoutColetanea.addWidget(self.listaColetanea)
        self.horizontalLayoutColetanea.addLayout(self.verticalLayoutColetanea)
        self.verticalLayout.addLayout(self.horizontalLayoutColetanea)
        self.horizontalLayout_2Coletanea.addWidget(self.boxColetanea)
        self.verticalLayout_11.addWidget(self.boxColetanea)

        self.verticalLayout_10.addLayout(self.verticalLayout_4)

        self.verticalLayout_11.addWidget(self.boxListaColetanea)

        self.boxColetanea.close()

        #=========================================================================#