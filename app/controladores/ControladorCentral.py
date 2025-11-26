from app.controladores.CuidadorControl import CuidadorControl
from app.controladores.FichaClinicaControl import FichaClinicaControl
from app.controladores.MascotaControl import MascotaControl
from app.controladores.ProcedimientoControl import ProcedimientoControl
from app.controladores.VeterinarioControl import VeterinarioControl
from app.vista.VistaCentral import VistaCentral

class ControladorCentral:
    def __init__(self, conexionContexto):
        self.conexionContexto = conexionContexto
        self.vistaCentral = VistaCentral()

        # inicializamos sub-controladores
        self.cuidadorControl = CuidadorControl(conexionContexto)
        self.fichaClinicaControl = FichaClinicaControl(conexionContexto)
        self.mascotaControl = MascotaControl(conexionContexto)
        self.procedimientoControl = ProcedimientoControl(conexionContexto)
        self.veterinarioControl = VeterinarioControl(conexionContexto)

    def ejecutar(self):
        while True:
            accionUsuario = self.vistaCentral.mostrarVistas()

            # eliminamos posibles espacios en blanco
            if accionUsuario:
                accionUsuario = accionUsuario.strip()

            print(f'{accionUsuario} de tipo {type(accionUsuario)}')

            if accionUsuario == "1":
                self.cuidadorControl.ejecutar()
            elif accionUsuario == "2":
                self.fichaClinicaControl.ejecutar()
            elif accionUsuario == "3":
                self.mascotaControl.ejecutar()
            elif accionUsuario == "4":
                self.procedimientoControl.ejecutar()
            elif accionUsuario == "5":
                self.veterinarioControl.ejecutar()
            elif accionUsuario == "0":
                print("\nSaliendo del sistema")
                break
            else:
                print("\nAccion invalida, intente nuevamente")
