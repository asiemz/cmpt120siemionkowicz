#cpu_functions.py


from logic_gates  import *



def one_bit_adder(a,b,ci):

    s = xor_g(xor_g(a,b),ci)

    v = xor_g(a,b)

    carry = or_g(and_g(v,ci),and_g(a,b))
    

  

    return(s,carry)

    
    
