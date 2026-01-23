from threading import Thread
from http.server import HTTPServer, BaseHTTPRequestHandler
import logging
import os

logger = logging.getLogger(__name__)

class SimpleHandler(BaseHTTPRequestHandler):
    """Simple HTTP handler to satisfy cloud health checks."""
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Bot is runnning!")

    def do_HEAD(self):
        """Handle HEAD requests (used by UptimeRobot)."""
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
    
    def log_message(self, format, *args):
        # Silence standard HTTP logging to keep console clean
        pass

def run_server(port):
    try:
        server_address = ('', port)
        httpd = HTTPServer(server_address, SimpleHandler)
        logger.info(f"Keep-alive web server running on port {port}")
        httpd.serve_forever()
    except Exception as e:
        logger.error(f"Failed to start keep-alive server: {e}")

def start(port=None):
    """Start the keep-alive server in a background thread."""
    if port is None:
        # Try to get port from environment (common in cloud apps)
        port = int(os.environ.get("PORT", 8080))
        
    t = Thread(target=run_server, args=(port,), daemon=True)
    t.start()
