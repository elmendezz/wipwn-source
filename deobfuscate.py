#!/usr/bin/env python3
import base64, zlib, marshal, sys

# Read the obfuscated file
with open('main.py', 'r') as f:
    content = f.read()

# Execute only the variable definitions
exec(content.split('exec(nnWccKBCIQPq)')[0])

# Now deobfuscate step by step
print("[+] Deobfuscating main.py...")

# Reconstruct the obfuscated data
hXiyYtr_TVbn = b''.join([CKessAk_, WTamYVwg, FiTeMOpp, oYtEAkSZ, dsHRfEwi, AhyZbxoa, cBgjHgoJ, KBxZetqB, cYS_eLyd, WbATtMcV, MaTspqgd, PKmisNsc, mVCOitBN, OWSjGhmb, uNXGTfuU, XJpvWzIa, aOveiZpd, ZS_cRFeU, bw_aaABV, xDnp_AgP, GzBGlATG, hZlvZelX, oRYthPdI, wYZIoABP, hTdjjvpz, pHvYsYso, TedtKzkT, RYkFgOCL, ebuBfxSH, bxgyNuYw, KLLtrUJm, UyaRZZGB, vnMohDog, UMekHemK, iSHunTHM, TbYGlQSE, KpEf_VjN, FBGihKhQ, CmhOdBf_, MsdSpHSd, hERWmGpf, mQDlCFuZ, pLAsNdtt, wSLCgtxE, xlnVfKGe, OlGDynjP, UhMLCqLm, DInYFXkl, hmYyGsHZ, iRToVbYD, neSYihwq, JPbhtAg_, MRGjhJDW, PEIq_kKW, uaMC_mLe, PBarqYRF, qseuGQnL, IfzuoOwn, iUcEmMwA, GMS_lIKu, Fqwgjazy, AmwAiYfh, mcQPyQTn, mNWYuWgv, wLAzTDjs, iDzbzPfC, tJvAzJNj, muKqdqCF, OaOxWDur, PQ_tAgmn, jvydrkoa, fvBSAAkl, FnQZaTxD, LzKID_Ra, btqWMLgZ, PIijshQC, LRaSeYZ_, MqdhFBSG, YlqNAdPJ, nnDybuEX, xLBVMcWD, wacuA_Gr, qu_jGTIj, pnOiwlrB, gIxrSiXL, pQFPgVdY, _jESeVyE, RQbGwRFG, WLIPocas, dTZBKqJr, WwSnalEi, liaVJWzu, ZDiWkenc, UICotXdS, ROhPKGzY, gfqeETcA, eUegOCtI, GmFtpnUd, vBmYgPNR, wsFjAURs, OTMWDoNP, SYizjCzY, bFcquRtU, agKukoEa, ojTDlpuP, WSPhaoPV, YeOWBUpO, tfUDnyeD, mukTyCvi, CdNUWOaC, UkhWEgmP, TOjsQ_pb, Zetcoygy])

print("[+] Step 1: Reverse and base64 decode...")
hXiyYtr_TVbn = base64.b64decode(hXiyYtr_TVbn[::-1])

print("[+] Step 2: Zlib decompress...")
hXiyYtr_TVbn = zlib.decompress(hXiyYtr_TVbn)

print("[+] Step 3: Reverse and base64 decode again...")
hXiyYtr_TVbn = base64.b64decode(hXiyYtr_TVbn[::-1])

print("[+] Step 4: Zlib decompress again...")
hXiyYtr_TVbn = zlib.decompress(hXiyYtr_TVbn)

print("[+] Step 5: Reverse and base64 decode...")
hXiyYtr_TVbn = base64.b64decode(hXiyYtr_TVbn[::-1])

print("[+] Step 6: Base32 decode...")
hXiyYtr_TVbn = base64.b32decode(hXiyYtr_TVbn)

print("[+] Step 7: XOR decrypt...")
hXiyYtr_TVbn = pumCwrHgdplf(hXiyYtr_TVbn, bytes(BnUibgPbluZA))

print("[+] Step 8: Base85 decode...")
hXiyYtr_TVbn = base64.b85decode(hXiyYtr_TVbn)

print("[+] Step 9: Zlib decompress...")
hXiyYtr_TVbn = zlib.decompress(hXiyYtr_TVbn)

print("[+] Step 10: XOR decrypt with final key...")
hXiyYtr_TVbn = pumCwrHgdplf(hXiyYtr_TVbn, bytes(MgPUggkKT_ir))

print("[+] Step 11: Marshal loads to get bytecode...")
nnWccKBCIQPq = marshal.loads(hXiyYtr_TVbn)

print("[+] Step 12: Decompiling bytecode...")
# Write the decompiled code
import dis
import types

# Save the code object
with open('main_deobfuscated.pyc', 'wb') as f:
    f.write(hXiyYtr_TVbn)

print("[+] Bytecode saved to main_deobfuscated.pyc")
print("[+] Attempting to extract source code...")

# Try to decompile using dis
print("\n[+] Disassembling bytecode (this is readable but not source code)...")
with open('main_disassembled.txt', 'w') as f:
    f.write("# Disassembled bytecode from main.py\n")
    f.write("# This is not the original source but shows the operations\n\n")
    import io
    import contextlib
    
    stream = io.StringIO()
    with contextlib.redirect_stdout(stream):
        dis.dis(nnWccKBCIQPq)
    
    f.write(stream.getvalue())

print("[+] Disassembly saved to main_disassembled.txt")
print("\n[!] To get readable source code, we need a decompiler like uncompyle6 or decompyle3")
print("[!] Installing decompiler...")
