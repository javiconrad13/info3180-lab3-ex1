
import smtplib 

from_addr = 'javmac876@gmail.com'
from_name = 'Javier'
to_addr  = 'javmac876@gmail.com' 
to_name  = 'New Javier'
msg = "Well this is cool"
subject = "Info3180 Test Email"

message = """From: {} <{}> 
To: {} <{}> 
Subject: {} 
{} 
""" 
message_to_send = message.format(from_name, from_addr, to_name, to_addr, subject, msg) 
# Credentials (if needed) 
username = 'javmac876@gmail.com' 
password = 'ujoexobkxigcujcb' 
# The actual mail send 
server = smtplib.SMTP('smtp.gmail.com:587') 
server.starttls() 
server.login(username,password) 
server.sendmail(from_addr, to_addr, message_to_send) 
server.quit() 
