// The default constructor obtains or returns the current date according your system
var date = new Date();
console.log("Current date: " + date);
// When we use a value(in ms) then this value will add to the default date 1 Juanuary 1970 UTC
var dateVal = new Date(1000);
console.log("Date with a value of 1000ms: " + dateVal);
// Also we can use a string as the parameter, but this must be in a format recognized by 
// Date.parse() function such as MM/DD/YYYY, Month Day, Year, etc
var string = "12/17/2000";
var dateString = new Date(string);
console.log("Date with a string \""+string+"\": "+dateString);
string = "December 17";
var dateString1 = new Date(string);
console.log("Date with a string \""+string+"\":"+dateString1);