import React, { useContext } from 'react';
import { MyContext } from '../App';

function ComponentB() {

  const data = useContext(MyContext)

  return (
    <div>
      {data}
    </div>
  )
}

export default ComponentB
