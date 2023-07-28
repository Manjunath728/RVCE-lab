#!/bin/bash

source="/home/manjunath/RVCE-lab/prct/imp/"
dest="/home/manjunath/RVCE-lab/prct/backup"

backup_file="${dest}/backup_$(date +'%Y%m%d%H%M%S').tar.gz"

tar -czf "$backup_file" -C "$source" . >/dev/null 2>&1

find "$dest" -type f -mmin +2 -delete >/dev/null 2>&1
