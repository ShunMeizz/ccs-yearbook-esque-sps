$(function () {
  $("#btn-clear-search-user").on("click", () => {
    $("#search-user").val("");
    $("#btn-clear-search-user").hide();
  });

  $("#search-user").on("input", () => {
    if ($("#search-user").val() != "") {
      $("#btn-clear-search-user").show();
    } else {
      $("#btn-clear-search-user").hide();
    }
  });
});
