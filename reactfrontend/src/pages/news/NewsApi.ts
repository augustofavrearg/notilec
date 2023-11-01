import News from "./News";

export async function searchNews(){

    let response = await fetch('http://localhost:8080/api/noticias',{
        "method":'GET',
        "headers":{
            "Content-Type": 'application/json'
        }
    })

    let json = await response.json()
    console.log("Esto es el listado de json: ", json)
    return json;
}

