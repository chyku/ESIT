const resemble = require('resemblejs/resemble');
const fs = require('fs');

var avg = 0.0;
var occupancy = 0;
var originpic = fs.readFileSync('./pictures/origin.jpg');
var pic0 = fs.readFileSync('./pictures/0.jpg');
var pic1 = fs.readFileSync('./pictures/1.jpg');
var pic2 = fs.readFileSync('./pictures/2.jpg');
var pictures = [pic0, pic1, pic2];
var bounds = [{left: 334, top: 723, right: 799, bottom: 927}, {left: 531, top: 603, right: 860, bottom: 719}, {left: 731, top: 450, right: 1010, bottom: 550}]
var areas = [921600 / (bounds[0].right - bounds[0].left)*(bounds[0].bottom - bounds[0].top), 0, 0, 0];

for (var i = 0; i < 3; i++){
	origin = resemble(originpic);
	
	resemble.outputSettings({
	  boundingBox: bounds[i],
	  useCrossOrigin: false,
	  outputDiff: true
	});
	
	for (var j = 0; j < 3; j++) {
		var diff = origin.compareTo(pictures[j]).onComplete(function(data){
			console.log(data.misMatchPercentage);
			avg += parseFloat(data.misMatchPercentage);
		});
	}
	
	avg = avg/3 * areas; // times proportion of area?
	if (avg > 1){ //need better number here
		occupancy += 25;
	}
	avg = 0;
}

console.log(occupancy);

// if above certain percentage difference, add 25% to image or 1/5 to image
/* var image = data.getImageDataUrl.toString();
    image = image.replace("image/png", "image/octet-stream");
    fs.writeFileSync('./mismatch.png', image);
    
    {
      misMatchPercentage : 100, // %
      isSameDimensions: true, // or false
      dimensionDifference: { width: 0, height: -1 }, // defined if dimensions are not the same
      getImageDataUrl: function(){}
    }
    */
    //fs.writeFileSync('./data.json', JSON.stringify(data, null, 4) , 'utf-8');

/* percentage is fraction of total percentage
 * but percentage difference * proportion of total area
 * equal it out to be compared
 */
