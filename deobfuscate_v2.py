#!/usr/bin/env python3
import base64, zlib, marshal
import sys
import os

print("[+] Reading obfuscated main.py...")

# Read the entire file and execute everything except the final exec
with open('main.py', 'r') as f:
    content = f.read()

# Split before the final exec statement
code_before_exec = content.split('exec(nnWccKBCIQPq)')[0]

print("[+] Executing deobfuscation chain...")

# Execute all the variable definitions and deobfuscation steps
exec(code_before_exec)

# Now nnWccKBCIQPq contains the deobfuscated bytecode
print(f"[+] Bytecode object type: {type(nnWccKBCIQPq)}")
print(f"[+] Bytecode size: {len(marshal.dumps(nnWccKBCIQPq))} bytes")

# Save the bytecode
print("[+] Saving bytecode to main_code.pyc...")
with open('main_code.pyc', 'wb') as f:
    # Write Python 3.11 pyc header (magic number + timestamp + size)
    f.write(b'\x55\x0d\x0d\x0a')  # Python 3.11 magic
    f.write(b'\x00' * 12)  # Timestamp and size fields
    marshal.dump(nnWccKBCIQPq, f)

print("[+] Bytecode saved!")
print("[+] Now attempting to decompile...")

# Try to use uncompyle6 or decompyle3
try:
    import uncompyle6
    print("[+] uncompyle6 found, decompiling...")
    import io
    import sys
    output = io.StringIO()
    uncompyle6.decompile(3.11, nnWccKBCIQPq, output)
    decompiled = output.getvalue()
    with open('main_deobfuscated.py', 'w') as f:
        f.write(decompiled)
    print("[+] SUCCESS! Code saved to main_deobfuscated.py")
except ImportError:
    print("[!] uncompyle6 not installed, trying decompyle3...")
    try:
        import decompyle3
        import io
        output = io.StringIO()
        decompyle3.decompile(3.11, nnWccKBCIQPq, output)
        decompiled = output.getvalue()
        with open('main_deobfuscated.py', 'w') as f:
            f.write(decompiled)
        print("[+] SUCCESS! Code saved to main_deobfuscated.py")
    except ImportError:
        print("[!] No decompiler found. Installing uncompyle6...")
        os.system('pip install -q uncompyle6')
        try:
            import uncompyle6
            import io
            output = io.StringIO()
            uncompyle6.decompile(3.11, nnWccKBCIQPq, output)
            decompiled = output.getvalue()
            with open('main_deobfuscated.py', 'w') as f:
                f.write(decompiled)
            print("[+] SUCCESS! Code saved to main_deobfuscated.py")
        except Exception as e:
            print(f"[!] Decompilation failed: {e}")
            print("[!] Trying pycdc instead...")
            
print("\n[+] Deobfuscation complete!")
