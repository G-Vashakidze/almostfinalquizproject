
const burger = document.querySelector('.burger');
const menu = document.querySelector('.menucontainer');
const head = document.querySelector('header')
const content = document.querySelector('.content')


burger.addEventListener('click', () => {
    console.log(burger )
  burger.classList.toggle('active');
  menu.classList.toggle('active');
  head.classList.toggle('inactive')
  content.classList.toggle('active')

});


const select = document.getElementById("selectQuiz")
const tables = document.querySelectorAll(".table");
if (select !== null){
  select.addEventListener('change' , ()=>{
    let value = select.value
    
    tables.forEach( table => {
    if (table.id === value){
        
    table.classList.remove("hidden");
    }else{
        table.classList.add("hidden");
    }
        
    });
})

}
    









function closeModal() {
  document.getElementById("myModal").style.display = "none";
}

const c = document.querySelector('.close')

c.addEventListener("click", closeModal);



  
