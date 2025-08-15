import tkinter as tk
from PIL import Image, ImageTk
import winsound
import threading

# Global variable to track if dog sound should be playing
dog_sound_playing = False
sound_thread = None

def play_dog_sound_loop():
    """Play dog sound in a loop while the window is open"""
    global dog_sound_playing
    import os
    import time
    sound_file = "dogsounds.wav"
    
    if not os.path.exists(sound_file):
        print(f"Sound file not found: {sound_file}")
        return
    
    while dog_sound_playing:
        try:
            # Play sound asynchronously so it doesn't block
            winsound.PlaySound(sound_file, winsound.SND_FILENAME | winsound.SND_ASYNC)
            
            # Wait for a bit, checking if we should stop
            for _ in range(50):  # Check 50 times over ~5 seconds
                if not dog_sound_playing:
                    break
                time.sleep(0.1)
                
        except Exception as e:
            print(f"Error playing sound: {e}")
            break

def stop_dog_sound():
    """Stop the dog sound when window closes"""
    global dog_sound_playing, sound_thread
    dog_sound_playing = False
    
    # Stop any currently playing sound
    try:
        winsound.PlaySound(None, winsound.SND_PURGE)
    except:
        pass
    
    # Don't wait for thread to join as it might cause hanging

def create_animal_window(title, image_file, sound_enabled=False):
    """Generic function to create animal windows with consistent styling"""
    global dog_sound_playing, sound_thread
    
    print(f"You chose a {title.lower()}!")
    
    # Create new window with better styling
    new_window = tk.Toplevel(root)
    new_window.title(f"{title} Gallery")
    new_window.geometry("400x500")
    new_window.configure(bg='#f0f0f0')
    new_window.resizable(False, False)
    
    # Center the window
    new_window.transient(root)
    new_window.grab_set()
    
    # Start sound if enabled (for dog)
    def on_window_close():
        if sound_enabled:
            stop_dog_sound()
        new_window.destroy()
    
    if sound_enabled:
        dog_sound_playing = True
        sound_thread = threading.Thread(target=play_dog_sound_loop, daemon=True)
        sound_thread.start()
    
    new_window.protocol("WM_DELETE_WINDOW", on_window_close)
    
    # Title frame
    title_frame = tk.Frame(new_window, bg='#f0f0f0')
    title_frame.pack(fill='x', padx=20, pady=(20, 10))
    
    title_label = tk.Label(
        title_frame,
        text=f"🐕 {title}!" if title == "Dog" else f"🐱 {title}!",
        font=("Segoe UI", 20, "bold"),
        bg='#f0f0f0',
        fg='#333333'
    )
    title_label.pack()
    
    # Image frame with border
    image_frame = tk.Frame(new_window, bg='white', relief='solid', bd=1)
    image_frame.pack(padx=30, pady=20)
    
    try:
        # Load and resize the image
        img = Image.open(image_file)
        img = img.resize((300, 300), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        
        # Image label with padding
        label = tk.Label(image_frame, image=photo, bg='white')
        label.image = photo  # Keep a reference
        label.pack(padx=10, pady=10)
        
    except FileNotFoundError:
        error_label = tk.Label(
            image_frame,
            text=f"📷 {title} image not found!",
            font=("Segoe UI", 12),
            bg='white',
            fg='#666666',
            width=40,
            height=20
        )
        error_label.pack(padx=10, pady=10)
    
    # Button frame
    button_frame = tk.Frame(new_window, bg='#f0f0f0')
    button_frame.pack(fill='x', padx=30, pady=20)
    
    # Close button with modern styling
    close_btn = tk.Button(
        button_frame,
        text="✕ Close",
        command=on_window_close,
        bg='#e74c3c',
        fg='white',
        font=("Segoe UI", 12, "bold"),
        relief='flat',
        padx=20,
        pady=8,
        cursor='hand2'
    )
    close_btn.pack()
    
    # Hover effects for close button
    def on_enter(e):
        close_btn.configure(bg='#c0392b')
    
    def on_leave(e):
        close_btn.configure(bg='#e74c3c')
    
    close_btn.bind("<Enter>", on_enter)
    close_btn.bind("<Leave>", on_leave)

def cow():
    create_animal_window("Cow", "cow.jpg", sound_enabled=False)

def dog():
    create_animal_window("Dog", "dogimage.jpg", sound_enabled=True)

def cat():
    create_animal_window("Cat", "cat.jpg", sound_enabled=False)

# Create main window with modern design
root = tk.Tk()
root.title("🎮 Animal Gallery Game")
root.geometry("500x500")
root.configure(bg='#2c3e50')
root.resizable(False, False)

# Center the window on screen
root.update_idletasks()
x = (root.winfo_screenwidth() // 2) - (500 // 2)
y = (root.winfo_screenheight() // 2) - (500 // 2)
root.geometry(f"500x500+{x}+{y}")

# Main container
main_frame = tk.Frame(root, bg='#2c3e50')
main_frame.pack(expand=True, fill='both', padx=40, pady=40)

# Title section
title_frame = tk.Frame(main_frame, bg='#2c3e50')
title_frame.pack(fill='x', pady=(0, 30))

title_label = tk.Label(
    title_frame,
    text="🎮 Animal Gallery",
    font=("Segoe UI", 28, "bold"),
    bg='#2c3e50',
    fg='white'
)
title_label.pack()

subtitle_label = tk.Label(
    title_frame,
    text="Choose your favorite animal to see!",
    font=("Segoe UI", 12),
    bg='#2c3e50',
    fg='#bdc3c7'
)
subtitle_label.pack(pady=(5, 0))

# Buttons container
button_frame = tk.Frame(main_frame, bg='#2c3e50')
button_frame.pack(expand=True)

# Dog button with modern styling
dog_btn = tk.Button(
    button_frame,
    text="🐕 Dog",
    command=dog,
    bg='#27ae60',
    fg='white',
    font=("Segoe UI", 16, "bold"),
    relief='flat',
    padx=40,
    pady=15,
    cursor='hand2',
    width=12
)
dog_btn.pack(pady=10)

# Cat button with modern styling
cat_btn = tk.Button(
    button_frame,
    text="🐱 Cat",
    command=cat,
    bg='#f39c12',
    fg='white',
    font=("Segoe UI", 16, "bold"),
    relief='flat',
    padx=40,
    pady=15,
    cursor='hand2',
    width=12
)
cat_btn.pack(pady=10)

cow_btn = tk.Button(
    button_frame,
    text="🐕 cow",
    command=cow,
    bg="#2729ae",
    fg='white',
    font=("Segoe UI", 16, "bold"),
    relief='flat',
    padx=40,
    pady=15,
    cursor='hand2',
    width=12
)
cow_btn.pack(pady=10)

# Hover effects for main buttons
def create_hover_effect(button, normal_color, hover_color):
    def on_enter(e):
        button.configure(bg=hover_color)
    
    def on_leave(e):
        button.configure(bg=normal_color)
    
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

create_hover_effect(dog_btn, '#27ae60', '#2ecc71')
create_hover_effect(cat_btn, '#f39c12', '#e67e22')

# Footer
footer_label = tk.Label(
    main_frame,
    text="Click a button to view your favorite animal!",
    font=("Segoe UI", 10),
    bg='#2c3e50',
    fg='#7f8c8d'
)
footer_label.pack(side='bottom', pady=(30, 0))

# Handle main window close
def on_main_window_close():
    stop_dog_sound()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_main_window_close)
root.mainloop()