#!/usr/bin/bash

page="`basename "${QUERY_STRING}"`"
_read(){
cat <<EOF
content-type: text/html

<!doctype html>
<html>
	<head>
		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
		<title>FreeWiki - Freedom Wiki - $page</title>
	</head>
	<body>
		<center>
			<a href="/" style="float:left;"><span class="fa fa-bank"></span> HOME</a>
			<a href="/create.html"><span class="fa fa-bullhorn"></span> CREATE A PAGE</a>
			<a href="/cgi-bin/readpage.cgi?e=$page" style="float:right;">EDIT PAGE  <span class="fa fa-edit"></span></a>
		</center>
		<hr style="clear:both;">
EOF
cat "../wikis/$page"
printf "\n"
cat <<EOF
	</body>
</html>
EOF
}
_edit(){
cat <<EOF
content-type: text/html

<!doctype html>
<html>
	<head>
		<title>FreeWiki - Freedom Wiki - Edit Page</title>
		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	</head>
	<body>
		<form action="/cgi-bin/createpage.cgi" method="POST">
			<input type="hidden" name="pagename" value="$page"/>
			<label for="pagecontent">Page Content: <br></label>
			<textarea cols="80" rows="25" id="pagecontent" name="pagecontent" required="">
`cat "../wikis/$page"`</textarea><br>
			<button type="submit"><span class="fa fa-chevron-right"></span> Submit Edit</button>
		</form>
	</body>
</html>
EOF
}
[ "${page:0:2}" = "e=" ] && {
	page="${page:2:${#page}}"
	_edit
} || _read
