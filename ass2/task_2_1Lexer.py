# Generated from task_2_1.g4 by ANTLR 4.5.3
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\t")
        buf.write("J\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\3\2\6\2\23\n\2\r\2\16\2\24\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\"\n\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\5\4,\n\4\3\5\3\5\3\5\3\5\3\5\3\6\6\6\64")
        buf.write("\n\6\r\6\16\6\65\3\6\6\69\n\6\r\6\16\6:\3\6\5\6>\n\6\3")
        buf.write("\7\3\7\3\7\3\7\3\b\6\bE\n\b\r\b\16\bF\3\b\3\b\2\2\t\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\3\2\5\4\2\f\f\17\17\3\2\62")
        buf.write(";\5\2\13\f\17\17\"\"S\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\3\22\3\2\2\2\5!\3\2\2\2\7+\3\2\2\2\t-\3\2\2\2\13=\3\2")
        buf.write("\2\2\r?\3\2\2\2\17D\3\2\2\2\21\23\t\2\2\2\22\21\3\2\2")
        buf.write("\2\23\24\3\2\2\2\24\22\3\2\2\2\24\25\3\2\2\2\25\26\3\2")
        buf.write("\2\2\26\27\b\2\2\2\27\4\3\2\2\2\30\31\7C\2\2\31\32\7C")
        buf.write("\2\2\32\"\7C\2\2\33\34\7C\2\2\34\35\7F\2\2\35\"\7F\2\2")
        buf.write("\36\37\7K\2\2\37 \7P\2\2 \"\7E\2\2!\30\3\2\2\2!\33\3\2")
        buf.write("\2\2!\36\3\2\2\2\"\6\3\2\2\2#$\7C\2\2$,\7Z\2\2%&\7D\2")
        buf.write("\2&,\7Z\2\2\'(\7E\2\2(,\7Z\2\2)*\7F\2\2*,\7Z\2\2+#\3\2")
        buf.write("\2\2+%\3\2\2\2+\'\3\2\2\2+)\3\2\2\2,\b\3\2\2\2-.\7]\2")
        buf.write("\2./\7C\2\2/\60\7Z\2\2\60\61\7_\2\2\61\n\3\2\2\2\62\64")
        buf.write("\t\3\2\2\63\62\3\2\2\2\64\65\3\2\2\2\65\63\3\2\2\2\65")
        buf.write("\66\3\2\2\2\66>\3\2\2\2\679\4\62\63\28\67\3\2\2\29:\3")
        buf.write("\2\2\2:8\3\2\2\2:;\3\2\2\2;<\3\2\2\2<>\7d\2\2=\63\3\2")
        buf.write("\2\2=8\3\2\2\2>\f\3\2\2\2?@\7.\2\2@A\3\2\2\2AB\b\7\2\2")
        buf.write("B\16\3\2\2\2CE\t\4\2\2DC\3\2\2\2EF\3\2\2\2FD\3\2\2\2F")
        buf.write("G\3\2\2\2GH\3\2\2\2HI\b\b\2\2I\20\3\2\2\2\n\2\24!+\65")
        buf.write(":=F\3\b\2\2")
        return buf.getvalue()


class task_2_1Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    NEWLINE = 1
    COMMAND = 2
    REG = 3
    MEMORY = 4
    IMMEDIATE = 5
    COMMA = 6
    WS = 7

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','" ]

    symbolicNames = [ "<INVALID>",
            "NEWLINE", "COMMAND", "REG", "MEMORY", "IMMEDIATE", "COMMA", 
            "WS" ]

    ruleNames = [ "NEWLINE", "COMMAND", "REG", "MEMORY", "IMMEDIATE", "COMMA", 
                  "WS" ]

    grammarFileName = "task_2_1.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


