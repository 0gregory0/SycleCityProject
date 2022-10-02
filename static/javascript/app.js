// document.getElementsByTagName("rent-action").onclick = function () {
//     alert("Bike booked successfully. Head to your pick up point.");
//   }

  var rentAction = document.querySelectorAll('[name="rentAction"]');
  for (var i = 0; i < rentAction.length; i++) {
    rentAction[i].addEventListener('click', function () {
            alert("Bike booked successfully. Head to your pick up point.");
          });
  }