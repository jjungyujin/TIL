// 체크와 배경색 변경 동시에 하기
// 전체 선택된 상태에서 하나라도 선택 취소하면 topCheckBox 해제하기
$("#topCheckBox").click(function(){
  if ($("#topCheckBox").is(":checked")) $(".listRow input").prop("checked", true);
  else $(".listRow input").prop("checked", false);
  if ($("#topCheckBox").is(":checked")) $(".listRow input").css("background-color", "rgb(237, 235, 233)");
  else $(".listRow input").css("background-color", "rgb(255, 255, 255)");
});

$("#delete").click(function(){
  $(".listRow input").each(function(){
    if ($(this).is(":checked")) $(this).parent().parent().remove()
  })
});

$("#createNew").click(function(){
  newRow = `<div class="listRow">
              <div class="fileCheck"><input class="checkBox" type="checkbox"></div>
              <div class="fileIconBox">
                <svg class="fileIcon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16">
                  <path d="M1 3.5A1.5 1.5 0 0 1 2.5 2h2.764c.958 0 1.76.56 2.311 1.184C7.985 3.648 8.48 4 9 4h4.5A1.5 1.5 0 0 1 15 5.5v7a1.5 1.5 0 0 1-1.5 1.5h-11A1.5 1.5 0 0 1 1 12.5v-9zM2.5 3a.5.5 0 0 0-.5.5V6h12v-.5a.5.5 0 0 0-.5-.5H9c-.964 0-1.71-.629-2.174-1.154C6.374 3.334 5.82 3 5.264 3H2.5zM14 7H2v5.5a.5.5 0 0 0 .5.5h11a.5.5 0 0 0 .5-.5V7z"/>
                </svg>
              </div>
              <div class="fileName">
                <div id="fileNameContainer">
                  <div id="fileNameText"><span>새 폴더</span></div>
                </div>
              </div>
              <div class="fileDate">
                <div class="listText"><span>2022년 1월 24일</span></div>
              </div>
              <div class="fileShare">
                <div class="listText"><span>공개</span></div>
              </div>
              <div class="fileSize">
                <div class="listText"><span>0바이트</span></div>
              </div>
            </div>`;
  $("#mainBoxList").append(newRow);
})

// 새로 추가한 폴더 선택 시 배경색 변경하기
$(".listRow input").click(function(){
  $(this).each(function(){
    if ($(this).is(":checked")) $(this).parent().parent().css("background-color", "rgb(237, 235, 233)");
    else $(this).parent().parent().css("background-color", "rgb(255, 255, 255)");
  })
});
