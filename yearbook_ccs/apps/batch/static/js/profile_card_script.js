// All functionalities for the profile modal: details and comments
// 1. Populating the profile modal with data
// 2. Array for storing filtered or searched profiles
// 3. Buttons: Syncing the previous and next buttons between the profile modal and comment modal
// 4. Buttons: View Comments and Back to Profile Buttons
// 5. Load comments based on the profile ID

let currentProfileIndex = 0; // Track the current profile index
let profilesData = [];

document.addEventListener("DOMContentLoaded", function () {
	const profileLinks = document.querySelectorAll(".profile-link");

	// Populate the Profile Modal with data
	function populateProfileModal(profile) {
		document.getElementById("profileModalLabel").textContent = profile.name;
		document.getElementById("profileImage").src = profile.image;
		document.getElementById("profileQuote").textContent = profile.quote;
		document.getElementById("profileHobbies").textContent = profile.hobbies;
		const socialLink = document.getElementById("socialLink");
		if (socialLink) {
			if (profile.social) {
				socialLink.href = profile.social;
				socialLink.style.display = "block";
			} else {
				socialLink.style.display = "none";
			}
		}
	}

	// Populate profilesData array use mainly for effective next and previous buttons
	profilesData = Array.from(profileLinks).map((link) => ({
		name: link.getAttribute("data-name"),
		image: link.getAttribute("data-image"),
		quote: link.getAttribute("data-quote"),
		hobbies: link.getAttribute("data-hobbies"),
		social: link.getAttribute("data-social"),
		id: link.getAttribute("data-id"),
	}));

	profileLinks.forEach((link, index) => {
		link.addEventListener("click", function () {
			currentProfileIndex = index;
			updateBothModals();
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
	function loadComments(profile) {
		$(".comment-list").load(`/comments/${profile.id}`, function () {
			$("#commentsModalLabel").text(`Comments for ${profile.name}`);
		});
	}
	//VIEW COMMENT BUTTON
	$("#viewCommentBtn").click(function (event) {
		event.preventDefault();
		$("#profileModal").modal("hide");
		$("#commentsModal").modal("show");
		loadComments(profilesData[currentProfileIndex]);
	});

	// Sync back to Profile Modal when Comment Modal is closed
	$("#commentsModal").on("hidden.bs.modal", function () {
		$("#profileModal").modal("show");
	});

	//BACK TO PROFILE BUTTON
	$("#backToProfileBtn").click(function (event) {
		event.preventDefault();
		$("#commentsModal").modal("hide");
		$("#profileModal").modal("show");
	});
});
