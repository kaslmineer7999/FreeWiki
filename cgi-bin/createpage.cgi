#!/usr/bin/bash

input="`busybox httpd -d "$(cat)"`"
pagecontent="`echo "$input"|cut -d\& -f2-|cut -d\= -f2-|sed 's|<script||g;s|</script||g;s|<style||g;s|</style||g'`"
pagename="`echo "$input"|cut -d\& -f1|cut -d\= -f2-|head -1|sed 's/ /_/g;s|/||g'`"

cat << EOF
content-type: text/plain

pagename: $pagename
pagecontent: $pagecontent
input: $input


wiriting info to "$pagename"
EOF
printf "$pagecontent" > "../wikis/$pagename"

