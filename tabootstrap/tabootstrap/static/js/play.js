
$(document).ready(function(){
    prev_words = [];
    $("#getNewSet").click(function(){
        getNewSet(prev_words);
    })

    function getNewSet(prev_words){
        prev_words_string = String(prev_words)
        var data = {};
        data['prev_words'] = prev_words_string;
        var new_word;
        var new_banned_words;
        $.ajax({
           type: "GET",
           url: "./",
           data: data,
           success: function(data){
               data_dict = eval("("+data+")")
               new_word = data_dict['taboo_word']
               new_banned_words = data_dict['banned_words']
               used_all = data_dict['used_all']
               if (used_all) {
                   prev_words.length = 0
               }
               prev_words.push(new_word)
               
               alert(prev_words)
               alert(new_word+": "+new_banned_words)
           }
        })
    }

})