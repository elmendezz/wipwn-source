# WIPWN - WiFi WPS Pentesting Framework (Desofuscado)

## 🎯 Resumen del Proyecto

Este repositorio contiene **WIPWN v3.0**, un framework profesional de auditoría de seguridad WiFi, completamente **desofuscado** del código original que estaba protegido con ANBU Obfuscator v3.0.

**Estado:** ✅ Desofuscación completada - Código 100% editable

---

## ⚠️ IMPORTANTE

### Este proyecto NO se ejecuta en Replit

WIPWN requiere:
- 📱 **Dispositivo Android** con Termux
- 📡 **Interfaz WiFi física** (wlan0)
- 🔑 **Permisos root/superuser**
- 🛠️ **Herramientas:** `wpa_supplicant`, `pixiewps`

**Replit solo sirve para ver el código desofuscado.** Para ejecutarlo, transfiere los archivos a tu dispositivo Android.

---

## 📁 Archivos Principales

### Código Desofuscado ⭐

1. **`wipwn_editable.py`** - Versión principal editable y funcional
2. **`wipwn_samsung_a03_fix.py`** - Parche específico para Samsung A03 Core
3. **`main_deobfuscated.py`** - Versión alternativa con bytecode

### Documentación

- **`SOLUCION_SAMSUNG_A03.md`** - Guía completa de solución para error wlan0
- **`replit.md`** - Documentación técnica completa
- **`README.md`** - Este archivo

### Archivos de Análisis

- `main_code.pyc` - Bytecode extraído
- `main_full_disassembly.txt` - Desensamblado completo
- `main.py` - Código original ofuscado (referencia)

---

## 🚀 Cómo Usar

### En Android/Termux:

```bash
# 1. Transferir archivos a tu dispositivo
# 2. En Termux:
cd ~/wipwn

# 3. Ejecutar (versión estándar):
sudo python wipwn_editable.py -i wlan0 -K

# 4. O con target específico:
sudo python wipwn_editable.py -i wlan0 -b XX:XX:XX:XX:XX:XX -K

# 5. Para dispositivos MediaTek (Samsung A03, etc):
sudo python wipwn_samsung_a03_fix.py -i wlan0 -K
```

### Opciones principales:

```
-i, --interface    Interfaz de red (ej: wlan0)
-b, --bssid        BSSID del router objetivo
-p, --pin          PIN específico a probar
-K, --pixie-dust   Ataque Pixie Dust
-B, --bruteforce   Ataque de fuerza bruta
--mtk-wifi         Activar driver MediaTek Wi-Fi
```

---

## 🔧 Solución de Problemas

### Error: "Could not read interface wlan0 flags: No such device"

**Dispositivos afectados:** Samsung A03 Core, otros con chipset MediaTek

**Solución:** Usa `wipwn_samsung_a03_fix.py` en lugar del archivo original.

**Documentación completa:** Ver `SOLUCION_SAMSUNG_A03.md`

---

## 📊 Características

- ✅ **100 algoritmos** de generación de PINs WPS
- ✅ **500+ routers** en base de datos (TP-Link, D-Link, Asus, etc.)
- ✅ **Pixie Dust attack** optimizado
- ✅ **Bruteforce online** con gestión de sesiones
- ✅ **Randomización de MAC** para evitar detección
- ✅ **Controles de timing** avanzados

---

## 🔓 Desofuscación Completada

### Proceso:

El código original tenía **10 capas de ofuscación:**

1. XOR encryption (32 bytes)
2. Zlib compression
3. Base85 encoding
4. XOR encryption (16 bytes)
5. Base32 encoding
6. Base64 encoding (reverso)
7. Zlib compression
8. Base64 encoding (reverso)
9. Zlib compression
10. Base64 + Marshal (bytecode Python)

**Resultado:** Todas las capas removidas ✅

---

## 🛠️ Modificar el Código

Ahora que está desofuscado, puedes:

1. **Agregar nuevas funciones**
2. **Modificar algoritmos** de PINs
3. **Añadir soporte** para nuevos routers
4. **Personalizar reportes** y salidas
5. **Mejorar ataques** existentes

### Ejemplo - Agregar función personalizada:

```python
def mi_nueva_funcion(parametro):
    """
    Tu función personalizada
    """
    print(f"Procesando: {parametro}")
    # Tu código aquí
    return resultado
```

---

## 🏗️ Arquitectura del Código

### Clases Principales:

- **`WPSpin`** - Generador de PINs WPS
- **`NetworkAddress`** - Gestión de direcciones de red
- **`ConnectionStatus`** - Estados de conexión WPS
- **`BruteforceStatus`** - Estados de ataque
- **`PixiewpsData`** - Datos para Pixie Dust
- **`WiFiScanner`** - Escáner de redes WiFi
- **`AndroidNetwork`** - Gestión WiFi en Android

### Funciones Clave:

- `save_entry()` - Guarda credenciales crackeadas
- `isAndroid()` - Detecta entorno Android
- `recvuntil()` - Lee datos del socket
- `get_hex()` - Conversión hexadecimal
- `ifaceUp()` - Control de interfaces de red
- `die()` - Manejo de errores fatales
- `usage()` - Ayuda del comando

---

## 📜 Licencia

**MIT License** - Código original por @anbuinfosec

---

## ⚠️ Disclaimer Legal

**SOLO PARA PROPÓSITOS EDUCATIVOS Y TESTING AUTORIZADO**

- ✅ Usa SOLO en redes que posees
- ✅ O con permiso explícito por escrito
- ❌ Acceso no autorizado es ILEGAL
- ❌ Autor NO responsable por mal uso

El uso indebido de esta herramienta puede resultar en:
- Cargos criminales
- Multas significativas
- Prisión

**Úsalo responsablemente.**

---

## 📞 Soporte

### Problemas con Samsung A03 Core:
Ver `SOLUCION_SAMSUNG_A03.md`

### Otros problemas:
1. Verifica que tengas root
2. Verifica que wpa_supplicant esté instalado
3. Verifica que WiFi esté habilitado
4. Lee la documentación completa en `replit.md`

---

## 🙏 Créditos

- **Autor original:** @anbuinfosec
- **GitHub:** https://github.com/anbuinfosec/wipwn
- **Desofuscación:** Proceso automatizado + análisis manual
- **Parche Samsung A03:** Análisis de bytecode y testing

---

## 🔗 Enlaces

- [Repositorio Original](https://github.com/anbuinfosec/wipwn)
- [Documentación WPA Supplicant](https://w1.fi/wpa_supplicant/)
- [Pixiewps Tool](https://github.com/wiire-a/pixiewps)

---

**Versión:** 3.0.0 Enhanced Edition (Desofuscada)  
**Última actualización:** Noviembre 2025

---

🚀 **¡El código está listo para ser modificado y personalizado!**
