# лексический анализ
import ply.lex as lex

tokens = ("TYPE", "ASSIGN", "IDENTIFIER", "CONSTANT", "BINARY_PLUS", "BINARY_UNARY_MINUS", "BINARY_MULTIPLY", "BINARY_DIVIDE", "LEFT_BRACKET", "RIGHT_BRACKET", "COMMA", "SEMICOLON")

t_TYPE = """Var"""
t_ASSIGN = """="""
t_IDENTIFIER = """[a-z]+"""
t_CONSTANT = """[0-9]+"""
t_BINARY_PLUS = """\+"""
t_BINARY_UNARY_MINUS = """-"""
t_BINARY_MULTIPLY = """\*"""
t_BINARY_DIVIDE = """/"""
t_LEFT_BRACKET = """\("""
t_RIGHT_BRACKET = """\)"""
t_COMMA = ""","""
t_SEMICOLON = """;"""

t_ignore = " \r\t\f"

lexicalResult = []

def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += len(t.value)

def t_error(t):
    global lexicalResult
    lexicalResult.append(("ERROR", t.value, t.lineno))
    t.lexer.skip(1)

lexer = lex.lex()

# лексический анализ анализирует
def analyze(data):
    lexer.input(data)
    global lexicalResult
    lexicalResult = []
    while True:
        # читаем следующий токен
        t = lexer.token()
        # закончились токены
        if not t:
            break
        lexicalResult.append((t.type, t.value, t.lineno))
    return lexicalResult
