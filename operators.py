operators:
python operators are spl symbols used to perform operations on variables and values.
they fall into the following main categories:
*arithmetic operations : +,-,*,/,%
*comparison(relational) : =,<=,>=,==,!=
*logical : AND,OR,NOT
*bitwise : &,|,^,~,<<,>> 
*assignment : =,+=,-=,*=,%=
*identity : is , is not
*membership : in, not in

variable: to change values

** ARTHEMETIC OPERATION **
x=20
y=10
print("addition:",x+y)
print("subtraction:", x-y)
print("multiplication:",x*y)
print("division:",x/y)
print("modulus:",x%y)
print("exponentiation:", x**y)
print("floor division:", x//y)

OUTPUT:
addition: 30
subtraction: 10
multiplication: 200
division: 2.0
modulus: 0
exponentiation: 10240000000000
floor division: 2

** COMPARISION **
a=12
b=30
print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
 
OUTPUT:
False
True
False
True
False
True

** LOGICAL **
a=False
b=True
print(a or b)
print(a and b)
print(not a)


OUTPUT:

True
False
True


{ TRUTH TABLE}
// AND operator://
condition A      condition B    result
true                true         true
true                false        false
flase               true         false
false               false        false

// OR //
TRUE               TRUE           TRUE
TRUE               FALSE          TRUE
FLASE              TRUE           TRUE
FALSE              FALSE         FALSE

// NOT//

TRUE-----> FALSE
FALSE----->TRUE


** BITWISE**
