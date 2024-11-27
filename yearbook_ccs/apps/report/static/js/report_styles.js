$(function () {
  $(".reportBtn").on("click", function (event) {
    var report_item_id = event.target.value;
    var class_list = event.target.classList;
    if (class_list.contains("post_report")) {
      $("#report_type").val(0);
    } else if (class_list.contains("comment_report")) {
      $("#report_type").val(1);
    } else if (class_list.contains("profile_report")) {
      $("#report_type").val(2);
    }

    $("#report_item_id").val(report_item_id);
    $("#reportModal").modal("show");
  });
});
