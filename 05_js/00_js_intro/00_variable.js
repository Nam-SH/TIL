let x = 1

if (x === 1) {
  let x = 2

  console.log(x)
}

console.log(x)


const MY_FAV = 7

console.log('my favorite number is: ' + MY_FAV)


if (MY_FAV === 7) {
  let MY_FAV = 20

  console.log('my facorite number is: ' + MY_FAV)
}

console.log('my facorite number is: ' + MY_FAV)

function varTest() {
  var x = 1
  if (true) {
    var x = 2
    console.log(x)
  }
  console.log(x)
}


varTest()

function letTest() {
  let x = 1
  if (true) {
    let x = 2
    console.log(x)
  }
  console.log(x)
}

letTest()


console.log()
console.log()

var a = 1
let b = 2
const c = 3

if (a === 1) {
  var a = 11
  let b = 22
  const c = 33

  console.log(a)
  console.log(b)
  console.log(c)
}
console.log()
console.log(a)
console.log(b)
console.log(c)

const dog = []

const rDecs = /.*/


class User {
  constructor(options) {
    this.name = option.name
  }
}

