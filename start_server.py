import http.server
import socketserver
import webbrowser
import os

# Configuration
PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def start_server():
    """Start a simple HTTP server to serve the swimming records page"""
    
    Handler = MyHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}/src/index.html"
        
        print("=" * 60)
        print("🏊 Tunisia Swimming Records - Local Server")
        print("=" * 60)
        print(f"\n✓ Server started successfully!")
        print(f"\n🌐 Server running at: http://localhost:{PORT}")
        print(f"📄 Landing page at: {url}")
        print(f"\n📂 Serving files from: {DIRECTORY}")
        print("\n⚠️  Press Ctrl+C to stop the server")
        print("=" * 60)
        
        # Automatically open the browser
        print("\n🚀 Opening browser...")
        webbrowser.open(url)
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n👋 Server stopped. Goodbye!")
            httpd.shutdown()

if __name__ == "__main__":
    start_server()
