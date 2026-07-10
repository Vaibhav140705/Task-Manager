// ======================================================
// Task Manager Dashboard JavaScript
// ======================================================

document.addEventListener("DOMContentLoaded", () => {

    initializeSearch();

    initializeStatusFilter();

    initializeClock();

    animateCards();

});


// ======================================================
// Live Search
// ======================================================

function initializeSearch(){

    const searchInput = document.getElementById("searchInput");

    if(!searchInput) return;

    searchInput.addEventListener("keyup", function(){

        const value = this.value.toLowerCase();

        const rows = document.querySelectorAll("#taskTable tbody tr");

        rows.forEach(row=>{

            const task = row.cells[0].innerText.toLowerCase();

            const assigned = row.cells[1].innerText.toLowerCase();

            if(task.includes(value) || assigned.includes(value)){

                row.style.display="";

            }

            else{

                row.style.display="none";

            }

        });

    });

}


// ======================================================
// Status Filter
// ======================================================

function initializeStatusFilter(){

    const filter=document.getElementById("statusFilter");

    if(!filter) return;

    filter.addEventListener("change",function(){

        const selected=this.value.toLowerCase();

        const rows=document.querySelectorAll("#taskTable tbody tr");

        rows.forEach(row=>{

            const status=row.cells[5].innerText.toLowerCase();

            if(selected==="all"){

                row.style.display="";

            }

            else if(status===selected){

                row.style.display="";

            }

            else{

                row.style.display="none";

            }

        });

    });

}


// ======================================================
// Dashboard Clock
// ======================================================

function initializeClock(){

    const welcome=document.querySelector(".welcome");

    if(!welcome) return;

    const clock=document.createElement("div");

    clock.id="clock";

    clock.style.fontSize="13px";

    clock.style.marginTop="4px";

    clock.style.opacity="0.9";

    welcome.appendChild(clock);

    updateClock();

    setInterval(updateClock,1000);

}


function updateClock(){

    const clock=document.getElementById("clock");

    if(!clock) return;

    const now=new Date();

    clock.innerHTML=now.toLocaleString();

}


// ======================================================
// Card Animation
// ======================================================

function animateCards(){

    const cards=document.querySelectorAll(".card");

    cards.forEach((card,index)=>{

        card.style.opacity=0;

        card.style.transform="translateY(20px)";

        setTimeout(()=>{

            card.style.transition="0.4s";

            card.style.opacity=1;

            card.style.transform="translateY(0)";

        },100*index);

    });

}


// ======================================================
// Progress Percentage
// ======================================================

function getProgress(){

    const total=document.querySelectorAll("#taskTable tbody tr").length;

    const completed=document.querySelectorAll(
        "#taskTable tbody input[type='checkbox']:checked"
    ).length;

    if(total===0) return 0;

    return Math.round((completed/total)*100);

}


// ======================================================
// Export CSV
// (Ready for future use)
// ======================================================

function exportTableToCSV(filename){

    const rows=document.querySelectorAll("table tr");

    let csv=[];

    rows.forEach(row=>{

        const cols=row.querySelectorAll("th,td");

        const data=[];

        cols.forEach(col=>{

            data.push('"' + col.innerText.replace(/"/g,'""') + '"');

        });

        csv.push(data.join(","));

    });

    const csvFile=new Blob([csv.join("\n")],{type:"text/csv"});

    const downloadLink=document.createElement("a");

    downloadLink.download=filename;

    downloadLink.href=window.URL.createObjectURL(csvFile);

    downloadLink.style.display="none";

    document.body.appendChild(downloadLink);

    downloadLink.click();

    document.body.removeChild(downloadLink);

}