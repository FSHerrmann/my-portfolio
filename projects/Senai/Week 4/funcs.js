function primeNums(n){
    let primenumsum = 0
    while (n >= 0){
    if(n%2 === 0){
        primenumsum +=1
        n--
    } else {
        n--
    }
    }
    console.log(primenumsum)
    }

primeNums(10);
