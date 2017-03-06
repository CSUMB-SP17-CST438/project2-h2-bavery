import * as React from 'react';

import { Button } from './Button';
import { Socket } from './Socket';

export class Content extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'messages': [],
            'users': []
            };
    }

    componentDidMount() {
        Socket.on('all messages', (data) => {
            this.setState({
                'messages': data['messages'],
            });
        })
        Socket.on('user list', (data) => {
            this.setState({
                'users': data['users'],
            })
        })
    }

    render() {
        let messages = this.state.messages.map(
            (n, index) => <li key= {index}>
                <img src= {n.picture} alt="avatar" />
                {n.name}: {n.message}
            </li>
        );
        let users = this.state.users.map(
            (i, index) => <li key= {index}>
                {i.user}: {i.length}
            </li>
        );
        return (
            <div>
                <h1 className="heading">Random Chat!</h1>
                <div
                    className="fb-login-button" 
                    data-max-rows="1" 
                    data-size="medium"
                    data-show-faces="false"
                    data-auto-logout-link="true">
                </div>
                <div
                    className="g-signin2"
                    data-theme="dark">
                </div>
                <div className="container">
                    <div className="userList">
                        <h4>Users:</h4>
                        <div className="list">
                            <ul>{users}</ul>
                        </div>
                    </div>
                    <div className="inputBox">
                        <div className="chatBox">
                            <ul>{messages}</ul>
                        </div>
                        <div className="input">
                            <Button />
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}
