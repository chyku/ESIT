const compareImages = require('resemblejs/compareImages');
const fs = require("fs");


async function getDiff(){
// The parameters can be Node Buffers
// data is the same as usual with an additional getBuffer() function
	const data = await compareImages(
		fs.readFileSync('./pictures/pic2.jpg'),
		fs.readFileSync('./pictures/pic3.jpg')
	);

	fs.writeFileSync('./output.png', data.getBuffer());
	fs.writeFileSync('./output.json', data.getBuffer());

}

getDiff();