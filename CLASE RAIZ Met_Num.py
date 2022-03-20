class Raiz:
    def biseccion(self,a,b,tolera):          
        import numpy as np
        import matplotlib.pyplot as plt
        fx = lambda x: x**2 + 7*x-4
        tramo = b-a
        while not(tramo<tolera):
            c = (a+b)/2
            fa = fx(a)
            fb = fx(b)
            fc = fx(c)
            cambia = np.sign(fa)*np.sign(fc)
            if cambia < 0: 
                a = a
                b = c
            if cambia > 0:
                a = c
                b = b
            tramo = b-a

        print("bisección")
        print('raiz aproximado: ', c)
        
    def secante(self,fa,b,tolera):        
        import numpy as np
        def secante_tabla(fx,xa,tolera):
            dx = 4*tolera
            xb = xa + dx
            tramo = dx
            tabla = []
            while (tramo>=tolera):
                fa = fx(xa)
                fb = fx(xb)
                xc = xa - fa*(xb-xa)/(fb-fa)
                tramo = abs(xc-xa)
                
                tabla.append([xa,xb,xc,tramo])
                xb = xa
                xa = xc

            tabla = np.array(tabla)
            return(tabla)

        fx = lambda x: x**2 + 7*x-4
        a  = 1
        b  = 2
        xa = 1.5
        tolera = 0.001
        tramos = 100

        tabla = secante_tabla(fx,xa,tolera)
        n = len(tabla)
        raiz = tabla[n-1,2]

        print("Secante")
        np.set_printoptions(precision=4)
        print('[xa ,\t xb , \t xc , \t tramo]')
        for i in range(0,n,1):
            print(tabla[i])
        print('raiz en: ', raiz)

    def newton(self, x0, tolera):
        import numpy as np
 
        fx  = lambda x: x**2+7*x-4 
        dfx = lambda x: 2*x + 7
        # PROCEDIMIENTO
        tabla = []
        tramo = abs(2*tolera)
        xi = x0
        while (tramo>=tolera):
            xnuevo = xi - fx(xi)/dfx(xi)
            tramo  = abs(xnuevo-xi)
            tabla.append([xi,xnuevo,tramo])
            xi = xnuevo
        tabla = np.array(tabla)
        n = len(tabla)
        print("Newton")
        print(['xi', '       xnuevo', '   tramo'])
        np.set_printoptions(precision = 4)
        print(tabla)
        print('Raiz: ', xi)
        print('con error de: ',tramo)
        
objeto = Raiz()

objeto.biseccion(1,2,0.01)
objeto.secante(1,3,0.1)
objeto.newton(2,0.01)