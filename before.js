
function messyFunction() {
    console.log('This is a very long line that exceeds the 120 character limit and should be refactored to be more readable and maintainable.');
    const x = 1;
    const y = 2;
    const z = x + y;
    console.log(z);
    return z;
}

messyFunction();
