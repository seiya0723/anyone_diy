window.addEventListener("load" , function (){

    // inputタグでEnterによる送信を禁止する。(誤送信防止)
    $(document).on("keypress", "input:not(.allow_submit)", function(event) {
        return event.which !== 13;
    });


    /* project/ */
    $("#add_material_form").on("click", function(){ add_material_form(); });

    /* project_single/ */
    $("#add_favorite").on("click", function(){ add_favorite(this); });
    $("#project_control_delete").on("click", function(){ project_control_delete(this); });
    $(".feedback_delete").on("click", function() { feedback_delete(this); });

    /* community_single */ 
    $("#community_control_closer").on("click",function() { community_control_closer(this); })
    $("#community_control_enter").on("click", function() { community_control_enter(this); })

    /* community_topic */
    $("#community_topic_control_closer").on("click",function() { community_topic_control_closer(this); })
    $(".topic_message_delete").on("click",function() { topic_message_delete(this); })

    //DjangoMessageFrameWorkの削除機能
    $(".notify_message_delete").on("click", function(){ $(this).parent(".notify_message").remove(); }); 
    
    //5秒経ったら自動的に消す
    setTimeout( function(){ $(".notify_message").remove(); }, "5000");



    // 画像のサムネイル表示
    // http://php.o0o0.jp/article/jquery-preview_thumbnail

    // 画像ファイルが指定された時、
    $(".image_input").change(function() {

        const label = $(this).parent("label");
        const file  = $(this).prop("files")[0];

        // 画像以外は処理を停止
        if (! file.type.match("image.*")) {
            $(this).val("");
            return;
        }

        // 画像表示
        const reader    = new FileReader();
        reader.onload   = function() {
            label.children(".image_input_preview").prop("src", reader.result );
        }
        reader.readAsDataURL(file);
    });


});


/* project/ */
// プロジェクト作成時の素材フォームの追加用。
function add_material_form() {
    const html = '<input type="hidden" name="id" value=""><div class="material_form"><input type="text" name="name" placeholder="素材名"><input type="text" name="amount" placeholder="量"></div>';
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


function project_control_delete(elem){

    if(!confirm('本当に削除しますか？')){ 
        return false;
    }

    const url       = $(elem).children("#project_control_delete_url").val();
    const data      = new FormData();
    const method    = "DELETE";

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


function community_topic_control_closer(elem){

    if(!confirm('本当に削除しますか？')){ 
        return false;
    }

    const url       = $(elem).children("#community_topic_control_closer_url").val();
    const data      = new FormData();
    const method    = "DELETE";

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
function topic_message_delete(elem){

    if(!confirm('本当に削除しますか？')){ 
        return false;
    }

    const url       = $(elem).children(".topic_message_delete_url").val();
    const data      = new FormData();
    const method    = "DELETE";

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






function feedback_delete(elem){
    if(!confirm('本当に削除しますか？')){ 
        return false;
    }

    const form_elem =   $(elem).parents("form");

    const data      = new FormData( $(form_elem).get(0) );
    const url       = $(form_elem).prop("action");
    const method    = "DELETE";

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


/* community_single */

function community_control_closer(elem){

    if(!confirm('本当に削除しますか？')){ 
        return false;
    }
    const url       = $(elem).children("#community_control_closer_url").val();
    const data      = new FormData();
    const method    = "DELETE";

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
function community_control_enter(elem){

    const url       = $(elem).children("#community_control_enter_url").val();
    const data      = new FormData();
    const method    = "PATCH";

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


/* community_single */













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
