
function isPointInsideRectangle(x, y, rect) {
  return (
    x >= rect.x &&
    x <= rect.x + rect.width &&
    y >= rect.y &&
    y <= rect.y + rect.height
  );
}

function getPaleo(text) {
  let PATTERN = "abgdefzhjiklmnxopsqrct";
  let word = "";
  for (let char of text) {
    let letternumber = PATTERN.indexOf(char) + 1;
    word += `<span class="icon-${letternumber}"></span>`;
  }
  return word;
}
function getContent(latlng) {
  let paleo = "";
  let trans = "";
  let line = "";
  for (let rectangle of RECTANGLES) {
    if (isPointInsideRectangle(latlng.lng, latlng.lat, rectangle)) {
      paleo = getPaleo(rectangle["paleo"]);
      trans = rectangle["trans"];
      line = rectangle["l"];
      break;
    }
  }
  return `<span style="font-size:25px">${paleo}</span>
  <br>${trans} (Levi:${line}) <br>(${latlng.lng}, ${latlng.lat})`;
}
