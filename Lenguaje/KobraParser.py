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
        4,1,16,76,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,4,0,16,8,0,11,0,12,0,17,1,1,1,1,1,1,1,1,3,1,24,8,1,1,2,1,2,
        1,2,1,2,3,2,30,8,2,1,3,1,3,1,3,1,3,1,3,1,3,4,3,38,8,3,11,3,12,3,
        39,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,4,4,50,8,4,11,4,12,4,51,1,4,1,
        4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,63,8,5,1,5,1,5,1,5,1,5,5,5,69,
        8,5,10,5,12,5,72,9,5,1,6,1,6,1,6,0,1,10,7,0,2,4,6,8,10,12,0,1,1,
        0,10,15,78,0,15,1,0,0,0,2,23,1,0,0,0,4,29,1,0,0,0,6,31,1,0,0,0,8,
        43,1,0,0,0,10,62,1,0,0,0,12,73,1,0,0,0,14,16,3,2,1,0,15,14,1,0,0,
        0,16,17,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,1,1,0,0,0,19,24,3,
        4,2,0,20,24,3,6,3,0,21,24,3,8,4,0,22,24,3,10,5,0,23,19,1,0,0,0,23,
        20,1,0,0,0,23,21,1,0,0,0,23,22,1,0,0,0,24,3,1,0,0,0,25,26,5,8,0,
        0,26,27,5,9,0,0,27,30,3,10,5,0,28,30,5,8,0,0,29,25,1,0,0,0,29,28,
        1,0,0,0,30,5,1,0,0,0,31,32,5,1,0,0,32,33,5,2,0,0,33,34,3,10,5,0,
        34,35,5,3,0,0,35,37,5,4,0,0,36,38,3,2,1,0,37,36,1,0,0,0,38,39,1,
        0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,41,1,0,0,0,41,42,5,5,0,0,42,
        7,1,0,0,0,43,44,5,6,0,0,44,45,5,2,0,0,45,46,3,10,5,0,46,47,5,3,0,
        0,47,49,5,4,0,0,48,50,3,2,1,0,49,48,1,0,0,0,50,51,1,0,0,0,51,49,
        1,0,0,0,51,52,1,0,0,0,52,53,1,0,0,0,53,54,5,5,0,0,54,9,1,0,0,0,55,
        56,6,5,-1,0,56,57,5,2,0,0,57,58,3,10,5,0,58,59,5,3,0,0,59,63,1,0,
        0,0,60,63,5,7,0,0,61,63,5,8,0,0,62,55,1,0,0,0,62,60,1,0,0,0,62,61,
        1,0,0,0,63,70,1,0,0,0,64,65,10,4,0,0,65,66,3,12,6,0,66,67,3,10,5,
        5,67,69,1,0,0,0,68,64,1,0,0,0,69,72,1,0,0,0,70,68,1,0,0,0,70,71,
        1,0,0,0,71,11,1,0,0,0,72,70,1,0,0,0,73,74,7,0,0,0,74,13,1,0,0,0,
        7,17,23,29,39,51,62,70
    ]

class KobraParser ( Parser ):

    grammarFileName = "Kobra.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'SI'", "'('", "')'", "'{'", "'}'", "'MIENTRAS'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NUM", "ID", 
                      "ASIG", "SUMA", "REST", "MULT", "DIV", "MAYR", "MENR", 
                      "WS" ]

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
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    NUM=7
    ID=8
    ASIG=9
    SUMA=10
    REST=11
    MULT=12
    DIV=13
    MAYR=14
    MENR=15
    WS=16

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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 454) != 0)):
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
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.match(KobraParser.ID)
                self.state = 26
                self.match(KobraParser.ASIG)
                self.state = 27
                self.expresion(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.match(KobraParser.ID)
                pass


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

        def expresion(self):
            return self.getTypedRuleContext(KobraParser.ExpresionContext,0)


        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KobraParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(KobraParser.InstruccionContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(KobraParser.T__0)
            self.state = 32
            self.match(KobraParser.T__1)
            self.state = 33
            self.expresion(0)
            self.state = 34
            self.match(KobraParser.T__2)
            self.state = 35
            self.match(KobraParser.T__3)
            self.state = 37 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 36
                self.instruccion()
                self.state = 39 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 454) != 0)):
                    break

            self.state = 41
            self.match(KobraParser.T__4)
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

        def expresion(self):
            return self.getTypedRuleContext(KobraParser.ExpresionContext,0)


        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KobraParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(KobraParser.InstruccionContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(KobraParser.T__5)
            self.state = 44
            self.match(KobraParser.T__1)
            self.state = 45
            self.expresion(0)
            self.state = 46
            self.match(KobraParser.T__2)
            self.state = 47
            self.match(KobraParser.T__3)
            self.state = 49 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 48
                self.instruccion()
                self.state = 51 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 454) != 0)):
                    break

            self.state = 53
            self.match(KobraParser.T__4)
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
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.state = 56
                self.match(KobraParser.T__1)
                self.state = 57
                self.expresion(0)
                self.state = 58
                self.match(KobraParser.T__2)
                pass
            elif token in [7]:
                self.state = 60
                self.match(KobraParser.NUM)
                pass
            elif token in [8]:
                self.state = 61
                self.match(KobraParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 70
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = KobraParser.ExpresionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                    self.state = 64
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 65
                    self.oper()
                    self.state = 66
                    self.expresion(5) 
                self.state = 72
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
            self.state = 73
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 64512) != 0)):
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
         




