import requests, zipfile
from io import BytesIO

# Defining the zip file URL
url = 'https://github.com/ytarazona/ft_data/raw/main/data/LC08_232066_20190727.zip'

# Split URL to get the file name
filename = url.split('/')[-1]

# Downloading the file by sending the request to the URL
req = requests.get(url)

# extracting the zip file contents
file = zipfile.ZipFile(BytesIO(req.content))
file.extractall()