RemotePyUpdate
==============

RemotePyUpdate can be added to a program to allow the author to remotely update said program. It must originally be given a url for the 'Manifest'. The manifest is simply a list of the urls of all the program files that must be downloaded. RemotePyUpdate then downloads each file, and renames it with the name contined within the file itself. 

Usage
==============
Upload program files online (paste bin works well) and copy their url's. Make the manifest as a new text file containing all of the url's of the program files. The manifest should look like this...

      www.file1url.com
      www.file2url.com
      www.file3url.com
      
Upload the manifest text file online (again, paste bin works well) and copy its url. Now execute RemotePyUpdate giving it the url of the manifest as a parameter. 

      python update.py www.manifestFileUrl.com
      
or if you are running it from another program...

      update.run('www.manifestUrl.com')
      
Requirements
==============
(1) The first line in each program file must contain the desired file name of that file. Example file...

      #desiredFileName.py
      number = 1+1
      print number
      
(2) The program and manifest url's must point to raw text. The safest way to do this is to have www.manifestUrl.com point to manifest.txt.
