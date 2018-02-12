from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse, Http404
from django.conf import settings
from os import listdir
from os.path import isfile, join
from PIL import Image


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def css(request, templatefile) :
    return render(request, 'css/' + templatefile, {})

def viewer(request, templatefile):
    return render(request, 'view/' + templatefile, {})
    
import time
def creategenerator_mjpegstream(filelist):
    # Load image files to RAM
    images = []
    filelist.sort()
    try: 
      for filename in filelist:
            with open(settings.SITE_ROOT + settings.STREAMSOURCE_DIR + '/' + filename, "rb") as f:
                image = f.read()
                images.append(image)
                f.close()
    except Exception as e:
        images = []
        red = Image.new('RGBA', (1, 1), (255,0,0,0))
        image = b''
        red.save(image, "JPEG")
        images.append(image)
    
    # start streaming loop
    while True:
      for image in images:
                chunkheader = b"Content-Type: image/jpeg\nContent-Length: " + str(len(image)).encode('ascii') + b"\n\n"
                boundary = b"\n--myboundary\n"
                yield (chunkheader + image + boundary)
                time.sleep(settings.CHUNK_DELAY)


def mjpeg(request):
    path = settings.SITE_ROOT + settings.STREAMSOURCE_DIR + '/'
    filelist = [f for f in listdir(path) if isfile(join(path, f))]
    mjpegstream = creategenerator_mjpegstream(filelist)
    return StreamingHttpResponse(mjpegstream, content_type='multipart/x-mixed-replace;boundary=myboundary')
