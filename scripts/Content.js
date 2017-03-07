import * as React from 'react';

import { Button } from './Button';
import { Socket } from './Socket';

export class Content extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'numbers': [],
            'users list': [],
            'user count': 0
            };
    }

    componentDidMount() {
        Socket.on('all numbers', (data) => {
            this.setState({
                'numbers': data['numbers'],
            });
        });
        Socket.on('user list', (data) => {
            this.setState({
                'users list': data['users'],
            });
        });
        Socket.on('user count', (data) => {
            this.setState({
                'user count': data['count']
            });
        });
       
    }

    render() {
        let numbers = this.state.numbers.map(
            (n, index) => <li key= {index}>
                <img src= {n.picture} />
                {n.name}: {n.message}
            </li>
        );
        
        var users_list = [];
        for (var user of this.state['users list']) {
            var item = <li key={user}>{user}</li>;
            users_list.push(item);
        }
        
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
                        <h4>Users:  {this.state['user_count']}</h4>
                        <div className="list">
                            <ul>{users_list}</ul>
                        </div>
                    </div>
                    <div className="inputBox">
                        <div className="chatBox">
                            <ul>{numbers}</ul>
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
