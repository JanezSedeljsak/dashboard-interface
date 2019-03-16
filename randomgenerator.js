const fs = require('fs');

// interface testing 
// javascript that generates random values to immitate arduino (backside)
function generator(){
    let fileContent = "";
    fileContent += `vlaga:${Math.floor(Math.random() * 180) + 1} `;
    fileContent += `temp:${Math.floor(Math.random() * 180) + 1} `;
    fileContent += `svetlost:${Math.floor(Math.random() * 180) + 1}`;
    setTimeout(() => {
        fs.writeFile("./values.txt", fileContent); 
        generator();
    }, 4000)
}(generator)()
