# 🌳 BST Guessing App

An interactive **Binary Search Tree (BST) visualization and guessing application** built using **Python, Tkinter, and Matplotlib**.
This application allows users to **guess a number and visually observe how a Binary Search Tree search algorithm works step-by-step**.

The project helps demonstrate **data structure concepts**, particularly how **Binary Search Trees traverse nodes during search operations**.

---

# 📌 Project Overview

The **BST Guessing App** is designed to help users understand the working of a **Binary Search Tree search algorithm** through visual animation.

Users enter a number to search in the tree, and the application visually shows:

* Nodes visited during the search
* Direction of traversal (left or right)
* Number of attempts taken to find the value
* Final result once the value is found

This makes the learning process **interactive and easy to understand**, especially for students studying **Data Structures and Algorithms**.

---

# 🎯 Features

✅ Interactive **GUI application** built with Tkinter
✅ **Binary Search Tree visualization**
✅ Step-by-step **search animation**
✅ Displays **visited nodes and attempts**
✅ Real-time **algorithm traversal simulation**
✅ Educational tool for learning **BST search logic**

---

# 🧠 How the Application Works

The application simulates the process of searching for a value in a **Binary Search Tree**.

### Step 1 — Tree Creation

A Binary Search Tree is constructed where:

* Left child contains values **smaller than the parent**
* Right child contains values **greater than the parent**

### Step 2 — User Input

The user enters a number they want to search for in the BST.

### Step 3 — Search Begins

The algorithm starts searching from the **root node**.

### Step 4 — Traversal Logic

At each step:

* If `guess < current node`, the algorithm moves **left**
* If `guess > current node`, the algorithm moves **right**
* If `guess == current node`, the value is **found**

### Step 5 — Visualization

The application highlights:

* Current node being visited
* Traversal direction
* Attempt number

### Step 6 — Final Result

Once the number is found, the app displays:

```
FOUND <number> in <attempts> attempts
```

---

# 🛠️ Tech Stack

| Technology      | Purpose                           |
| --------------- | --------------------------------- |
| Python          | Core programming language         |
| Tkinter         | GUI development                   |
| Matplotlib      | Tree visualization                |
| Data Structures | Binary Search Tree implementation |

---

# 📂 Project Structure

```
BST_Guessing_App
│
├── bst_gui_app.py
├── README.md
└── requirements.txt
```

---

# ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/BST-Guessing-App.git
```

---

### 2️⃣ Navigate to the Project Folder

```bash
cd BST-Guessing-App
```

---

### 3️⃣ Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

---

### 4️⃣ Install Dependencies

```bash
pip install matplotlib
```

---

# ▶️ Running the Application

Run the following command:

```bash
python bst_gui_app.py
```

The **GUI window will open**, allowing you to interact with the BST guessing application.

---

# 📊 Learning Objectives

This project demonstrates the following concepts:

* Binary Search Tree (BST)
* Tree traversal logic
* Algorithm visualization
* GUI development in Python
* Interactive learning tools for data structures

---

# 🚀 Future Improvements

Possible enhancements for this project include:

* Add **tree insertion visualization**
* Allow **dynamic BST generation**
* Improve graphical visualization of nodes
* Add **web-based version using Streamlit or React**
* Add **step-by-step traversal explanation panel**

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve the project:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a Pull Request

---

# 👨‍💻 Author

**Shivam Kumar**

GitHub:
https://github.com/shivam-9s

---

# ⭐ Support

If you find this project useful, please consider **starring the repository** to support the work.
