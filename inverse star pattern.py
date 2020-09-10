Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> i=0
n=eval(input("How many rows"))
for i in range (n):
    print(n * "*")
    n=n-1
    
SyntaxError: multiple statements found while compiling a single statement
>>> 