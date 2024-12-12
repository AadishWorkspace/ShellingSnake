#!/bin/sh
#
# This script is used to run your program
# 
# This runs after runcompile/compile.sh
#

# Exit early if any commands fail
set -e

exec pipenv run python3 -u -m app.main "$@"
