import * as React from 'react';

import { Socket } from './Socket';

export class Button extends React.Component {
    handleSubmit(event) {
        event.preventDefault();

        let random = Math.floor(Math.random() * 100);
        console.log('Generated a random number: ', random);
        FB.getLoginStatus((response) => {
            if (response.status == 'connected') {
                Socket.emit('new number', {
                    'google_user_token': '',
                    'facebook_user_token':
                        response.authResponse.accessToken,
                    'number': random,
                });
            
        } else {

                let auth = gapi.auth2.getAuthInstance();
                let user = auth.currentUser.get();
                if(user.isSignedIn()) {
                    Socket.emit('new number', {
                        'google_user_token':
                            user.getAuthResponse().id_token,
                        'facebook_user_token': '',
                        'number':random,
                    });
                }
            }
        });
        console.log('Sent up the random number to server!');
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <input type="text" name="message" /><button>Post</button>
            </form>
        );
    }
}
