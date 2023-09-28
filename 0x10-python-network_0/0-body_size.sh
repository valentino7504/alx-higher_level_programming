#!/bin/bash
# a script to check the length of a response
curl -sI "$1" | grep -iF content-length | cut -b 17-
