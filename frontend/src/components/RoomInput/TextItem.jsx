import React from "react";

const TextItem = ({ roomname, id, handleClick, mainmember }) => {
  return (
    <div>
      <p>{roomname}</p>
      <p>{mainmember}</p>
      <button onClick={() => handleClick(id)}>삭제</button>
    </div>
  );
};

export default TextItem;