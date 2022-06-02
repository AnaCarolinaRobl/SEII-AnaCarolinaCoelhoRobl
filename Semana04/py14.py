import os

os.chdir('/Users/anaca/Desktop/Ex')

print(os.getcwd())

for f in os.listdir():
    #print(os.path.splitext(f))
    file_name, file_ext = os.path.splitext(f)
    print(file_name)

    f_title, f_course, f_number = file_name.split('-')

    f_title = f_title.strip()
    f_course = f_course.strip()
    f_number = f_number.strip()[1:].zfill(2)

    
    #print('{}-{}-{}{}'.format(f_number, f_course, f_title, file_ext))

    new_name = '{}-{}{}'.format(f_number, f_title, file_ext)

    os.rename(f, new_name)
