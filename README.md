# Prime_Sieve
The prime sieve of Eratosthenes

The aim is to find all the prime numbers from 1 up to n.
We start by creating a list of all the numbers.
Then we filter out all the numbers divisible by 2.

From the numbers left some might be prime and some might not be.
We know the first item in our remaining numbers is prime so we add
this to our list of primes.

We then divide our remaining numbers by our second prime (3)
Then we filter out all the numbers divisible by our second prime.
We know the first item in our remaining numbers is prime so we add
this to our list of primes. Now we have 3 primes.

We continue this process.

Each time we do this our remaining number list gets smaller and our prime
number list gets bigger.

We stop once we have no more remaining numbers.
