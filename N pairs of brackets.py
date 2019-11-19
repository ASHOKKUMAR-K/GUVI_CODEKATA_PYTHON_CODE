l = []
def printParenthesis(str, n): 
    if(n > 0): 
        _printParenthesis(str, 0, n, 0, 0); 
    return
  
def _printParenthesis(str, pos, n, open, close): 
      
    if(close == n):
        l.append(1) 
        return
    else: 
        if(open > close): 
            str[pos] = '}'
            _printParenthesis(str, pos + 1, n, open, close + 1); 
        if(open < n): 
            str[pos] = '{'
            _printParenthesis(str, pos + 1, n, open + 1, close)
n = int(input()); 
str = [""] * 2 * n; 
printParenthesis(str, n); 
print(len(l))
