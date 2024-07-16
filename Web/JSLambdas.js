/*  JavaScript Lambdas 
One of the biggest flaws in JS is that it has no implementation of 
namespaces or modules - functions you define may accidentally overwrite 
functions in any library you use. This also makes it easy to accidentally 
declare global vars and introduce bugs.

// \x -> x in JS:
function(x){
  return x;
}
*/

var myAdd = function(a,b){
    c = a + b; // without the var keyword we accidentally create a global var
    return c;
}

var a = 2;
var b = 3;
var c = a + b;

var d = myAdd(10,20); // accesses global c var in myAdd

console.log(c); // c in myAdd: 30, not 5


/* To solve this, use lamda functions. Wrapping code in lambda and immediately
calling, we can keep code safe. This is called an immediately invoked function
expression (IIFE): */
(function(){
 var a = 2;
 var b = 3;
 var c = a + b;
 
var d = myAdd(10,20);
 
 console.log(c); // is now 5
})()

/* Whenever a new func is created, a new scope is created. When a var is used, 
the program looks to the nearest scope; if the var isn't found there, it goes 
to the next level up. This is called lexical scope. */