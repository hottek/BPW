#!/bin/bash
sudo docker run --name=c-bluescreens -v v-certs:/certs -v v-bpw-db:/database --detach -p 13002:13002 c-bluescreens
