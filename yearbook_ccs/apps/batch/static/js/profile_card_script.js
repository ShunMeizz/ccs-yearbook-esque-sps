//FOR NEXT2X PURPOSES IN PROFILE-CARD-MODAL
let currentProfileIndex = 0; // Track the current profile index
let profilesData = []; // Store profiles data to switch between them

document.addEventListener("DOMContentLoaded", function () {
  const profileLinks = document.querySelectorAll(".profile-link");

  // Populate profilesData array with profile data
  profilesData = Array.from(profileLinks).map((link) => ({
    name: link.getAttribute("data-name"),
    image: link.getAttribute("data-image"),
    quote: link.getAttribute("data-quote"),
    hobbies: link.getAttribute("data-hobbies"),
    social: link.getAttribute("data-social"),
  }));

  profileLinks.forEach((link, index) => {
    link.addEventListener("click", function () {
      populateProfile(profilesData[currentProfileIndex]);
    });
  });

  // Next Profile Button
  document
    .getElementById("nextProfileBtn")
    .addEventListener("click", function () {
      currentProfileIndex = (currentProfileIndex + 1) % profilesData.length;
      populateProfile(profilesData[currentProfileIndex]);
    });

  // Previous Profile Button
  document
    .getElementById("prevProfileBtn")
    .addEventListener("click", function () {
      currentProfileIndex =
        (currentProfileIndex - 1 + profilesData.length) % profilesData.length;
      populateProfile(profilesData[currentProfileIndex]);
    });

  function populateProfile(profile) {
    document.getElementById("profileModalLabel").textContent = profile.name;
    document.getElementById("profileImage").src = profile.image;
    document.getElementById("profileQuote").textContent = profile.quote;
    document.getElementById("profileHobbies").textContent = profile.hobbies;

    const socialLink = document.getElementById("socialLink");
    if (profile.social) {
      socialLink.href = profile.social;
      socialLink.style.display = "block";
    } else {
      socialLink.style.display = "none";
    }
  }
});
