#! /bin/bash

LSLEN=`ls Takeout* | wc -l`

if [[ $LSLEN == "1" ]]; then
    echo "File: `ls Takeout*`"
else
    echo "Wrong number of Google Takeout Files: download yours at https://takeout.google.com/"
fi
