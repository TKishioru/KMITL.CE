// Please see documentation at https://docs.microsoft.com/aspnet/core/client-side/bundling-and-minification
// for details on configuring this project to bundle and minify static web assets.

// Write your JavaScript code.

const arr_result = [];
var num = '0';
var check = false;
var dotn = 0;
function calnum(key) {
    if (num.length > 38) {
        alert("Maximum Value Enter!");
        boolVar = true;
        //document.getElementById("result").innerHTML = 'Enter Number.';
        document.getElementById("result").value = 'Enter Number.';
        num = '0'
        return;
    }

    if (check == false || num == '0') {
        num = key;
        check = true;
    } else {
        if (key == '.' && dotn > 0) {
            alert("Plase, Fill dot once.");
        }
        else if (key == '.' && dotn == 0) {
            dotn++;
            num += '.';
        } else {
            num += key;
        }

    }
    document.getElementById("result").value = num;
}

function calop(key) {
    if (key == '+' || key == '-' || key == '*' || key == '/') {
        n = document.getElementById("result").value;
        if (n != '' || n != '0' || n != 'Enter Number.') {
            arr_result.push(parseFloat(n));
            arr_result.push(key);
            num = '0';
            document.getElementById("result").value = 'Enter Number.';
        }
        else {
            alert("ERROR, Please Enter Number");
        }
        document.getElementById("solve").innerHTML = arr_result;
    } else if (key == '=') {
        if (num == '0') {
            alert("Error input!");
        }
        else {
            var x;
            n = document.getElementById("result").value;
            if (n != '' || n != '0' || n != 'Enter Number.') {
                arr_result.push(parseFloat(n));
            }
            document.getElementById("solve").innerHTML = arr_result;
            arr_result.reverse();
            while (arr_result.length > 1) {
                var temp1 = arr_result.pop();
                var op = arr_result.pop();
                if (op == '+') {
                    var temp2 = arr_result.pop();
                    x = temp1 + temp2;
                    arr_result.push(x);
                } else if (op == '-') {
                    var temp2 = arr_result.pop();
                    x = temp1 - temp2;
                    arr_result.push(x);
                } else if (op == '*') {
                    var temp2 = arr_result.pop();
                    x = temp1 * temp2;
                    arr_result.push(x);
                } else if (op == '/') {
                    var temp2 = arr_result.pop();
                    x = temp1 / temp2;
                    arr_result.push(x);
                }
            }
            num = '0';
            check = false;
            document.getElementById("result").value = arr_result.pop();
        }
        
    } else if (key == 'C') {
        alert("Clear");
        arr_result.length = 0;
        num = '0';
        check = false;
        document.getElementById("solve").innerHTML = 'Solve.';
        document.getElementById("result").value = 'Enter Number.';
    }
}