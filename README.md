A rudimentary proof checker

Current version runs in default python without any external libraries

Axioms are formatted as follows:
First - the variables separated by spaces
Second - "Assume:" followed by any assumptions, the assumptions are separated by '&'
Third - "Then:" followed by any results, the results are separated by '&'
Axioms must have the ".axiom" file extension in order to be used to prove theorems

Theorems are formatted similarly to axioms at the start then afterwards
"Proof:" followed by the proof
The proof must be formatted as stataements separated by '&'
After the statement and before the '&', In square brackets '[', ']' the axiom or theorem being used to prove it is applied in the following format:
[Result_Name.extension(var1, var2, var3, ...){label1. label2. label3. ...}]

All statements being used in a proof must be labeled. 
Labeling is done as follows:
The label followed by a '.' preceeds the statement to be proven. 