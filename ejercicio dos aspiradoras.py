#estados: Posibles estados de la Aspiradora
#terminar: Estados donde termina su trabajo
#acciones: Limpiar, Izquierda, Derecha
#estado1: accion1=>estado y accion inicial

def formular(estados,terminar,acciones,estado1):
    propositos=[]  #caminos a recorrer
    accionesE=[]   #acciones que realizara la aspiradora
    estado=estado1
    accion=0
    propositos.append(estado)
    accionTotal=0
    #si llega a una de las Metas
    if estado in terminar:
        acciones.append("Apagar")
    else:
        while accionTotal<2:
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
                        nestado=estados[nestado][accion]

                  
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
    while i<len(propon):
        
        propon.index(-1,i)
        separaciones.append(propon.index(-1,i))
        k=k+1
        i=i+propon.index(-1,i)+1
    
    i=0
    k=0
    while i<separaciones[k]:
        resultado.append(propon[i])
        i=i+1
   
    return resultado
      


estados=[[16,4,4],[18,18,8],[15,9,9],[9,9,9],[9,19,16],[16,20,20],[20,14,14],[14,14,20],[20,20,21],[17,17,14],[14,17,15],[20,22,23],[23,23,21],[21,21,21]
estados=[[4,0,1],[3,0,1],[6,2,3],[3,2,3],[4,4,5],[7,4,5],[6,6,7],[7,6,7]]
terminar=[6,7]
acciones=["Limpiar","Izquierda","Derecha","Apagar"]
estadoInicial=1
propon=formular(estados,terminar,acciones,estadoInicial)
print("Proposiciones*****")
print(propon)
print("Acciones a Realizar")
print(busqueda(propon))

