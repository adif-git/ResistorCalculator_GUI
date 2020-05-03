# colors_band = [COLOR, BAND_VALUE, TOLERANCE], for undefined value will be 0 by default
# Source = https://www.allaboutcircuits.com/tools/resistor-color-code-calculator/
# Note : Resistor tolerance value maybe differ between many resources, so it won't be accurate
colors_band = [['Black',0,0],
                ['Brown',1,0.01],
                ['Red',2,0.02],
                ['Orange',3,0.03],
                ['Yellow',4,0.04],
                ['Green',5,0.005],
                ['Blue',6,0.0025],
                ['Violet',7,0.001],
                ['Gray',8,0.0005],
                ['White',9,0]]

#tolerance_band will be from BROWN until GRAY with addition GOLD and SILVER
tolerance_band = colors_band[1:9]+[['Gold',0,0.05],['Silver',0,0.1]]

class calculateResistor:
    def __init__(self):
        self.value = None
        self.result= []

    #To find value for 1,2,3 band of color band
    def findValue(self,color):
        for sublist in colors_band:
            if sublist[0] == color:
                self.value = sublist[1]
                return self.value
                break

    #To find value of tolerance of color band
    def findTolerance(self,color):
        for sublist in tolerance_band:
            if sublist[0] == color:
                self.value = sublist[2]
                return self.value
                break
