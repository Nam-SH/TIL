const numberAddEach = number => {
  let sum = 0
  for (const number of numbers) {
    sum += number
  }
  return sum
}

const numberSubEach = number => {
  let sum = 0
  for (const number of numbers) {
    sum -= number
  }
  return sum
}

const numberMulEach = number => {
  let mul = 1
  for (const number of numbers) {
    mul *= number
  }
  return mul
}

console.log('---------------------------------------------------------')

const numbersEach = (numbers, callback) => {
  let acc
  for (const number of numbers) {
    acc = callback(number, acc)
  }
  return acc
}

const addEach = (number, acc = 0) => { return acc + number }
const subEach = (number, acc = 0) => { return acc - number }
const mulEach = (number, acc = 1) => { return acc * number }

const numbers2 = [1, 2, 3, 4, 5,]
console.log()

console.log(numbersEach(numbers2, addEach))
console.log(numbersEach(numbers2, subEach))
console.log(numbersEach(numbers2, mulEach))

console.log('---------------------------------------------------------')

console.log(numbersEach(numbers2, (number, acc = 0) => acc + number))
console.log(numbersEach(numbers2, (number, acc = 0) => acc - number))
console.log(numbersEach(numbers2, (number, acc = 1) => acc * number))

