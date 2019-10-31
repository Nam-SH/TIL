function doSomething(subject) {
  console.log(`이제 ${subject} 과목평가를 준비를 시작해볼까`)
}

// doSomething('django')


doSomething('django', function() { console.log('내일') })

