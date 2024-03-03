def fibRec(n):
    '''Funkcja zwraca n-ty wyraz ciągu Fibonacciego'''
    if n < 2:
        return n # zakonczenie rekurencji
    else: 
        return fibRec(n-1) + fibRec(n-2) # dalsza czesc rekurencji


print(fibRec(10)) # wywolanie funkcji