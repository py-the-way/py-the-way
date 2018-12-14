import React, { Component } from 'react';
import Reorder from 'react-reorder'

import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1>py-the-way</h1>
        </header>
        <Reorder
          reorderId="my-list" // Unique ID that is used internally to track this list (required)
          reorderGroup="reorder-group" // A group ID that allows items to be dragged between lists of the same group (optional)
          // getRef={this.storeRef.bind(this)} // Function that is passed a reference to the root node when mounted (optional)
          component="ul" // Tag name or Component to be used for the wrapping element (optional), defaults to 'div'
          placeholderClassName="placeholder" // Class name to be applied to placeholder elements (optional), defaults to 'placeholder'
          draggedClassName="dragged" // Class name to be applied to dragged elements (optional), defaults to 'dragged'
          lock="horizontal" // Lock the dragging direction (optional): vertical, horizontal (do not use with groups)
          holdTime={500} // Default hold time before dragging begins (mouse & touch) (optional), defaults to 0
          touchHoldTime={500} // Hold time before dragging begins on touch devices (optional), defaults to holdTime
          mouseHoldTime={200} // Hold time before dragging begins with mouse (optional), defaults to holdTime
          //onReorder={this.onReorder.bind(this)} // Callback when an item is dropped (you will need this to update your state)
          autoScroll={true} // Enable auto-scrolling when the pointer is close to the edge of the Reorder component (optional), defaults to true
          disabled={false} // Disable reordering (optional), defaults to false
          disableContextMenus={true} // Disable context menus when holding on touch devices (optional), defaults to true
          placeholder={
            <div className="custom-placeholder" /> // Custom placeholder element (optional), defaults to clone of dragged element
          }
        >
          {
            this.state.list.map((item) => (
              <li key={item.name}>
                {item.name}
              </li>
            )).toArray()
            /*
            Note this example is an ImmutableJS List so we must convert it to an array.
            I've left this up to you to covert to an array, as react-reorder updates a lot,
            and if I called this internally it could get rather slow,
            whereas you have greater control over your component updates.
            */
          }
        </Reorder>
      </div>
    );
  }
}

export default App;
