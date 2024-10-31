const myModal = document.getElementById('myModal')
const myInput = document.getElementById('myInput')

myModal.addEventListener('shown.bs.modal', () => {
  myInput.focus()
})

const editModal = document.getElementById('editpostModal')
const editInput = document.getElementById('editBtn')

editModal.addEventListener('shown.bs.modal', () => {
  editInput.focus()
})

//hldahkl populating the modal
// document.getElementById('editBtn').addEventListener('click', function(event) {
//   var title = event.target.dataset.postTitle;
//   var content = event.target.dataset.postContent;
//   var media = event.target.dataset.postMedia;
  
//   document.getElementById('editTitle').value = title;
//   document.getElementById('editContent').value = content;
//   document.getElementById('editMedia').value = media;
// });
