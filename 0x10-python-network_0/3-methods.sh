#!/bin/bash
# gets methods available
curl -siX OPTIONS "$1" | grep -iF allow | cut -b 8-
