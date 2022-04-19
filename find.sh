#!/bin/bash

DIR="$1"
SRC_DIR="../../js/app/"

for f in $(find "$DIR") ; do
    if grep '.png$' <<< "$f" > /dev/null ; then
        fd="$(sed 's/.png$//' <<< "$f")"
        found=""

        if rg "\b$fd\b" "$SRC_DIR" > /dev/null ; then
            found="\e[90m$fd \e[32myes\e[0m"
        else
            found="\e[1m$f \e[21m\e[31mno\e[0m"
        fi

        echo -e "$found"
    fi
done
