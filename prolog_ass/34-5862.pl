noun(noun(boy)) --> [boy].
noun(noun(man)) --> [man].
noun(noun(box)) --> [box].
noun(noun(room)) --> [room].
noun(noun(school)) --> [school].
noun(noun(woman)) --> [woman].
noun(noun(shed)) --> [shed].
noun(noun(envelope)) --> [envelope].
noun(noun(building)) --> [building].
noun(noun(tree)) --> [tree].
noun(noun(girl)) --> [girl].
noun(noun(students)) --> [students].
noun(noun(professors)) --> [professors].
noun(noun(lecturers)) --> [lecturers].
noun(noun(scientists)) --> [scientists].
noun(noun(researchers)) --> [researchers].
noun(noun(car)) --> [car].
noun(noun(train)) --> [train].
noun(noun(bus)) --> [bus].
noun(noun(university)) --> [university].
noun(noun(drugs)) --> [drugs].
noun(noun(money)) --> [money].

verb(verb(show)) --> [show].
verb(verb(showed)) --> [showed].
verb(verb(worked)) --> [worked].
verb(verb(work)) --> [work].
verb(verb(pushed)) --> [pushed].
verb(verb(push)) --> [push].
verb(verb(stored)) --> [stored].
verb(verb(store)) --> [store].
verb(verb(gave)) --> [gave].
verb(verb(give)) --> [give].
verb(verb(climbed)) --> [climbed].
verb(verb(climb)) --> [climb].
verb(verb(watched)) --> [watched].
verb(verb(watch)) --> [watch].
verb(verb(admired)) --> [admired].
verb(verb(admire)) --> [admire].
verb(verb(appreciated)) --> [appreciated].
verb(verb(appreciate)) --> [appreciate].
verb(verb(played)) --> [played].
verb(verb(play)) --> [play].
verb(verb(love)) --> [love].
verb(verb(loved)) --> [loved].
verb(verb(hate)) --> [hate].
verb(verb(hated)) --> [hated].
verb(verb(manipulate)) --> [manipulate].
verb(verb(manipulated)) --> [manipulated].
verb(verb(seduce)) --> [seduce].
verb(verb(seduced)) --> [seduced].
verb(verb(go)) --> [go].
verb(verb(went)) --> [went].
verb(verb(pray)) --> [pray].
verb(verb(prayed)) --> [prayed].
verb(verb(have)) --> [have].
verb(verb(had)) --> [had].
verb(verb(stopped)) --> [stopped].
verb(verb(stop)) --> [stop].
verb(verb(wait)) --> [wait].
verb(verb(waited)) --> [waited].
verb(verb(sing)) --> [sing].
verb(verb(sang)) --> [sang].
verb(verb(act)) --> [act].
verb(verb(acted)) --> [acted].
verb(verb(run)) --> [run].
verb(verb(ran)) --> [ran].
verb(verb(fix)) --> [fix].
verb(verb(fixed)) --> [fixed].

det(det(the)) --> [the].
det(det(a)) --> [a].
det(det(an)) --> [an].
det(det(every)) --> [every].
det(det(each)) --> [each].
det(det(this)) --> [this].
det(det(that)) --> [that].
det(det(these)) --> [these].
det(det(those)) --> [those].
det(det(some)) --> [some].
det(det(all)) --> [all].
det(det(few)) --> [few].
det(det(many)) --> [many].
det(det(any)) --> [any].
det(det(my)) --> [my].
det(det(our)) --> [our].
det(det(your)) --> [your].
det(det(his)) --> [his].
det(det(her)) --> [her].
det(det(their)) --> [their].
det(det(its)) --> [its].

