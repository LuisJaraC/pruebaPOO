from infra.repositorios.CuidadorRepo import CuidadorRepo
from infra.repositorios.FichaClinicaRepo import FichaClinicaRepo
from infra.repositorios.MascotaRepo import MascotaRepo
from infra.repositorios.ProcedimientoRepo import ProcedimientoRepo
from infra.repositorios.VeterinarioRepo import VeterinarioRepo

class RepoCentral:
    def __init__(self, mydb):
        self.CuidadorRepo = CuidadorRepo(mydb)
        self.FichaClinicaRepo = FichaClinicaRepo(mydb)
        self.MascotaRepo = MascotaRepo(mydb)
        self.ProcedimientoRepo = ProcedimientoRepo(mydb)
        self.VeterinarioRepo = VeterinarioRepo(mydb)