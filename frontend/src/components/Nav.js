import React, { Component } from 'react';
import '../static/Nav.css'

class Nav extends Component {
    render() {
        return (
            <div className="Nav">
                <div className="Nav-logo">
                    <h1>Triphub</h1>
                </div>
                <div className="Nav-prof">
                    <a href="/">PROFILE</a>
                </div>
                <div className="Nav-login">
                    <a href="/">LOGOUT</a>
                </div>
            </div>
        );
    }
}

export default Nav;