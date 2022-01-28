// 입력창 핸들러 등록
const inputBoxTag = document.getElementById("inputBox");

function enterKey() {
  if (window.event.keyCode == 13) {
    newToDoText = document.getElementById("inputBox").value;
    addToDoList(newToDoText);
    resetInputBox();
  }
}

function resetInputBox(){
  inputBoxTag.value = null;
}

function addToDoList(newToDoText) {
  const toDoListTableTag = document.getElementById("toDoListTable");
  let newRow = toDoListTableTag.insertRow(1);
  let newCell1 = newRow.insertCell(0);

  newCell1.innerHTML = '<input type="checkbox" />';
  newCell1.innerHTML += ('<input type="text" class="toDo" value="' + newToDoText + '" readOnly="true"  />');
  newCell1.innerHTML += '<input type="button" class="edit" onclick="editToDo(this)" value="수정">';
  newCell1.innerHTML += '<input type="button" class="save" onclick="saveToDo(this)" value="저장">';
}

inputBoxTag.addEventListener('keypress', enterKey);

// 하단 버튼 핸들러 등록
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
      // <tr> - <td> - <input type="checkbox">
      checkBox.parentNode.parentNode.remove();
    }
  })
}

// 각 행의 수정, 삭제 핸들러 등록
function editToDo(editBox){
  toDoText = editBox.previousElementSibling;
  toDoText.readOnly = false;
}

function saveToDo(saveBox){
  toDoText = saveBox.previousElementSibling.previousElementSibling;
  toDoText.readOnly = true;
}
