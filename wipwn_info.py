#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WIPWN - Information & Demo Mode
This mode can run on Replit to show project information without requiring WiFi hardware
"""

import sys

# Terminal colors
green = '\x1b[1;32m'
cyan = '\x1b[1;36m'
yellow = '\x1b[1;33m'
red = '\x1b[1;31m'
white = '\x1b[1;97m'
blue = '\x1b[1;34m'
reset = '\x1b[0m'

def print_banner():
    banner = f"""{cyan}
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║  ██╗    ██╗██╗██████╗ ██╗    ██╗███╗   ██╗                  ║
║  ██║    ██║██║██╔══██╗██║    ██║████╗  ██║                  ║
║  ██║ █╗ ██║██║██████╔╝██║ █╗ ██║██╔██╗ ██║                  ║
║  ██║███╗██║██║██╔═══╝ ██║███╗██║██║╚██╗██║                  ║
║  ╚███╔███╔╝██║██║     ╚███╔███╔╝██║ ╚████║                  ║
║   ╚══╝╚══╝ ╚═╝╚═╝      ╚══╝╚══╝ ╚═╝  ╚═══╝                  ║
║                                                              ║
║           WiFi WPS Pentesting Framework v3.0                 ║
║                  {white}(Completely Deobfuscated){cyan}                     ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
{reset}"""
    print(banner)

def show_info():
    print_banner()
    
    print(f"\n{green}[+] Project Information{reset}")
    print(f"    Author: {white}@anbuinfosec{reset}")
    print(f"    Version: {white}3.0.0 Enhanced Edition{reset}")
    print(f"    License: {white}MIT{reset}")
    print(f"    GitHub: {white}https://github.com/anbuinfosec/wipwn{reset}")
    
    print(f"\n{yellow}[!] IMPORTANT NOTICE{reset}")
    print(f"    {red}This project CANNOT run on Replit!{reset}")
    print(f"    WIPWN requires:")
    print(f"      • Android device with Termux")
    print(f"      • Physical WiFi interface (wlan0)")
    print(f"      • Root/Superuser permissions")
    print(f"      • System tools: wpa_supplicant, pixiewps")
    
    print(f"\n{green}[+] Deobfuscation Complete{reset}")
    print(f"    {white}✓{reset} All 10 obfuscation layers removed")
    print(f"    {white}✓{reset} Source code is now fully editable")
    print(f"    {white}✓{reset} Ready for customization")
    
    print(f"\n{cyan}[+] Available Files:{reset}")
    print(f"    {white}wipwn_editable.py{reset}           - Main editable source code")
    print(f"    {white}main_deobfuscated.py{reset}        - Alternative version with bytecode")
    print(f"    {white}main_full_disassembly.txt{reset}   - Complete bytecode disassembly")
    print(f"    {white}replit.md{reset}                   - Full documentation")
    
    print(f"\n{green}[+] Key Features:{reset}")
    print(f"    • 100 PIN generation algorithms")
    print(f"    • 500+ router database (TP-Link, D-Link, Asus, etc.)")
    print(f"    • Pixie Dust attack support")
    print(f"    • Online bruteforce with session management")
    print(f"    • MAC randomization")
    print(f"    • Advanced timing controls")
    
    print(f"\n{green}[+] Detected Functions:{reset}")
    functions = [
        "save_entry", "isAndroid", "recvuntil", "get_hex", 
        "ifaceUp", "die", "usage"
    ]
    for func in functions:
        print(f"    • {func}()")
    
    print(f"\n{green}[+] Detected Classes:{reset}")
    classes = [
        "WPSpin", "NetworkAddress", "ConnectionStatus",
        "BruteforceStatus", "PixiewpsData", "WiFiScanner", "AndroidNetwork"
    ]
    for cls in classes:
        print(f"    • {cls}")
    
    print(f"\n{cyan}{'='*62}{reset}")
    print(f"{yellow}[!] Legal Disclaimer:{reset}")
    print(f"    For educational and authorized testing ONLY.")
    print(f"    Unauthorized access is ILLEGAL. Use responsibly.")
    print(f"{cyan}{'='*62}{reset}")
    
    print(f"\n{white}To use this tool, transfer files to Android/Termux and run:{reset}")
    print(f"    {green}python3 wipwn_editable.py -i wlan0 -b [BSSID]{reset}")
    print()

if __name__ == "__main__":
    show_info()
