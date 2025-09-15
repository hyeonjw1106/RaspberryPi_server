var n = 0;
var num = document.querySelector("#num");
var increase = document.querySelector("#plus");
var submit = document.querySelector("#go");

increase.addEventListener("click", function() {
    n+=1;
    num.innerHTML = n;
})
submit.addEventListener("click", async () => {
    let res = await fetch("/submit", {
        method:"POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({value: n})
    });
    n=0;
    num.innerHTML = n;
})