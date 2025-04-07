# Python Project with Virtual Environment

This project demonstrates how to use Python virtual environments, manage dependencies, and best practices for working with Python packages.

## 1. How to Run the Project on Another Machine

If you clone your project directory to another machine, you’ll need to recreate the virtual environment and install the necessary dependencies again. Here’s how you can do that:

---

### Steps:

1. **Clone the repository**:
   First, clone the repository to your new machine:

   ```
   git clone <your-repository-url>
   ```

---

2. **Navigate to the project directory: Once cloned, navigate into the project folder**

   ```
   cd <FolderName>
   ```

---

3. **Create a virtual environment: On the new machine, you need to recreate the virtual environment (since .venv is specific to the machine and shouldn't be pushed to GitHub).**
   ```
   python3 -m venv .venv
   ```

---

4. **Activate the virtual environment: Now, activate the virtual environment:**
   ```
   On macOS/Linux : source .venv/bin/activate
   On Windows : .venv\Scripts\activate
   ```

---

5. **Install dependencies: If you’re using requirements.txt (which is the recommended practice), you can install the necessary packages listed in that file:**
   ```
   pip install -r requirements.txt
   ```

---

6. **Run the Python script: Once the environment is set up, you can run your Python script as usual:**
   ```
   python3 <FileName>.py
   ```

---

## Remove .venv from Git (if it was accidentally added earlier)
    ```
    git rm -r --cached .venv
    git commit -m "Remove .venv from the repository"
    git push
    ```
