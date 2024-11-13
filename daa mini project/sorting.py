import tkinter as tk
from tkinter import messagebox

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


def perform_sorting():
    try:
       
        data = entry.get()
        numbers = list(map(int, data.split(',')))
        
      
        algorithm = algo_var.get()
        
        if algorithm == "Bubble Sort":
            sorted_numbers = bubble_sort(numbers)
        elif algorithm == "Quick Sort":
            sorted_numbers = quick_sort(numbers)
        else:
            raise ValueError("Invalid Algorithm")
        
    
        result_label.config(text=f"Sorted List: {sorted_numbers}")
    
    except ValueError:
 
        messagebox.showerror("Input Error", "Please enter valid numbers separated by commas.")


root = tk.Tk()
root.title("DAA - Sorting Algorithm Visualizer")


tk.Label(root, text="Enter numbers (comma-separated):").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root, width=40)
entry.grid(row=0, column=1, padx=10, pady=10)


tk.Label(root, text="Choose Sorting Algorithm:").grid(row=1, column=0, padx=10, pady=10)
algo_var = tk.StringVar()
algo_var.set("Bubble Sort")  
algo_menu = tk.OptionMenu(root, algo_var, "Bubble Sort", "Quick Sort")
algo_menu.grid(row=1, column=1, padx=10, pady=10)


sort_button = tk.Button(root, text="Sort", command=perform_sorting)
sort_button.grid(row=2, column=0,  columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="Sorted List: ")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()