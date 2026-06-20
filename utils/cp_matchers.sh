ls /design/glob | grep -vE '^test' | while read fname; do if [ -f "/design/glob/$fname" ]; then  cp "/design/glob/$fname" /design/parse; fi; done

