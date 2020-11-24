import os
from config import DefaultConfig


#file_path = 'C:\\Website\\app\\static\\test.txt'
#f = open(file_path, 'w')
#f.close()


print(os.path.join(DefaultConfig.UPLOAD_FOLDER, 'test.txt'))
f = open(os.path.join(DefaultConfig.UPLOAD_FOLDER, 'test.txt'), 'w')
f.write('hello bitches')
f.close()