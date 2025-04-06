charClass = None
lexeme = ""
nextChar = ""
lexLen = 0
token = 0
nextToken = 0
in_fp = None

LETTER = 0
DIGIT = 1
UNKNOWN = 99

INT_LIT = 10
IDENT = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26

def addChar():
    """A function to add nextChar to lexeme"""
    global lexeme, nextChar, lexLen
    
    if lexLen <= 98:
        lexeme += nextChar
        lexLen += 1
    else:
        print("Error - lexeme is too long")

def getChar():
    """
    A function to get the next character of input and 
    determine its character class
    """
    global nextChar, charClass, in_fp
    
    try:
        nextChar = in_fp.read(1)  
        if nextChar:  
            if nextChar.isalpha():
                charClass = LETTER
            elif nextChar.isdigit():
                charClass = DIGIT
            else:
                charClass = UNKNOWN
        else:  
            charClass = EOF
    except Exception as e:
        print(f"Error reading from file: {e}")
        charClass = EOF

def getNonBlank():
    """
    A function to call getChar until it returns a non-whitespace character
    """
    global nextChar
    
    while nextChar.isspace():
        getChar()

def lookup(ch):
    """
    A function to lookup operators and parentheses and return the token
    """
    global nextToken
    
    if ch == '(':
        addChar()
        nextToken = LEFT_PAREN
    elif ch == ')':
        addChar()
        nextToken = RIGHT_PAREN
    elif ch == '+':
        addChar()
        nextToken = ADD_OP
    elif ch == '-':
        addChar()
        nextToken = SUB_OP
    elif ch == '*':
        addChar()
        nextToken = MULT_OP
    elif ch == '/':
        addChar()
        nextToken = DIV_OP
    else:
        addChar()
        nextToken = EOF
        
    return nextToken

def lex():
    """
    A simple lexical analyzer for arithmetic expressions
    """
    global lexLen, nextToken, lexeme, charClass, nextChar
    
    lexLen = 0
    lexeme = ""
    
    getNonBlank()
    
    if charClass == EOF:
        nextToken = EOF
        lexeme = "EOF"
        return nextToken
    
    if charClass == LETTER:
        addChar()
        getChar()
        while charClass == LETTER or charClass == DIGIT:
            addChar()
            getChar()
        nextToken = IDENT
    elif charClass == DIGIT:
        addChar()
        getChar()
        while charClass == DIGIT:
            addChar()
            getChar()
        nextToken = INT_LIT
    elif charClass == UNKNOWN:
        lookup(nextChar)
        getChar()
    
    print(f"Next token is: {nextToken}, Next lexeme is {lexeme}")
    return nextToken

def main():
    """Main driver function"""
    global in_fp, nextToken, charClass, EOF
    
    EOF = -1
    
    try:
        in_fp = open("front.in", "r")
        getChar()
        
        while True:
            lex()
            if nextToken == EOF:
                break
                
    except FileNotFoundError:
        print("ERROR - cannot open front.in")
    finally:
        if in_fp:
            in_fp.close()

with open("front.in", "w") as f:
    f.write("a + 4 * (b - 2)\n")

if __name__ == "__main__":
    main()
