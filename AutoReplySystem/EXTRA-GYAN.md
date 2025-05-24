# AutoReplySystem - GUI Access & pyautogui Setup on Linux

## 🛠 Requirements

Ensure your system has the necessary dependencies:

```bash
sudo apt-get update
sudo apt-get install python3-tk python3-dev
```

### 🧠 Understanding xhost and GUI Access
- pyautogui needs access to the graphical environment (X11). Linux systems protect this by default. You can control access using xhost.

---

## 🚫 DO NOT use this (unsafe):
```
xhost +
```
- ❗ This disables all access control. Any user or host can control your GUI. Avoid it unless you're testing in a secure, isolated environment.

### ✅ Safe alternative:
- Allow your local user access to the X server:

1. Find your username:
```
whoami
```

2. Allow that user:
```
xhost +SI:localuser:your_username
```

3. To revoke access later:
```
xhost -SI:localuser:your_username
```

4. To re-enable default access control:
```
xhost -
```

### xhost +	: ❌ Insecure – allows all access
### xhost -	: ✅ Re-enable access control
### xhost +SI:localuser:USERNAME	: ✅ Safely allow local user access
### xhost -SI:localuser:USERNAME	: 🔒 Revoke local user access
