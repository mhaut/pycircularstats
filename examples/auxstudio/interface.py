# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(780, 538)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 11, 761, 481))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.drawmoduleandazimuthdistribution = QtWidgets.QRadioButton(self.groupBox)
        self.drawmoduleandazimuthdistribution.setChecked(True)
        self.drawmoduleandazimuthdistribution.setObjectName("drawmoduleandazimuthdistribution")
        self.verticalLayout.addWidget(self.drawmoduleandazimuthdistribution)
        self.drawdistribution = QtWidgets.QRadioButton(self.groupBox)
        self.drawdistribution.setObjectName("drawdistribution")
        self.verticalLayout.addWidget(self.drawdistribution)
        self.drawhistogram = QtWidgets.QRadioButton(self.groupBox)
        self.drawhistogram.setObjectName("drawhistogram")
        self.verticalLayout.addWidget(self.drawhistogram)
        self.drawPoints = QtWidgets.QRadioButton(self.groupBox)
        self.drawPoints.setObjectName("drawPoints")
        self.verticalLayout.addWidget(self.drawPoints)
        self.drawdensityMap = QtWidgets.QRadioButton(self.groupBox)
        self.drawdensityMap.setObjectName("drawdensityMap")
        self.verticalLayout.addWidget(self.drawdensityMap)
        self.drawqqplot = QtWidgets.QRadioButton(self.groupBox)
        self.drawqqplot.setObjectName("drawqqplot")
        self.verticalLayout.addWidget(self.drawqqplot)
        self.drawVectors = QtWidgets.QRadioButton(self.groupBox)
        self.drawVectors.setObjectName("drawVectors")
        self.verticalLayout.addWidget(self.drawVectors)
        self.modstats = QtWidgets.QRadioButton(self.groupBox)
        self.modstats.setObjectName("modstats")
        self.verticalLayout.addWidget(self.modstats)
        self.azimuthstats = QtWidgets.QRadioButton(self.groupBox)
        self.azimuthstats.setObjectName("azimuthstats")
        self.verticalLayout.addWidget(self.azimuthstats)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 1, 1, 1)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(20, 500, 751, 27))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.type0 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.type0.setChecked(True)
        self.type0.setObjectName("type0")
        self.gridLayout_3.addWidget(self.type0, 0, 0, 1, 1)
        self.type1 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.type1.setObjectName("type1")
        self.gridLayout_3.addWidget(self.type1, 0, 1, 1, 1)
        self.type2 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.type2.setObjectName("type2")
        self.gridLayout_3.addWidget(self.type2, 0, 2, 1, 1)
        self.type3 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.type3.setObjectName("type3")
        self.gridLayout_3.addWidget(self.type3, 0, 4, 1, 1)
        self.calculate = QtWidgets.QPushButton(self.layoutWidget1)
        self.calculate.setEnabled(False)
        self.calculate.setObjectName("calculate")
        self.gridLayout_3.addWidget(self.calculate, 0, 5, 1, 1)
        self.buttonload = QtWidgets.QPushButton(self.layoutWidget1)
        self.buttonload.setObjectName("buttonload")
        self.gridLayout_3.addWidget(self.buttonload, 0, 6, 1, 1)
        self.labelpath = QtWidgets.QLabel(self.layoutWidget1)
        self.labelpath.setText("")
        self.labelpath.setObjectName("labelpath")
        self.gridLayout_3.addWidget(self.labelpath, 0, 7, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Function:"))
        self.drawmoduleandazimuthdistribution.setText(_translate("Form", "ModuleandAzimuthDistribution"))
        self.drawdistribution.setText(_translate("Form", "Distribution"))
        self.drawhistogram.setText(_translate("Form", "Histogram"))
        self.drawPoints.setText(_translate("Form", "Points"))
        self.drawdensityMap.setText(_translate("Form", "DensityMap"))
        self.drawqqplot.setText(_translate("Form", "QQplot"))
        self.drawVectors.setText(_translate("Form", "Vectors"))
        self.modstats.setText(_translate("Form", "Module stats"))
        self.azimuthstats.setText(_translate("Form", "Azimuths stats"))
        self.type0.setText(_translate("Form", "Cartesian"))
        self.type1.setText(_translate("Form", "Incremental"))
        self.type2.setText(_translate("Form", "Polar"))
        self.type3.setText(_translate("Form", "Vectors"))
        self.calculate.setText(_translate("Form", "Calculate"))
        self.buttonload.setText(_translate("Form", "Select file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
