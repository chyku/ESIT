const resemble = require('resemblejs/resemble');
const fs = require('fs');

var avg = 0.0;
var occupancy = 0;
var pictures = [pic0, pic1, pic2];
var bounds = [{left: 350, top: 00, right: 530, bottom: 280}, {left: 531, top: 603, right: 860, bottom: 719}, {left: 731, top: 450, right: 1010, bottom: 550}]
var areas = [921600 / (bounds[0].right - bounds[0].left)*(bounds[0].bottom - bounds[0].top), 0, 0, 0];

resemble.outputSettings({
	  boundingBox: bounds[1],
	  useCrossOrigin: false,
	  outputDiff: true
});

var diff = resemble(fs.readFileSync('.first.jpg')).compareTo(fs.readFileSync('.second.jpg')).onComplete(function(data){
	console.log(data.misMatchPercentage);
});
