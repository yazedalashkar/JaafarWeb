# -*- coding: utf-8 -*-
"""
خادم محلي خفيف جداً لصالة ساحة الأساطير
يقوم بتشغيل التطبيق وتأمين حفظ البيانات تلقائياً في ملف data.json على قرص اللابتوب
"""
import os
import json
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

PORT = 8080
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.json')

class LegendsArenaHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/api/save':
            try:
                content_length = int(self.headers.get('Content-Length', 0))
                post_body = self.rfile.read(content_length)
                data = json.loads(post_body.decode('utf-8'))
                
                with open(DATA_FILE, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(b'{"status":"saved","file":"data.json"}')
                return
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(str(e).encode('utf-8'))
                return
        super().do_POST()

    def do_GET(self):
        if self.path == '/api/load':
            if os.path.exists(DATA_FILE):
                try:
                    with open(DATA_FILE, 'rb') as f:
                        content = f.read()
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    self.wfile.write(content)
                    return
                except Exception:
                    pass
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'{"status":"not_found"}')
            return
        super().do_GET()

if __name__ == '__main__':
    print("=" * 60)
    print("   ساحة الأساطير - خادم الحفظ المزدوج والتأمين التلقائي")
    print(f"   الرابط: http://localhost:{PORT}/index.html")
    print(f"   ملف الحفظ الفعلي على القرص: data.json")
    print("=" * 60)
    server_address = ('', PORT)
    httpd = ThreadingHTTPServer(server_address, LegendsArenaHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nتم إيقاف الخادم بأمان.")
