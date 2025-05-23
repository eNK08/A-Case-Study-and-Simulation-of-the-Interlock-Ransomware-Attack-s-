# A Case Study and Simulation of the Interlock Ransomware Attack(s)

**By **[Nikoloz Kurtanidze](https://github.com/eNK08)**** and **[James McGrath](https://github.com/JMcGrath2025)**  

---

## Overview

This project presents a technical case study and experimental demonstration of the **Interlock Ransomware group**, an emerging threat actor publicly identified in 2024. We examined their tactics, techniques, and procedures (TTPs), which include phishing, LOLBins abuse, remote access tools, and custom encryption using LibTomCrypt.

The simulation aims to **recreate a ransomware attack workflow** in a safe, ethical environment using Python, VirtualBox, and GoPhish. We did not deploy actual malware—this is a strictly educational demonstration.

---

## Paper

The full term paper, containing research, threat modeling, methodology, tools used, and results, can be found in the `/paper` directory:

---

## Demonstration Scripts

Located in the `/demo` directory:

- `NSPyLogger.py`  
    A Python keylogger script that silently records keystrokes and stores them in `log.txt`. Pressing `ESC` ends logging.
    
- `PyEncrypter.py`  
    A Python script that encrypts a file using AES (CBC mode), simulating ransomware encryption.
    
- `PyDecrypter.py`  
    The corresponding decryption tool for recovering the encrypted file using the original key and IV.
    

---

## Technical Summary

- **Attack Simulation Flow**:
    
    1. Simulated phishing campaign via GoPhish.
        
    2. Remote access using RustDesk (posing as IT support).
        
    3. Transfer and execution of `NSPyLogger.py` on victim VM.
        
    4. Exfiltration and encryption of stolen files using custom Python tools.
        
- **Environment**:
    
    - Host: Windows 11
        
    - VM: Windows 10 (via VirtualBox)
        
    - Email simulation: Mailtrap.io
        
    - Tools: GoPhish, RustDesk, Python 3
        
- **Constraints**:
    
    - No real malware or Trojan use (legal/ethical)
        
    - Resource-limited VM environment
        
    - No actual data theft or system damage
        

---

## Authors

| Name               | Role                       | GitHub                                           |
| ------------------ | -------------------------- | ------------------------------------------------ |
| Nikoloz Kurtanidze | Research, Writing, Testing | [@eNK08](https://github.com/eNK08)               |
| James McGrath      | Research, Development      | [@JMcGrath2025](https://github.com/JMcGrath2025) |

---

## License

This project is licensed under the **MIT License**. See `LICENSE` for details.

---

## Disclaimer

This project is for **educational purposes only**. All tools and scripts included here were used in a **controlled lab environment**. We do **not** condone or support malicious use of this code or any related techniques.

---
