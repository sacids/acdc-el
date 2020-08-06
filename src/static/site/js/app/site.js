

$.fn.exists = function () {
    return this.length !== 0;
}

$(document).ready(function() {
    
    if( $('.les').exists() ){
        var video_src   = $('.les').attr('lesson_src');
        $("#lesson_content_vid source").attr('src', video_src);
        $("#lesson_content_vid").load();

        var topPos     = $("#scrollable").scrollTop();
        var divPos     = $('.les').offset().top - 125;
        $("#scrollable").animate({ scrollTop: divPos+topPos });

        $(".section_item, .lesson_item").removeClass('active_item');
        $('.les').addClass('active_item');
    }
});


$(document).ready(function(){

    $(".section_item").click(function(){

        var lesson_id   = $(this).attr('wrp_id');
        var section_id  = $(this).attr('id');

        $('.section_item_clr .fa').removeClass('fa-angle-up');
        $('.section_item_clr .fa').addClass('fa-angle-down');
        if($('#'+lesson_id).is(":visible")){
            $('#'+lesson_id).slideUp();
        }else{
            $('#'+lesson_id).slideDown();
            $('#'+section_id+' .section_item_clr .fa').addClass('fa-angle-up')
            $('#'+section_id+' .section_item_clr .fa').removeClass('fa-angle-down');
        }
    });

    $(".lesson_item").click(function(){
        var video_src   = $(this).attr('lesson_src');
        $("#lesson_content_vid source").attr('src', video_src);
        $("#lesson_content_vid").load();

        var href = window.location.origin+$('#c_url').val()+'/'+$(this).attr("href");
        //alert(href)
        window.history.pushState({href: href}, '', href);
        //return false; //intercept the link
    });

    window.addEventListener('popstate', function(e){
        if(e.state)
          openURL(e.state.href);
    }); 

    $(".section_item, .lesson_item").click(function(){
        var topPos     = $("#scrollable").scrollTop();
        var divPos     = $(this).offset().top - 125;
        $("#scrollable").animate({ scrollTop: divPos+topPos });

        $(".section_item, .lesson_item").removeClass('active_item');
        $(this).addClass('active_item');
    });

    $(".mcl_category_wrp .list-group-item").click(function(){

        var cat_id      = $(this).attr('cat_id');
        $('.mcl_category_wrp .list-group-item').removeClass('active');
        $(this).addClass('active');
        if(cat_id == 0){
            $(".course_item").show();
        }else{
            $(".course_item").hide();
            $(".course_item[cat="+cat_id+"]").show();
        }
    });


    //onclick resource tab
    $('#resources-tab').on("click",function () {
        var lesson_id = $(this).attr('ls-id');

        //base url
        var base_url=window.location.origin;

        $.ajax({
            url: base_url + "/api/resources/retrieve/el_path/2",
            type: "GET",
            dataType: "json",

            //success
            success: function(data){
                var html = "";

                if (data.status === "success") {
                    var resources = data.resources;

                    html +="<ul>";
                    $.each(resources, function(i, resource){
                        html+="<li>"+
                        "<div class='media v-middle'>" +
                        "<div class='media-body text-body-2'>" +
                        "<h5>" + resource.title + "</h5>" +
                        "<p>Posted on " + resource.created_on + "</p>" +
                        "<p>" + resource.description + "</p>" +
                        "<a href='#' download class='btn btn-primary btn-sm'><i class='fa fa-download'></i> Download</a>" +
                        "</div>" +
                        "</div>" +
                        "</li>";
                    });  
                    html+="</ul>";
                } else {
                    html='<div class="alert alert-danger">No data available</div>';
                }
                $("#results").html(html);
            }
        });
    });

    //post comments
    $(".ac_form").each(function (i){
        $(this).on("submit", function (e){
            e.preventDefault();

            //get data posted
            var csrf_token = $('input[name=csrfmiddlewaretoken]:eq(' + i + ')').val();
            var ann_id     = $('input[name=ann_id]:eq(' + i + ')').val();
            var comments   = $('input[name=comments]:eq(' + i + ')').val();

            //base url
            var base_url = window.location.origin;

            //post to url
            $.ajax({
                url: base_url + "/api/comments/create",
                data: {
                    csrfmiddlewaretoken: csrf_token,
                    description: comments,
                    table_name: "el_announcements",
                    table_id: ann_id
                },
                type: "POST",
                dataType: "json",

                //success
                success: function (data) {
                    if (data.status==="success") {
                        alert("Success insertion");

                        //todo : append new comments
                        
                    }

                    if (data.status==="failed") {
                        $("#failed").html('<div class="alert alert-danger">' + data.message + '</div>');
                    }

                    //clear text fields
                    $('input[name=comments]:eq(' + i + ')').val('');
                }
            });


        })
    });

    //post note
    $('#submit-note').on("click", function(e){
        e.preventDefault();

        //base url
        var base_url=window.location.origin;

        //post data
        var csrf_token = $('input[name=csrfmiddlewaretoken]').val();
        var el_path_id = $('input[name=el_path]').val();
        var note = $.trim($("#note").val());

        //ajax post
        $.ajax({
            url: base_url + "/api/notes/create",
            data: {
                csrfmiddlewaretoken: csrf_token,
                description: note,
                table_name: "el_path",
                table_id: el_path_id
            },
            type: "POST",
            dataType: "json",

            //success
            success: function (data) {
                if (data.status==="success") {
                    alert("Success insertion");

                    //todo : append new note

                }

                if (data.status==="failed") {
                    $("#failed").html('<div class="alert alert-danger">' + data.message + '</div>');
                }

                //clear text fields
                $("#note").val('');
            }
        });

    });
  });