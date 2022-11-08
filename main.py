from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory = "templates")

@app.get('/')
def home():
    
    return "Welcome"

@app.get("/greet")
def greet_user(name):
   
    
    name = input("Enter your Username: ")
    password = int(input("Enter your Password: "))
    if( password == 9231045):
        
        
        return " Login Successfully: " +name
    else:
        return "Failed"
