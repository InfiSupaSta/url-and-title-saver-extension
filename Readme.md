Browser extension for storing page title and url in any storage on your PC. 
Store options can be modified in the future.

__Purpose of this mini-project as-is:__

>Often during internet crawling I am facing potentially interesting 
resource but not ready to interact with that right now for some reason. 
Most likely in that situation I am just leave tab opened and opening another 
tab for searching. After some similar iterations amount of 
tabs grows rapidly, so its better for me to store it somewhere 
else - and it how that extension was born :)  


---
`--Important--`

Current version requires running server on localhost.

---


`--About--`


__How it works:__

- __on the client side__: javascript code (called script.js) just scrapping 
url and page title, sending it to backend server on python after. _manifest.json_
contains metadata about extension.
- __on the server side__: simple HTTP server using python as backend
serving OPTIONS and POST methods - for CORS and receiving
files respectively. By default two writers for data are used:
FIleWriter and SQLiteWriter. You can create your own writer (python 
class that include .write() method) and configure list of writers
in JsonRequestHandler.writers class attribute of _server.py_ module.

---
`--Quickstart--`

_For starting server:_
> python3 ./python_server/server.py _host_ _port_

host and port are optional - by default its __localhost__ and __56789__

_For adding extension_: go to browser extensions page, activate developer mode,
choose upload unpacked extension and provide path to this project directory.

If all steps above went smoothly then you can use extension. 
For saving url and title use the following keys combination:

__ctrl__ + __alt__ + __spacebar__

If you did not change writers that used by default on the backend, two files 
will be created in the root of project: __db.sqlite3__ and __READ_ME_ASAP.txt__.
Thats it!