adjective((adjective(old))) --> [old].
adjective((adjective(poor))) --> [poor].
adjective((adjective(young))) --> [young].
adjective((adjective(white))) --> [white].
adjective((adjective(big))) --> [big].
adjective((adjective(large))) --> [large].
adjective((adjective(empty))) --> [empty].
adjective((adjective(brilliant))) --> [brilliant].
adjective((adjective(many))) --> [many].
adjective((adjective(talented))) --> [talented].
adjective((adjective(bright))) --> [bright].
adjective((adjective(dangerous))) --> [dangerous].
adjective((adjective(fast))) --> [fast].
adjective((adjective(slow))) --> [slow].
adjective((adjective(beautiful))) --> [beautiful].
adjective((adjective(hot))) --> [hot].
adjective((adjective(cold))) --> [cold].
adjective((adjective(slick))) --> [slick].
adjective((adjective(smart))) --> [smart].
adjective((adjective(stupid))) --> [stupid].
adjective((adjective(sharp))) --> [sharp].
adjective((adjective(soft))) --> [soft].
adjective((adjective(smooth))) --> [smooth].
adjective((adjective(hard))) --> [hard].
adjective((adjective(easy))) --> [easy].
adjective((adjective(difficult))) --> [difficult].
adjective((adjective(filthy))) --> [filthy].
adjective((adjective(loud))) --> [loud].

preposition(preposition(in)) --> [in].
preposition(preposition(after)) --> [after].
preposition(preposition(behind)) --> [behind].
preposition(preposition(for)) --> [for].
preposition(preposition(on)) --> [on].
preposition(preposition(at)) --> [at].
preposition(preposition(over)) --> [over].
preposition(preposition(under)) --> [under].
preposition(preposition(into)) --> [into].
preposition(preposition(onto)) --> [onto].
preposition(preposition(before)) --> [before].
preposition(preposition(around)) --> [around].
preposition(preposition(above)) --> [above].

conj(conj(and)) --> [and].

pronoun(pronoun(who)) --> [who].
pronoun(pronoun(while)) --> [while].

adverb(adverb(quickly)) --> [quickly].
adverb(adverb(secretly)) --> [secretly].
adverb(adverb(truthfully)) --> [truthfully].
adverb(adverb(painfully)) --> [painfully].
adverb(adverb(uneasily)) --> [uneasily].
adverb(adverb(secretly)) --> [secretly].
adverb(adverb(secretly)) --> [secretly].
adverb(adverb(secretly)) --> [secretly].
adverb(adverb(secretly)) --> [secretly].
adverb(adverb(secretly)) --> [secretly].
adverb(adverb(secretly)) --> [secretly].

%s(T, [the,young,boy,who,worked,for,the,old,man,pushed,and,stored,a,big,box,in,the,large,empty,room,after,school],[]).

s(s(NP,VP)) --> np(NP),vp(VP).
s(s(NP,CONJ,REST)) --> sHelper(NP), conj(CONJ), s(REST).
sHelper(sHelper(NP,VP)) --> np(NP), vp(VP).

np(np(N)) --> noun(N).
np(np(ADJ, N)) --> adjectiveRec(ADJ),noun(N).
np(np(DET, N)) --> det(DET),noun(N).
np(np(DET, ADJ, N)) --> det(DET),adjectiveRec(ADJ),noun(N).

np(np(NP, PRO, VP)) --> npHelper(NP),pronoun(PRO),verb(VP).
np(np(NP, CONJ, VP)) --> npHelper(NP),conj(CONJ),verb(VP).

npHelper(npHelper(N)) --> noun(N).
npHelper(npHelper(ADJ, N)) --> adjectiveRec(ADJ),noun(N).
npHelper(npHelper(DET, N)) --> det(DET),noun(N).
npHelper(npHelper(DET, ADJ, N)) --> det(DET),adjectiveRec(ADJ),noun(N).

adjectiveRec(ADJ) --> adjectiveRec(ADJ).
adjectiveRec(ADJ, REST) --> adjective(ADJ), adjectiveRec(REST).

prepositionRec(prepositionRec(PRO, NP)) --> preposition(PRO), np(NP).
prepositionRec(prepositionRec(PRO, NP, REST)) --> preposition(PRO), np(NP), prepositionRec(REST).

vp(vp(V,NP)) --> verb(V),np(NP).
vp(vp(V))    --> verb(V).
vp(vp(V,CONJ,VP)) --> verb(V),conj(CONJ),vp(VP).
vp(vp(ADV,VP)) --> adverb(ADV),vp(VP).



