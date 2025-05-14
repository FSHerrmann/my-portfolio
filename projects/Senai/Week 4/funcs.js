  // Count how many prime numbers exist from 2 up to the given number
  function countPrimes(num) {
    let primeNumbers = [];
    let primeCount = 0;

    for (let x = num; x >= 2; x--) {
      let isPrime = true;

      for (let y = 2; y < x; y++) {
        if (x % y === 0) {
          isPrime = false;
          break;
        }
      }

      if (isPrime) {
        primeNumbers.push(x);
        primeCount++;
      }
    }

    return { primeNumbers, primeCount };
  }

  // Count even numbers from 1 to the given number
  function countEven(num) {
    let evenCount = 0;
    while (num >= 1) {
      if (num % 2 === 0) {
        evenCount++;
      }
      num--;
    }
    return { evenCount };
  }

  // Count odd numbers from 1 to the given number
  function countOdd(num) {
    let oddCount = 0;
    while (num >= 1) {
      if (num % 2 !== 0) {
        oddCount++;
      }
      num--;
    }
    return { oddCount };
  }

  // Arrow functions for basic arithmetic operations
  const add = (a, b) => a + b;
  const subtract = (a, b) => a - b;

  // Handle button clicks once the page loads
  window.onload = function () {
    const inputNum1 = document.getElementById("inputNum1");
    const inputNum2 = document.getElementById("inputNum2");
    const resultDisplay = document.getElementById("result");

    document.getElementById("btnAdd").addEventListener("click", function () {
      const a = parseFloat(inputNum1.value);
      const b = parseFloat(inputNum2.value);
      const result = add(a, b);
      resultDisplay.textContent = `Result: ${result}`;
    });

    document.getElementById("btnSubtract").addEventListener("click", function () {
      const a = parseFloat(inputNum1.value);
      const b = parseFloat(inputNum2.value);
      const result = subtract(a, b);
      resultDisplay.textContent = `Result: ${result}`;
    });

    document.getElementById("btnEven").addEventListener("click", function () {
      const num = parseInt(inputNum1.value);
      const result = countEven(num);
      resultDisplay.textContent = `Even numbers count: ${result.evenCount}`;
    });

    document.getElementById("btnOdd").addEventListener("click", function () {
      const num = parseInt(inputNum1.value);
      const result = countOdd(num);
      resultDisplay.textContent = `Odd numbers count: ${result.oddCount}`;
    });

    document.getElementById("btnPrime").addEventListener("click", function () {
      const num = parseInt(inputNum1.value);
      const result = countPrimes(num);
      resultDisplay.textContent = `Prime numbers count: ${result.primeCount}`;
    });
  };
