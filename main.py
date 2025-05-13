from antlr4 import *
from antlr4.tree.Tree import TerminalNodeImpl
from Lenguaje import KobraLexer
from Lenguaje import KobraParser

def imprimir_arbol(node, parser, indent=0):
    if isinstance(node, TerminalNodeImpl):
        print("  " * indent + f"'{node.getText()}'")
    else:
        rule_name = parser.ruleNames[node.getRuleIndex()]
        print("  " * indent + f"<{rule_name}>")
        for child in node.children or []:
            imprimir_arbol(child, parser, indent + 1)

if __name__ == '__main__':
    input_stream = InputStream(input("> "))
    lexer = KobraLexer.KobraLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    print("--- TOKENS IDENTIFICADOS ---")

    token_stream.fill()
    for token in token_stream.tokens:
        print(f"'{token.text}'")

    parser = KobraParser.KobraParser(token_stream)
    tree = parser.programa()

    print("\n--- ARBOL SINTACTICO ----")

    print(tree.toStringTree(recog=parser))
    imprimir_arbol(tree, parser)
