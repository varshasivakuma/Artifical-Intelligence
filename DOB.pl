dob(aashrit, date(2002, 5, 15)).
dob(bhanu, date(205, 10, 20)).
dob(naveen, date(2004, 2, 8)).
dob(dhanush, date(2000, 7, 3)).
dob(reddy, date(2005, 9, 25)).
dob(sri, date(2002,8,9)).
dob(sonu, date(2003,2,22)).
dob(ali, date(2000,7,2)).
get(Name, DOB) :-
    dob(Name, DOB).



|    dob(sri,X).
X = date(2002, 8, 9).
