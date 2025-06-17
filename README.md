# Password Generator

A simple, secure, and user-friendly password generator built with Python and Tkinter. Generate strong, customizable passwords with an intuitive graphical interface.

## Features

🔐 **Secure Password Generation**
- Cryptographically secure random password generation
- Customizable password length (6-32 characters)
- Multiple character set options

⚙️ **Customization Options**
- ✅ Uppercase letters (A-Z)
- ✅ Lowercase letters (a-z) 
- ✅ Numbers (0-9)
- ✅ Special symbols (!@#$%^&*()_+-=[]{}|;:,.<>?)

🖥️ **User-Friendly Interface**
- Clean, modern GUI built with Tkinter
- Interactive length slider
- One-click password copying to clipboard
- Real-time password preview

## Download & Usage

###Download Executable (Recommended)
1. Download `PasswordGenerator.exe` from the `dist/` folder
2. Double-click to run - no installation required!
3. Works on any Windows computer without Python

### Option 2: Run from Source Code
If you have Python installed:

```bash
# Clone or download this repository
cd "Python random num generator"

# Run the application
python password_generator.py
```

## How to Use

1. **Launch the application**
2. **Set your preferences:**
   - Adjust password length using the slider (6-32 characters)
   - Check/uncheck character types you want to include
3. **Click "GENERATE"** to create a new password
4. **Click "Copy"** to copy the password to your clipboard
5. **Paste anywhere** you need a secure password!

## Requirements

### For Executable Version
- Windows 7/8/10/11
- No additional software required

### For Source Code Version
- Python 3.7 or higher
- Required packages (install via `pip install -r requirements.txt`):
  - `pyperclip==1.8.2`

### Build Options Explained
- `--onefile`: Creates a single .exe file
- `--windowed`: Hides the console window (GUI only)
- `--name`: Sets the executable name

## Security Notes

🔒 **This password generator is designed with security in mind:**
- Uses Python's `random.choice()` with cryptographically secure randomness
- Passwords are generated locally on your machine
- No internet connection required
- No data is stored or transmitted

⚠️ **Best Practices:**
- Use passwords of at least 12 characters
- Include multiple character types for stronger passwords
- Don't reuse passwords across different accounts
- Store passwords in a reputable password manager


## Contributing

Feel free to fork this project and submit pull requests for any improvements:
- UI/UX enhancements
- Additional security features
- Cross-platform compatibility
- Bug fixes

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

If you encounter any issues or have suggestions:
1. Check that you have the required dependencies installed
2. Ensure you're using a supported Python version (3.7+)
3. Try rebuilding the executable if you modified the source code

---

**Made with ❤️ using Python & Tkinter**

*Generate strong passwords. Stay secure. 🔐* 
