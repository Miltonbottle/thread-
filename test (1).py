import threading
import random
import time


# Function to simulate the display of random values on each block
def display_random_value(name, lb, ub, refresh_time):
    while True:
        # Generate a random value within the specified range
        value = random.randint(lb, ub)
        print(f"{name}: Value = {value} (Refresh Time = {refresh_time}s)")

        # Wait for the specified refresh time
        time.sleep(refresh_time)


# Define display settings
displays = [
    ("Display 1", 10, 20, 10),
    ("Display 2", -10, 10, 20),
    ("Display 3", -100, 0, 8),
    ("Display 4", 0, 20, 12), 00
    ("Display 5", -40, 40, 16),
    ("Display 6", 100, 200, 14),
]

# Create and start a thread for each display
threads = []
for name, lb, ub, refresh_time in displays:
    thread = threading.Thread(
        target=display_random_value, args=(name, lb, ub, refresh_time)
    )
    thread.daemon = True  # Daemon threads will terminate when the main program exits
    threads.append(thread)00.21\
    thread.start()

# Keep the main thread alive to allow daemon threads to run
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting program...")
    
#alternative code   
'''import os, sys, time, threading, multiprocessing, random as r


# Function runs for random seconds
def task(cmd):
    waitingTime = r.randint(5, 10)

    print("Task started")
    print("Task running for %d sec...." % (waitingTime))
    time.sleep(waitingTime

    print("Task ends")
    return


# Main Program
startTime = time.time()

activeThreads = threading.active_count()
print("Active Threads = ", activeThreads)

cmd = "Sample task"

print("Program Started")
print("Thread starts")

t = threading.Thread(target=task, args=(cmd,))
t.start()
time.sleep(1)

# Waiting to finish the Threads
while True:
    if threading.active_count() == activeThreads:
        break
    else:
        print(
            "Thread still running (left %d)..."
            % (threading.active_count() - activeThreads)
        )
        time.sleep(1)

print("Thread ends")

print("Program Finished")
print("Total Time %f sec" % (round(time.time() - startTime, 4)))'''
    
''''
import threading
import random
import time
import tkinter as tk


# Function to update the display with random values
def update_display(label, lb, ub, refresh_time):
    while True:
        # Generate a random value within the specified range
        value = random.randint(lb, ub)

        # Update the label text
        label.config(text=f"Value: {value} (Refresh every {refresh_time}s)")

        # Wait for the specified refresh time
        time.sleep(refresh_time)


# Create the main Tkinter window
root = tk.Tk()
root.title("Random Value Dashboard")
root.geometry("400x400")

# Define display settings 
displays = [
    ("Display 1", 10, 20, 10, "#FFCC99"),  # Peach
    ("Display 2", -10, 10, 20, "#CCE5FF"),  # Light Blue
    ("Display 3", -100, 0, 8, "#CCFFCC"),  # Light Green
    ("Display 4", 0, 20, 12, "#FFD966"),  # Yellow
    ("Display 5", -40, 40, 16, "#D9EAD3"),  # Light Grayish Green
    ("Display 6", 100, 200, 14, "#E6B8AF"),  # Light Pink
]

# Create a label for each display and start a thread to update each one
for name, lb, ub, refresh_time, color in displays:
    frame = tk.Frame(root, pady=10)
    frame.pack()

    # Label for the name of the display
    name_label = tk.Label(frame, text=name, font=("Arial", 12, "bold"))
    name_label.pack()

    # Label for displaying the random value and refresh time with background color
    value_label = tk.Label(
        frame, text="Initializing...", font=("Arial", 10), bg=color, width=30, height=2
    )
    value_label.pack()

    # Start a new thread for each display to update the value
    thread = threading.Thread(
        target=update_display, args=(value_label, lb, ub, refresh_time)
    )
    thread.daemon = True  # Daemon threads will close with the main program
    thread.start()

# Run the Tkinter event loop
root.mainloop()
'''
