import webbrowser
import time
print(''' This application shell has been created by 
      NoxatraDev other name on youtube Sapientes Art & Technology 
      commands:
          1- root -e
          2- exit
          ---------------------------
          1- git open
          2- itch open
          3- /search
          4- ai_makejoke
          5- open c-gpt
          6- exit
          ---------------------------
          1- /exitSearchmode
          2- whatever you write. It searches.''')
def undefined():
    print("Error 1071: Command undefined. \n")

    
def search_item(search):
    url = "https://google.com/search?q="+search
    webbrowser.get().open(url)
    print("Results about on default browser screen about: ",end=(search))

def open_github():
    
                git_url = "https://github.com/"
                webbrowser.get().open(git_url)
                print("opening github...")
def open_itch():
    
                git_url = "https://itch.io/"
                webbrowser.get().open(git_url)
                print("opening itch...")
def  make_joke():
    joker_url = "https://pointerpointer.com/"
    webbrowser.get().open_new_tab(joker_url)
    
    
def chatGPT():
        chat_url = "https://chat.openai.com/chat"
        webbrowser.get().open(chat_url)
        print("Opening my BFF <3..")
        
def human_Thanks():
    print("-<3- You're welcome. ;) -<3-")


password = input("Please enter new root password: ")
while(True):
    com = input("\nPlease enter a command:-# ")
    if(com == "root -e"):
        while(True):
            psswd = input("Please enter root password: ")
            if(psswd == password):    
                 #linux_shell
                    a = input("\nroot@Admin:-$ ")
                    if(a == "/search"):
                        #google'da arama modu
                        while(True):
                            searchitem = input("\nwhat do you search:-$ ")
                            if(searchitem == "/exitSearchmode"):
                                print("Quitting searchmode...")
                                break
                            else:
                                search_item(searchitem)
                
                    elif(a == "exit"):
                        break
                    elif(a == "git open"):
                        open_github()
                    elif(a == "itch open"):
                        open_itch()
                    elif(a == "ai_makejoke"):
                        make_joke()
                    elif(a == "open c-gpt"):
                        chatGPT()
                    elif(a == "Thanks"):
                        human_Thanks()
                
                    else:
                        undefined()
            elif(psswd != password):
                print("Password incorrect! Please retry in 3 secs.")
                time.sleep(3)
                continue
    elif(com == "exit"):
        break
    else:
        undefined()