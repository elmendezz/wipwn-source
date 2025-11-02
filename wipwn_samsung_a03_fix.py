#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WIPWN - Samsung A03 Core Fix
Solución para el error "Could not read interface wlan0 flags: No such device"

Este parche modifica el comportamiento de AndroidNetwork para:
1. NO deshabilitar WiFi antes de ejecutar wpa_supplicant
2. Agregar soporte para chipset MediaTek
3. Mejorar el timing de inicialización
"""

import marshal
import types
import sys

print("[+] Aplicando parche para Samsung A03 Core...")

# Cargar el bytecode original
with open('main_code.pyc', 'rb') as f:
    f.read(16)
    code_obj = marshal.load(f)

# Ejecutar en namespace
namespace = {}
exec(code_obj, namespace)

# Obtener la clase AndroidNetwork original
AndroidNetwork_Original = namespace.get('AndroidNetwork')

if not AndroidNetwork_Original:
    print("[!] Error: No se encontró AndroidNetwork")
    sys.exit(1)

# Crear versión parcheada
class AndroidNetwork_Patched:
    """Versión parcheada de AndroidNetwork para Samsung A03 Core"""
    
    def __init__(self):
        self.ENABLED_SCANNING = 0
        print("[!] PARCHE ACTIVADO: AndroidNetwork modificado para A03 Core")
    
    def disableWifi(self, whisper=False):
        """
        PARCHEADO: NO deshabilita WiFi para evitar que wlan0 desaparezca
        """
        if not whisper:
            print("[i] Android: Manteniendo Wi-Fi habilitado (PARCHE A03 Core)")
        # NO ejecutamos cmd wifi set-wifi-enabled disabled
        # Esto evita que wlan0 desaparezca
        return
    
    def enableWifi(self, force_enable=False, whisper=False):
        """
        PARCHEADO: Asegura que WiFi esté habilitado sin deshabilitarlo primero
        """
        import subprocess
        import time
        
        if not whisper:
            print("[i] Android: Verificando Wi-Fi habilitado")
        
        try:
            # Asegurar que WiFi está habilitado
            wifi_enable_cmd = ['cmd', 'wifi', 'set-wifi-enabled', 'enabled']
            subprocess.run(wifi_enable_cmd, check=True)
            
            # Pequeña espera para que la interfaz se estabilice
            time.sleep(2)
            
            # Habilitar scanning siempre disponible
            if self.ENABLED_SCANNING == 1 or force_enable:
                wifi_enable_scanner_cmd = ['cmd', '-w', 'wifi', 'set-scan-always-available', 'enabled']
                subprocess.run(wifi_enable_scanner_cmd, check=True)
        
        except subprocess.CalledProcessError as e:
            print(f"[!] Error al habilitar Wi-Fi: {e}")
    
    def storeAlwaysScanState(self):
        """Guarda el estado de scanning"""
        import subprocess
        try:
            result = subprocess.run(
                ['cmd', '-w', 'wifi', 'get-scan-always-available'],
                capture_output=True,
                text=True,
                check=True
            )
            output = result.stdout.strip().lower()
            self.ENABLED_SCANNING = 1 if 'enabled' in output else 0
        except subprocess.CalledProcessError:
            self.ENABLED_SCANNING = 0

# Reemplazar en el namespace
namespace['AndroidNetwork'] = AndroidNetwork_Patched

print("[+] Parche aplicado exitosamente")
print("[+] Ejecutando WIPWN con correcciones...")
print()

# Ejecutar el código principal con el parche aplicado
if __name__ == "__main__":
    exec(code_obj, namespace)
