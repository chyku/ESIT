const resemble = require('resemblejs/resemble');
const fs = require('fs');

var avg = 0.0;
var occupancy = 0;
var origin = resemble(fs.readFileSync('./pictures/origin.jpg'));
var pic0 = fs.readFileSync('./pictures/0.jpg');
var pic1 = fs.readFileSync('./pictures/1.jpg');
var pic2 = fs.readFileSync('./pictures/2.jpg');
var pictures = [pic0, pic1, pic2];
var bounds = [{left: 60, top: 250, right: 450, bottom: 720}, {left: 650, top: 250, right: 1030, bottom: 720}, {left: 350, top: 0, right: 560, bottom: 250}, {left: 630, top: 0, right: 830, bottom: 250}];
var areas = [5.03, 4.95, 17.55, 18.43];

for (var i = 0; i < 4; i++){
	resemble.outputSettings({
	  boundingBox: bounds[i],
	  useCrossOrigin: false,
	  outputDiff: true
	});
	
	
	for (var j = 0; j < 3; j++) {
		var mismatch = 0;
		var diff = origin.compareTo(pictures[j]).onComplete(function(data){
			mismatch = data.misMatchPercentage;
		});
		
		console.log(mismatch);
		avg += parseFloat(mismatch);
	}
		
	avg = avg/3 * areas[i]; 
	if (areas[i] > 10){
		if (avg - 30 > 0){ //need better number here
			occupancy += avg/35;
		}
	} else {
		if (avg - 30 > 0){
			occupancy += avg/40;
		}
	}
	avg = 0;
}
if (occupancy > 10} {
	occupancy = 10;
}
console.log(occupancy*10);

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
