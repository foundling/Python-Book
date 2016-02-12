#!/bin/sh

if [ ! -d ./env ]; then
  echo "Creating a virtualenv named 'env'."
  /usr/local/bin/virtualenv ./env
fi

. env/bin/activate

if [ -f ./requirements.txt ];  then
  echo "installing Python packages in requirements.txt ... "
  pip install -r requirements.txt
fi
