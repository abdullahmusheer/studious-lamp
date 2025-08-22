import requests
from fastapi import FastAPI
#calling the fastapi module - represents our entire application for Crud apps
app = FastAPI()

#now access this "app" created 

@app.get("/hello")
def hello():
    return {"Hello":"how are you doing?"}

@app.get("/funtest")
def fun():
    name =input ("whats your name? ")
    return {f"thanks {name}"}
    

@app.get("/")
def root():
    return {"this is the root page"}

@app.get("/catfact")
def inquire():
    req = requests.get("https://catfact.ninja/fact")
    return req.json()
   