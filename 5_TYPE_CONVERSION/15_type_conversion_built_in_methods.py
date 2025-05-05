            
Str = input("\nEnter String : ")    #Enter String : 65

print("\nint : ", int(Str))         #int :  65

#print("\nlong : ", long(Str))      #not defined long

print("\nfloat : ", float(Str))     #float :  65.0

print("\ncomplex : ", complex(Str)) #complex:  (65+0j)

print("\nstring : ", str(Str))      #string :  65

print("\nExpression String : ", repr(Str))  #Expression String :  '65'

print("\nobject return by eval : ", eval(Str))  #object return by eval :  65

Tuple = tuple(Str)
print("\ntuple : ", Tuple)          #tuple :  ('6', '5')

print("\nlist : ", list(Str))       #list :  ['6', '5']

print("\nset : ", set(Str))         #set :  {'6', '5'}

#print("\ndictionary : ", dict(Tuple)) #dictionary update sequence element #0 has length 1; 2 is required

print("\nfrozenset : ", frozenset(Str))#frozenset :  frozenset({'6', '5'})

No = int(Str)
print("\nCharcter : ", chr(No))     #Charcter :  A

#print("\nUnicode charcter : ", unichr(Str)) #NameError: name 'unichr' is not defined

print("\nCharacter To Integer : ", ord(chr(No)))    #Character To Integer :  65

print("\nHexadecimal : ", hex(No))                  #Hexadecimal :  0x41

print("\nOctal : ", oct(No))                        #Octal :  0o101

