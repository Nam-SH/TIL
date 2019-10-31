const nothing = () => {
  console.log('sleeeeeeping~~~')
}

console.log('start')
setTimeout(nothing, 3000)
console.log('end')

console.log('-----------------------------------')

function sleep_3s() {
  setTimeout(() => console.log('wake up'), 3000)
}

console.log('start2')
sleep_3s()
console.log('end2')

console.log('-----------------------------------')

function first() {
  console.log('first')
}

function second() {
  console.log('second')
}

function third() {
  console.log('third')
}

first()
setTimeout(second, 1000)
third()


console.log('-----------------------------------')


function printHello() {
  console.log('hello from baz')
}

function baz() {
  setTimeout(printHello, 3000)
}

function bar() {
  baz()
}

function foo() {
  bar()
}

foo()