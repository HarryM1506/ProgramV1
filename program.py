seB=int
seC=int

############################################################################

print('Welcome to the AS Maths Algebra Revision tool.')
print(' ')
print('Would you like to revise C1 or C2?')
print(' ')

############################################################################

while True:
    choice=int(input('Enter 1 for C1 or 2 for C2    '))
    
    if choice == 1:
        print(' ')
        print('C1 Selected')
        break
    
    elif choice == 2:
        print(' ')
        print('C2 Selected')
        break

    else:
        print(' ')
        print(' Not an option')
        print(' ')
    
##############################################################################

if choice == 1:
    print(' ')
    c1alg=int(input('C1 Algebra & Functions ?  1 for Yes  ---  0 for No    '))
elif choice == 2:
    print(' ')
    c2alg=int(input('C2 Algebra & Functions ?  1 for Yes  ---  0 for No    '))
else:
    print('Restart')
    
##############################################################################


if c1alg == 1:
    print(' ')
    print('C1 Algebra & Functions Selected')
    print(' ')
    seA=int(input('C1 Algebra Simplifying Expressions - 1A ?  1 for Yes  ---  0 for No    '))

elif c1alg == 0:
    print(' ')
    quad=int(input('C1 Quadratics ?  1 for Yes  ---  0 for No'))

else:
    print(' ')

##########################################   Exercise 1A   ##########################################
if seA == 1:
    print(' ')
    print('Simplifying Expressions - 1A Selected')
    print(' ')
    print('Examples')
    print(' ')
    print('Simplify : 3x + 2xy + 7 - x + 3xy - 9       AND      3( a + b^2 ) - 2( 3a - 4b^2)')
    print(' ')
    print('3x + 2xy + 7 - x + 3xy - 9   ==>   3x - x + 2xy + 3xy + 7 - 9   ==> 2x + 5xy -2')
    print(' ')
    print(' ')
    print('3( a + b^2 ) - 2( 3a - 4b^2)     ==>   3a + 3b^2 - 6a - 8b^2     ==>  -3a + 11b^2')
    print(' ')
    print(' ')
    print('Questions')
    print(' ')
  
    q1=str(raw_input('Q1 ----- Simplify    4x - 5y +3x + 6y ------  '    ))
    if q1 == '7x + y':
      print('Correct')
      print(' ')
    else:
      print('Incorrect')
      print(' ')
    
    q2=str(raw_input('Q2 ----- Simplify   3r + 7t - 5r + 3t ------  '   ))
    if q2 == '−2r + 10t':
      print('Correct')
      print(' ')
    else:
      print('Incorrect')
      print(' ')
    
    q3=str(raw_input('Q3 ----- Simplify   7( 1 - x^2) + 3( 2 - 3x + 5x^2) ------  '))
    if q3 == '8x^2 − 9x + 13':
      print('Correct')
      print(' ')
    else:
      print('Incorrect')
      print(' ')
    
    q4=str(raw_input('Q4 ----- Simplify   4( c + 3d^2) - 3( 2c + d^2) ------  '))
    if q4 == '−2c + 9d^2':
      print('Correct')
      print(' ')
    else:
      print('Incorrect')
      print(' ')
  
    q5=str(raw_input('Q5 ----- Simplify  ( r^2 + 3t^2 + 9 ) - ( 2r^2 + 3t^2 - 4 ) ------  '))
    if q5 == '13 - r^2':
      print('Correct')
      print(' ')
    else:
      print('Incorrect')
      print(' ')
      
print(' ')

cont=int(input('Enter 1 to continue  '))
    
##########################################   Exercise 1B Choice   ##########################################
    

if seA == 0 or cont == 1 or 0:
    print(' ')
    seB=int(input('C1 Algebra Simplifying Expressions - 1B ?  1 for Yes  ---  0 for No    '))

else:
    print(' ')

##########################################   EXERCISE 1B   ##########################################

