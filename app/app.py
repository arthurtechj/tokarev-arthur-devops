
import os
from http.server import BaseHTTPRequestHandler, HTTPServer


def student_info():
    return {
        "name": os.getenv("STUDENT_NAME", "Arthur"),
        "surname": os.getenv("STUDENT_SURNAME", "Tokarev"),
        "group": os.getenv("STUDENT_GROUP", "IT2-2312"),
        "id": os.getenv("STUDENT_ID", "37460"),
    }


def make_message():
    student = student_info()
    return f"""
================================
DevOps Student Application
================================
Name: {student['name']}
Surname: {student['surname']}
Group: {student['group']}
Student ID: {student['id']}

Application is running successfully!
""".strip()


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = make_message().encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(message)))
        self.end_headers()
        self.wfile.write(message)


if __name__ == "__main__":
    print(make_message(), flush=True)
    print("Server listening on port 8000", flush=True)
    HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
