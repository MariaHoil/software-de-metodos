 class raiz:

    def  Biseccion ( self , a , b , tolerar ):
              
       
        importar  numpy  como  np
        importar  matplotlib . pyplot  como  plt

        fx  =  lambda  x : x ** 3  +  4 * x -  10 

        tramo  =  b - a
        mientras  no ( tramo < tolerar ):
            c  = ( un + segundo ) / 3
            fa  =  fx ( un )
            fb  =  fx ( segundo )
            fc  =  fx ( c )
            cambia  =  np . signo ( fa ) * np . firmar ( fc )
            si  cambia  <  0 :
                un  =  un
                b  =  c
            si  cambia  >  0 :
                un  =  c
                segundo  =  segundo
            tramo  =  b - a

        print ( "Bisección" )
        print ( ' Raíz en: ' , c )
        print ( 'error en el tramo: ' , tramo )



            

    def  Newton ( self , x0 , tolerar ):
        importar  numpy  como  np
 
        fx   =  lambda  x : x ** 2  +  7 * x -  10 
        dfx  =  lambda  x : 2 * x  +  7
        tablas  = []
        tramo  =  abdominales ( 2 * tolerar )
        xi  =  x0
        while ( tramo >= tolerar ):
            xnuevo  =  xi  -  fx ( xi ) / dfx ( xi )
              tramo =  abs ( xnuevo - xi )
            tabla _ agregar ([ xi , xnuevo , tramo ])
            xi  =  xnuevo

        tabla  =  np . arreglo ( tabla )
        n  =  len ( tabla )

        imprimir ( "Newton" )
        imprimir ([ 'xi' , 'xnuevo' , 'tramo' ])
        np _ set_printoptions ( precisión  =  7 )
        imprimir _ _ _
        imprimir ( 'raiz en: ' , xi )
        print ( 'error en el tramo: ' , tramo )
        
      
        
    def  Sec ( self , fa , b , tolerar ):        
        importar  numpy  como  np
        def  sec_tabla ( fx , xa , tolerar ):
            dx  =  6 * tolerar
            xb  =  xa  +  dx
            tramo  =  dx
            tablas  = []
            while ( tramo >= tolerar ):
                fa  =  fx ( xa )
                fb  =  fx ( xb )
                xc  =  xa  -  fa * ( xb - xa ) / ( fb - fa )
                tramo  =  abs ( xc - xa )
                
                tabla _ añadir ([ xa , xb , xc , tramo ])
                xb  =  xa
                xa  =  xc

            tabla  =  np . arreglo ( tabla )
            volver ( tabla )

        fx  =  lambda  x : x ** 3  +  6 * x -  10 
        un   =  1
        segundo   =  3
        xa  =  1,5
        tolerar  =  0.001
        tramos  =  100

        tabla  =  sec_tabla ( fx , xa , tolerar )
        n  =  len ( tabla )
        raíz  =  tabla [ n - 1 , 3 ]

        imprimir ( "--Secante" )
        np _ set_printoptions ( precisión = 6 )
        imprimir ( '[xa , \t xb , \t xc , \t tramo]' )
        para  i  en  rango ( 0 , n , 1 ):
            imprimir ( tabla [ i ])
        print ( 'raiz en: ' , raiz )
        

aprox  =  Métodos ()

aprox _ Bisección ( 1 , 2 , 0.01 )
aprox _ Newton ( 3 , 0.01 )
aprox _ Sec ( 1 , 3 , 0.1 )
