import os
import flask
import flask_socketio
import requests
import flask_sqlalchemy
import models

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)


@app.route('/')
def hello():
    return flask.render_template('index.html')

@socketio.on('connect')
def on_connect():
    print 'Someone connected!'
    
    socketio.emit('all numbers', {
        'numbers': all_mah_numbers
    })
    

@socketio.on('disconnect')
def on_disconnect():
    print 'Someone disconnected!'

all_mah_numbers = []
user_list = []
bot_img_url = "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwj0r8_DjKPSAhXjrVQKHaNpDRMQjRwIBw&url=%2Furl%3Fsa%3Di%26rct%3Dj%26q%3D%26esrc%3Ds%26source%3Dimages%26cd%3D%26cad%3Drja%26uact%3D8%26ved%3D0ahUKEwj0r8_DjKPSAhXjrVQKHaNpDRMQjRwIBw%26url%3Dhttps%253A%252F%252Fplus.google.com%252F115511694512557777290%26psig%3DAFQjCNEiUuNGMK6fEgyLabfX9Pe5ZblB1A%26ust%3D1487832064882648&psig=AFQjCNEiUuNGMK6fEgyLabfX9Pe5ZblB1A&ust=1487832064882648"

@socketio.on('new number')
def on_new_number(data):
    if (data['facebook_user_token'] != ''):
        response= requests.get('https://graph.facebook.com/v2.8/me?fields=id%2Cname%2Cpicture&access_token='+data['facebook_user_token'])
        json= response.json()
        
        print "Got an event for new number with data:", data
        all_mah_numbers.append({
            'name': json['name'],
            'picture': json['picture']['data']['url'],
            'message':data['message'],
        })
        containsFlag = 0
        for x in user_list:
            if json['name'] == x['user']:
                containsFlag = 1
        if containsFlag == 0:
            user_list.append({'user': json['name']})
            
    elif (data['google_user_token'] != ''):
        response= requests.get('https://www.googleapis.com/oauth2/v3/tokeninfo?id_token='+data['google_user_token'])
        json= response.json()
        
        print "Got an event for new number with data:", data
        all_mah_numbers.append({
            'name': json['name'],
            'picture': json['picture'],
            'message':data['message'],
        })
        containsFlag = 0
        for x in user_list:
            if json['name'] == x['user']:
                containsFlag = 1
        if containsFlag == 0:
            user_list.append({'user': json['name']})
            
   
    socketio.emit('all numbers', {
        'numbers': all_mah_numbers
    })
    
    socketio.emit('user list', {
        'users': user_list
    })

if __name__ == '__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )

