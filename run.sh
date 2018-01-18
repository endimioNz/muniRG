#!/bin/bash

docker run -v "$PWD":/usr/src/app -w /usr/src/app -it --rm -p 8000:8080 python:3 /bin/bash
