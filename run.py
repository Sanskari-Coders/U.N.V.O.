import subprocess
import webbrowser
webbrowser.open('http://127.0.0.1:8000/')
subprocess.call(['python','manage.py','runserver'])
