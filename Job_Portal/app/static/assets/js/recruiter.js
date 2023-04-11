document.getElementById('Qcard').style.display = 'none'; 
document.getElementById('cdetailcard').style.display = 'none'; 
document.getElementById('homecard').style.display = 'block'; 


function home(){
    document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('Qcard').style.display = 'none'; 
document.getElementById('cdetailcard').style.display = 'none'; 
document.getElementById('homecard').style.display = 'block'; 
    });



 
}
function addQuestion() {
    // myprofile=true;
    // document.getElementById('rules').style.display='none'
    // document.getElementById('mydiv').style.display = 'none';
    document.addEventListener('DOMContentLoaded', function() {
    console.log("add question")
    document.getElementById('homecard').style.display = 'none'; 
    document.getElementById('Qcard').style.display = 'block'; 
    document.getElementById('cdetailcard').style.display = 'none'; 
    });
     


    }
function CandidatesDetail() {
    document.addEventListener('DOMContentLoaded', function() {
        myprofile=true;
        // document.getElementById('rules').style.display='none'
        // document.getElementById('mydiv').style.display = 'none'; 
        document.getElementById('Qcard').style.display = 'none'; 
        document.getElementById('cdetailcard').style.display = 'block';
        document.getElementById('homecard').style.display = 'none'; 
    });

        }    