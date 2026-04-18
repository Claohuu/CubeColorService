import http.server
import json

current_color = {"r": 1.0, "g": 0.0, "b": 0.0}

class ColorHandler(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        if self.path == "/":
            html = self.build_html_page()
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))            

        elif self.path == "/color":
            response = json.dumps(current_color).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(response)

    
    #building the html page!!
    def build_html_page(self):
        r = int(current_color["r"] * 255)
        g = int(current_color["g"] * 255)
        b = int(current_color["b"] * 255)
        hex_color = "#{:02x}{:02x}{:02x}".format(r, g, b)

        return f"""
    <html>
        <body style="font-family: Arial, sans-serif;">
            <h1>Cube Color Controller</h1>
            <p>Made by Catherine!! :D </p>
            <p>Current color: {hex_color}</p>
            <input type="color" id="colorPicker" value="{hex_color}">
            <button onclick="sendColor()">Update Color</button>

                <script>
                    function sendColor() {{
                        const hex = document.getElementById("colorPicker").value;
                        const r = parseInt(hex.slice(1,3), 16) / 255;
                        const g = parseInt(hex.slice(3,5), 16) / 255;
                        const b = parseInt(hex.slice(5,7), 16) / 255;

                        fetch("/color", {{
                            method: "POST",
                            headers: {{"Content-Type": "application/json"}},
                            body: JSON.stringify({{r, g, b}})
                        }}).then(() => location.reload());
                    }}
                </script>
            </body>
        </html>
        """    

    def do_POST(self):
        if self.path == "/color":
            content_length = int(self.headers["Content-Length"])
            body = self.rfile.read(content_length)
            
            global current_color
            current_color = json.loads(body)
            
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Color updated")

    def log_message(self, format, *args):
        print(f"Request: {self.path} - {args[0]}")

with http.server.HTTPServer(("", 8080), ColorHandler) as server:
    print("Color service running on http://localhost:8080")
    server.serve_forever()

