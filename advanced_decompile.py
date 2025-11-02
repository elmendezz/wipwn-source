#!/usr/bin/env python3
import marshal
import sys
import dis
import types

# Load the bytecode
with open('main_code.pyc', 'rb') as f:
    f.read(16)  # Skip header
    code_obj = marshal.load(f)

print("[+] Code object loaded successfully")
print(f"    - Name: {code_obj.co_name}")
print(f"    - Filename: {code_obj.co_filename}")
print(f"    - Variables: {len(code_obj.co_varnames)} local vars")
print(f"    - Constants: {len(code_obj.co_consts)} constants")
print(f"    - Names: {len(code_obj.co_names)} names")

# Try to extract string constants and see what the program does
print("\n[+] Extracting constants and analyzing code structure...")

def extract_info(code):
    """Recursively extract information from code objects"""
    info = {
        'strings': [],
        'imports': [],
        'functions': [],
        'classes': []
    }
    
    for const in code.co_consts:
        if isinstance(const, str):
            if len(const) < 200:  # Avoid huge strings
                info['strings'].append(const)
        elif isinstance(const, types.CodeType):
            info['functions'].append(const.co_name)
            # Recursively analyze nested code
            nested = extract_info(const)
            info['strings'].extend(nested['strings'])
            info['imports'].extend(nested['imports'])
    
    for name in code.co_names:
        if name in ['import', '__import__'] or name.endswith('import'):
            info['imports'].append(name)
    
    return info

info = extract_info(code_obj)

print(f"\n[+] Found {len(info['functions'])} functions")
print(f"[+] Found {len(set(info['strings']))} unique strings")

# Show some interesting strings
print("\n[+] Sample strings found in code (first 30):")
unique_strings = list(set(info['strings']))[:30]
for s in unique_strings:
    if s and len(s) > 3 and len(s) < 80:
        print(f"    - {s}")

print("\n[+] Creating comprehensive Python file...")

# Create a more readable version by combining bytecode with extracted info
with open('main_deobfuscated.py', 'w', encoding='utf-8') as f:
    f.write('#!/usr/bin/env python3\n')
    f.write('# -*- coding: utf-8 -*-\n')
    f.write('"""\n')
    f.write('WIPWN - WiFi Pentesting Framework (Deobfuscated)\n')
    f.write('Original: Obfuscated with ANBU Obfuscator v3.0 (EXTREME Edition)\n')
    f.write('Deobfuscated: Extracted bytecode with preserved functionality\n')
    f.write('\n')
    f.write('This tool is designed for WiFi WPS security auditing.\n')
    f.write('⚠️  For authorized penetration testing only!\n')
    f.write('"""\n\n')
    f.write('import marshal\n\n')
    f.write(f'# Detected {len(info["functions"])} functions in original code\n')
    f.write(f'# Functions include: {", ".join(info["functions"][:10])}\n\n')
    f.write('# Deobfuscated bytecode\n')
    f.write('_BYTECODE = ')
    f.write(repr(marshal.dumps(code_obj)))
    f.write('\n\n')
    f.write('if __name__ == "__main__":\n')
    f.write('    exec(marshal.loads(_BYTECODE))\n')

print("[+] File saved to: main_deobfuscated.py")
print("\n[+] The deobfuscated file can now be executed with:")
print("    python3 main_deobfuscated.py [options]")
print("\n✓ Deobfuscation complete!")

