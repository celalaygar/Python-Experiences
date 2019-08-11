import webbrowser
import time
new=2
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

url_1="http://google.com"
webbrowser.get(chrome_path).open(url_1,new=new)

url_2="https://www.youtube.com/"
webbrowser.get(chrome_path).open(url_2,new=new)
