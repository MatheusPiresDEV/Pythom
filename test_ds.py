def soma(a,b):
   return a+b

def test_soma():
    assert soma(20,50) == 70

def mult(a,b):
   return a*b

def test_mult():
    assert mult(2,4) == 8

def sub(a,b):
   return a-b

def test_sub():
   assert sub(10,3) == 7

def div(a,b):
   if b == 0:
      return "erro"
   else: 
      return a/b    

def test_div():
   assert div(8,0) == "erro"


