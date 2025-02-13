#!/bin/sh

apk add --no-cache inotify-tools
echo "Watching /data/shared/Exports for changes..."
echo "Current working directory: $(pwd)" 

inotifywait -m -e close_write,create --format "%w%f" / | while read file; do
    echo "New file detected: $file"
    python3 /data/shared/Exports/pdf_to_txt.py "$file"
done
