import tkinter as tk
import random

fast_food_nc = {
    "Bojangles": {
        "menu": {
            "Cajun Chicken Biscuit": 3.79,
            "Bo-Tato Rounds": 2.29,
            "Chicken Supremes Combo": 7.99,
            "Sweet Tea (Large)": 1.99
        }
    },
    "Cook Out": {
        "menu": {
            "Cook Out Tray": 6.99,
            "Cheddar Style Burger": 3.99,
            "Quesadilla (Chicken)": 2.99,
            "Milkshake (any flavor)": 3.29
        }
    },
    "Chick-fil-A": {
        "menu": {
            "Chicken Sandwich": 4.29,
            "Waffle Fries (Medium)": 2.79,
            "8-count Nuggets": 4.99,
            "Lemonade (Medium)": 2.25
        }
    },
    "Hardee's": {
        "menu": {
            "Frisco Burger": 5.49,
            "Curly Fries": 2.49,
            "Loaded Omelet Biscuit": 3.69,
            "Chicken Tenders (3-piece)": 4.79
        }
    },
    "Wendy's": {
        "menu": {
            "Baconator": 6.49,
            "Spicy Chicken Sandwich": 5.29,
            "Frosty (Small)": 1.49,
            "4 for $4 Meal": 4.00
        }
    },
    "McDonald's": {
        "menu": {
            "Big Mac": 4.99,
            "McChicken": 1.79,
            "French Fries (Medium)": 2.89,
            "McFlurry": 3.69
        }
    },
    "Taco Bell": {
        "menu": {
            "Crunchwrap Supreme": 4.49,
            "Doritos Locos Taco": 2.29,
            "Cheesy Gordita Crunch": 4.19,
            "Baja Blast (Medium)": 2.19
        }
    },
    "Zaxby’s": {
        "menu": {
            "Chicken Finger Plate": 8.49,
            "Zaxby’s Zalad": 7.99,
            "Texas Toast": 0.99,
            "Zax Sauce (Extra)": 0.29
        }
    },
    "Popeyes": {
        "menu": {
            "Spicy Chicken Sandwich": 4.59,
            "Red Beans and Rice (Regular)": 2.29,
            "Biscuit": 1.19,
            "Cajun Fries": 2.49
        }
    },
    "Raising Cane’s": {
        "menu": {
            "Box Combo": 8.49,
            "Cane’s Sauce (Extra)": 0.39,
            "Texas Toast": 1.00,
            "Crinkle-Cut Fries": 2.19
        }
    }
}

# Function to generate suggestion
def get_suggestion():
    restaurant = random.choice(list(fast_food_nc.keys()))
    menu = fast_food_nc[restaurant]["menu"]
    item = random.choice(list(menu.keys()))
    price = menu[item]

    result = f"🍔 {restaurant}\n\n👉 {item}\n💵 ${price:.2f}"
    output_label.config(text=result)

# GUI setup
root = tk.Tk()
root.title("NC Fast Food Picker")
root.geometry("400x400")
root.configure(bg="#ffc0cb")  # Soft pink background

# Title Label
title_label = tk.Label(root, text="✨ Fast Food Picker ✨", font=("Helvetica", 18, "bold"), bg="#ffc0cb", fg="#800000")
title_label.pack(pady=20)

# Output Label
output_label = tk.Label(root, text="Click below to pick a place!", font=("Helvetica", 14), wraplength=300, bg="#ffc0cb")
output_label.pack(pady=40)

# Suggestion Button
suggest_button = tk.Button(root, text="🍟 Get Suggestion", font=("Helvetica", 12, "bold"), bg="#ff69b4", fg="white", command=get_suggestion)
suggest_button.pack(pady=10)

# Exit Button
exit_button = tk.Button(root, text="Exit", font=("Helvetica", 10), command=root.destroy)
exit_button.pack(pady=5)

# Run the GUI
root.mainloop()
