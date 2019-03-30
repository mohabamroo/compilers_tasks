noun(noun(boy)) --> [boy].
noun(noun(girl)) --> [girl].
noun(noun(man)) --> [man].
noun(noun(box)) --> [box].
noun(noun(room)) --> [room].
noun(noun(school)) --> [school].
noun(noun(woman)) --> [woman].
noun(noun(envelope)) --> [envelope].
noun(noun(shed)) --> [shed].
noun(noun(building)) --> [building].
noun(noun(tree)) --> [tree].
noun(noun(students)) --> [students].
noun(noun(professors)) --> [professors].
noun(noun(lecturers)) --> [lecturers].
noun(noun(scientists)) --> [scientists].
noun(noun(researchers)) --> [researchers].
noun(noun(ball)) --> [ball].
noun(noun(page)) --> [page].
noun(noun(line)) --> [line].
noun(noun(hat)) --> [hat].


adjective(adjective(young)) --> [young].
adjective(adjective(old)) --> [old].
adjective(adjective(big)) --> [big].
adjective(adjective(large)) --> [large].
adjective(adjective(empty)) --> [empty].
adjective(adjective(poor)) --> [poor].
adjective(adjective(white)) --> [white].
adjective(adjective(brilliant)) --> [brilliant].
adjective(adjective(many)) --> [many].
adjective(adjective(talented)) --> [talented].
adjective(adjective(bright)) --> [bright].
adjective(adjective(young)) --> [young].
adjective(adjective(tasty)) --> [tasty].
adjective(adjective(dramatic)) --> [dramatic].
adjective(adjective(habitual)) --> [habitual].
adjective(adjective(infamous)) --> [infamous].
adjective(adjective(dangerous)) --> [dangerous].
adjective(adjective(shy)) --> [shy].
adjective(adjective(superb)) --> [superb].
adjective(adjective(cute)) --> [cute].
adjective(adjective(interesting)) --> [interesting].
adjective(adjective(rough)) --> [rough].

adverb(adverb(secretly)) --> [secretly].
adverb(adverb(quickly)) --> [quickly].
adverb(adverb(generally)) --> [generally].
adverb(adverb(speedily)) --> [speedily].
adverb(adverb(knowingly)) --> [knowingly].
adverb(adverb(repeatedly)) --> [repeatedly].
adverb(adverb(helplessly)) --> [helplessly].
adverb(adverb(greatly)) --> [greatly].
adverb(adverb(extremely)) --> [extremely].
adverb(adverb(physically)) --> [physically].
adverb(adverb(completely)) --> [completely].


determiner(determiner(the)) --> [the].
determiner(determiner(a)) --> [a].
determiner(determiner(every)) --> [every].
determiner(determiner(some)) --> [some].

verb(verb(work)) --> [worked].
verb(verb(shoot)) --> [shoots].
verb(verb(push)) --> [pushed].
verb(verb(store)) --> [stored].
verb(verb(give)) --> [gave].
verb(verb(climb)) --> [climbed].
verb(verb(watch)) --> [watched].
verb(verb(admire)) --> [admired].
verb(verb(appreciate)) --> [appreciated].

preposition(preposition(in)) --> [in].
preposition(preposition(for)) --> [for].
preposition(preposition(after)) --> [after].
preposition(preposition(behind)) --> [behind].
preposition(preposition(while)) --> [while].

conj(conj(while)) --> [while].
conj(conj(and)) --> [and].

pronoun(pronoun(who)) --> [who].
% pronoun --> [who].

%s(T, [the, young, boy, who, worked, for, the, old, man, pushed, and, stored, a, big, box, in, the, large, empty, room, after, school],[]).
%s(T, [the, old, woman, and, the, old, man, gave, the, poor, young, man, a, white, envelope, in, the, shed, behind, the, building],[]).
%s(T, [every, boy, quickly, climbed, some, big, tree, while, every, girl, secretly, watched, some, boy],[]).
%s(T, [some, brilliant, students, and, many, professors, watched, and, admired, talented, lecturers, and, appreciated, bright, scientists, and, researchers],[]).

%---------------------------------------------------------------
%sentence
%---------------------------------------------------------------
%base
s(s(X,Y)) --> np(X), vp(Y).
%left rec
s(s(X,Y,Z)) --> s_conj(X), conj(Y), s(Z).
%eliminate left rec
s_conj(s_conj(X,Y)) --> np(X), vp(Y).
%---------------------------------------------------------------
%nounphrase
%---------------------------------------------------------------
%base
np(np(X)) --> noun(X).
np(np(X,Y)) --> determiner(X), noun(Y).
np(np(X,Y,Z)) --> determiner(X), adjective_h(Y), noun(Z).
np(np(X,Y)) --> adjective_h(X), np(Y).
%left rec
np(np(X,Y,Z)) --> np_dash(X), pronoun(Y), vp(Z).
np(np(X,Y,Z)) --> np_dash(X), conj(Y), np(Z).
%eliminate left rec
np_dash(np_dash(X)) --> noun(X).
np_dash(np_dash(X,Y)) --> determiner(X), noun(Y).
np_dash(np_dash(X,Y,Z)) --> determiner(X), adjective_h(Y), noun(Z).
np_dash(np_dash(X,Y)) --> adjective_h(X), np(Y).
%---------------------------------------------------------------
%verbphrase
%---------------------------------------------------------------
%base
vp(vp(X)) --> verb(X).
vp(vp(X,Y)) --> verb(X), pp(Y).
vp(vp(X,Y)) --> verb(X), np(Y).
vp(vp(X,Y,Z)) --> verb(X), np(Y), np(Z).
vp(vp(X,Y,Z)) --> verb(X), np(Y), pp(Z).
vp(vp(W,X,Y,Z)) --> verb(W), np(X), np(Y), pp(Z).
vp(vp(X,Y)) --> adverb(X), vp(Y).
%left rec
vp(vp(X,Y,Z)) --> vp_dash(X), conj(Y), vp(Z).
%eliminate left rec
vp_dash(vp_dash(X)) --> verb(X).
vp_dash(vp_dash(X,Y)) --> verb(X), pp(Y).
vp_dash(vp_dash(X,Y)) --> verb(X), np(Y).
vp_dash(vp_dash(X,Y,Z)) --> verb(X), np(Y), np(Z).
vp_dash(vp_dash(X,Y,Z)) --> verb(X), np(Y), pp(Z).
vp_dash(vp_dash(W,X,Y,Z)) --> verb(W), np(X), np(Y), pp(Z).
vp_dash(vp_dash(X,Y)) --> adverb(X), vp_dash(Y).
%---------------------------------------------------------------
%prepositionphrase
%---------------------------------------------------------------
pp(pp(X,Y)) --> preposition(X), np(Y).
pp(pp(X,Y,Z)) --> preposition(X), np(Y), pp(Z).
%---------------------------------------------------------------
%adjective
%---------------------------------------------------------------
adjective_h(adjective_h(X)) --> adjective(X).
adjective_h(adjective_h(X,Y)) --> adjective(X), adjective_h(Y).