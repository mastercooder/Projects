console.log("Attached");

let boxes = document.querySelectorAll(".box");
let resetBtn = document.querySelector("#reset_button");
let newBtn = document.querySelector("#new_button");
let msgCont = document.querySelector(".msg_container");
let msgWinner = document.querySelector("#winner");

let turnx = true; // 1st Player Turn

const winPattern = [
  [0, 1, 2],
  [0, 3, 6],
  [0, 4, 8],
  [1, 4, 7],
  [2, 5, 8],
  [2, 4, 6],
  [3, 4, 5],
  [6, 7, 8],
];

const resetGame = () => {
  turnx = true;
  enableBoxes();
  msgCont.classList.add("hide");
};

boxes.forEach((box) => {
  box.addEventListener("click", () => {
    console.log("Box was Clicked!");
    if (turnx) {
      box.innerText = "X";
      box.style.color = '#402E2A';
      turnx = false;
    } else {
      box.innerText = "O";
      box.style.color = '#684551';
      turnx = true;
      turnColor();
    }
    box.disabled = true;
    checkWinner();
  });
});

const disableBoxes = () => {
  for (let box of boxes) {
    box.disabled = true;
  }
};

const enableBoxes = () => {
  for (let box of boxes) {
    box.disabled = false;
    box.innerText = "";
  }
};

const showWinner = (winner) => {
  msgWinner.innerText = `Congrachulations Winner is ${winner}`;
  msgCont.classList.remove("hide");
  disableBoxes();
};

const checkWinner = () => {
  for (pattern of winPattern) {
    let posVal1 = boxes[pattern[0]].innerText;
    let posVal2 = boxes[pattern[1]].innerText;
    let posVal3 = boxes[pattern[2]].innerText;

    if (posVal1 != "" && posVal2 != "" && posVal3 != "") {
      if (posVal1 === posVal2 && posVal2 === posVal3) {
        console.log("Winner", posVal1);
        showWinner(posVal1);
      }
    }
  }
};

newBtn.addEventListener("click", resetGame);
resetBtn.addEventListener("click", resetGame);
