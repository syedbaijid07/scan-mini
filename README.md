# Scan-Max & Scan-Mini 🚀

I made these scripts because I wanted to automate my Nmap workflow. Instead of typing complex commands every time, I can just run one of these scripts.

## Which one to use?
- **Scan-Max.py:** This is the deep version. It runs 50 different scan types. Use this when you need every bit of info.  
  *Time:* **30-40 minutes**.
- **Scan-Mini.py:** This is the fast version. It covers the most important things like OS detection, Vulns, and Stealth.  
  *Time:* **2-10 minutes** (depending on the network speed).

## Setup
1. Clone it: `git clone https://github.com/YOUR_USERNAME/Scan-Max.git`
2. Run Scan-Mini: `sudo python3 scan-mini.py`
3. Run Scan-Max: `sudo python3 scan-max.py`

## Requirements
- Linux OS (Kali, Ubuntu, etc.)
- Python 3
- Nmap installed (`sudo apt install nmap`)

**Legal Warning:** Do not use this for illegal stuff. Only for learning and authorized testing.

**Created by:** Syed Baijid
