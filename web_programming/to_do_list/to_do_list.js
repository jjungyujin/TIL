// 입력창 핸들러 등록
const inputBoxTag = document.getElementById("inputBox");

function resetInputBox(){
  inputBoxTag.value = "해야 할 일을 입력해 주세요.";
}

function clearInputBox(){
  inputBoxTag.value = null;
}

function enterKey() {
  if (window.event.keyCode == 13) {
    newToDo = document.getElementById("inputBox").value;
    addToDoList(newToDo);
    resetInputBox();
  }
}

function addToDoList(newToDo){
  const toDoListTableTag = document.getElementById("toDoListTable");
  const newRow = toDoListTableTag.insertRow(1)
  const newCell1 = newRow.insertCell(0);
  const newCell2 = newRow.insertCell(1);

  newCell1.innerHTML = '<input type="checkbox" />';
  newCell1.innerHTML += ('<text>' + newToDo + '</text>');
  newCell2.innerHTML = '<input type="button" value="수정"><input type="button" value="저장">'
}

inputBoxTag.addEventListener('click', clearInputBox);
inputBoxTag.addEventListener('keypress', enterKey);
