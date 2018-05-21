var num = 0;
var date_1 = new Date().getTime();

for (var i = -999999999; i < 999999999; i++) {
    num++
}
console.log(num, new Date().getTime() - date_1);

// var index = 0;
// while (index < 999999999 * 2) {
//     index++;
// }
// console.log(num, new Date().getTime() - date_1);