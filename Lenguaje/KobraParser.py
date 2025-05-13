# Generated from Kobra.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,18,66,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,4,0,16,8,0,11,0,12,0,17,1,1,1,1,1,1,1,1,3,1,24,8,1,1,2,1,2,
        1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,53,8,5,1,5,1,5,1,5,1,5,5,
        5,59,8,5,10,5,12,5,62,9,5,1,6,1,6,1,6,0,1,10,7,0,2,4,6,8,10,12,0,
        1,1,0,12,17,65,0,15,1,0,0,0,2,23,1,0,0,0,4,25,1,0,0,0,6,29,1,0,0,
        0,8,37,1,0,0,0,10,52,1,0,0,0,12,63,1,0,0,0,14,16,3,2,1,0,15,14,1,
        0,0,0,16,17,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,1,1,0,0,0,19,
        24,3,4,2,0,20,24,3,6,3,0,21,24,3,8,4,0,22,24,3,10,5,0,23,19,1,0,
        0,0,23,20,1,0,0,0,23,21,1,0,0,0,23,22,1,0,0,0,24,3,1,0,0,0,25,26,
        5,4,0,0,26,27,5,7,0,0,27,28,3,10,5,0,28,5,1,0,0,0,29,30,5,5,0,0,
        30,31,5,8,0,0,31,32,3,10,5,0,32,33,5,9,0,0,33,34,5,10,0,0,34,35,
        3,2,1,0,35,36,5,11,0,0,36,7,1,0,0,0,37,38,5,6,0,0,38,39,5,8,0,0,
        39,40,3,10,5,0,40,41,5,9,0,0,41,42,5,10,0,0,42,43,3,2,1,0,43,44,
        5,11,0,0,44,9,1,0,0,0,45,46,6,5,-1,0,46,47,5,1,0,0,47,48,3,10,5,
        0,48,49,5,2,0,0,49,53,1,0,0,0,50,53,5,3,0,0,51,53,5,4,0,0,52,45,
        1,0,0,0,52,50,1,0,0,0,52,51,1,0,0,0,53,60,1,0,0,0,54,55,10,4,0,0,
        55,56,3,12,6,0,56,57,3,10,5,5,57,59,1,0,0,0,58,54,1,0,0,0,59,62,
        1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,11,1,0,0,0,62,60,1,0,0,0,
        63,64,7,0,0,0,64,13,1,0,0,0,4,17,23,52,60
    ]

