#!/bin/bash
gunicorn --timeout 999999 --log-level debug --certfile=/certs/bluescreens.zeekay.dev/fullchain.pem --keyfile=/certs/bluescreens.zeekay.dev/privkey.pem --bind 0.0.0.0:13002 server:app

