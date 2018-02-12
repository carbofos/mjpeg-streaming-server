Python/Django MJPEG image push Axis IP camera simulation server

This is an Axis IP camera simulation program which can stream JPEG sequence to browser using push image technology.
The technology was popular in some IP cameras because it provides a simple solution to embed your video stream into HTML page using <img /> tag.
Old Panasonic, Linksys IP cameras and modern Axis cameras does provide MJPEG/HTTP stream.

This Django software have a HTML template of an Axis IP camera.

To run it you should

1. Install Python 2 or Python 3
2. Install Django framework: 
$ pip install django

3. Run server from the project directory:
mjpegstreamingserver$ python2 ./manage.py runserver

You should see a message:
Starting development server at http://127.0.0.1:8000/

4. Visit the provided URL in your browser so you can see sample JPEG stream in a fake Axis IP camera interface.
You could change HTML templates and some stream settings in settings.py
