$(document).ready(function () {
  $("#submit").click(function () {
    let url = $("#url").val();

    $.get(
      `https://privacypolicysummarizer.brinascode.repl.co/summarizer?url=${url}`,
      function (data) {
        $("#result").html(data);
      }
    );
  });
});
