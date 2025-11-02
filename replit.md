# WIPWN - WiFi Pentesting Framework (Desofuscado)

## 📋 Resumen del Proyecto

Este es **WIPWN**, un framework profesional de auditoría de seguridad WiFi, completamente desofuscado del código original que estaba ofuscado con ANBU Obfuscator v3.0.

### ⚠️ IMPORTANTE: Este proyecto NO puede ejecutarse en Replit

WIPWN es una herramienta de pentesting WiFi diseñada específicamente para:
- **Dispositivos Android** con Termux
- Requiere acceso a **interfaces WiFi físicas** (wlan0)
- Necesita **permisos root/superuser**
- Requiere herramientas de sistema: `wpa_supplicant`, `pixiewps`

Por estas razones, **no es posible ejecutar este proyecto en el entorno cloud de Replit**.

## 📁 Archivos Desofuscados

### Archivos Principales

1. **`wipwn_editable.py`** ⭐ - Versión completamente desofuscada y editable
   - Código fuente legible
   - Todas las funciones y clases extraídas
   - Lista para editar y modificar

2. **`main_deobfuscated.py`** - Primera versión desofuscada con bytecode
3. **`main_fully_editable.py`** - Versión alternativa editable
4. **`main_source_reconstructed.py`** - Reconstrucción del código fuente

### Archivos de Análisis

- **`main_code.pyc`** - Bytecode extraído del código ofuscado
- **`main_full_disassembly.txt`** - Desensamblado completo del bytecode
- **`main.py`** - Archivo original ofuscado (mantener como referencia)

## 🔧 Estructura del Código

### Funciones Principales Detectadas:

- `save_entry()` - Guarda credenciales crackeadas
- `isAndroid()` - Detecta si se ejecuta en Android
- `recvuntil()` - Lee datos del socket hasta un patrón
- `get_hex()` - Convierte datos a hexadecimal
- `ifaceUp()` - Levanta/baja interfaces de red
- `die()` - Maneja errores fatales
- `usage()` - Muestra ayuda del comando

### Clases Principales:

- `WPSpin` - Generador de PINs WPS
- `NetworkAddress` - Manejo de direcciones de red
- `ConnectionStatus` - Estados de conexión WPS
- `BruteforceStatus` - Estados de ataque bruteforce
- `PixiewpsData` - Datos para ataque Pixie Dust
- `WiFiScanner` - Escáner de redes WiFi
- `AndroidNetwork` - Gestión de redes en Android

## 🛠️ Cómo Usar (En Android/Termux)

```bash
# En tu dispositivo Android con Termux:
python3 wipwn_editable.py -i wlan0 -b [BSSID] [opciones]

# Opciones principales:
-i, --interface  : Interfaz de red (ej: wlan0)
-b, --bssid      : BSSID del router objetivo
-p, --pin        : PIN específico a probar
-K, --pixie-dust : Ataque Pixie Dust
-B, --bruteforce : Ataque de fuerza bruta
```

## 🔧 Problemas Conocidos

### Samsung A03 Core (modelo a032f) - Error wlan0

**Síntoma:** `Could not read interface wlan0 flags: No such device`

**Causa:** El código deshabilita WiFi antes de ejecutar wpa_supplicant, causando que la interfaz wlan0 desaparezca.

**Solución:** 
- Usa `wipwn_samsung_a03_fix.py` en lugar de `wipwn_editable.py`
- Ver guía completa en `SOLUCION_SAMSUNG_A03.md`

**Dispositivos afectados:**
- Samsung A03 Core (chipset MediaTek)
- Posiblemente otros dispositivos MediaTek

## 📝 Modificar el Código

Ahora que el código está completamente desofuscado, puedes:

1. **Agregar nuevas funciones** en `wipwn_editable.py`
2. **Modificar algoritmos** de generación de PINs
3. **Añadir soporte** para nuevos routers
4. **Personalizar la salida** y reportes
5. **Mejorar la lógica** de ataque

### Ejemplo: Agregar nueva función

```python
def mi_nueva_funcion(parametro):
    """
    Descripción de tu función
    """
    # Tu código aquí
    print(f"Procesando: {parametro}")
    return resultado
```

## 🚀 Desofuscación Completada

### Proceso de Desofuscación:

El código original pasó por 10 capas de ofuscación:
1. XOR encryption (clave de 32 bytes)
2. Zlib compression
3. Base85 encoding  
4. XOR encryption (clave de 16 bytes)
5. Base32 encoding
6. Base64 encoding (reverso)
7. Zlib compression
8. Base64 encoding (reverso)
9. Zlib compression
10. Base64 encoding (reverso) + Marshal (bytecode)

**Todas las capas han sido removidas exitosamente.**

## 📜 Licencia

MIT License - Original por @anbuinfosec

## ⚠️ Disclaimer Legal

Este código es solo para propósitos educativos y testing autorizado. El uso en redes sin permiso es ILEGAL.

---

**Nota**: Si necesitas ejecutar este código, usa un dispositivo Android con Termux instalado y los permisos necesarios.
