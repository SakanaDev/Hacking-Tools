import subprocess
import platform
import re
import sys

# ANSII Color Codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'
BOLD = '\033[1m'

def get_ttl(ip_address: str) -> int: 
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    proc = subprocess.Popen(['ping', param, '1', ip_address], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    
    ttl = re.findall(r'TTL=\d+', str(out))
    
    if ttl:
        ttl = re.findall(r'\d+', ttl[0])[0]
        return int(ttl)
    else:
        False
    

def get_os(ttl: int) -> str:
    if ttl >= 0 and ttl <= 64:
        return 'Linux'
    if ttl >= 65 and ttl <= 128:
        return 'Windows'
    else:
        return 'Not Found'
        
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"\n[!] Use: python3 {sys.argv[0]} <ip_address>\n")
        sys.exit(1)
    
    ip_address = sys.argv[1]
    
    print(f"{CYAN}[+] Pinging {ip_address}...{RESET}")

    ttl = get_ttl(ip_address)
    
    if (ttl):
        os_name = get_os(ttl)
        print(f"{GREEN}[✓] TTL Detected: {ttl}{RESET}")
        print(f"{GREEN}[✓] Likely OS: {BOLD}{os_name}{RESET}")
    else:
         print(f"{RED}[!] Failed to detect TTL. Host unreachable or not responding.{RESET}")
