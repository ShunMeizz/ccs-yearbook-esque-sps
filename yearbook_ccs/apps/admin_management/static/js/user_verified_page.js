$(function () {
  $("#btn-clear-serarch-user").hide();
  $("#btn-clear-search-user").on("click", () => {
    $("#search-user").val("");
    $("#btn-clear-search-user").hide();
  });
});
