import os
import flask
import flask_socketio
import requests
import flask_sqlalchemy
import models

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)
messages = []
user_list = []
bot_img_url = ""


@app.route('/')
def hello():
    return flask.render_template('index.html')

@socketio.on('connect')
def on_connect():
    print 'Someone connected!'
    
    messages.append({
            'name': "Robbie",
            'picture': bot_img_url,
            'message': "Someone Connected!!",
        })
    
    socketio.emit('all messages', {
        'messages': messages
    })
    

@socketio.on('disconnect')
def on_disconnect():
    print 'Someone disconnected!'
    messages.append({
            'name': "Robbie",
            'picture': bot_img_url,
            'message': "Someone Disconnected!!",
        })
    
    socketio.emit('all messages', {
        'messages': messages
    })


@socketio.on('new message')
def on_new_message(data):
    if (data['facebook_user_token'] != ''):
        response= requests.get('https://graph.facebook.com/v2.8/me?fields=id%2Cname%2Cpicture&access_token='+data['facebook_user_token'])
        json= response.json()
        
        print "Got an event for new number with data:", data
        messages.append({
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
        messages.append({
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
            
   
    socketio.emit('all messages', {
        'messages': messages
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

