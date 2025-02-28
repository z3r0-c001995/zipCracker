# 🔐 Zip & RAR Password Cracker

A Python script to crack password-protected ZIP and RAR files using a dictionary (wordlist) attack.

---

## 🚀 Features
✅ Supports ZIP and RAR formats  
✅ Uses a wordlist for password cracking  
✅ Displays a progress bar using `tqdm`  
✅ Works with Python 3+  

---

## 📌 Requirements
Ensure you have the following installed:

🔹 Python 3+  
🔹 `tqdm` (for progress bar)  
🔹 `rarfile` (for RAR support)  
🔹 `unrar` (must be installed and in system PATH for RAR extraction)  

### 📥 Install dependencies:
```bash
pip install tqdm rarfile
```

---

## 🎯 Installation
Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/z3r0-c001995/zipCracker.git
cd zipCracker
```

Then install the required dependencies:
```bash
pip install -r requirements.txt
```

---

## 🎯 Usage
Run the script with the following command:
```bash
python crack.py <file> <wordlist>
```

### 🔍 Example:
```bash
python crack.py secret.zip rockyou.txt
```

### 📝 Arguments:
📂 `<file>` : Path to the ZIP or RAR file  
📖 `<wordlist>` : Path to the password wordlist file  

---

## ⚙️ How It Works
1️⃣ The script reads passwords from the provided wordlist.  
2️⃣ It attempts to extract the contents using each password.  
3️⃣ If a correct password is found, it prints the password and stops.  
4️⃣ If no password is found, it displays a failure message.  

---

## 📌 Notes
⚠️ Cracking time depends on the wordlist size.  
⚠️ The script does **not** support brute-force attacks.  
⚠️ Ensure `unrar` is installed and in the system's PATH for RAR files.  

---

## ⚠️ Disclaimer
🚨 This tool is intended for educational and legal purposes only. Do **not** use it for unauthorized access. The developer is not responsible for any misuse. 🚨

---

## 📜 License
This project is licensed under the MIT License. 📝

