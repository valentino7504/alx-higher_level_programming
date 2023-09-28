#!/bin/bash
# gets methods available
curl -siX OPTIONS 0.0.0.0:5000/route_4 | grep -iF allow | cut -b 8-
