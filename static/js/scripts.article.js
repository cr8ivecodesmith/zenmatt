$(function() {
    var article = $('#article');
    article.readingTime({
        readingTimeTarget: article.find('.reading-time'),
        wordCountTarget: article.find('.word-count'),
        wordsPerMinute: 127,
    });
});
