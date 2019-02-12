// test.g4 file
 grammar task_2_1;

NEWLINE     : [\r\n]+ -> skip;
COMMAND     : ('AAA' | 'ADD' | 'INC');
REG         : ('AX' | 'BX' | 'CX' | 'DX');
MEMORY      : ('[AX]') ;
IMMEDIATE   : [0-9]+ | ('0' | '1')+'b';
COMMA       : ',' -> skip;
WS : [ \t\r\n]+ -> skip ;

expr        : aaa | add | inc;

aaa         : COMMAND;

add         : COMMAND REG COMMA MEMORY
            | COMMAND MEMORY COMMA REG
            | COMMAND REG COMMA REG
            | COMMAND MEMORY COMMA IMMEDIATE
            | COMMAND REG COMMA IMMEDIATE
            ;

inc         : COMMAND REG
            | COMMAND MEMORY
            ;

start       : (expr NEWLINE)*;