class KobraParser ( Parser ):

    grammarFileName = "Kobra.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "NUM", "ID", 
                      "IF", "WHILE", "ASIG", "PARI", "PARD", "LLAVI", "LLAVD", 
                      "SUMA", "REST", "MULT", "DIV", "MAYR", "MENR", "WS" ]

    RULE_programa = 0
    RULE_instruccion = 1
    RULE_asignacion = 2
    RULE_condicion = 3
    RULE_ciclo = 4
    RULE_expresion = 5
    RULE_oper = 6

    ruleNames =  [ "programa", "instruccion", "asignacion", "condicion", 
                   "ciclo", "expresion", "oper" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    NUM=3
    ID=4
    IF=5
    WHILE=6
    ASIG=7
    PARI=8
    PARD=9
    LLAVI=10
    LLAVD=11
    SUMA=12
    REST=13
    MULT=14
    DIV=15
    MAYR=16
    MENR=17
    WS=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KobraParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(KobraParser.InstruccionContext,i)


        def getRuleIndex(self):
            return KobraParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = KobraParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.instruccion()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 122) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(KobraParser.AsignacionContext,0)


        def condicion(self):
            return self.getTypedRuleContext(KobraParser.CondicionContext,0)


        def ciclo(self):
            return self.getTypedRuleContext(KobraParser.CicloContext,0)


        def expresion(self):
            return self.getTypedRuleContext(KobraParser.ExpresionContext,0)


        def getRuleIndex(self):
            return KobraParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)




    def instruccion(self):

        localctx = KobraParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruccion)
        try:
            self.state = 23
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.asignacion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.condicion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 21
                self.ciclo()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 22
                self.expresion(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(KobraParser.ID, 0)

        def ASIG(self):
            return self.getToken(KobraParser.ASIG, 0)

        def expresion(self):
            return self.getTypedRuleContext(KobraParser.ExpresionContext,0)


        def getRuleIndex(self):
            return KobraParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)




    def asignacion(self):

        localctx = KobraParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(KobraParser.ID)
            self.state = 26
            self.match(KobraParser.ASIG)
            self.state = 27
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(KobraParser.IF, 0)

        def PARI(self):
            return self.getToken(KobraParser.PARI, 0)

        def expresion(self):
            return self.getTypedRuleContext(KobraParser.ExpresionContext,0)


        def PARD(self):
            return self.getToken(KobraParser.PARD, 0)

        def LLAVI(self):
            return self.getToken(KobraParser.LLAVI, 0)

        def instruccion(self):
            return self.getTypedRuleContext(KobraParser.InstruccionContext,0)


        def LLAVD(self):
            return self.getToken(KobraParser.LLAVD, 0)

        def getRuleIndex(self):
            return KobraParser.RULE_condicion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicion" ):
                listener.enterCondicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicion" ):
                listener.exitCondicion(self)




    def condicion(self):

        localctx = KobraParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_condicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(KobraParser.IF)
            self.state = 30
            self.match(KobraParser.PARI)
            self.state = 31
            self.expresion(0)
            self.state = 32
            self.match(KobraParser.PARD)
            self.state = 33
            self.match(KobraParser.LLAVI)
            self.state = 34
            self.instruccion()
            self.state = 35
            self.match(KobraParser.LLAVD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CicloContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(KobraParser.WHILE, 0)

        def PARI(self):
            return self.getToken(KobraParser.PARI, 0)

        def expresion(self):
            return self.getTypedRuleContext(KobraParser.ExpresionContext,0)


        def PARD(self):
            return self.getToken(KobraParser.PARD, 0)

        def LLAVI(self):
            return self.getToken(KobraParser.LLAVI, 0)

        def instruccion(self):
            return self.getTypedRuleContext(KobraParser.InstruccionContext,0)


        def LLAVD(self):
            return self.getToken(KobraParser.LLAVD, 0)

        def getRuleIndex(self):
            return KobraParser.RULE_ciclo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCiclo" ):
                listener.enterCiclo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCiclo" ):
                listener.exitCiclo(self)




    def ciclo(self):

        localctx = KobraParser.CicloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ciclo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(KobraParser.WHILE)
            self.state = 38
            self.match(KobraParser.PARI)
            self.state = 39
            self.expresion(0)
            self.state = 40
            self.match(KobraParser.PARD)
            self.state = 41
            self.match(KobraParser.LLAVI)
            self.state = 42
            self.instruccion()
            self.state = 43
            self.match(KobraParser.LLAVD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KobraParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(KobraParser.ExpresionContext,i)


        def NUM(self):
            return self.getToken(KobraParser.NUM, 0)

        def ID(self):
            return self.getToken(KobraParser.ID, 0)

        def oper(self):
            return self.getTypedRuleContext(KobraParser.OperContext,0)


        def getRuleIndex(self):
            return KobraParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = KobraParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expresion, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 46
                self.match(KobraParser.T__0)
                self.state = 47
                self.expresion(0)
                self.state = 48
                self.match(KobraParser.T__1)
                pass
            elif token in [3]:
                self.state = 50
                self.match(KobraParser.NUM)
                pass
            elif token in [4]:
                self.state = 51
                self.match(KobraParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 60
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = KobraParser.ExpresionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                    self.state = 54
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 55
                    self.oper()
                    self.state = 56
                    self.expresion(5) 
                self.state = 62
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OperContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUMA(self):
            return self.getToken(KobraParser.SUMA, 0)

        def REST(self):
            return self.getToken(KobraParser.REST, 0)

        def MULT(self):
            return self.getToken(KobraParser.MULT, 0)

        def DIV(self):
            return self.getToken(KobraParser.DIV, 0)

        def MAYR(self):
            return self.getToken(KobraParser.MAYR, 0)

        def MENR(self):
            return self.getToken(KobraParser.MENR, 0)

        def getRuleIndex(self):
            return KobraParser.RULE_oper

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOper" ):
                listener.enterOper(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOper" ):
                listener.exitOper(self)




    def oper(self):

        localctx = KobraParser.OperContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_oper)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 258048) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         




