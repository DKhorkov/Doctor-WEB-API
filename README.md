# Doctor WEB API

"Doctor WEB API" - application, written on Flask, 
that allows user to:
1) upload files to server, if user is authorized;
2) download files from server;
3) delete files from server, if user is authorized and
those files belongs to user.

Technical specifications, on basis of which application 
was developed, are located in
<b><i>technical_specifications.pdf</i></b> file.


### Authorization:
Application uses Basic-Auth authorization.<br>
Allowed users are stored in <b><i>src/users.py</i></b> file.


### Routing usage:

##### Upload:
To upload file, user should use 
<b><i>http://API_Domain/upload/</i></b> url.<br>
HTTP method should be POST.<br>
File should be attached in request body in field with name "file".

##### Download:
There are two ways to download file 
(for both HTTP GET method should be used):
1) use <b><i>http://API_Domain/download/{hashed_filename}></i></b> 
url.
2) use <b><i>http://API_Domain/download/</i></b> url and pass 
<b><i>hashed_filename</i></b> parameter using query in 
field without name or in field with according name ("hashed_filename").

<b><i>hashed_filename</i></b> - is a hash of file, 
which will be returned in response during uploading 
file to the server.

##### Delete:
There are two ways to delete file 
(for both HTTP DELETE method should be used):
1) use <b><i>http://API_Domain/delete/{hashed_filename}></i></b> 
url.
2) use <b><i>http://API_Domain/delete/</i></b> url and pass 
<b><i>hashed_filename</i></b> parameter using query in 
field without name or in field with according name ("hashed_filename").

<b><i>hashed_filename</i></b> - is a hash of file, 
which will be returned in response during uploading 
file to the server.

### Run via docker:

To run application via docker, use next command line in 
project's root directory:

    make -C docker build && make -C docker run


### Run using source files:

To run application using source files, use next commands 
in project's root directory:
    
    pip install -r requirements.txt
    python -m flask --app src/app.py run
