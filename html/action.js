async function SubmitVars() {


    var formData = new FormData(document.forms[0])
    // get all form keys and values
    var obj = Object.fromEntries(Array.from(formData.keys())
        .map(key => [key, formData.getAll(key).length > 1 ? 
        formData.getAll(key) : formData.get(key)]))

    var jsonreq  = (`${JSON.stringify(obj)}`)

    const options = {
        method: 'POST',
        body:  jsonreq,
        headers: {"Content-type": "application/json; charset=UTF-8"}
    };

    const result = await fetch('http://127.0.0.1:8000/v1/check-ip/', options )
        .then( response => response.json())
        .then( response => {
        console.log (response);
        let results = response;
        document.write(results.result)
    } );
    
    //document.write("demo").innerHTML = result;
    
  

}