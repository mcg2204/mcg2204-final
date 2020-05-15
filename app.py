# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: mcalregreenlees

Mary Clare Greenlees
mcg2204 
1006 Final
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def home_page():
    return render_template("index.html")

#return <b> Test 123 </b>
    #this makes something bolded

@app.route("/classes")
def classes():
    return render_template("classes.html")

# to link to other things - use <a href-"website"></a>
           

#start the server
if __name__ == "__main__":
    app.run()