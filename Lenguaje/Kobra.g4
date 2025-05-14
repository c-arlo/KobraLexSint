grammar Kobra;

programa : instruccion+ ;

instruccion
    : asignacion
    | condicion
    | ciclo
    | expresion
    ;

asignacion : ID ASIG expresion ;

condicion : 'SI' '(' expresion ')' '{' instruccion+ '}' ;

ciclo : 'MIENTRAS' '(' expresion ')' '{' instruccion+ '}' ;

expresion
    : expresion oper expresion
    | '(' expresion ')'
    | NUM
    | ID
    ;

oper
    : SUMA
    | REST
    | MULT
    | DIV
    | MAYR
    | MENR
    ;

NUM : [0-9]+ ;
ID : [a-zA-Z][a-zA-Z0-9_]* ;

ASIG : [=] ;
SUMA : [+] ;
REST : [-] ;
MULT : [*] ;
DIV : [/] ;
MAYR : [>] ;
MENR : [<] ;

WS : [ \t\r\n]+ -> skip ;