if seB == 1:
    print(' ')
    print('Simplifying Expressions - 1B Selected')
    print(' ')
    print('Examples')
    print(' ')
    print('Simplify : x^2 X x^5 ' '  ,   ''6x^-3 / 3x^-5    AND   (a^3)^2 X 2a^2')
    print(' ')
    print(' ')
    print('  x^2 X x^5  ==>   x^7    ( X == Add Powers ) ')
    print(' ')
    print(' ')
    print(' 6x^-3 / 3x^-5    ==>    6/3 X x^-3 / x^-5   ==>    2x^2    ( -3--5 = +)'  )
    print(' ')
    print(' ')
    print(' (a^3)^2 X 2a^2    ==>  a^6 X 2a^2   ==>   2 X a^8   ==>  2a^8 ')
    print(' ')
    print(' ')
    print('Questions')
    print(' ')  

  
    b1=str(raw_input('Q1 ----- Simplify  2x^3 X 3x^2 ------     '))
    if b1 == '6x^5':
        print('Correct')
        print(' ')
    else:
        print('Incorrect')
        print(' ')
    
    b2=str(raw_input('Q2 ----- Simplify   k^3 / k^-2 ------     '))
    if b2 == 'k^5':
        print('Correct')
        print(' ')
    else:
        print('Incorrect')
        print(' ')
    
    b3=str(raw_input('Q3 ----- Simplify   (2a^3)^2 / 2a^3 ------    '))
    if b3 == '6a^-9':
        print('Correct')
        print(' ')
    else:
        print('Incorrect')
        print(' ')
    
    b4=str(raw_input('Q4 ----- Simplify   7a^4 X (3a^4)^2 ------    '))
    if b4 == '63a^12':
        print('Correct')
        print(' ')
    else:
        print('Incorrect')
        print(' ')
  
    b5=str(raw_input('Q5 ----- Simplify  2a^3 / 3a^2 X 6a^5 ------    '))
    if b5 == '4a^6':
        print('Correct')
        print(' ')
    else:
        print('Incorrect')
        print(' ')

print(' ')
cont=input('Enter 1 to continue  ')
           
##########################################   Exercise 1C Choice   ##########################################

if seB == 0 or cont == 1 or 0:
    print(' ')
    seC=int(input('C1 Algebra Expanding & Simplifying Expressions - 1C ?  1 for Yes  ---  0 for No    '))

else:
    print(' ')

##########################################   EXERCISE 1C   ##########################################

if seC == 1:
    print(' ')
    print('Expanding & Simplifying Expressions - 1C Selected')
    print(' ')
    print('Examples')
    print(' ')
    print('Expand & Simplify : -5x(4x +1)  ,   7(x -2) + 3(x +4) - 6(x -2)    AND   4x(x +3) - 2x(3x -7)'  )
    print(' ')
    print(' ')
    print('  -5x(4x +1)  ==>   -20x^2 -5x ')
    print(' ')
    print(' ')
    print(' 7(x -2) + 3(x +4) - 6(x -2)    ==>   (7x -14) + (3x +12) - (6x -12)    ==>  4x +14 '  )
    print(' ')
    print(' ')
    print(' 4x(x +3) - 2x(3x -7)   ==>  (4x^2 + 12x ) - (6x^2 -14x)    ==>  -2X^2 + 26x ')
    print(' ')
    print(' ')
    print('Questions')
    print(' ')

    c1=str(raw_input('Q1 -----  Expand & Simplify  (4x + 5)x  ------    '))
    if c1 == '4x^2 + 5x':
        print('Correct')
        print(' ')
    else:
        print('Incorrect')
        print(' ')
    
    c2=str(raw_input('Q2 ----- Expand & Simplify   5x -6 -(3x -2) ------     '))
    if c2 == '2x -8':
        print('Correct')
        print(' ')
    else:
        print('Incorrect')
        print(' ')
    
    c3=str(raw_input('Q3 ----- Expand & Simplify   x(3x^2 -2x +5) ------     '))
    if c3 == '3x^3 -2x^2 +5x':
        print('Correct')
        print(' ')
    else:
        print('Incorrect')
        print(' ')
    
    c4=str(raw_input('Q4 ----- Expand & Simplify   -2y^2(5 -7y +3y^2) ------     '))
    if c4 == '-10y^2 +14y^3 -6y^4':
        print('Correct')
        print(' ')
    else:
        print('Incorrect')
        print(' ')
  
    c5=str(raw_input('Q5 ----- Expand & Simplify  3x^2(2x +1) -5x^2(3x -4) ------     '))
    if c5 == '-9x^3 +23x^2':
        print('Correct')
        print(' ')
    else:
        print('Incorrect')
        print(' ')

