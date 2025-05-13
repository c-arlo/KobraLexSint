grammar Kobra;

programa : instruccion+ ;

instruccion
    : asignacion
    | condicion
    | ciclo
    | expresion
    ;

asignacion : ID ASIG expresion ;

condicion : IF PARI expresion PARD LLAVI instruccion LLAVD ;

ciclo : WHILE PARI expresion PARD LLAVI instruccion LLAVD ;

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
ID : [a-zA-Z][a-zA-Z0-9]* ;

IF : [IF] ;
WHILE : [WHILE] ;

ASIG : [=] ;
PARI : [(] ;
PARD : [)] ;
LLAVI : [{] ;
LLAVD : [}] ;

SUMA : [+] ;
REST : [-] ;
MULT : [*] ;
DIV : [/] ;
MAYR : [>] ;
MENR : [<] ;

WS : [ \t\r\n]+ -> skip ;