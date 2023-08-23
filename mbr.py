import ctypes

class mbr(ctypes.Structure):
    _fields_ = [
        ('tamano', ctypes.c_int),
        ('fecha', ctypes.c_char * 16),
        ('asignatura', ctypes.c_int)
    ]
    def __init__(self):
        self.tamano = 0
        self.fecha = b'\0' * 16
        self.asignatura = 0

    def set_tamano(self,tamano):
        self.tamano = tamano 
    
    def set_fecha(self, fecha):
        self.fecha = fecha.encode('utf-8')[:15].ljust(16, b'\0')
    
    def set_asignatura(self, asignatura):
        self.asignatura = asignatura
    
    def set_information(self, tamano, fecha, asignatura):
        self.set_tamano(tamano)
        self.set_fecha(fecha)
        self.set_asignatura(asignatura)
    
    def display_info(self):
        print(f"mbr_tamano: {self.tamano}")
        print(f"mbr_fecha_creacion: {self.fecha.decode()}")
        print(f"mbr_dsk_signature: {self.asignatura}")
    
import ctypes

class mbr(ctypes.Structure):
    _fields_ = [
        ('tamano', ctypes.c_int),
        ('fecha', ctypes.c_char * 16),
        ('asignatura', ctypes.c_int)
    ]
    def __init__(self):
        self.tamano = 0
        self.fecha = b'\0' * 16
        self.asignatura = 0

    def set_tamano(self,tamano):
        self.tamano = tamano 
    
    def set_fecha(self, fecha):
        self.fecha = fecha.encode('utf-8')[:15].ljust(16, b'\0')
    
    def set_asignatura(self, asignatura):
        self.asignatura = asignatura
    
    def set_information(self, tamano, fecha, asignatura):
        self.set_tamano(tamano)
        self.set_fecha(fecha)
        self.set_asignatura(asignatura)
    
    def display_info(self):
        print(f"mbr_tamano: {self.tamano}")
        print(f"mbr_fecha_creacion: {self.fecha.decode()}")
        print(f"mbr_dsk_signature: {self.asignatura}")
    
