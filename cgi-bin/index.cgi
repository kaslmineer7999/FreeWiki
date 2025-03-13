#!/usr/bin/bash

cat <<EOF
content-type: text/html

<!doctype html>
<html>
	<head>
		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
		<title>FreeWiki - Freedom Wiki</title>
	</head>
	<body><center>
		<h1><span class="fa fa-gavel"></span> ACTIONS:</h1>
		<a href="/create.html"><span class="fa fa-bullhorn" style="font-size:23px;"></span> CREATE A PAGE</a>
		<hr>
		<h1><span class="fa fa-info"></span> WIKI PAGES:</h1>
		<div style="background:linear-gradient(#c9c9c9,white);width:650px;height:600px;overflow:scroll;border-radius:15px;resize:both;">
EOF
find ../wikis/|\
	while IFS='' read -r file
	do
		[ "$file" = "../wikis/" ] && continue
		basename="`basename "$file"`"
		printf "\t\t\t<b><a href='/cgi-bin/readpage.cgi?$basename' style='font-size:25px;display:inline-block;margin-left:10px;'>$basename</a></b>\n"
	done

cat <<EOF
		</div>
	</center></body>
</html>
EOF
