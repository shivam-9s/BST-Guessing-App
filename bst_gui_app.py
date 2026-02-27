import tkinter as tk
from tkinter import messagebox

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# ---------------- NODE CLASS ---------------- #
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# ---------------- INSERT BST ---------------- #
def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root


# ---------------- DRAW TREE ---------------- #
def draw_tree(node, x, y, dx, visited, found_node, ax):
    if node is None:
        return

    # Node Color
    if node.value == found_node:
        color = "green"
    elif node.value in visited:
        color = "red"
    else:
        color = "lightblue"

    ax.text(
        x, y,
        str(node.value),
        fontsize=12,
        ha="center",
        va="center",
        bbox=dict(boxstyle="circle", facecolor=color)
    )

    # Left child
    if node.left:
        ax.plot([x, x - dx], [y, y - 1])
        draw_tree(node.left, x - dx, y - 1, dx / 2, visited, found_node, ax)

    # Right child
    if node.right:
        ax.plot([x, x + dx], [y, y - 1])
        draw_tree(node.right, x + dx, y - 1, dx / 2, visited, found_node, ax)


# ---------------- GUI APP ---------------- #
class BSTApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BST Guessing Visualizer App PRO")

        # BST root node
        self.tree_root = None

        # Search variables
        self.visited = []
        self.current = None
        self.guess = None
        self.attempts = 0

        # ---------------- GUI LAYOUT ---------------- #

        tk.Label(root, text="BST Visualizer Application",
                 font=("Arial", 16, "bold")).pack(pady=10)

        # Input Frame
        frame = tk.Frame(root)
        frame.pack()

        tk.Label(frame, text="Enter Number:", font=("Arial", 12)).grid(row=0, column=0)

        self.entry = tk.Entry(frame, font=("Arial", 12), width=10)
        self.entry.grid(row=0, column=1, padx=5)

        # Buttons Frame
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        self.insert_btn = tk.Button(btn_frame, text="Insert Node",
                                    command=self.insert_node)
        self.insert_btn.grid(row=0, column=0, padx=5)

        self.search_btn = tk.Button(btn_frame, text="Search Node",
                                    command=self.start_search)
        self.search_btn.grid(row=0, column=1, padx=5)

        self.reset_btn = tk.Button(btn_frame, text="Reset Highlight",
                                   command=self.reset_tree)
        self.reset_btn.grid(row=0, column=2, padx=5)

        self.clear_btn = tk.Button(btn_frame, text="Clear Tree",
                                   command=self.clear_tree)
        self.clear_btn.grid(row=0, column=3, padx=5)

        # Status Label
        self.status = tk.Label(root, text="Insert nodes to build tree...",
                               font=("Arial", 12))
        self.status.pack(pady=5)

        # Matplotlib Figure
        self.fig, self.ax = plt.subplots(figsize=(7, 5))
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack()

        self.update_tree([], None)

    # ---------------- UPDATE TREE DRAWING ---------------- #
    def update_tree(self, visited, found_node):
        self.ax.clear()
        self.ax.axis("off")
        self.ax.set_title("Binary Search Tree Visualization")

        if self.tree_root:
            draw_tree(self.tree_root, 0, 0, 2, visited, found_node, self.ax)

        self.canvas.draw()

    # ---------------- INSERT NODE ---------------- #
    def insert_node(self):
        try:
            value = int(self.entry.get())
        except:
            messagebox.showerror("Error", "Enter a valid number!")
            return

        self.tree_root = insert(self.tree_root, value)

        self.status.config(text=f"Inserted {value} into BST!")
        self.update_tree([], None)

    # ---------------- RESET HIGHLIGHTS ---------------- #
    def reset_tree(self):
        self.visited = []
        self.status.config(text="Tree highlights reset!")
        self.update_tree([], None)

    # ---------------- CLEAR TREE ---------------- #
    def clear_tree(self):
        self.tree_root = None
        self.visited = []
        self.status.config(text="Tree cleared! Insert new nodes.")
        self.update_tree([], None)

    # ---------------- START SEARCH ---------------- #
    def start_search(self):
        if self.tree_root is None:
            messagebox.showwarning("Warning", "Tree is empty! Insert nodes first.")
            return

        try:
            self.guess = int(self.entry.get())
        except:
            messagebox.showerror("Error", "Enter a valid number!")
            return

        # Reset search state
        self.visited = []
        self.current = self.tree_root
        self.attempts = 0

        self.search_btn.config(state="disabled")

        self.animate_search()

    # ---------------- SMOOTH SEARCH ANIMATION ---------------- #
    def animate_search(self):
        if self.current is None:
            self.status.config(
                text=f"{self.guess} NOT FOUND after {self.attempts} attempts!"
            )
            self.search_btn.config(state="normal")
            return

        self.attempts += 1
        self.visited.append(self.current.value)

        self.status.config(
            text=f"Attempt {self.attempts}: Visiting Node {self.current.value}"
        )

        self.update_tree(self.visited, None)

        # Found
        if self.current.value == self.guess:
            self.status.config(
                text=f"FOUND {self.guess} in {self.attempts} attempts!"
            )
            self.update_tree(self.visited, self.guess)
            self.search_btn.config(state="normal")
            return

        # Move left/right
        if self.guess < self.current.value:
            self.current = self.current.left
        else:
            self.current = self.current.right

        self.root.after(800, self.animate_search)


# ---------------- RUN APP ---------------- #
if __name__ == "__main__":
    root = tk.Tk()
    app = BSTApp(root)
    root.mainloop()
