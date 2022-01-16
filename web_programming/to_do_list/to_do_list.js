// 입력창 핸들러 등록
const inputBoxTag = document.getElementById("inputBox");

function resetInputBox(){
  inputBoxTag.value = "해야할 일을 입력해 주세요.";
}

function clearInputBox(){
  if (inputBoxTag.value == "해야할 일을 입력해 주세요."){
    inputBoxTag.value = null;
  }
}

function enterKey() {
  if (window.event.keyCode == 13) {
    newToDo = document.getElementById("inputBox").value;
    addToDoList(newToDo);
    resetInputBox();
  }
}

function addToDoList(newToDo) {
  const toDoListTableTag = document.getElementById("toDoListTable");
  const newRow = toDoListTableTag.insertRow(1);
  const newCell1 = newRow.insertCell(0);
  const newCell2 = newRow.insertCell(1);

  newCell1.innerHTML = '<input type="checkbox" />';
  newCell1.innerHTML += ('<text>' + newToDo + '</text>');
  newCell2.innerHTML = '<input type="button" value="수정"><input type="button" value="저장">';
}

inputBoxTag.addEventListener('click', clearInputBox);
inputBoxTag.addEventListener('keypress', clearInputBox);
inputBoxTag.addEventListener('keypress', enterKey);

// 버튼 핸들러 등록
const selectAllTag = document.getElementById("selectAll");
const releaseAllTag = document.getElementById("releaseAll");
const deleteSelectionTag = document.getElementById("deleteSelection");

function selectAllCheckBox() {
  const allCheckBox = document.querySelectorAll("input[type=checkbox]");
  allCheckBox.forEach((checkBox)=>{
    checkBox.checked = true;
  })
}

function releaseAllCheckBox() {
  const allCheckBox = document.querySelectorAll("input[type=checkbox]");
  allCheckBox.forEach((checkBox)=>{
    checkBox.checked = false;
  })
}

function deleteSelectedList() {
  const allCheckBox = document.querySelectorAll("input[type=checkbox]");
  allCheckBox.forEach((checkBox)=>{
    if (checkBox.checked == true){
      checkBox.parentElement.parentElement.remove();
    }
  })
}

selectAllTag.addEventListener('click', selectAllCheckBox);
releaseAllTag.addEventListener('click', releaseAllCheckBox);
deleteSelectionTag.addEventListener('click', deleteSelectedList);
