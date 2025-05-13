# Generated from Kobra.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .KobraParser import KobraParser
else:
    from KobraParser import KobraParser

# This class defines a complete listener for a parse tree produced by KobraParser.
class KobraListener(ParseTreeListener):

    # Enter a parse tree produced by KobraParser#programa.
    def enterPrograma(self, ctx:KobraParser.ProgramaContext):
        pass

    # Exit a parse tree produced by KobraParser#programa.
    def exitPrograma(self, ctx:KobraParser.ProgramaContext):
        pass


    # Enter a parse tree produced by KobraParser#instruccion.
    def enterInstruccion(self, ctx:KobraParser.InstruccionContext):
        pass

    # Exit a parse tree produced by KobraParser#instruccion.
    def exitInstruccion(self, ctx:KobraParser.InstruccionContext):
        pass


    # Enter a parse tree produced by KobraParser#asignacion.
    def enterAsignacion(self, ctx:KobraParser.AsignacionContext):
        pass

    # Exit a parse tree produced by KobraParser#asignacion.
    def exitAsignacion(self, ctx:KobraParser.AsignacionContext):
        pass


    # Enter a parse tree produced by KobraParser#condicion.
    def enterCondicion(self, ctx:KobraParser.CondicionContext):
        pass

    # Exit a parse tree produced by KobraParser#condicion.
    def exitCondicion(self, ctx:KobraParser.CondicionContext):
        pass


    # Enter a parse tree produced by KobraParser#ciclo.
    def enterCiclo(self, ctx:KobraParser.CicloContext):
        pass

    # Exit a parse tree produced by KobraParser#ciclo.
    def exitCiclo(self, ctx:KobraParser.CicloContext):
        pass


    # Enter a parse tree produced by KobraParser#expresion.
    def enterExpresion(self, ctx:KobraParser.ExpresionContext):
        pass

    # Exit a parse tree produced by KobraParser#expresion.
    def exitExpresion(self, ctx:KobraParser.ExpresionContext):
        pass


    # Enter a parse tree produced by KobraParser#oper.
    def enterOper(self, ctx:KobraParser.OperContext):
        pass

    # Exit a parse tree produced by KobraParser#oper.
    def exitOper(self, ctx:KobraParser.OperContext):
        pass



del KobraParser