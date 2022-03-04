'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'timeConversion' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

function timeConversion(s) {
    var hours = parseInt(s.substring(0, 2), 10)
    var minutes = parseInt(s.substring(3,5), 10)
    var seconds = parseInt(s.substring(6,8), 10)
    var amOrPm = s.substring(s.length-2, s.length)
    
    if (amOrPm.toUpperCase() === "AM") {
        if (hours === 12) {
            hours -= 12
        }
    }

    if (amOrPm.toUpperCase() === "PM") {
        if (hours !== 12) {
            hours += 12
        }
    }

    var sHours = hours
    if (hours < 10) {
        sHours = '0' + sHours
    }
    var sMinutes = minutes
    if (minutes < 10) {
        sMinutes = '0' + sMinutes
    }
    var sSeconds = seconds
    if (seconds < 10) {
        sSeconds = '0' + sSeconds
    }

    return `${sHours}:${sMinutes}:${sSeconds}`
}

function main() {
    const s = readLine();
    const result = timeConversion(s);
    console.log(result)
}
