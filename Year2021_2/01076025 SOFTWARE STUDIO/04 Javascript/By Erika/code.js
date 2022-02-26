let clicked = false;
let color = ["#ff8844","#99ddff","#ffc0cb","#f0e68c","#cccccc","#abbe9e"]
let index = 0;
let displayMember = false
let image = [ "https://i.ytimg.com/vi/aHYiO8Y5H3Y/maxresdefault.jpg",
              "https://image.freepik.com/free-vector/premium-quality-product-golden-label-design_1017-12393.jpg",
              "https://pbs.twimg.com/profile_images/3472865522/e3a573718853d0f6c9b8d26bd013bde9_400x400.jpeg",
              "https://i.pinimg.com/474x/06/7d/bb/067dbbb32bfe1fc9180592115ebcd3a2.jpg",
            ]
function ShowDate(){
    if(clicked == false){
        document.getElementById('dateButton').innerHTML = Date()
        document.getElementById("dateButton").style.backgroundColor = color[index];
        document.getElementById("dateButton").style.color = "red";
        clicked = true;
    }
    else {
        document.getElementById("dateButton").style.backgroundColor = color[index];  
    }
    index +=1;
    if(index==6) index=0;
}

function ShowMemberBackground(show){
    if(show == 1){
        document.getElementById("memberText").style.backgroundColor = "#99ddff";
        document.getElementById("memberText").style.color = "blue";
        document.getElementById("memberText").style.cursor = "pointer";
    }
    else {
        document.getElementById("memberText").style.color = "black";
        document.getElementById("memberText").style.backgroundColor = "transparent";
    }
}

function ToggleMember(){
    if (displayMember == true) {
        document.getElementById('memberDetail').style.display = 'none';
        displayMember = false;
    }
    else {
        document.getElementById('memberDetail').style.display = 'block';
        displayMember = true;
    }
}

function ChangeImage(selector){
    document.getElementById('KImage').src = image[selector];
}