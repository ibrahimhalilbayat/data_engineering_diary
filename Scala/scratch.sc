// This is a comment
// Values are immutable constants
val hello: String = "Hola!"

// Variables are mutable

var helloThere: String = hello

helloThere = hello + " There!"

println(helloThere)

val immutableHelloBro = hello + " BRO!"
println(immutableHelloBro)

// Data Types
val numberOne: Int = 1
val truth: Boolean = true
val letterA: Char = 'a'
val pi: Double = 3.14
val piSinglePrecision: Float = 3.14159265f
val bigNumber: Long = 123456789
val smallNumber: Byte = 127

println("Here is a mess: " +  numberOne + truth + letterA + pi + bigNumber + piSinglePrecision)

println(f"The value of pi is: $piSinglePrecision%.4f")

println(f"Zero padding on the left: $numberOne%05d")

println(s"Sum of 1 and 2 are ${1+2}")

val theUltimateAnswer: String = "In common tongue it says 1 ring to rule them all one ring to find them"
val pattern = """.* ([\d]+).*""".r
val pattern(answerString) = theUltimateAnswer
val answer = answerString.toInt
println(answer)

val isGreater = 1 > 2
val isLesser = 1 < 2
val impossible = isGreater & isLesser
val anotherWay = isGreater || isLesser

