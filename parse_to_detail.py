import json
import os

from urllib.request import urlopen


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


for x in range(1,4):
	"""
	Ambil 30 artikel pertama
	"""
	html = urlopen('http://www.codepolitan.com/api/v2/posts/latest/post/{}'.format(x)).read()
	parsed_json = json.loads(html.decode('utf-8'))
	for article in parsed_json['result']:
		createFolder(os.getcwd() + '/article/{}'.format(article['id']))
		file = open(os.getcwd() + '/article/' + '{}/index.json'.format(article['id']), 'w') # Buat file baru dengan nama sesuai id artikel
		json_str_to_write = '{"code": 200, "result": ' + json.dumps(article) + '}'
		file.write(json_str_to_write) # Isi kontennya dengan string json
		file.close()
