# -*- coding: utf-8 -*-
from Tkinter import *
import tkFileDialog
#from tkinter import filedialog
import tkMessageBox
from cls_mkparser import markdownParser

# Interface Classe mit TkInter
class interface:
    def __init__(self):

        # Initialisiere den Parser
        self.parser = markdownParser()

        # Erstelle die Grundlage des Interfaces
        self.root = Tk()
        self.root.wm_title("Markdown Parser")

        # Erstelle das Interface
        self.makeInterface(self.root)

    def makeInterface(self,master):

        # Größe und Skalierung des Interfaces festlegen und bauen
        Grid.rowconfigure(master,1,weight=1,minsize=10)
        Grid.rowconfigure(master, 2, weight=1,minsize=10)
        Grid.rowconfigure(master, 3, weight=1,minsize=10)
        Grid.rowconfigure(master, 4, weight=1,minsize=10)
        Grid.columnconfigure(master, 0, weight=1,minsize=10)
        Grid.columnconfigure(master, 1, minsize=10)

        self.label = Label(master,text="Markdown Parser")
        self.label.grid(row=0,columnspan=2)

        # Textfeld bauen und standard Text einfügen
        self.einf_textfeld = Text(master, height=5, width=50)
        self.einf_textfeld.grid(row=1, column=0,sticky=E+W+N+S,rowspan=2)
        self.einf_textfeld.insert(END, "Fügen sie hier ihren Text ein!")

        self.ausg_textfeld = Text(master, height=5, width=50)
        self.ausg_textfeld.grid(row=3, column=0,sticky=E+W+N+S,rowspan=2)
        self.ausg_textfeld.insert(END, "Hier erscheint der geparste Text")

        # Pars-Button und Ende-Button erstellen
        self.buttonParse = Button(master, text="Parse Textfeld", command=self.parseText)
        self.buttonParse.grid(row=1, column=1,sticky=E+W)

        self.buttonOpenFile = Button(master,text="Wähle Datei",command=self.openFile)
        self.buttonOpenFile.grid(row=2, column=1,sticky=E+W)

        self.buttonParseFile = Button(master, text="Parse Datei", command=self.parseToFile)
        self.buttonParseFile.grid(row=3, column=1,sticky=E+W)
        self.buttonParseFile.config(state=DISABLED)

        self.buttonQuit = Button(master, text="Ende", command=quit, fg="red")
        self.buttonQuit.grid(row=4, column=1, sticky=E+W)


        #Darstellung starten
        mainloop()

    def parseText(self):
        # Leere Ausgabetextfeld
        self.ausg_textfeld.delete("1.0",END)

        # Lese Eingabetextfeld und erkennen der Zeilen
        eingabe = self.einf_textfeld.get("1.0", END)
        zeilen = eingabe.split("\n")

        #Parse jede zeile einzeln und Zeige das Ergebniss im Ausgabetextfeld an
        for zeile in zeilen:
            self.ausg_textfeld.insert(END,self.parser.parse(zeile)+"\n")
            print self.parser.parse(zeile)

    def openFile(self):
        #Auswählen der Datei, öffnen und in das Eingabetextfeld schreiben
        path = tkFileDialog.askopenfilename()
        if path != "":

            # Aktivieren des "Parse Datei" Buttons
            self.buttonParseFile.config(state=NORMAL)
            datei = open(path,"r")
            # Leeren des Eingabetextefeldes und einfügen des Dateinhalts
            self.einf_textfeld.delete("1.0", END)
            for line in datei:
                self.einf_textfeld.insert(END,line)


    def parseToFile(self):

        # Wählen der Zieldatei
        path = tkFileDialog.asksaveasfilename()

        # Leerer geparster Text
        parsed_text = ""

        # Einlesen des Eingabetextefeldes
        eingabe = self.einf_textfeld.get("1.0", END)
        zeilen = eingabe.split("\n")

        # Parsen jeder Zeile und zusammensetzen des geparsten Textes
        for zeile in zeilen:
            parsed_text = parsed_text +  self.parser.parse(zeile) + "\n"

        # Schreiben in die gewählte Ausgabedatei
        datei = open(path,"w")
        datei.write(parsed_text)

        # Anzeigen der Nachricht
        tkMessageBox.showinfo("Gespeichert","Die Datei wurde unter "+ path + " gespeichert!")

