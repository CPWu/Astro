import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import cv2
from aiortc import RTCPeerConnection, RTCSessionDescription

# Set Appearance (System, Light, Dark)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Constants
WIN_WIDTH, WIN_HEIGHT = 860, 580
VID_WIDTH, VID_HEIGHT = 640, 480

# GUI Configuration
app = ctk.CTk()
app.geometry("{}x{}".format(WIN_WIDTH, WIN_HEIGHT))
app.title("Astro - Robot Viewier")

# Video Capture - Setup
camera = cv2.VideoCapture(0)


# Functions
def webrtc() -> None:
    print("Initialize RTCPeerConnection...")
    peer_connection = RTCPeerConnection()


def connect() -> None:
    HOST = entry_ip_address.get()
    entry_ip_address.configure(state="disabled")
    ret, frame = camera.read()
    if ret:
        # Get frame and convert to Image
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        cv2image_resized = cv2.resize(cv2image, (0, 0), fx=0.5, fy=0.5)
        imgPIL = Image.fromarray(cv2image_resized)
        imgTK = ImageTk.PhotoImage(image=imgPIL)
        lbl_video_stream = ctk.CTkLabel(frame_video, image=imgTK)
        lbl_video_stream.grid(row=0, column=0)
        app.after(15, connect)
    else:
        disconnect()


def disconnect() -> None:
    print("Disconnecting...")
    entry_ip_address.configure(state="normal")


frame_video = ctk.CTkFrame(app, width=VID_WIDTH, height=VID_HEIGHT, border_width=1)
entry_ip_address = ctk.CTkEntry(
    app, width=300, height=40, border_width=1, placeholder_text="Robot IPv4 Address..."
)
btn_connect = ctk.CTkButton(app, height=30, text="Connect", command=connect)
btn_disconnect = ctk.CTkButton(app, height=30, text="Disconnect", command=disconnect)
btn_exit = ctk.CTkButton(app, height=30, text="Exit", command=app.quit)


# UX Grid
frame_video.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
entry_ip_address.grid(row=1, column=1, padx=10, pady=10)
btn_connect.grid(row=1, column=2, padx=10, pady=10)
btn_disconnect.grid(row=1, column=3, padx=10, pady=10)
btn_exit.grid(row=1, column=4, padx=10, pady=10)

app.mainloop()
