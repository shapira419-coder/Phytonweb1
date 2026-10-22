#belajar website
#belajarweb1.py

import wsgiref.simple_server


def application(environ, start_response):
    # response
    response = b"HELLO WORD"

    # status respon
    status = "200 OK"

    # header respon
    headers = [("content-type", "text/html")]

    # pengaturan status dan header
    start_response(status, headers)

    return [response]


if __name__ == "__main__":
    w_s = wsgiref.simple_server.make_server(
        host="localhost",
        port=8021,
        app=application
    )

    w_s.handle_request()
