window.addEventListener("load" , function (){

    /* project/ */
    $("#add_material_form").on("click", function(){ add_material_form(); });

    /* project_single/ */
    $("#add_favorite").on("click", function(){ add_favorite(this); });


});


/* project/ */
// プロジェクト作成時の素材フォームの追加用。
function add_material_form() {
    const html = '<div class="material_form"><input type="text" name="name" placeholder="素材名"><input type="text" name="amount" placeholder="量"></div>';
    $("#material_form_area").append(html);
}


/* project_single/ */
function add_favorite(elem) {
    
    const form_elem =   $(elem).parents("form");

    const data      = new FormData( $(form_elem).get(0) );
    const url       = $(form_elem).prop("action");
    const method    = $(form_elem).prop("method");

    for (let v of data ){ console.log(v); }
    for (let v of data.entries() ){ console.log(v); }


    $.ajax({
        url: url,
        type: method,
        data: data,
        processData: false,
        contentType: false,
        dataType: 'json'
    }).done( function(data, status, xhr ) { 

        location.reload();

    }).fail( function(xhr, status, error) {
        console.log(status + ":" + error );
    }); 

}



/* project_single/ */
















/*
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
*/
