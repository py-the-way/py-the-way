import React, { Component } from 'react';
import Reorder, {reorderImmutable} from 'react-reorder'
import Immutable from 'immutable';

import './App.css';

class App extends Component {

  constructor () {
    super();

    this.state = {
      list: Immutable.List(
        ["Education","Employment","Home","Healthcare","Wealth"]
      )
    };
  }

  onReorder (event, previousIndex, nextIndex) {
    const list = reorderImmutable(this.state.list, previousIndex, nextIndex);

    this.setState({
      list: list
    });

  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1>py-the-way</h1>
        </header>
        <Reorder
          reorderId="myList"
          component="ul"
          className={"order"}
          placeholderClassName={"placeholdr"}
          draggedClassName={"dragged"}
          lock="horizontal"
          
          holdTime={250}
          onReorder={this.onReorder.bind(this)}
        >
          {
            this.state.list.map((val) => (
              <div key={val} className={"sel"}>
                <li
                  className={"listItem"}
                >
                  {val}
                </li>
              </div>
            )).toArray()
          }
        </Reorder>
      </div>
    );
  }
}

export default App;
