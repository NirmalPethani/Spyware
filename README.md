# Spyware
This project is a simple Python spyware tool that:  Captures the screen of the user at regular intervals  Saves the screenshot as a .png file  Uploads the screenshot automatically to a specified FTP server  It demonstrates basic use of libraries like PIL (Pillow) for capturing screenshots and ftplib for FTP file transfer.  


Features
Automatic screenshot capture

FTP upload of screenshots

Configurable server details

Lightweight and easy to modify

Setup
Clone this repository or download the script.

Install the required Python library:

bash
Copy
Edit
pip install Pillow
Edit the script to update FTP credentials:

python
Copy
Edit
ftp_host = "your_ftp_server_ip"
ftp_user = "your_username"
ftp_pass = "your_password"
ftp_dir = "directory_to_upload"
Run the script:

bash
Copy
Edit
python spyware.py
How it Works
It captures a screenshot every 10 seconds.

Each screenshot is saved as screenshot.png.

The screenshot is then uploaded to the specified FTP server.

The process repeats indefinitely.

Disclaimer
This script is intended only for ethical, educational, and testing purposes (such as learning about data transfer, automation, or creating monitoring solutions for your own devices).
Do not use this code for malicious purposes. Unauthorized surveillance and data capture are illegal and punishable by law.