print(' ')
cont=int(input('Enter 1 to continue  '))
           
##########################################   Exercise 1D Choice   ##########################################

if seC == 0 or cont == 1 or 0:
    print(' ')
    seD=int(input('C1 Factorising Expressions - 1D ?  1 for Yes  ---  0 for No    '))

else:
    print(' ')

##########################################   EXERCISE 1D   ##########################################

if seD == 1:
    print(' ')
    print('Factorising Expressions - 1D Selected')
    print(' ')
    print('Examples')
    print(' ')
    print('Factorise: 4x +8  ,   35x^2 -28x    AND   4x^2 +12x ' )
    print(' ')
    print(' ')
    print('  4x +8   ==>   -4(x +2)  ')
    print(' ')
    print(' ')
    print(' 35x^2 -28x   ==>   7x(5x -4)  '  )
    print(' ')
    print(' ')
    print(' 4x^2 +12x     ==>  4x(x +3) '  )
    print(' ')
    print(' ')
    print('Questions')
    print(' ')

    d1=str(raw_input('Q1 -----  Factorise  6ab -2ab^2  ------     '))
    if d1 == '2ab(3 -b)':
           print('Correct')
           print(' ')
    else:
           print('Incorrect')
           print(' ')
    
    d2=str(raw_input('Q2 -----  Factorise   9xy^2 + 12x^2y ------     '))
    if d2 == '3xy(3y +4x)':
           print('Correct')
           print(' ')
    else:
           print('Incorrect')
           print(' ')
    
    d3=str(raw_input('Q3 -----  Factorise   12x^2y + 8xy^2 ------     '))
    if d3 == '4xy(3x +2y)':
           print('Correct')
           print(' ')
    else:
           print('Incorrect')
           print(' ')
    
    d4=str(raw_input('Q4 -----  Factorise   15y -20yz^2 ------     '))
    if d4 == '5y(3 -4z^2)':
           print('Correct')
           print(' ')
    else:
           print('Incorrect')
           print(' ')
  
    d5=str(raw_input('Q5 -----  Factorise  xy^2 - x^2y ------     '))
    if d5 == 'xy(y -x)':
           print('Correct')
           print(' ')
    else:
           print('Incorrect')
           print(' ')

print(' ')
cont=int(input('Enter 1 to continue  '))
           
##########################################   Exercise 1E Choice   ##########################################

if seD == 0 or cont == 1 or 0:
    print(' ')
    seE=int(input('C1 Algebra Factorising Quadratics - 1E ?   1 for Yes  ---  0 for No    '))

else:
    print(' ')

