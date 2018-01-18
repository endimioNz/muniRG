#!/bin/bash

docker run -v "$PWD":/usr/src/app -w /usr/src/app -it --rm -p 8080:8000 python:3 /bin/bash
