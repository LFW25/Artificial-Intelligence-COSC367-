/* First create a new knowledge base 
Now add a new predicate of the form diagnosis(Recommend, Age, Astigmatic, Tear_Rate) to the knowledge base where the arguments are:

Recommend is either hard_lenses, soft_lenses, or no_lenses;
Age will be an integer;
Astigmatic will be either yes or no (note that these are atoms 'yes' and 'no' not true or false.); and
Tear_Rate will be a positive integer.
The predicate must be the translation of the following natural-language rules to logic:

If the patient is young and has a normal tear rate then the type of lenses will depend on astigmatism. If the patient is astigmatic then hard lenses must be recommended, otherwise soft lenses.
If the person has a low tear rate then 'no lenses' must be recommended.

*/



/* tear rate related clauses */
normal_tear_rate(RATE) :- RATE >= 5.
low_tear_rate(RATE) :- RATE < 5.

/* age-related clauses */
young(AGE) :- AGE < 45.

diagnosis(Recommend, Age, Astigmatic, Tear_Rate) :- low_tear_rate(Tear_Rate), Recommend = no_lenses.
diagnosis(Recommend, Age, Astigmatic, Tear_Rate) :- Recommend = hard_lenses, young(Age), Astigmatic = yes, normal_tear_rate(Tear_Rate).
diagnosis(Recommend, Age, Astigmatic, Tear_Rate) :- Recommend = soft_lenses, young(Age), Astigmatic = no, normal_tear_rate(Tear_Rate).


/* Recommend is either hard_lenses, soft_lenses, or no_lenses;
Age will be an integer;
Astigmatic will be either yes or no (note that these are atoms 'yes' and 'no' not true or false.); and
Tear_Rate will be a positive integer.
*/