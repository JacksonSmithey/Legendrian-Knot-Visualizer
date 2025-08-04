About
*****
The LPG takes generating families for Legendrian knots and plots their embeddings in \(R^3\).
A generating family is a polynomial that generates a positive dimensional system of equations
whose critical locus generates an embedding of S^1 in R^3.

Enter the generating family as a polynomial function f(x,E). Where E is an n-dimensional vector space.
To vary a constant and create multiple graphs of the same generating family, use A={a1,a2,...}
values and the provided table entry. 
ex. with one E-dimension, and one a control value. Results in an unknot for a_1 > 0. 
f(x,E) = (a_1-x^2)e_1-e_1^3

Text Entry Rules:
Polynomials must be parsable by Python math libraries. Meaning explicit * for multiplication, 
** for exponentiation, and careful parenthesis to preserve order of operations (especially with division).
When typing your generating family, use e1,e2,... for E variables and a1,a2,... for user determined constants. 

Other Notes:
The LPG will attempt to solve and plot anything, even if it's not Legendrian. 
Exponential functions are supported in solving, but trig functions may not have all solutions returned.
Multiple sets of graphs (for multiple a-values) will multiply calculation times.
If a plot has no points or the page never loads, 
check if the critical locus of f is empty or the solution set is infinite


VSCode Startup Instructions
***************************
Navigate to the FlaskStack folder. Typically "cd ./FlaskStack" from parent "LPV" directory.
python -m flask --version //check version
set FLASK_APP=flaskApp.py
set FLASK_DEBUG=1
python -m flask run
*******if these commands raise errors in the local VSCode powershell terminal, 
run them in a cmd prompt instead and double check the filepath '/FlaskStack'*******

Development browser URL: http://127.0.0.1:5000

