async function SubmitVars() {

    // data sent from the POST request
    var formData = new FormData(document.forms[0])

    // get all form keys and values
    var obj = Object.fromEntries(Array.from(formData.keys())
        .map(key => [key, formData.getAll(key).length > 1 ?
            formData.getAll(key) : formData.get(key)]))

    var jsonreq = (`${JSON.stringify(obj)}`)

    const response = await fetch('http://127.0.0.1:8000/v1/check-ip/', {
    method: "POST",
    body: jsonreq,
    headers: {"Content-type": "application/json; charset=UTF-8"}
  })

  const responseText = await response.text();
  console.log(responseText); // logs 'OK'
  var x = document.getElementById("answer");  
  x.style.color = "red"; 
  x.innerHTML = JSON.stringify(responseText);
  x.title = "FOOBAR";
}