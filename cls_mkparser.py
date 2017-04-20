# -*- coding: utf-8 -*-
# Parser
class markdownParser:

    def __init__(self):
        self.para = False

    # Eigentliche Parsingfunktion, parste zeilenweise
    def parse(self, line):
        # Überschrift
        if line.find("#") != -1:
            if line.find('##') != -1:
                parts = line.split("##")
                newline = ""
                for part in parts[1:]:
                    newline = newline + part
                    newline = newline.rstrip()
                return "<h2>" + newline + "</h2>"
            else:
                parts = line.split("#")
                newline = ""
                for part in parts[1:]:
                    newline = newline + part
                    newline = newline.rstrip()
                return "<h1>" + newline + "</h1>"

        # Fett, Kursiv, Aufzählung
        elif line.find("*") != -1:
            if line.find('**') != -1:
                parts = line.split("**")

                newline = ""
                for part in parts[1:]:
                    newline = newline + part
                    newline = newline.rstrip()
                return "<b>" + newline + "</b>"
            else:
                parts = line.split("*")
                if len(parts) > 2:
                    newline = ""
                    for part in parts[1:]:
                        newline = newline + part
                        newline = newline.rstrip()
                    return "<i>" + newline + "</i>"
                else:
                    newline = ""
                    for part in parts[1:]:
                        newline = newline + part
                        newline = newline.rstrip()
                    return "<li>" + newline + "</li>"

        # Zitat, Paragraph
        elif line.find(">") != -1:
            parts = line.split(">")
            newline = ""
            for part in parts[1:]:
                newline = newline + part
                newline = newline.rstrip()
            return "<blockquote>" + newline + "</blockquote>"
        elif line == "" or line == "\n" and not self.para:
            self.para = True
            return "<p>"
        elif line == "" or line == "\n" and self.para:
            self.para = False
            return "</p>"
        else:
            return line.rstrip()

    # Dateianalyse für die Kommandozeilenfunktion
    def analysiereDatei(self, dateiname):
        try:
            parsed = ""
            datei = open(dateiname, "r")
            for line in datei:
                parsed = parsed + self.parse(line) + "\n"
            return parsed
        except IOError:
            print "File not Found!"
        except Exception as e:
            print e
