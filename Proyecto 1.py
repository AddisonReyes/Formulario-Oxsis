from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import String, Numeric, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd
import os

#Addison Amin Reyes Cedano 2021-2026
engine = create_engine("sqlite:///Formulario.db", echo=True)
BASE = declarative_base()


class Formulario(BASE):
    __tablename__ = 'Formulario'
    Nombre = Column(String(30), primary_key=True)
    Empresa = Column(String(30), primary_key=True)
    Tipo_empresa = Column(String(30))
    Empresa_expimp = Column(String(9))
    Rnc = Column(Numeric)
    Email = Column(String(40))
    Telefono = Column(String(14))
    Direccion = Column(String(40))
    Mercancias = Column(String(30))
    Servicio_necesitado = Column(String(20))
    Certificado = Column(Boolean)
    Usuario = Column(String(15))
    Persona_contacto = Column(String(30))
    Referido = Column(Boolean)
    Persona_referida = Column(String(30))


BASE.metadata.create_all(engine)


datos = {
    'Nombre': [],
    'Empresa': [],
    'Tipo de empresa': [],
    'Empresa exp o imp': [],
    'RNC': [],
    'Email': [],
    'Telefono': [],
    'Direccion': [],
    'Mercancias': [],
    'Servicio necesitado': [],
    'Certificado adunal': [],
    'Usuario': [],
    'Persona de contacto': [],
    'Referido': [],
    'Persona referida': []
}


Session = sessionmaker(bind=engine)
session = Session()


def main():
    os.system("cls")
    formulario = False
    print("""Bienvenido al formulario para nuevos clientes de Oxsis
    Hecho por: Addison Reyes 2021-2026""")
    try:
        datos['Nombre'].append(str(input("\nEscribe tu nombre completo: ")))
        datos['Empresa'].append(str(input("\nEscribe el nombre de tu empresa: ")))
        print("\nTu empresa es exportadora(0) o importadora(1)")
        aux = int(input("Escoge una opcion: "))
        if aux == 0:
            datos['Empresa exp o imp'].append(aux)
        elif aux == 1:
            datos['Empresa exp o imp'].append(aux)
        else:
            while aux != 0 or aux != 1:
                aux = int(input("Escoge una opcion: "))
                if aux == 0:
                    datos['Empresa exp o imp'].append(aux)
                    break
                if aux == 1:
                    datos['Empresa exp o imp'].append(aux)
                    break

        aux = str(input("\nDigita el RNC: "))
        if len(aux) == 9:
            datos['RNC'].append(aux)
        else:
            while len(aux) != 9:
                aux = str(input("Digita el RNC correctamente: "))
                if len(aux) == 9:
                    datos['RNC'].append(aux)

        datos['Email'].append(str(input("\nEscriba el correo electronico: ")))
        datos['Telefono'].append(str(input("\nDigita el numero de telefono: ")))
        datos['Direccion'].append(str(input("\nEscribe la direccion: ")))
        datos['Mercancias'].append(str(input("\nTipo de mercancias que manejan: ")))
        datos['Servicio necesitado'].append(str(input("\n¿Cuales servicios requieren? ")))
        datos['Tipo de empresa'].append(str(input("\n¿Que tipo de empresa tienes? ")))
        aux = str(input("\n¿Tiene un certificado digital aduanal? (Si o No) "))
        if aux.lower() == "si":
            datos['Certificado adunal'].append(True)
            datos['Usuario'].append(str(input("Digita tu usuario: ")))
        elif aux.lower() == "no":
            print("Le enviaremos via correo los pasos que debe tomar para tener un certicado digital de aduanal.")
            datos['Certificado adunal'].append(False)
            datos['Usuario'].append("")
        else:
            while aux.lower() != "si" or aux.lower() != "no":
                aux = str(input("¿Tienes un certificado si o no? "))
                if aux.lower() == "si":
                    datos['Certificado adunal'].append(True)
                    datos['Usuario'].append(str(input("Digita tu usuario: ")))
                    break
                if aux.lower() == "no":
                    print("Le enviaremos via correo los pasos que debe tomar para tener un certificado digital de aduanal.")
                    datos['Certificado adunal'].append(False)
                    datos['Usuario'].append("")
                    break

        datos['Persona de contacto'].append(str(input("\nEscriba el nombre de la persona de contacto para pagos: ")))
        aux = str(input("\n¿Es referido? (Si o No) "))
        if aux.lower() == "si":
            datos['Referido'].append(True)
            datos['Persona referida'].append(str(input("¿Quien te refirio? ")))
        elif aux.lower() == "no":
            datos['Referido'].append(False)
            datos['Persona referida'].append("")
        else:
            while aux.lower() != "si" or aux.lower() != "no":
                aux = str(input("¿Eres un referido si o no? "))
                if aux.lower() == "si":
                    datos['Referido'].append(True)
                    datos['Persona referida'].append(str(input("¿Quien te refirio? ")))
                    break
                if aux.lower() == "no":
                    datos['Referido'].append(False)
                    datos['Persona referida'].append("")
                    break

        print("\nGracias por completar el formulario!")
        formulario = True
    except ValueError:
        print("\nError: Escribiste un valor invalido.")

    if formulario:
        datos_aux = pd.DataFrame(data=datos)
        formularioguardado = Formulario(
            Nombre=datos_aux['Nombre'][0],
            Empresa=datos_aux['Empresa'][0],
            Tipo_empresa=datos_aux['Tipo de empresa'][0],
            Empresa_expimp=datos_aux['Empresa exp o imp'][0],
            Rnc=datos_aux['RNC'][0],
            Email=datos_aux['Email'][0],
            Telefono=datos_aux['Telefono'][0],
            Direccion=datos_aux['Direccion'][0],
            Mercancias=datos_aux['Mercancias'][0],
            Servicio_necesitado=datos_aux['Servicio necesitado'][0],
            Certificado=datos_aux['Certificado adunal'][0],
            Usuario=datos_aux['Usuario'][0],
            Persona_contacto=datos_aux['Persona de contacto'][0],
            Referido=datos_aux['Referido'][0],
            Persona_referida=datos_aux['Persona referida'][0]
        )
        session.add(formularioguardado)
        session.commit()


if __name__ == '__main__':
    main()
