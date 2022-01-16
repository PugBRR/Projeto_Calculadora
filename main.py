import gi
from Calculos import calculos

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

Builder = Gtk.Builder()
Builder.add_from_file('ui.glade')


class Manipulador:


    def __init__(self):
        self.operacao = None
        self.calc = calculos()
    
    def on_main_window_destroy(self, window):
        Gtk.main_quit()

    def on_btreset_clicked(self, button):
        Builder.get_object("visor").set_text("0")

    def on_btdigito_clicked(self, btdigito):
        if Builder.get_object("visor").get_text() == "0":
            Builder.get_object("visor").set_text(str(btdigito.get_label()))
        else:
            Builder.get_object("visor").set_text(str(Builder.get_object("visor").get_text() + btdigito.get_label()))

    def on_btvirgula_clicked(self, btvirgula):
        Builder.get_object("visor").set_text(str(Builder.get_object("visor").get_text() + btvirgula.get_label()))

    def on_btmaisoumenos_clicked(self, btmaisoumenos):
        valor1 = float(Builder.get_object("visor").get_text())
        valor2 = valor1 * -1
        Builder.get_object("visor").set_text(str(valor2))

    def on_btmais_clicked(self, button):
        self.operacao = "soma"
        Builder.get_object("visor").set_text(str(Builder.get_object("visor").get_text() + " " + "+" + " "))

    def on_btmenos_clicked(self, button):
        self.operacao = "subtracao"
        Builder.get_object("visor").set_text(str(Builder.get_object("visor").get_text() + " " + "-" + " "))

    def on_btmultiplicacao_clicked(self, button):
        self.operacao = "multiplicacao"
        Builder.get_object("visor").set_text(str(Builder.get_object("visor").get_text() + " " + "*" + " "))

    def on_btdivisao_clicked(self, button):
        self.operacao = "divisao"
        Builder.get_object("visor").set_text(str(Builder.get_object("visor").get_text() + " " + "/" + " "))

    def on_btraiz_clicked(self, button):
        self.operacao = "raiz_quadrada"
        Builder.get_object("visor").set_text(str(Builder.get_object("visor").get_text() + " " + "²√" + " "))

    def on_btexpoente_clicked(self, button):
        self.operacao = "quadrado"
        Builder.get_object("visor").set_text(str(Builder.get_object("visor").get_text() + " " + "x²" + " "))

    def on_btporcentagem_clicked(self, button):
        txt = Builder.get_object("visor").get_text()
        x = txt.split()
        resultado = self.calc.funcoes["porcentagem"](float(x[0]), float(x[2]))
        Builder.get_object("visor").set_text("")
        Builder.get_object("visor").set_text(x[0] + " " + x[1] + " " + str(resultado))
        
    def on_btigual_clicked(self, button):
        if self.operacao == "raiz_quadrada" or self.operacao == "quadrado":
            txt = Builder.get_object("visor").get_text()
            x = txt.split()
            resultado = self.calc.funcoes[self.operacao](float(x[0]))
            Builder.get_object("visor").set_text(str(resultado))
        else:
            txt = Builder.get_object("visor").get_text()
            x = txt.split()
            resultado = self.calc.funcoes[self.operacao](float(x[0]), float(x[2]))
            Builder.get_object("visor").set_text(str(resultado)) 


Builder.connect_signals(Manipulador())
Window: Gtk.Window = Builder.get_object("main_window")
Window.show_all()
Gtk.main()
