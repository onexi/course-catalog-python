import urllib.request

urls = [
    'http://student.mit.edu/catalog/m1a.html',
    'http://student.mit.edu/catalog/m1b.html'
    # 'http://student.mit.edu/catalog/m1c.html',
    # 'http://student.mit.edu/catalog/m2a.html',
    # 'http://student.mit.edu/catalog/m2b.html',
    # 'http://student.mit.edu/catalog/m2c.html',
    # 'http://student.mit.edu/catalog/m3a.html',
    # 'http://student.mit.edu/catalog/m3b.html',
    # 'http://student.mit.edu/catalog/m4a.html',
    # 'http://student.mit.edu/catalog/m4b.html',
    # 'http://student.mit.edu/catalog/m4c.html',
    # 'http://student.mit.edu/catalog/m4d.html',
    # 'http://student.mit.edu/catalog/m4e.html',
    # 'http://student.mit.edu/catalog/m4f.html',
    # 'http://student.mit.edu/catalog/m4g.html',
    # 'http://student.mit.edu/catalog/m5a.html',
    # 'http://student.mit.edu/catalog/m5b.html',
    # 'http://student.mit.edu/catalog/m6a.html',
    # 'http://student.mit.edu/catalog/m6b.html',
    # 'http://student.mit.edu/catalog/m6c.html',
    # 'http://student.mit.edu/catalog/m7a.html',
    # 'http://student.mit.edu/catalog/m8a.html',
    # 'http://student.mit.edu/catalog/m8b.html',
    # 'http://student.mit.edu/catalog/m9a.html',
    # 'http://student.mit.edu/catalog/m9b.html',
    # 'http://student.mit.edu/catalog/m10a.html',
    # 'http://student.mit.edu/catalog/m10b.html',
    # 'http://student.mit.edu/catalog/m10c.html',
    # 'http://student.mit.edu/catalog/m11a.html',
    # 'http://student.mit.edu/catalog/m11b.html',
    # 'http://student.mit.edu/catalog/m11c.html',
    # 'http://student.mit.edu/catalog/m12a.html',
    # 'http://student.mit.edu/catalog/m12b.html',
    # 'http://student.mit.edu/catalog/m12c.html',
    # 'http://student.mit.edu/catalog/m14a.html',
    # 'http://student.mit.edu/catalog/m14b.html',
    # 'http://student.mit.edu/catalog/m15a.html',
    # 'http://student.mit.edu/catalog/m15b.html',
    # 'http://student.mit.edu/catalog/m15c.html',
    # 'http://student.mit.edu/catalog/m16a.html',
    # 'http://student.mit.edu/catalog/m16b.html',
    # 'http://student.mit.edu/catalog/m18a.html',
    # 'http://student.mit.edu/catalog/m18b.html',
    # 'http://student.mit.edu/catalog/m20a.html',
    # 'http://student.mit.edu/catalog/m22a.html',
    # 'http://student.mit.edu/catalog/m22b.html',
    # 'http://student.mit.edu/catalog/m22c.html'
]

# fetch content
def pull(url):
    # Enter your code here
    return data

# save file
def store(data,file):
    # Enter your code here
    print('save: ' + file)    

# loop through urls
for url in urls:
    # Enter your code here
    data = pull(url)
    # Enter your code here
    store(data, file)
