document.addEventListener("DOMContentLoaded", function () {
	const closeButtons = document.querySelectorAll(".close");
	closeButtons.forEach(function (button) {
		button.addEventListener("click", function () {
			this.parentElement.style.display = "none";
		});
	});
	setTimeout(() => {
		alertContainer.style.animation = "fadeOut 0.3s forwards";
		setTimeout(() => {
			alertContainer.remove();
		}, 300);
	}, 3000);
});
