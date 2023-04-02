window.addEventListener("load" , function (){





});

const submit = () => {
    const form_elem   = "#form_area";

    const data    = new FormData( (form_elem).get(0) );
    const url     = (form_elem).prop("action");
    const method  = (form_elem).prop("method");

    //送信するデータの確認
    for (let v of data ){ console.log(v); }
    for (let v of data.entries() ){ console.log(v); }

    .ajax({
        url: url,
        type: method,
        data: data,
        processData: false,
        contentType: false,
        dataType: 'json'
    }).done( function(data, status, xhr ) { 

        if (data.error){
            console.log("ERROR");
        }
        else{
            ("#content_area").html(data.content);
            ("#textarea").val("");
        }

    }).fail( function(xhr, status, error) {
        console.log(status + ":" + error );
    }); 
}
