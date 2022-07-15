# синтаксический анализ
import ply.yacc as yacc
# получение токенов
from lexer import tokens

syntaxResult = []
lexicalResult = []
counter = 0

precedence = (('left', 'BINARY_PLUS', 'BINARY_UNARY_MINUS'), ('left', 'BINARY_MULTIPLY', 'BINARY_DIVIDE'))

good = "Хороший"
bad = "Плохой"

def p_error(p):
    global counter
    if p:
        syntaxResult.append((p.value, bad, lexicalResult[counter][2]))
    else:
        syntaxResult.append(("?", bad, lexicalResult[counter][2]))
    counter = counter + 1
    

def p_program(p):
    """program : declaringvariables descriptionofcalculations"""
    p[0] = str(p[1]) + str(p[2])

def p_declaringvariables(p):
    """declaringvariables : TYPE listofvariables SEMICOLON"""
    global counter
    p[0] = str(p[1]) + " " + str(p[2]) + "\n"
    syntaxResult.append((p[1], good, lexicalResult[counter][2]))
    counter = counter + 1
    syntaxResult.append((p[3], good, lexicalResult[counter][2]))
    counter = counter + 1

def p_listofvariables(p):
    """listofvariables : identifier COMMA listofvariables
                       | identifier"""
    global counter
    if (len(p) == 4):
        p[0] = str(p[1]) + str(p[2]) + " " + str(p[3])
        syntaxResult.append((p[2], good, lexicalResult[counter][2]))
        counter = counter + 1
    elif (len(p) == 2):
        p[0] = str(p[1])

def p_identifier(p):
    """identifier : IDENTIFIER"""
    global counter
    p[0] = str(p[1])
    syntaxResult.append((p[0], good, lexicalResult[counter][2]))
    counter = counter + 1

def p_descriptionofcalculations(p):
    """descriptionofcalculations : listofassignments"""
    p[0] = "Begin\n\t" + str(p[1]) + "\nEnd"

def p_listofassignments(p):
    """listofassignments : assignment listofassignments
                         | assignment"""
    if len(p) == 3:
        p[0] = str(p[1]) + "\n\t" + str(p[2])
    elif len(p) == 2:
        p[0] = str(p[1])

def p_assignment(p):
    """assignment : identifier ASSIGN expression"""
    global counter
    p[0] = str(p[1]) + " := " + str(p[3])
    syntaxResult.append((p[2], good, lexicalResult[counter][2]))
    counter = counter + 1

def p_expression(p):
    """expression : BINARY_UNARY_MINUS subexpression
                  | subexpression"""
    global counter
    if len(p) == 3:
        p[0] = "-" + str(p[2])
        syntaxResult.append((p[1], good, lexicalResult[counter][2]))
        counter = counter + 1
    elif len(p) == 2:
        p[0] = str(p[1])

def p_subexpression(p):
    """subexpression : LEFT_BRACKET expression RIGHT_BRACKET
                     | expression BINARY_PLUS expression
                     | expression BINARY_UNARY_MINUS expression
                     | expression BINARY_MULTIPLY expression
                     | expression BINARY_DIVIDE expression
                     | operand"""
    global counter
    if len(p) == 4:
        if p[1] == "(" and p[3] == ")":
            p[0] = str(p[1]) + str(p[2]) + str(p[3])
            syntaxResult.append((p[1], good, lexicalResult[counter][2]))
            counter = counter + 1
            syntaxResult.append((p[3], good, lexicalResult[counter][2]))
            counter = counter + 1
        elif p[2] == "+":
            p[0] = str(p[1]) + " " + str(p[2]) + " " + str(p[3])
            syntaxResult.append((p[2], good, lexicalResult[counter][2]))
            counter = counter + 1
        elif p[2] == "-":
            p[0] = str(p[1]) + " " + str(p[2]) + " " + str(p[3])
            syntaxResult.append((p[2], good, lexicalResult[counter][2]))
            counter = counter + 1
        elif p[2] == "*":
            p[0] = str(p[1]) + " " + str(p[2]) + " " + str(p[3])
            syntaxResult.append((p[2], good, lexicalResult[counter][2]))
            counter = counter + 1
        elif p[2] == "/":
            p[0] = str(p[1]) + " " + str(p[2]) + " " + str(p[3])
            syntaxResult.append((p[2], good, lexicalResult[counter][2]))
            counter = counter + 1
    elif len(p) == 2:
        p[0] = str(p[1])

def p_operand(p):
    """operand : identifier
               | constant"""
    p[0] = str(p[1])

def p_constant(p):
    """constant : CONSTANT"""
    global counter
    p[0] = str(p[1])
    syntaxResult.append((p[0], good, lexicalResult[counter][2]))
    counter = counter + 1

parser = yacc.yacc()

# синтаксический анализ
def analyze(data, lexicalResult_):
    global lexicalResult
    lexicalResult = lexicalResult_
    global syntaxResult
    syntaxResult = []
    global counter
    counter = 0
    return parser.parse(data), syntaxResult


