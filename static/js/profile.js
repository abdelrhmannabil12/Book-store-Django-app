var updatebtns=document.getElementsByClassName('update-cart')

for(var i=0;i<updatebtns.length;i++){
    updatebtns[i].addEventListener('click',function(){
        var bookid = this.dataset.book
        var action=this.dataset.action
        console.log(bookid,action)

        if(user === "AnonymousUser"){
            console.log('no logged in')
        }
        else{updateUserOrder(bookid,action)
        }
    })
}


function updateUserOrder(bookid,action){
    console.log("user is logged in , sending data")

    var url='/update_item/'

    fetch(url,{
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken
        },
        body:JSON.stringify({'bookid':bookid,'action':action})
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        console.log('data: ',data)
        location.reload()
    })
}


function togglePopup(){
    document.getElementById("popup-1").classList.toggle("active");
}