import React from 'react';
import ReactDOM from 'react-dom';

// react router
import { Router, Route } from 'react-router-dom';
import { createBrowserHistory} from 'history';
import FirstSearch from './components/Attraction/FirstSearch'
import Login from './components/Login/Login'
import Main from './components/Main/Main'
import Register from './components/Regist/Register'
import RoomInput from './components/RoomInput/RoomInput'

import * as serviceWorker from './serviceWorker';

const history = createBrowserHistory();

ReactDOM.render(
  
  <Router history={history}>
    <Route exact path='/' component={Main} history={history} />
    <Route exact path='/regist' component={Register} history={history} />
    <Route path="/attraction" component={FirstSearch} history={history} />
    <Route path="/login" component={Login} history={history} />
    <Route path="/room" component={RoomInput} history={history} />

  </Router>
  , document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
