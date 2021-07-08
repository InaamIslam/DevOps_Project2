from flask import Flask, render_template

@app.route('/', methods=['GET','POST'])
def index():
    #get the name of the city 
    city = requests.get("http://...
    #get the activty 
    activty = requests.get("http://...
    #post the random holiday plan
   
    holiday_plan= requests.post("http://...

  return render_template('index.html', 
  title='Holiday Plan', city = city.text, 
  activity=activity.text info=info,)