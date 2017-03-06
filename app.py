import os
import flask
import flask_socketio
import requests
import flask_sqlalchemy
import models

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)
all_mah_numbers = []
user_list = []
user_count = 0
bot_img_url = "https://robohash.org/robbie"


@app.route('/')
def hello():
    return flask.render_template('index.html')

@socketio.on('connect')
def on_connect():
    print 'Someone connected!'
    
    all_mah_numbers.append({
            'name': "Robbie",
            'picture': bot_img_url,
            'message': "Someone Connected!!",
        })
    
    user_list.append({'user': 'Anonymous', 'sesId': flask.requests.sesId})
    user_count = user_list.count()
    
    socketio.emit('all numbers', {
        'numbers': all_mah_numbers
    })
    

@socketio.on('disconnect')
def on_disconnect():
    print 'Someone disconnected!'
    all_mah_numbers.append({
            'name': "Robbie",
            'picture': bot_img_url,
            'message': "Someone Disconnected!!",
        })
    
    socketio.emit('all numbers', {
        'numbers': all_mah_numbers
    })


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
        for x in user_list:
            if flask.requests.sesId == x['sesId']:
                x['user'] = json['name']
            
    elif (data['google_user_token'] != ''):
        response= requests.get('https://www.googleapis.com/oauth2/v3/tokeninfo?id_token='+data['google_user_token'])
        json= response.json()
        
        print "Got an event for new number with data:", data
        all_mah_numbers.append({
            'name': json['name'],
            'picture': json['picture'],
            'message':data['message'],
        })
        for x in user_list:
            if flask.requests.sesId == x['sesId']:
                x['user'] = json['name']
            
   
    socketio.emit('all numbers', {
        'numbers': all_mah_numbers
    })
    
    socketio.emit('user list', {
        'users': user_list,
        'count': user_count,
    })

if __name__ == '__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )

