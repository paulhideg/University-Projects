let size = 4;
let numberOfTiles = size ** 2;
let highlighted = numberOfTiles;
let shuffled = false;

let buttonContainer = document.getElementById('tiles');

newGame();

function newGame() {
    loadTiles();
    shuffle();
}

// Create buttons
function loadTiles() {
    for (let b = 1; b <= numberOfTiles; b++) {
        var newTile = document.createElement('button');
        newTile.id = `btn${b}`;
        newTile.setAttribute('index', b);
        // for numbers version
        // newTile.innerHTML = b
        // for images version
        imagelink = ''
        if (b < 10) {
            imagelink = '<img src="0' +  b.toString() + '.png" style="width:70px; height:70px;">'
        }
        else {
            imagelink = '<img src="' +  b.toString() + '.png" style="width:70px; height:70px;">'
        }
        newTile.innerHTML = imagelink
        if (b == 16) {
            newTile.innerHTML = '<img src="16.png" style="display:none; width:70px; height:70px;">';
        }
        // end of images version
        newTile.classList.add('btn');
        newTile.addEventListener('click', function () {
            swap(parseInt(this.getAttribute('index')));
        });
        
        buttonContainer.append(newTile);
    }
    selectedTileId = 'btn' + highlighted;
    selectedTile = document.getElementById(selectedTileId);
    selectedTile.classList.add("selected");
}

function shuffle() {
    let minShuffles = 2;
    let totalShuffles = minShuffles + Math.floor(Math.random() * (200 - 100) + 100);

    for (let i = minShuffles; i <= totalShuffles; i++) {
        setTimeout(function timer() {
            let x = Math.floor(Math.random() * 4);
            let direction = 0;
            if (x == 0) {
                direction = highlighted + 1;
            } else if (x == 1) {
                direction = highlighted - 1;
            } else if (x == 2) {
                direction = highlighted + size;
            } else if (x == 3) {
                direction = highlighted - size;
            }
            swap(direction);
            if (i >= totalShuffles - 1) {
                shuffled = true;
            }
        }, i * 10);
    }
}

// Swap tiles 
function swap(clicked) {
    if (clicked < 1 || clicked > (numberOfTiles)) {
        return;
    }

    // Check if we are trying to swap right
    if (clicked == highlighted + 1) {
        if (clicked % size != 1) {
            setSelected(clicked);
        }
        // Check if we are trying to swap left
    } else if (clicked == highlighted - 1) {
        if (clicked % size != 0) {
            setSelected(clicked);
        }
        // Check if we are trying to swap up
    } else if (clicked == highlighted + size) {
        setSelected(clicked);
        // Check if we are trying to swap down 
    } else if (clicked == highlighted - size) {
        setSelected(clicked);
    }

    if (shuffled) {
        if (checkHasWon()) {
            alert("Winner!")
        }
    }
}

function checkHasWon() {
    for (let b = 1; b <= numberOfTiles; b++) {
        currentTile = document.getElementById(`btn${b}`);
        currentTileIndex = currentTile.getAttribute('index');
        // for numbers version
        // currentTileValue = currentTile.innerHTML;
        // for images version
        currentTileValue = currentTileValue.substring(10, 12);
        if (parseInt(currentTileIndex) != parseInt(currentTileValue)) {
            return false;
        }
    }
    return true;
}

// Applies stylings to the selected tile
function setSelected(index) {
    currentTile = document.getElementById(`btn${highlighted}`);
    currentTileText = currentTile.innerHTML;
    currentTile.classList.remove('selected');
    newTile = document.getElementById(`btn${index}`);
    currentTile.innerHTML = newTile.innerHTML;
    newTile.innerHTML = currentTileText;
    newTile.classList.add("selected");
    highlighted = index;
}