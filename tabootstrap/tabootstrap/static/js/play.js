
$(document).ready(function(){

    $("#getNewSet").click(function(){
        getNewSet(["fe","twitter"]);
    })

    function getNewSet(prev_words){
        prev_words = String(prev_words)
        var data = {};
        data['prev_words'] = prev_words;
        var new_word;
        var new_banned_words;
        $.ajax({
                   type: "GET",
                   url: "./",
                   data: data,
                   success: function(word){
                       alert("BRO")
                       alert(word);
                   }
               })
    }

})