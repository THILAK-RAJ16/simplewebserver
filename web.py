from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <title>List of protocols in TCP/IP Protocol Suite-212224040353</title>
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
        <h1>List of protocols in TCP/IP Protocol Suite-212224040353</h1>
        <table>
            <tr>
                <th>Layer</th>
                <th>Protocol(s)</th>
                <th>Description</th>
            </tr>
            <tr>
                <td>Application Layer</td>
                <td>HTTP, FTP, SMTP, DNS, POP3, IMAP, Telnet</td>
                <td>Provides network services directly to applications (e.g., web browsing, file transfer).</td>
            </tr>
            <tr>
                <td>Transport Layer</td>
                <td>TCP, UDP</td>
                <td>Ensures reliable (TCP) or unreliable (UDP) data transmission between devices.</td>
            </tr>
            <tr>
                <td>Internet Layer</td>
                <td>IP, ICMP, ARP</td>
                <td>Responsible for logical addressing and routing of data across networks.</td>
            </tr>
            <tr>
                <td>Link Layer</td>
                <td>Ethernet, Wi-Fi, PPP, ARP</td>
                <td>Handles physical transmission of data over the network medium (Ethernet, Wi-Fi).</td>
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