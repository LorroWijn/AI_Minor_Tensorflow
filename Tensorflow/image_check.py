from PIL import Image     
import os
import shutil

train_path = 'E:/School/Minor - Artificial Intelligence/Projects/Code/Tensorflow/workspace/images/train/'
test_path = 'E:/School/Minor - Artificial Intelligence/Projects/Code/Tensorflow/workspace/images/test/'
new_path = 'E:/School/Minor - Artificial Intelligence/Images Sorted/extra'


def file_check(resource_path, information):
      moved = False
      img_count = 0
      xml_count = 0
      others_count = 0
      file_count = 0
      for file in os.listdir(resource_path):
            file_count = file_count + 1
            extension = file.split('.')[-1]
            if extension == 'jpeg':
                  img_count = img_count + 1
                  fileLoc = resource_path+file
                  img = Image.open(fileLoc)
                  if img.mode != 'RGB':
                        img.close()
                        print(file)
                        # moved = True
                        os.replace(resource_path + file, new_path + file)
                  img.close()
            elif extension == 'xml':
                  xml_count = xml_count + 1
                  if moved == True:
                        print(file + ' SECOND')
                        os.replace(resource_path + file, new_path + file)
                        moved = False
            else:
                  others_count = others_count + 1
                  print(file)
      print (information + ': JPEG files: ' + str(img_count) + " | XML files: " + str(xml_count) + " | otherscount: " + str(others_count) + " | total file: " + str(file_count))

def is_image(filename, verbose=True):

      data = open(filename,'rb').read(10)

      # check if file is JPG or JPEG
      if data[:3] == b'\xff\xd8\xff':
            if verbose == True:
                  print(filename+" is: JPG/JPEG.")
            return True

      # check if file is PNG
      if data[:8] == b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a':
            if verbose == True:
                  print(filename+" is: PNG.")
            return True

      # check if file is GIF
      if data[:6] in [b'\x47\x49\x46\x38\x37\x61', b'\x47\x49\x46\x38\x39\x61']:
            if verbose == True:
                  print(filename+" is: GIF.")
            return True

      return False


import os
import cv2
import imghdr

def check_images(s_dir, ext_list):
    bad_images=[]
    bad_ext=[]
    s_list= os.listdir(s_dir)
    for klass in s_list:
        klass_path=os.path.join (s_dir, klass)
        print ('processing class directory ', klass)
        if os.path.isdir(klass_path):
            file_list=os.listdir(klass_path)
            for f in file_list:               
                f_path=os.path.join (klass_path,f)
                tip = imghdr.what(f_path)
                if ext_list.count(tip) == 0:
                  bad_images.append(f_path)
                if os.path.isfile(f_path):
                    try:
                        img=cv2.imread(f_path)
                        shape=img.shape
                    except:
                        print('file ', f_path, ' is not a valid image file')
                        bad_images.append(f_path)
                else:
                    print('*** fatal error, you a sub directory ', f, ' in class directory ', klass)
        else:
            print ('*** WARNING*** you have files in ', s_dir, ' it should only contain sub directories')
    return bad_images, bad_ext

source_dir = train_path
good_exts=['jpg', 'png', 'jpeg', 'gif', 'bmp' ] # list of acceptable extensions
bad_file_list, bad_ext_list=check_images(source_dir, good_exts)
if len(bad_file_list) !=0:
      print('improper image files are listed below')
for i in range (len(bad_file_list)):
      print (bad_file_list[i])
else:
      print(' no improper image files were found')


# for file in os.listdir(test_path):
#       fileLoc = test_path+file
#       is_image(fileLoc)

# for file in os.listdir(train_path):
#       fileLoc = train_path+file
#       is_image(fileLoc)
      

# file_check(test_path, 'Test files')
# file_check(train_path, 'Train files')