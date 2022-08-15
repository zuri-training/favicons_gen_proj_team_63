import os
import re
import shutil
from datetime import datetime
from django.conf import settings
from django.http import HttpResponse, Http404

def delete(path):
    """path could either be relative or absolute. """
    # check if file or directory exists
    if os.path.isfile(path) or os.path.islink(path):
        # remove file
        os.remove(path)
    elif os.path.isdir(path):
        # remove directory and all its content
        shutil.rmtree(path)
    else:
        raise ValueError(f"Path {path} is not a file or dir.")



def download(request, path):
    # get the download path
    download_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(download_path):
        with open(download_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/adminupload")
            response['Content-Disposition'] = f'inline; filename={os.path.basename(download_path)}'

            return response
    raise Http404


def user_directory_path(instance, filename):

    # To generate a new file name, we get the current date and time 
    # and add a prefix to it then join the extension at the end
    a = f"FAV{str(datetime.now())}"
    # Remove special chacracters and spaces from the date string
    filename = ''.join(re.split(r'-|\.|:|\ ', a))
    # Combine the date string with file extension to form new file name


    return f"user_{instance.uploaded_by.id}/{filename}"