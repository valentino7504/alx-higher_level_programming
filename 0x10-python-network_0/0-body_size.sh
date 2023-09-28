#!/bin/bash
# a script to check the lenght of a response
curl -sI 0.0.0.0:5000 | grep -iF content-length | cut -b 17-
