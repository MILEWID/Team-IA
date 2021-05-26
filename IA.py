
def formular(estados,terminar,acciones,estado1):
    propositos=[]  #caminos a recorrer
    estado=estado1
    accion=0
    propositos.append(estado)
    accionTotal=0
    #si llega a una de las Metas
    if estado in terminar:
        propositos.append("Apagar")
        propositos.append(-1)
        propositos.append(-1)
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
      



estados=[[9,0,1],[7,0,2],[5,1,2],[15,3,4],[13,3,5],[5,4,5],[18,6,7],[7,6,8],
[14,7,8],[9,9,10],[19,9,11],[17,10,11],[21,12,13],[13,12,14],[14,13,14],[15,15,16],
[22,15,17],[17,16,17],[18,18,19],[19,18,20],[23,19,20],[21,21,22],[22,21,23],[23,23,22]]

terminar=[21,22,23]
acciones=["Limpiar","Izquierda","Derecha","Apagar"]
estadoInicial=-1
print("INGRESE EL ESTADO INICIAL:")
while(estadoInicial>23)or(estadoInicial<0):
    estadoInicial=int(input())
propon=formular(estados,terminar,acciones,estadoInicial)
print()
print()
print("Proposiciones*****")
print(propon)
print("Acciones a Realizar")
print(busqueda(propon))