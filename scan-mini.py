#!/usr/bin/env python3
import os
import sys

# Author: Syed Baijid
# Version: 1.0
# Description: Fast scan version of Scan-Max. Takes 2-10 minutes.

def run_mini_scan(target):
    print("\n" + "="*60)
    print(f" SCAN-MINI: Fast Recon started for: {target}")
    print("="*60)
    print("[*] Estimated Time: 2-10 minutes (Depends on network)")

    # Step 1: Fast Scan
    print("\n[1] Running Fast Scan (Top 100 ports)...")
    os.system(f"nmap -F -Pn {target}")

    # Step 2: Aggressive Scan
    print("\n[2] Running Aggressive Scan (OS, Version, Traceroute)...")
    os.system(f"nmap -A -Pn -T4 {target}")

    # Step 3: Vuln Check
    print("\n[3] Checking for Vulnerabilities (NSE Scripts)...")
    os.system(f"nmap --script vuln -Pn {target}")

    # Step 4: Evasion Scan
    print("\n[4] Running Firewall Evasion & Fragmented Scan...")
    os.system(f"nmap -sS -f -Pn {target}")

    print("\n" + "="*60)
    print("[!] Scan-Mini Finished. Check results above.")
    print("="*60)

if __name__ == "__main__":
    target_ip = input("Enter Target IP: ").strip()
    if target_ip:
        try:
            run_mini_scan(target_ip)
        except KeyboardInterrupt:
            print("\n[!] Stopped by user.")
            sys.exit()
    else:
        print("[!] Target IP is required.")
