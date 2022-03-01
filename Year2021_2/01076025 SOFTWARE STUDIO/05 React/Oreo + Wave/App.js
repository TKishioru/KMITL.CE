import './App.css';
import { Component } from 'react';

class Head extends Component{
  render(){
    return(
      <div class="T1">
        <h1 >Group's Members</h1>
      </div>
    )
  }
}


class Card extends Component{
  state = {
    value1 :"MIN",
  }
  
    
  updateValue(){
    var Buffer = 0
    if(this.state.value1.toString() === "MIN"){
      this.setState({value1: 1})
    }
    else if(this.state.value1 >= 1 && this.state.value1 <= 8  ){
      Buffer = this.state.value1
      Buffer++
      this.setState({value1: Buffer})
    }
    else if(this.state.value1 === 9){
      this.setState({value1: "MAX"})
    }
    else if(this.state.value1.toString() === "MAX"){ 
      alert("can't vote")
    }
}
  updateValue2(){
    var Buffer = 0
    if(this.state.value1.toString() === "MAX"){
      this.setState({value1: 9})
    }
    else if(this.state.value1 >= 2 && this.state.value1 <= 9  ){
      Buffer = this.state.value1
      Buffer--
      this.setState({value1: Buffer})
    }
    else if(this.state.value1 === 1){
      this.setState({value1: "MIN"})
    }
    else if(this.state.value1.toString() === "MIN"){ 
      alert("can't Unvote")
    }
  }
    
  
  render(){
  return(
    <div>
      <div class="rectangle"> 
        <h1>{this.props.name}</h1>
        <img src= {this.props.img} alt="" class="pic"></img>
        <h2>{this.props.StuNum}</h2>

        <div class= "flex-content">
        <p>{this.props.content}</p>
        </div>

        <div class="buttonZone">
          <div class="flexbutton">
            <button class="buttons" type="button" onClick={this.updateValue.bind(this)}>Click to Vote</button>
            <div class="vote"><h2>{this.state.value1.toString()}</h2></div>
            <button class="buttons" type="button"onClick={this.updateValue2.bind(this)}>Click to Unvote</button>
          </div>
        </div>
      </div>
    </div>
  );
  }
}


class Main extends Component{

  render(){
    return(
      <div>
        <Head />
        <Card name="MS. Krittikamas Sunophak" StuNum="62010029" img ="https://www.w3schools.com/howto/img_avatar2.png"
          content="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
          AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
          AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
          AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
          AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
          AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
          AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
          AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        />

        <Card name="MS. Khampeerada Poothong" StuNum="62010090" img ="https://www.w3schools.com/howto/img_avatar2.png"
          content="BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
          BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
          BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
          BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
          BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
          BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
          BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
          BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
        />
        <Card name="MR .Patcharapol Prompang" StuNum="63015117" img ="https://www.w3schools.com/howto/img_avatar.png"
          content="CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
          CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
          CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
          CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
          CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
          CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
          CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
          CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC"
        />
        <Card name="MR .Sarayut Aree" StuNum="63015166" img ="https://www.w3schools.com/howto/img_avatar.png"
          content="CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
          CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
          CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
          CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
          CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
          CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
          CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
          CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC"
        />
        <Card name="MR .Sarin Hongthong" StuNum="63015183" img ="https://www.w3schools.com/howto/img_avatar.png"
          content="CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
          CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
          CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
          CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
          CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
          CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
          CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
          CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC"
        />
      </div>
    )
  }
}


export default Main;