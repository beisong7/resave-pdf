import os
import pikepdf
 
# assign directory
rootdir = "G:\EDMS Upload"
 
# iterate over files in that directory
# resave the files again after opening
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        filename = os.path.join(subdir, file)
        print(filename)
        if(filename.lower().endswith('.pdf')):    
            try:    
                with pikepdf.open(filename, allow_overwriting_input=True) as pdf:
                    pdf.save(filename)
            except:
                print("an exception occured")
        else:
            print("skipping - not a pdf")
        