About
*****
The LKV takes generating families for Legendrian knots and plots their embeddings in R^3.
A generating family f_x for a Legendrian knot is a family of functions whose critical values encode a projection of the knot. 
It turns out there's a diffeomorphism between the critical locus of f and the embedding 
        {(x,y,z) | \frac{\partial(f)}{\partial(e)} = y and f(x,e)=z }

Enter the generating family as a polynomial function f(x,E). Where E is an n-dimensional vector space.
To vary a constant and create multiple graphs of the same generating family, use A={a1,a2,...}
values and the provided table entry. 
ex. with one E-dimension, and one a control value. Results in an unknot for a_1 > 0. 
f(x,E) = (a_1-x^2)e_1-e_1^3

Text Entry Rules:
Polynomials must be written using Python math operators. 
Meaning ^ must be replaced with ** for exponentiation (standard +, -, *, /) and careful use of parenthesis 
to preserve order of operations. Especially among dividends and divisors. The sqrt() function is not yet 
supported so use **(1/2) instead.
When typing your generating family, use e1,e2,... for E variables and a1,a2,... for user determined constants. 

Other Notes:
The LKV will attempt to solve and plot anything, even if it's not Legendrian. 
Exponential functions are supported in solving, but trig functions may not have all solutions returned.
Multiple sets of graphs (for multiple a-values) will multiply calculation times.
If a plot has no points or the page never loads, 
check if the critical locus of f is empty or the solution set is infinite


VSCode Startup Instructions for Running on Localhost
****************************************************
Navigate to the FlaskStack folder. Typically "cd ./FlaskStack" from parent "LKV" directory.
python -m flask --version //check version
set FLASK_APP=flaskApp.py
set FLASK_DEBUG=1
python -m flask run

*******if these commands raise errors in the VSCode powershell terminal, 
run them in a cmd prompt terminal instead and double check the filepath '/FlaskStack'*******

Development browser URL: http://127.0.0.1:5000

