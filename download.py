from urllib.request import urlretrieve

PAPER_DIR = 'acl_2016/'

for i in range(1, 232):
    file_url = 'http://aclweb.org/anthology/P16-1' + str(i).rjust(3, '0')
    file_path = PAPER_DIR + str(i).rjust(3, '0') + '.pdf'

    urlretrieve(file_url, file_path)
