#Integrantes
#Jessica Ballesteros 6593
#Dennys Rojas 6574
def formular(estados,terminar,acciones,estado1):
    propositos=[]  #caminos a recorrer
    estado=estado1
    accion=0
    propositos.append(estado)
    accionTotal=0
    #si llega a una de las Metas
    if estado in terminar:
        propositos.append("Apagar")
    else:
        while accionTotal<3:
            seguir=True
            estado=estado1
            accion=accionTotal
            #actualiza el estado
            nestado=estados[estado][accion]
            while seguir:
                #si llega a una de las metas
                if nestado in terminar:
                   seguir=False
                   propositos.append(acciones[accion])
                   propositos.append(nestado)
                   propositos.append(acciones[3])
                else:
                    #para que no repita el Estado
                    if nestado in propositos:
                        accion=accion+1
                        
                    else:
                        propositos.append(acciones[accion])
                        propositos.append(nestado)
                        accion=0
                    
                    if accion>=3:
                        seguir=False
                        propositos.append(acciones[3])
                    else:
                        #actualiza el estado
                        nestado1=nestado
                        nestado=estados[nestado][accion]
                        if (nestado<nestado1)and(nestado>16):
                            nestado=nestado1

                  
            #while interno
            propositos.append(-1)
            
            accionTotal=accionTotal+1

            
            
        #while externo
    return propositos 


def busqueda(propon):
    #print(propon)
    indice=0
    resultado=[]
    separaciones=[]
    i=0
    k=0
    while i<=len(propon):
        y=propon.index(-1,i)
        separaciones.append(y)
        k=k+1
        i=i+y+1
        
    
    i=0
    k=0
    while i<separaciones[k]:
        resultado.append(propon[i])
        i=i+1
   
    return resultado
      
estados=[[3,0,1],[4,0,2],[5,1,2],[3,3,6],[4,7,10],[5,8,5],[9,3,6],[13,7,4],
[14,11,5],[9,13,12],[16,4,10],[18,11,8],[15,9,12],[13,9,9],[14,19,16],[15,20,15],
[16,14,16],[17,17,20],[18,18,21],[17,19,14],[20,17,15],[20,22,23],[22,22,21],[23,21,23]]

terminar=[15,17,20]
acciones=["Limpiar","Izquierda","Derecha","Apagar"]
estadoInicial=-0
propon=formular(estados,terminar,acciones,estadoInicial)
print()
print()
print("Proposiciones")
print(propon)
print("Acciones a Realizar")
print(busqueda(propon))