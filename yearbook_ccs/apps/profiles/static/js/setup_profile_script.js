$(function () {
  // $("#modal-add-socials").modal("show")
  $("#btn-add-social-links").on("click", () => {
    $("#modal-add-socials").modal("show");
  });

  $("#id_profile_pic").on("change", (event) => {
    $("#profile_pic_container").attr(
      "src",
      URL.createObjectURL(event.target.files[0])
    );
  });

  function validateURL(url, platform) {
    const regexes = {
      facebook: /^https?:\/\/(www\.)?facebook\.com/,
      linkedin: /^https:\/\/(www\.)?linkedin\.com\/in\//,
      github: /^https?:\/\/(www\.)?github\.com/,
      instagram: /^https?:\/\/(www\.)?instagram\.com/,
    };
    return regexes[platform].test(url);
  }

  $("#id_facebook_link").on("input", () => {
    const value = $("#id_facebook_link").val();
    console.log(value);
    if (!validateURL(value, "facebook") && value != "") {
      console.log("error");
      $("#facebook-error-message").text("Please enter a valid Facebook URL.");
    } else {
      $("#facebook-error-message").text("");
      console.log("check");
    }
  });

  $("#id_linkedin_link").on("input", () => {
    const value = $("#id_linkedin_link").val();
    if (!validateURL(value, "linkedin") && value != "") {
      $("#linkedin-error-message").text("Please enter a valid LinkedIn URL.");
    } else {
      $("#linkedin-error-message").text("");
    }
  });

  $("#id_github_link").on("input", () => {
    const value = $("#id_github_link").val();
    if (!validateURL(value, "github") && value != "") {
      $("#github-error-message").text("Please enter a valid GitHub URL.");
    } else {
      $("#github-error-message").text("");
    }
  });

  $("#id_instagram_link").on("input", () => {
    const value = $("#id_instagram_link").val();
    if (!validateURL(value, "instagram") && value != "") {
      $("#instagram-error-message").text("Please enter a valid Instagram URL.");
    } else {
      $("#instagram-error-message").text("");
    }
  });
});
