// 1번
let user = {
    name: "John",
    surname: "Smith"
};

user.name = "Pete";
delete user.name;


// 2번
function isEmpty(obj) {
    for (let key in obj) {
        return false; 
}
return true;
}


//3번
let sum = 0;
for (let key in salaries) {
    sum += salaries[key];
}

alert(sum);


//4번
function multiplyNumeric(obj) {
    for (let key in obj) {
        if (typeof obj[key] === "number");
        obj[key] *= 2;
    }
}


//5번
function makeUser() {
    return {
        name: "John",
        ref: this
    };
};

let user = makeUser();

alert( user.ref.name ); 


//6번
let calculator = {
    sum() {
        return this.a + this.b;
    },

    mul() {
        return this.a * this.b;
    },

    read() {
        this.a = +prompt('첫 번째 값:', 0);
        this.b = +prompt('두 번째 값:', 0);
    }
};

calculator.read();
alert( calculator.sum() );
alert( calculator.mul() );
