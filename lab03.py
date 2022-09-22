#Función para sumar dos números binarios
def suma(A, B):
    sumador = 0
    ext = ''
 
    for i in range (len(A)-1, -1, -1):
        temp = int(A[i]) + int(B[i]) + sumador
        if (temp>1):
            ext += str(temp % 2)
            sumador = 1
        else:
            ext += str(temp)
            sumador = 0
    return ext[::-1]   
 
#Funcion para en contrar el complemento
def complemento(C):
    M = ''
    for i in range (0, len(C)):
        # Calculando el complemento
        M += str((int(C[i]) + 1) % 2)
    #Sumando 1 
    M = suma(M, '0001')
    return M
     

def division(Q, M, A):
     
    count = len(M)
    comp_M = complemento(M)
    flag = 'paso'   

    print ('Valores: A:', A,' Q:', Q, ' M:', M)
     
    # longitud del número binario
    while (count):
        print ("\npaso:", len(M)-count + 1,
               end = ' | ')
        A = A[1:] + Q[0]
        
        if (flag == 'paso'):
            A = suma(A, comp_M)
        else:
            A = suma(A, M)
        print('A:', A, ' Q:', Q[1:]+'_', end ='')

        if (A[0] == '1'):
            Q = Q[1:] + '0'  
            flag = 'no paso'
            print ('| A:', A, ' Q:', Q,)
        else:
            Q = Q[1:] + '1'
            flag = 'paso'
            print ('| A:', A, ' Q:', Q)
                   
        count -= 1
    print ('\n(Q):', Q,' (A):', A)
 

if __name__ == "__main__":
    num = 56  # Numero a convertir.
    tamano = 4  # Cantidad de digitos 
    binario = ''.join([str(min(2**i & num, 1)) for i in range(tamano-1,-1,-1)])
    dividendo = '0111'
    A = '0' * len(dividendo)
    divisor = '0101'
    division(dividendo,divisor,A)
