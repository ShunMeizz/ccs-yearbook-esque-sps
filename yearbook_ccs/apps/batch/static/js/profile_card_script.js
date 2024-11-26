// All functionalities for the profile modal: details and comments
// 1. Populating the profile modal with data
// 2. Array for storing filtered or searched profiles
// 3. Buttons: Syncing the previous and next buttons between the profile modal and comment modal
// 4. Buttons: View Comments and View(Back to) Profile Buttons
// 5. Load comments based on the profile ID

let currentProfileIndex = 0; // Track the current profile index
let profilesData = [];

$(function () {
  const profileLinks = document.querySelectorAll(".profile-link");

  // Populate the Profile Modal with data
  function populateProfileModal(profile) {
    $("#profileModalLabel").text(profile.name);
    $("#profileUsername").text(profile.username);
    $("#profileProgram").text(
      profile.program === "BSCS"
        ? "Computer Science"
        : profile.program === "BSIT"
        ? "Information Technology"
        : profile.program
    );
    $("#profileBatchYear").text(profile.batch_year);
    $("#profileImage").attr("src", profile.image);
    $("#profileQuote").text(profile.quote);
    $("#profileHobbies").text(profile.hobbies);
    $("#profile_report").val(profile.id);

    const socialIconsContainer = document.getElementById(
      "socialIconsContainer"
    );
    socialIconsContainer.innerHTML = "";
    const socialContainer = document.getElementById("socialContainer");

    const rawSocialLinks = [
      {
        name: "Facebook",
        url: profile.visible_social_links.facebook,
        icon: "/static/images/facebook_logo.png",
      },
      {
        name: "LinkedIn",
        url: profile.visible_social_links.linkedin,
        icon: "/static/images/linkedin_logo.png",
      },
      {
        name: "GitHub",
        url: profile.visible_social_links.github,
        icon: "/static/images/github_logo.png",
      },
      {
        name: "Instagram",
        url: profile.visible_social_links.instagram,
        icon: "/static/images/instagram_logo.png",
      },
    ];

    // Filter out links with null or undefined URLs
    const socialLinks = rawSocialLinks.filter(
      (link) =>
        link.url && link.url.trim() !== "" && link.url.toLowerCase() !== "null"
    );

    // Create icons dynamically based on link presence
    socialLinks.forEach((link) => {
      const anchor = document.createElement("a");
      anchor.href = link.url;
      anchor.target = "_blank";
      anchor.innerHTML = `<img src="${link.icon}" alt="${link.name}"/>`;
      socialIconsContainer.appendChild(anchor);
    });

    socialContainer.style.display =
      socialIconsContainer.children.length > 0 ? "block" : "none";
  }

  // Populate profilesData array use mainly for effective next and previous buttons
  profilesData = Array.from(profileLinks).map((link) => ({
    id: link.getAttribute("data-id"),
    name: link.getAttribute("data-name"),
    username: link.getAttribute("data-username"),
    program: link.getAttribute("data-program"),
    batch_year: link.getAttribute("data-batch-year"),
    image: link.getAttribute("data-image"),
    quote: link.getAttribute("data-quote"),
    hobbies: link.getAttribute("data-hobbies"),
    visible_social_links: {
      facebook: link.getAttribute("data-facebook"),
      linkedin: link.getAttribute("data-linkedin"),
      github: link.getAttribute("data-github"),
      instagram: link.getAttribute("data-instagram"),
    },
  }));

  profileLinks.forEach((link, index) => {
    link.addEventListener("click", function () {
      currentProfileIndex = index;
      populateProfileModal(profilesData[currentProfileIndex]);
      $("#profileModal").modal("show");
    });
  });

  // next/prev Button for Profile Modal
  document
    .getElementById("nextProfileBtn")
    .addEventListener("click", nextProfile);
  document
    .getElementById("prevProfileBtn")
    .addEventListener("click", prevProfile);

  //next/prev Button for Comment Modal
  $("#nextCommentProfileBtn").click(nextProfile);
  $("#prevCommentProfileBtn").click(prevProfile);

  function nextProfile() {
    currentProfileIndex = (currentProfileIndex + 1) % profilesData.length;
    updateBothModals();
  }

  function prevProfile() {
    currentProfileIndex =
      (currentProfileIndex - 1 + profilesData.length) % profilesData.length;
    updateBothModals();
  }

  // Update both modals (profile and comment) with the current profile's data
  function updateBothModals() {
    const profile = profilesData[currentProfileIndex];
    populateProfileModal(profile);
    if ($("#commentsModal").is(":visible")) {
      loadComments(profile);
    }
  }
  // Load comments based on the profile ID
  async function loadComments(profile) {
    $("#commentsModalLabel").html(`
			<img class="comment-header-pic" src="${profile.image}" alt="${profile.username}'s profile picture" />
			<span class="comment-header-username">${profile.username}</span> 
            <span class="comment-header-name">${profile.name}</span>`);

    console.log(profile.id);
    const csrfToken = $('meta[name="csrf-token"]').attr("content");

    $.ajax({
      url: `/batch_page/profile_comment/${profile.id}/`,
      type: "GET",
      headers: {
        "X-CSRFToken": csrfToken,
      },
      success: function (result) {
        $("#commentsModal .comment-list").html(result);
      },
      dataType: "html",
    });
    // $("#commentsModal .comment-list").html('').load(`{% url 'create_profile_comment.html' %}?profile_id=${profile.id}`)
  }
  //VIEW COMMENT BUTTON
  $("#viewCommentBtn").click(function (event) {
    event.preventDefault();
    switchModals("#profileModal", "#commentsModal");
    loadComments(profilesData[currentProfileIndex]);
  });

  //VIEW PROFILE BUTTON
  $("#viewProfileBtn").click(function (event) {
    event.preventDefault();
    switchModals("#commentsModal", "#profileModal");
  });

  // Sync back to Profile Modal when Comment Modal is closed
  $("#commentsModal").on("hidden.bs.modal", function () {
    switchModals("#commentsModal", "#profileModal");
  });

  function switchModals(hideModal, showModal) {
    const $hide = $(hideModal);
    const $show = $(showModal);

    $hide.removeClass("show").css({ transform: "rotateY(90deg)" });

    setTimeout(function () {
      $hide.modal("hide");
      $show.css({ transform: "rotateY(90deg)" });
      $show.modal("show");
      setTimeout(function () {
        $show.addClass("show").css({ transform: "rotateY(0deg)" });
      });
    }, 200);
  }
  $(".modal").on("hidden.bs.modal", function () {
    $(this).removeClass("show").css({ transform: "", display: "" });
  });
});
