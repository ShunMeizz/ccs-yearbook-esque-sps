$(function () {
  // Event listener for profile card click
  $(".profile-card").on("click", function () {
    const profilePic = $(this).data("profile-pic");
    const firstName = $(this).data("first-name");
    const lastName = $(this).data("last-name");
    const batchYear = $(this).data("batch-year");

    // Set modal content
    $("#modal-profile-pic").attr("src", profilePic);
    $("#modal-full-name").text(`${firstName} ${lastName}`);
    $("#modal-batch-year").text(batchYear);
  });
});
