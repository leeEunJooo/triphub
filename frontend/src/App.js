import React, { Component } from 'react';
import './App.css';
import axios from "axios";
import TextItem from "./TextItem";

import Nav from './components/Nav';
import Loading from './components/Loading';

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken"

class App extends Component {
  state = {
    roomname: "",
    mainmember: "",
    roomList: []
  };

  componentDidMount() {
    this._renderText();
  }
  render() {
    const { roomList, roomname, mainmember } = this.state;
    return (
      <div className="App">
        <Nav/>
        {/* <hr/> Nav-bar구분용 추후에 삭제예정 */}
        <Loading/>
        <div className='logo-hidden'>Triphub</div>
        <h1> 리액트 연동 테스트 앱 </h1>
        <div>
          <label>
            방이름:
            <input
              type="text"
              value={roomname}
              onChange={this._handleChangeRoom}
            />
          </label>
          <label>
            방장이름:
            <input
              type="text"
              value={mainmember}
              onChange={this._handleChangeMember}
            />
          </label>
          <button onClick={this._handleSubmit}>제출</button>
        </div>
        <h2>입력값들 리스트</h2>
        {roomList.map((room, index) => {
          return (
            <TextItem
              roomname={room.roomname}
              mainmember={room.mainmember}
              key={index}
              id={room.id}
              handleClick={this._deleteText}
            />
          );
        })}
      </div>
    );
  }
  _handleChangeRoom = event => {
    this.setState({ roomname: event.target.value });
    
  };

  _handleChangeMember = event => {
    this.setState({ mainmember: event.target.value });
    
  };

  _handleSubmit = () => {
    const { roomname, mainmember } = this.state;
    const now = new Date();
    console.log(roomname + mainmember);

    axios
      .post("/api/roominput/", {date:now, roomname: roomname, mainmember:mainmember })
      .then(res => this._renderText());
  };

  _renderText = () => {
    axios
      .get("/api/roominput/")
      .then(res => this.setState({ roomList: res.data }))
      .catch(err => console.log(err));
  };

  _deleteText = id => {
    axios.delete(`/api/roominput/${id}`).then(res => this._renderText());
  };
}

export default App;
