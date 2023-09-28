#!/bin/bash
# gets methods available
curl -sI "$1" | grep "Allow" | cut -b 8-
