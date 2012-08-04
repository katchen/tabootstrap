var return_dict = {}

$(document).ready(function(){
    var prev_words = [];
    $("#getNewSet").click(function(){
        getNewSet();
    })

    function getNewSet(){
        prev_words_string = String(prev_words)
        var data = {};
        data['prev_words'] = prev_words_string;
        $.ajax({
           type: "GET",
           url: "./",
           data: data,
           success: function(data){
                data_dict = eval("("+data+")")
                used_all = data_dict['used_all']
                new_word = data_dict['taboo_word']
                new_banned_words = data_dict['banned_words']
                if (used_all) {
                    prev_words.length = 0
                }
                prev_words.push(new_word)
                setDict(new_word,new_banned_words);

               // START DOING STUFF WITH DATA HERE
               // new_word is a string of the new taboo word
               // new_banned_word is an array of strings, which are the words not allowed to be used


           }
        })
    }

    function setDict(new_word,new_banned_words) {
        return_dict['taboo_word'] = new_word;
        return_dict['new_banned_words'] = new_banned_words;
        alert(return_dict['taboo_word'])
    }

})