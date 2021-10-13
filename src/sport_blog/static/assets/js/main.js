//;(function() {
//    $(function() {
//     const $el = $('.author')
//     $el.append("<div><button class='show-authors'> Показать всех АВТОРОВ </button></div>");
//     const $btn = $el.find('.show-authors')
//
//     const authorUrl = "http://127.0.0.1:8000/api/v1/author/?format=json";
//     const author_table = "http://127.0.0.1:8000/authors/all/"
//     const $pageContainer = $(".content");
////     const $pageContainer = $(".author_table");
//     $btn.click(function() {
//        $.get(authorUrl, function(data, status) {
//                $pageContainer.hide("slow");
//                $pageContainer.empty();
//            $.each(data, function(index,value) {
//                $pageContainer.load(authorUrl);
//            $.each(data, function(index,value){
//                    $pageContainer.append(`<p>${index} - ${name} - {email}</p>`);
//                })
//            })
//            $pageContainer.fadeIn(5000);
//
//        })
//     })
//    })
//})()
