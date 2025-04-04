# EX01 Developing a Simple Webserver
## Date:29/03/2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <title>DEVICE CONFIGURATION-212224040353</title>
    <body>
        <style>
            body {
                font-family: Arial;
                text-align: center;
            }
            table {
                margin: auto; 
                border-collapse: collapse;
                border: 1px solid black;
            }
            th, td {
                border: 1px solid black;
                padding: 10px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
        <h1>DEVICE CONFIGURATION-212224040353</h1>
        <table >
            <tr>
                <th>Device name:</th>
                <td>DESKTOP-MOHHBTU</td>
            </tr>
            
            <tr>
                <th>Processor:</th>
                <td>D13th Gen Intel(R) Core(TM) i5-1335U 1.30 GHz</td>
            </tr>
                         
            <tr>
                <th>Installed RAM:</th>
                <td>16.0 GB (15.7 GB usable) </td>
            </tr>
                         
            <tr>
                <th>Device ID:</th>
                <td>15EEA3B2-7EF5-4DEC-903D-577382C3C005</td>
            </tr>
                            
            <tr>
                <th>Product ID:</th>
                <td>00342-42709-07393-AAOEM</td>
            </tr>
              
            <tr>
                <th>System type:</th>
                <td>64-bit operating system, x64-based processor</td>
            </td>
                  
            <tr>
                <th>Pen and touch:</th>
                <td>No pen or touch input is available for this display </td>
            </tr>
    
          </table>  
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
```

## OUTPUT:
![alt text](<Screenshot 2025-03-29 184430.png>)

![alt text](<Screenshot 2025-03-29 184443.png>)
## RESULT:
The program for implementing simple webserver is executed successfully.
