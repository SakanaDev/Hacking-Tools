# 🖥️ OS Detection via TTL

A simple Python script to **detect the likely operating system of a remote host** using its IP address by analyzing the TTL (Time-To-Live) value in the response from a ping request.

## 🚀 Purpose

This script helps identify whether a remote system is likely running **Linux** or **Windows**, based on the TTL value returned in a ping reply. Different operating systems set different default TTL values in their IP stack, which can be used as an approximate indicator of the OS.

## 🛠️ How It Works

- Sends a single ping to the target IP address.
- Extracts the TTL value from the ping response.
- Uses TTL ranges to guess the operating system:
  - TTL 0–64 → Likely **Linux**
  - TTL 65–128 → Likely **Windows**
  - TTL >128 or undetectable → **Unknown or Not Found**

> ⚠️ **Note:** TTL can be affected by firewalls, routers, or customized system settings. This is a heuristic-based method, not guaranteed to be accurate.

## 📦 Requirements

- Python 3.x
- Works on **Linux**, **macOS**, and **Windows**

## 📄 Usage

```bash
python3 whichSystem.py <ip_address>
```

**Example**
```python
python3 detect_os.py 192.168.1.1
```

**Sample Output**
```python
[+] Pinging 192.168.1.1...
[✓] TTL Detected: 128
[✓] Likely OS: Windows
```

## 🎨 Terminal Colors
The script uses ANSI color codes for clearer and more colorful CLI output:
- ✅ Green: Successful detection
- ⚠️ Yellow: Warnings
- ❌ Red: Errors

## ⚙️ Notes
- Ensure the target host allows ICMP (ping) requests.
- Requires appropriate privileges to run ping commands (especially on Linux/macOS).
