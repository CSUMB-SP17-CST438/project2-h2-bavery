import * as React from 'react';

import { Socket } from './Socket';

export class Button extends React.Component {
    handleSubmit(event) {
        event.preventDefault();

        let message = document.getElementById("message").value;
        console.log('Post button clicked');
        FB.getLoginStatus((response) => {
            if (response.status == 'connected') {
                Socket.emit('new number', {
                    'google_user_token': '',
                    'facebook_user_token':
                        response.authResponse.accessToken,
                    'message': message,
                });
            
        } else {

                let auth = gapi.auth2.getAuthInstance();
                let user = auth.currentUser.get();
                if(user.isSignedIn()) {
                    Socket.emit('new number', {
                        'google_user_token':
                            user.getAuthResponse().id_token,
                        'facebook_user_token': '',
                        'message':message,
                    });
                }
            }
        });
        console.log('Sent up the message to server!');
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <span>
                    <input type="text" id="message" /><button>Post</button>
                </span>
            </form>
        );
    }
}