##########################################   EXERCISE 1E   ##########################################
if seE == 1:
    print(' ')
    print('Factorising Quadratics - 1E Selected')
    print(' ')
    print('Examples')
    print(' ')
    print('Factorise: 6x^2 +9x  ,   x^2 -25    AND  x^2 -5x -6  ' )
    print(' ')
    print(' ')
    print('  6x^2 +9x   ==>   3x(2x +3)  ')
    print(' ')
    print(' ')
    print(' x^2 -25  ==>  (x +5)(x -5)  ==>  Difference of two squares '  )
    print(' ')
    print(' ')
    print(' x^2 -5x -6    ==>  (x +1)(x -6) '  )
    print(' ')
    print(' ')
    print('Questions')
    print(' ')

    e1=str(raw_input('Q1 -----  Factorise x^2 + 11x + 24   ------     '))
    if e1 == '(x +8)(x +3)':
           print('Correct')
           print(' ')
           
    elif e1 == '(x +3)(x +8)':
           print('Correct')
           print(' ')
           
    else:
           print('Incorrect')
           print(' ')
    
    e2=str(raw_input('Q2 -----  Factorise   x^2 + 3x -40 -----   '))
    if e2 == '(x +8)(x -5)':
           print('Correct')
           print(' ')
           
    elif e2 == '(x -5)(x +8)':
           print('Correct')
           print(' ')
    else:
           print('Incorrect')
           print(' ')
    
    e3=str(raw_input('Q3 -----  Factorise  2x^2 + 5x + 2  ----  '))
    if e3 == '(2x +1)(x +2)':
           print('Correct')
           print(' ')
           
    elif e3 == '(x +2)(2x +1)':
           print('Correct')
           print(' ')
           
    else:
           print('Incorrect')
           print(' ')
    
    e4=str(raw_input('Q4 -----  Factorise  4x^2 − 25 --- '))
    if e4 == "(2x +5)(2x −5)":
           print('Correct')
           print(' ')

    elif e4 == '(2x -5)(2x +5)':
           print('Correct')
           print(' ')
    
    else:
           print('Incorrect')
           print(' ')
  
    e5=str(raw_input('Q5 -----  Factorise  15x^2 + 42x − 9 --- '))
    if e5 == '3(5x −1)(x +3)':
           print('Correct')
           print(' ')
           
    else:
           print('Incorrect')
           print(' ')

print(' ')
cont=int(input('Enter 1 to continue  '))

##########################################   Exercise 1F Choice   ##########################################

if seE == 0 or cont == 1 or 0:
    print(' ')
    seF=int(input('C1 Algebra Simplifying & Evaluating Indices - 1F ?   1 for Yes  ---  0 for No    '))

else:
    print(' ')

##########################################   EXERCISE 1F   ##########################################


if seF == 1:
    print(' ')
    print('Simplifying & Evaluating Indices - 1F Selected')
    print(' ')
    print('Examples')
    print(' ')
    print('Evaluate:  9^1/2  ,   25^-3/2    AND  (x^2)^3/2  ' )
    print(' ')
    print(' ')
    print('  9^1/2   ==>   sqrt 9   ==>    3     ( 9^1 , Square root answer as it is a 2 ) ')
    print(' ')
    print('                 ___1___           ___1___           __1__           _1_ ')
    print(' 25^-3/2   ==>    25^3/2   ==>    (sqrt 25)^3   ==>  (5)^2    ==>     25  '  )
    print(' ')
    print(' ')
    print(' Simplify :  (x^2)^3/2    ==>  sqrt x^2 = x,   Ans^3 = x^3 '  )
    print(' ')
    print(' ')
    print('Questions')
    print(' ')

    f1=str(raw_input('Q1 -----  Evaluate  81^1/2  ------     '))
    if f1 == '9':
           print('Correct')
           print(' ')
    else:
           print('Incorrect')
           print(' ')
    
    f2=str(raw_input('Q2 -----  Evaluate  4^-2 ---- '))
    if f2 == '1/16':
           print('Correct')
           print(' ')
    else:
           print('Incorrect')
           print(' ')
    
    f3=str(raw_input('Q3 -----  Evaluate  (3/4)^0------     '))
    if f3 == '1':
           print('Correct')
           print(' ')
    else:
           print('Incorrect')
           print(' ')
    
    f4=str(raw_input('Q4 ----- Evaluate  (27/8)^2/3 ----  '))
    if f4 == '9/4':
           print('Correct')
           print(' ')
    else:
           print('Incorrect')
           print(' ')
  
    f5=str(raw_input('Q5 -----  3x^4  X  2x^-5 ----  '))
    if f5 == '6x^-1':
           print('Correct')
           print(' ')
    else:
           print('Incorrect')
           print(' ')

print(' ')
cont=int(input('Enter 1 to continue  '))

##########################################   Exercise 1G Choice   ##########################################

if seF == 0 or cont == 1 or 0:
    print(' ')
    seG=int(input('C1 Surds - 1G ?   1 for Yes  ---  0 for No    '))

else:
    print(' ')

##########################################   EXERCISE 1G   ##########################################


