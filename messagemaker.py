import time
import os
from shutil import copyfile
from shutil import rmtree

cards = [
            "asd2asdas","senpai","smalltree4asdas","idoitic5dads","6s","noobmaster7s","severe8s","randoms","ursisteris_hot0s","unsubscribeT_series4k","qqwrdQs","Ks","As"
            "dsad2h","sdasd3h","chemistry_isbad_for_health","crush","yourmoron6h","hackedyh","kikidoyouloveme","dierip9h","ssowqooqoweo10h","Jh","asdhjaksdhQh","Kh","dqwhdwqdAh"
            "bigtree2d","tree3d","kontol4d","sadasjdhj5d","6d","erzor7d","fiftyshades","9d","10dasdasdfsdd","Jd","patners","kimjong","Adityabanik"
            "llslas2c","qweqe3c","x4c","kontolx5xxc","fuckingseaserver6dc","donald_trump_isdead","8asdasdc","9c","qduqhduhj10c","jackfromunbox","Qc","ajsdhjkasdKc","e2eAc"
           ]


"""creating an message from alphabets in sorted order by their ascii values path is /alphabets"""
def message_generator(message):
    img_path= os.getcwd() + r'/alphabets'
    folder_path= os.getcwd() + r'/Secret'
    #creating new folder to store messages
    try:
        os.makedirs(folder_path)
    except FileExistsError:
        rmtree(folder_path)
        time.sleep(1)
        os.makedirs(folder_path)

    # this method gets the images present in our folder
    alphabets = os.listdir(img_path)
    for i,e in enumerate(message):
        search_string= str(ord(e))+'.jpg'

        if search_string in alphabets:
            copyfile(img_path + '/'+ search_string , folder_path +'/'+ str(i)+'.jpg')
    print('message generated')


"""encrypts the generated sequence of image message using illuminati's algorithm"""
def encrypter():
    #getting current_path of the terminal
    current_path=os.getcwd()
    folder_path= current_path + r'/Secret'
    #getting files from the folder
    try:
        files = os.listdir(folder_path)
    except FileExistsError:
        return
    #Switching terminal to Secret directory
    os.chdir(folder_path)
    #applying illuminati level encryption
    for i,e in enumerate(files):
        os.rename(e,cards[i]+'.jpg')
    #Switch the terminal back to current_path
    os.chdir(current_path)
    print('renaming completed')

"""reveils the encrypted message safely"""
def reveil():
    #getting current_path of the terminal
    current_path=os.getcwd()
    folder_path= current_path + r'/Secret'
    #getting files from the folder
    try:
        files = os.listdir(folder_path)
    except:
        return
    #Switching terminal to Secret directory
    os.chdir(folder_path)
    #applying illuminati level encryption
    for e in files:
        try:
            index=cards.index(e[:e.find('.')])
        except:
            os.chdir(current_path)
            return
        os.rename(e,str(index)+'.jpg')
    #Switch the terminal back to current_path
    os.chdir(current_path)
    print('illuminati')
