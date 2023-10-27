import tkinter as tk
import speedtest

def get_speed():
    st = speedtest.Speedtest()
    st.get_best_server()

    download_speed = st.download() / 1024 / 1024  # Convert to Mbps
    upload_speed = st.upload() / 1024 / 1024  # Convert to Mbps

    result_label.config(text=f"Download Speed: {download_speed:.2f} Mbps\nUpload Speed: {upload_speed:.2f} Mbps")

# Create a basic Tkinter window
window = tk.Tk()
window.title("Internet Speed Test")

# Create a label to display results
result_label = tk.Label(window, text="", font=("Helvetica", 14))
result_label.pack(pady=20)

# Create a button to initiate the speed test
test_button = tk.Button(window, text="Run Speed Test", command=get_speed)
test_button.pack()

# Run the Tkinter main loop
window.mainloop()
