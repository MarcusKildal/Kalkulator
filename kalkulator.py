#Dette er en kalkulattor og dette er mine koder med hjelp av nette
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

qtCreatorFile = "kaklulator.ui" #her sier du til QT hvilket annet program den skal sende beskjer til
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QMainWindow, Ui_MainWindow): # Det som står før (self.) går til QT programmet, mens det som står i (Self.) går til definisjonene under.
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #funksjonene
        self.KnappPluss.clicked.connect(self.PlussTrykket)
        self.KnappMinus.clicked.connect(self.MinusTrykket)
        self.KnappGange.clicked.connect(self.GangeTrykket)
        self.KnappDele.clicked.connect(self.DeleTrykket)
        self.KnappRot.clicked.connect(self.RotTrykket)
        self.KnappKvadratet.clicked.connect(self.KvadratTrykket)
        self.KnappProsent.clicked.connect(self.ProsentTrykket)
        self.KnappRs.clicked.connect(self.RSTrykket)
        #tallene
        self.KnappNi.clicked.connect(self.NiTrykket)
        self.KnappAAtte.clicked.connect(self.AAtteTrykket)
        self.KnappSju.clicked.connect(self.SjuTrykket)
        self.KnappSeks.clicked.connect(self.SeksTrykket)
        self.KnappFem.clicked.connect(self.FemTrykket)
        self.KnappFire.clicked.connect(self.FireTrykket)
        self.KnappTre.clicked.connect(self.TreTrykket)
        self.KnappTo.clicked.connect(self.ToTrykket)
        self.KnappEn.clicked.connect(self.EnTrykket)
        self.Knapp_Null.clicked.connect(self.NullTrykket)

    #funksjonene
    def PlussTrykket(self): #det er her selve regnestyket blir til og sier vilken knapp den sakl sende meldingen til
        TallEn = float(self.Tall_en.toPlainText())
        TallTo = float(self.Tall_to.toPlainText())
        Resultat = TallEn + TallTo 
        self.Svar.display(Resultat)


    def MinusTrykket(self):
        TallEn = float(self.Tall_en.toPlainText())
        TallTo = float(self.Tall_to.toPlainText())
        Resultat = TallEn - TallTo 
        self.Svar.display(Resultat)


    def GangeTrykket(self):
        TallEn = float(self.Tall_en.toPlainText())
        TallTo = float(self.Tall_to.toPlainText())
        if TallEn == TallTo:
            self.Svar.display("Error")
        else:
            Resultat = TallEn * TallTo 
            self.Svar.display(Resultat)


    def DeleTrykket(self):
        TallEn = float(self.Tall_en.toPlainText())
        TallTo = float(self.Tall_to.toPlainText())
        if TallTo == 0:
            self.Svar.display("Error")
        else:
            Resultat = TallEn / TallTo
            self.Svar.display(Resultat)


    def RotTrykket(self):
        TallEn = float(self.Tall_en.toPlainText())
        Resultat = TallEn **0.5
        self.Svar.display(Resultat)

    def  KvadratTrykket(self):
        TallEn = float(self.Tall_en.toPlainText())
        TallTo = float(self.Tall_to.toPlainText())
        Resultat = TallEn ** TallTo 
        self.Svar.display(Resultat)

    def  ProsentTrykket(self):
        TallEn = float(self.Tall_en.toPlainText())
        TallTo = float(self.Tall_to.toPlainText())
        Resultat = TallEn /100 * TallTo
        self.Svar.display(Resultat)
    

    def RSTrykket(self):
        Resultat = 0
        self.Svar.display(Resultat)
    #tallene
    def NiTrykket(self):
        x = self.Svar.intValue()
        Resultat = x * 10 + 9
        self.Svar.display(Resultat)

    def AAtteTrykket(self):
        x = self.Svar.intValue()
        Resultat = x * 10 + 8
        self.Svar.display(Resultat)

    def SjuTrykket(self):
        x = self.Svar.intValue()
        Resultat = x * 10 + 7
        self.Svar.display(Resultat)
    
    def SeksTrykket(self):
        x = self.Svar.intValue()
        Resultat = x * 10 + 6
        self.Svar.display(Resultat)

    def FemTrykket(self):
        x = self.Svar.intValue()
        Resultat = x * 10 + 5
        self.Svar.display(Resultat)

    def FireTrykket(self):
        x = self.Svar.intValue()
        Resultat = x * 10 + 4
        self.Svar.display(Resultat)

    def TreTrykket(self):
        x = self.Svar.intValue()
        Resultat = x * 10 + 3
        self.Svar.display(Resultat)

    def ToTrykket(self):
        x = self.Svar.intValue()
        Resultat = x * 10 + 2
        self.Svar.display(Resultat)

    def EnTrykket(self):
        x = self.Svar.intValue()
        Resultat = x * 10 + 1
        self.Svar.display(Resultat)
    
    def NullTrykket(self):
        x = self.Svar.intValue()
        Resultat = x * 10 + 0
        self.Svar.display(Resultat)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
