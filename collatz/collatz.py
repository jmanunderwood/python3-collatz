class collatz(object):

    def collatz_numbers(c):
        '''
        Given a starting point c>=1, returns a collatz sequence starting at c
        '''
        numbers = []
        while c>1:
            if c%2==0:
                c/=2
            else:
                c=(c*3)+1
            numbers.append(c) 
        return numbers       
