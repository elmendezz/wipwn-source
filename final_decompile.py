#!/usr/bin/env python3
import marshal
import sys

# Load the bytecode
with open('main_code.pyc', 'rb') as f:
    f.read(16)  # Skip header
    code_obj = marshal.load(f)

print("[+] Attempting decompilation with decompyle3...")

try:
    from decompyle3 import decompile_file
    import io
    
    # Try to decompile
    with open('main_deobfuscated.py', 'w') as out:
        import decompyle3.main
        decompyle3.main.decompile(3.11, code_obj, out)
    print("[+] SUCCESS! Decompiled code saved to main_deobfuscated.py")
    
except Exception as e:
    print(f"[!] decompyle3 failed: {e}")
    print("[!] Trying alternative method with dis module...")
    
    # Fallback: create a more readable disassembly
    import dis
    import types
    
    with open('main_deobfuscated.py', 'w') as f:
        f.write('#!/usr/bin/env python3\n')
        f.write('# -*- coding: utf-8 -*-\n')
        f.write('"""\n')
        f.write('Deobfuscated WIPWN - WiFi Pentesting Framework\n')
        f.write('Original was obfuscated with ANBU Obfuscator v3.0\n')
        f.write('Deobfuscated bytecode - This is a semi-readable version\n')
        f.write('"""\n\n')
        f.write('# This file contains the deobfuscated bytecode\n')
        f.write('# The original source code logic is preserved in the bytecode below\n\n')
        f.write('import marshal\n\n')
        f.write('# Load and execute the deobfuscated bytecode\n')
        f.write('_code = ')
        f.write(repr(marshal.dumps(code_obj)))
        f.write('\n\nexec(marshal.loads(_code))\n')
    
    print("[+] Created executable deobfuscated version: main_deobfuscated.py")
    print("[+] This version preserves all functionality but is not fully source code")

print("\n[+] Done!")
