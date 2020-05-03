import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTabWidget, QFormLayout, QLabel, QComboBox, QPushButton, QMessageBox
from PyQt5.QtCore import pyqtSlot
from Operator import calculateResistor, colors_band, tolerance_band #All value for every resistor value get from this file

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Resistor Calculator'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 230
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #Start for making tab
        self.table_widget = TableWidget(self)
        self.setCentralWidget(self.table_widget)

class TableWidget(QTabWidget):
    def __init__(self, parent):
        super(QTabWidget, self).__init__(parent)
        #Initialize tab screen
        self.tab_3band = QWidget()
        self.tab_4band = QWidget()
        self.tab_5band = QWidget()

        #Add tabs
        self.addTab(self.tab_3band,"3 Band")
        self.addTab(self.tab_4band,"4 Band")
        self.addTab(self.tab_5band,"5 Band")

        #Show every tab UI
        self.tab_3band_UI()
        self.tab_4band_UI()
        self.tab_5band_UI()

    def tab_3band_UI(self):
        #Form layout_3band for Input
        self.layout_3band = QFormLayout()

        #Gather all option of resistor color for 3 band resistor
        self.band1_3band = self.getColor()
        self.band2_3band = self.getColor()
        self.band3_3band = self.getColor()
        self.layout_3band.addRow(QLabel("Band 1:"), self.band1_3band)
        self.layout_3band.addRow(QLabel("Band 2:"), self.band2_3band)
        self.layout_3band.addRow(QLabel("Band 3(Multiplier):"), self.band3_3band)

        #Submit button for 3 band resistor
        self.submit_3band = QPushButton("Calculate")
        self.layout_3band.addRow(self.submit_3band)
        self.submit_3band.clicked.connect(self.result3band)

        #Display layout for 3 band tab
        self.tab_3band.setLayout(self.layout_3band)

    def tab_4band_UI(self):
        #Form layout_4band for Input
        self.layout_4band = QFormLayout()

        #Gather all option of resistor color for 4 band resistor
        self.band1_4band = self.getColor()
        self.band2_4band = self.getColor()
        self.band3_4band = self.getColor()
        self.band4_4band = self.getToleranceColor()
        self.layout_4band.addRow(QLabel("Band 1:"), self.band1_4band)
        self.layout_4band.addRow(QLabel("Band 2:"), self.band2_4band)
        self.layout_4band.addRow(QLabel("Band 3 (Multiplier):"), self.band3_4band)
        self.layout_4band.addRow(QLabel("Band 4 (Tolerance):"), self.band4_4band)

        #Submit button for 4 band resistor
        self.submit_4band = QPushButton("Calculate")
        self.layout_4band.addRow(self.submit_4band)
        self.submit_4band.clicked.connect(self.result4band)

        #Display layout for 4 band tab
        self.tab_4band.setLayout(self.layout_4band)

    def tab_5band_UI(self):
        #Form layout_5band for Input
        self.layout_5band = QFormLayout()

        #Gather all option of resistor color for 5 band resistor
        self.band1_5band = self.getColor()
        self.band2_5band = self.getColor()
        self.band3_5band = self.getColor()
        self.band4_5band = self.getColor()
        self.band5_5band = self.getToleranceColor()
        self.layout_5band.addRow(QLabel("Band 1:"), self.band1_5band)
        self.layout_5band.addRow(QLabel("Band 2:"), self.band2_5band)
        self.layout_5band.addRow(QLabel("Band 3:"), self.band3_5band)
        self.layout_5band.addRow(QLabel("Band 4 (Multiplier):"), self.band4_5band)
        self.layout_5band.addRow(QLabel("Band 5 (Tolerance):"), self.band5_5band)

        #Submit button for 5 band resistor
        self.submit_5band = QPushButton("Calculate")
        self.layout_5band.addRow(self.submit_5band)
        self.submit_5band.clicked.connect(self.result5band)

        #Display layout for 5 band tab
        self.tab_5band.setLayout(self.layout_5band)

    #Function to display all option for color resistor
    def getColor(self):
        colors = QComboBox()
        for color in colors_band:
            colors.addItem(color[0])
        return colors

    #Function to display all option for tolerance color resistor
    def getToleranceColor(self):
        colors = QComboBox()
        for color in tolerance_band:
            colors.addItem(color[0])
        return colors

    #Function to calculate 3 band resistor if submitted
    @pyqtSlot()
    def result3band(self):
        #Get all color band value
        band1value_3band = calculateResistor.findValue(self,self.band1_3band.currentText())
        band2value_3band = calculateResistor.findValue(self,self.band2_3band.currentText())
        band3value_3band = calculateResistor.findValue(self,self.band3_3band.currentText())

        #Calculate output 3 band resistor value
        self.output_3band = int(str(band1value_3band)+str(band2value_3band))*(10**band3value_3band)

        #Show result for 3 band resistor
        #Note: Resistor tolerance value maybe differ between many resources, so it won't be accurate. You can ignore it.
        #Source is in operator.py file
        msg_3band = QMessageBox()
        msg_3band.setWindowTitle("Result 3 Band Resistor")
        msg_3band.setText(
            'Result : \n\n'+\
            str(self.output_3band)+' \u03A9 \n'+ \
            str(self.output_3band/1000)+' k'+'\u03A9 \n'+ \
            str(self.output_3band/10**6)+' M'+'\u03A9 \n\n'+ \
            'Band 1: '+ self.band1_3band.currentText()+' [ Value: ' + str(band1value_3band) + ' ]\n' + \
            'Band 2: '+ self.band2_3band.currentText()+' [ Value: ' + str(band2value_3band) + ' ]\n' + \
            'Band 3: '+ self.band3_3band.currentText()+' [ Value: ' + '10^'+ str(band3value_3band) + ' ]'
            )
        msg_3band.exec_()

    #Function to calculate 4 band resistor if submitted
    @pyqtSlot()
    def result4band(self):
        #Get all color band value
        band1value_4band = calculateResistor.findValue(self,self.band1_4band.currentText())
        band2value_4band = calculateResistor.findValue(self,self.band2_4band.currentText())
        band3value_4band = calculateResistor.findValue(self,self.band3_4band.currentText())
        band4value_4band = calculateResistor.findTolerance(self,self.band4_4band.currentText())

        #Calculate output and range 4 band resistor value
        self.output_4band = int(str(band1value_4band)+str(band2value_4band))*(10**band3value_4band)
        self.range_4band = [self.output_4band-(self.output_4band*band4value_4band),self.output_4band+(self.output_4band*band4value_4band)]

        #Show result for 4 band resistor
        #Note: Resistor tolerance value maybe differ between many resources, so it won't be accurate. You can ignore it.
        #Source is in operator.py file
        msg_4band = QMessageBox()
        msg_4band.setWindowTitle("Result 4 Band Resistor")
        msg_4band.setText(
            'Result : \n'+\
            str(self.output_4band)+' \u03A9 \n'+ \
            str(self.output_4band/1000)+' k\u03A9 '+'\n'+ \
            str(self.output_4band/10**6)+' M\u03A9 \n\n'+ \
            'Range : \n'+\
            '[ ' + str(self.range_4band[0])+' , ' + str(self.range_4band[1]) +' ] \u03A9 \n'+ \
            '[ ' + str(self.range_4band[0]/1000)+' , ' + str(self.range_4band[1]/1000) +' ] k\u03A9 \n'+ \
            '[ ' + str(self.range_4band[0]/10**6)+' , ' + str(self.range_4band[1]/10**6) +' ] M\u03A9 \n\n'+ \
            'Details : \n'+\
            'Band 1: '+ self.band1_4band.currentText()+' [ Value: ' + str(band1value_4band) + ' ]\n' + \
            'Band 2: '+ self.band2_4band.currentText()+' [ Value: ' + str(band2value_4band) + ' ]\n' + \
            'Band 3: '+ self.band3_4band.currentText()+' [ Multiplier: ' + '10^'+ str(band3value_4band) + ' ]\n' + \
            'Band 4: '+ self.band4_4band.currentText()+' [ Tolerance: \u00b1' + str(band4value_4band*100) + '% ]\n'
            )
        msg_4band.exec_()

    #Function to calculate 5 band resistor if submitted
    @pyqtSlot()
    def result5band(self):
        #Get all color band value
        band1value_5band = calculateResistor.findValue(self,self.band1_5band.currentText())
        band2value_5band = calculateResistor.findValue(self,self.band2_5band.currentText())
        band3value_5band = calculateResistor.findValue(self,self.band3_5band.currentText())
        band4value_5band = calculateResistor.findValue(self,self.band4_5band.currentText())
        band5value_5band = calculateResistor.findTolerance(self,self.band5_5band.currentText())

        #Calculate output and range 5 band resistor value
        self.output_5band = int(str(band1value_5band)+str(band2value_5band)+str(band3value_5band))*(10**band4value_5band)
        self.range_5band = [self.output_5band-(self.output_5band*band5value_5band),self.output_5band+(self.output_5band*band5value_5band)]

        #Show result for 5 band resistor
        #Note: Resistor tolerance value maybe differ between many resources, so it won't be accurate. You can ignore it.
        #Source is in operator.py file
        msg_5band = QMessageBox()
        msg_5band.setWindowTitle("Result 5 Band Resistor")
        msg_5band.setText(
            'Result : \n'+\
            str(self.output_5band)+' \u03A9 \n'+ \
            str(self.output_5band/1000)+' k\u03A9 '+'\n'+ \
            str(self.output_5band/10**6)+' M\u03A9 \n\n'+ \
            'Range : \n'+\
            '[ ' + str(self.range_5band[0])+' , ' + str(self.range_5band[1]) +' ] \u03A9 \n'+ \
            '[ ' + str(self.range_5band[0]/1000)+' , ' + str(self.range_5band[1]/1000) +' ] k\u03A9 \n'+ \
            '[ ' + str(self.range_5band[0]/10**6)+' , ' + str(self.range_5band[1]/10**6) +' ] M\u03A9 \n\n'+ \
            'Details : \n'+\
            'Band 1: '+ self.band1_5band.currentText()+' [ Value: ' + str(band1value_5band) + ' ]\n' + \
            'Band 2: '+ self.band2_5band.currentText()+' [ Value: ' + str(band2value_5band) + ' ]\n' + \
            'Band 3: '+ self.band3_5band.currentText()+' [ Value: ' + str(band3value_5band) + ' ]\n' + \
            'Band 4: '+ self.band4_5band.currentText()+' [ Multiplier: ' + '10^'+ str(band4value_5band) + ' ]\n' + \
            'Band 5: '+ self.band5_5band.currentText()+' [ Tolerance: \u00b1' + str(band5value_5band*100) + '% ]\n'
            )
        msg_5band.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
