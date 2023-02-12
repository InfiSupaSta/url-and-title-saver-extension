import logging
import sys
from http import server

from db import DatabasePreparation
from writers import SQLiteWriter, FileWriter

DEFAULT_HOST = 'localhost'
DEFAULT_PORT = 56789


class JsonRequestHandler(server.BaseHTTPRequestHandler):
    timeout = 3
    writers = [FileWriter(), SQLiteWriter()]

    def _set_basic_headers(self):
        self.send_header('Host', 'localhost')
        self.send_header('Content-Type', 'text/html')
        self.send_header("Location", f"{self.path}")

    def _set_cors_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST,HEAD,OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def set_headers(self):
        self._set_basic_headers()
        self._set_cors_headers()
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.set_headers()

    def do_POST(self):
        self.set_headers()

        size_of_data_from_request = int(
            self.headers.get('Content-Length', 0)
        )
        if size_of_data_from_request == 0:
            self.send_response(400)
            self.wfile.write(b'Post request can not have empty body.\n')
            return

        self.send_response(200)

        request_body = self.rfile.read(size_of_data_from_request)
        for writer in self.writers:
            writer.write(request_body)

        self.wfile.write(b'Successfully added data to chosen store.\n')


class CustomHTTPServer(server.HTTPServer):
    def __init__(self, **kwargs):
        addr = kwargs.get('server_address')
        server_address = addr if addr is not None else (DEFAULT_HOST, DEFAULT_PORT)

        request_handler = kwargs.get('RequestHandlerClass')
        handler = request_handler if request_handler is not None else JsonRequestHandler

        if 'server_address' in kwargs:
            kwargs.pop('server_address')

        super().__init__(server_address, handler, **kwargs)

    def serve_forever(self, poll_interval: float = 0.5) -> None:
        logging.info(f'Server start working on {self.server_address}')
        super().serve_forever(poll_interval)


def main():
    DatabasePreparation().create_db()
    srvr = CustomHTTPServer()
    srvr.serve_forever()


if __name__ == '__main__':

    logging.basicConfig(
        level=logging.INFO,
        format='[%(levelname)s] :: %(asctime)s :: %(filename)s(%(lineno)s) :: %(message)s',
    )
    try:
        if len(sys.argv) == 3:
            host = sys.argv[1]
            port = int(sys.argv[2])
            CustomHTTPServer(server_address=(host, port)).serve_forever()
        else:
            main()
    except KeyboardInterrupt:
        logging.warning('Server stopped working due keyboard interrupt.')
    except Exception as exc:
        logging.error(f'Something going wrong: {exc.with_traceback(exc.__traceback__)}')
