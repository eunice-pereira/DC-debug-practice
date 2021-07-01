function nextFunc() {
	console.log(
		`Hubba, 
        Hubba,
        Hubba,
    `
	);
}

const anotherFunc = function () {
	console.log('I am here.');
};

nextFunc(anotherFunc, 12);
//should say
/*
Hubba,
Hubba,
Hubba
I am here.
*/
