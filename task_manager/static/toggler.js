function toggleTaskFilteringForm() {
  var taskFilterCard = document.getElementById("task-filter");
  if (taskFilterCard.style.display === "none") {
    taskFilterCard.style.display = "block";
  } else {
    taskFilterCard.style.display = "none";
  }
}
