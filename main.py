from random import randint
import random, codecs, string, os

try:
    from pystyle import *
except:
    os.system("pip install pystyle")
    from pystyle import *

#this is just the rot13 code and echo off. U can deobf if u want idc
code = r"""%♙S♵v♵⚔♫%@%♙S♵v♵⚔♫%e%⚕p%c%♞j♶%h%♤k⚖♱%o%♆☟⚉PfuY♴% %☴⚞O♭bqM♕⚇⚇%o%☥♗☱H%f%♩⚐♜♦⚃Th%f%⚅r%
S%A%E%☳☻♙⚜♚wt%T%♡⚋⚆OQ♪%L%⚃☴W%O%e♡☹O%C%♆nn%A%ch♆%L%⚝r% %g♡☴♘⚜fR%E%♵B♕♮%n%☤♘oZ♞cu♅%a%♡♦x%b%♕⚋Xy⚏♠☟p♖%l%LuT♻♦⚛☦⚇♼%e%⚃☷⚚⚃%D%Il%e%w%l%♲⚑lMv⚊%a%Ehkk☹s%y%♣%e%d⚀♘d☞☸F♲%d%TQ♫♛♗u☷%E%U♥☻♛♛L⚘%x%⚎♧⚆kZ⚜♭⚈%p%♕♡♨⚌♠IDS%a%♹♻bI♠%n%ubu♙♪g⚞⚜%s%O☰☰⚜♣%i%⚋l%o%h%n%♘%&%⚒lh☰⚐♫☦⚋%s%S☦⚗♥%e%♖⚞%t%YIv⚌♭⚈♗♕♝⚍% %☟n♠K♪♶C%"%⚟t♘J☥%n%♙eo⚌D⚎%=%☰⚎♜⚌☦%a%☤D♙♡⚁♣%"%♦☶♡♔⚃Np% %m♘E%&%♼♴♨☹b⚞♰%s%⚋Q%e%Nn%t%♦♡% %O⚂♸♯r⚖♭%"%h♘♨⚜☹⚁y☳%o%fR⚙A%=%Yiw♳%b%⚊♖♫C⚘%"%t% %⚉⚒X⚙qcGWE%&%♚♹N⚄♭♼♗♩⚂%s%♾%e%⚂%t%B⚕♛t% %☰J☸☻♚☻R♙%"%oMSA☴%p%☲♘U%=%♽%c%U♶e⚂♚⚉♭♡☹♽%"%♽PD♖⚙♡e⚕♨♣% %☤t⚞aSfe♫⚂♴%&%⚐⚗♼♸Xo⚒⚄♱☞%s%♞%e%yi♶⚚⚏⚜♶k♔%t%☤☳♵♽⚛S⚝☶☟% %♤U☥g⚂⚀⚍x♲%"%Qd♗O⚙☣%q%⚜♆Hdm☶⚒♖☴♴%=%V%d%k☥♪r☧☱C♱☟%"%♅♽cW♖p⚟♫Y♱% %☷R⚝b☲♭%&%Z%s%♣y♜⚏A⚊I☞⚏⚞%e%Iwh♹☡♹%t%♯% %☱⚒☡%"%⚋⚔P♻⚀Tjg⚃%r%Y♥☧⚉%=%☤☸☸%e%v♢⚀m⚔♦b♦⚑%"%E♡⚞X% %☤☻⚂♤♗⚂⚚%&%A☦Ll%s%nR⚁♮⚙%e%vj♕ePxrl%t%PL♾♩♥d⚙% %☱⚖%"%♫♽I⚇H♸⚚B%s%♖♳%=%♴♫♝♾z♩♼c%f%♨♟♗♩c♜⚞f%"%X% %♥%&%♱%s%♩n⚇N♹⚇y%e%⚃♅%t%⚗⚙% %♦Qnj♯N⚕%"%♧M☵Pb⚔Dv♫%t%☴G♴⚀♴♵pC♡♶%=%x⚐☰rV%g%x☰⚆☡♝%"%♻% %⚗♖f☦☢⚛%&%⚐t⚒♬☥M%s%i%e%♯A☹☦%t%☦% %⚌⚃%"%⚚♛☻⚔♡⚇v♳☷♩%u%♶♥♶⚀%=%♙☻yw♟☻☧♥⚐%h%k⚏%"%⚆K⚄pnS% %♛x%&%Dp♘⚇♜g⚗%s%♚♤%e%E⚛%t%♚P♧♗% %T☧♣⚅☶⚉D♱n%"%☻☷☠⚞r☧⚌Zj%v%♼☳♞p♡%=%ZE♨M%i%⚘o⚖☞Sdt☦♵%"%☷l⚀♮♱eL% %⚋s⚙XO⚀d%&%♻♦⚍z%s%♪♹♾%e%TB⚏☸♡Uf♔Xn%t%♟ZH⚄♝♝t♽♜Y% %♘♱Tqe⚕♔☹%"%pE☴%w%♚⚔⚚☥♪F%=%♆♛O♻j☵☧♪⚂%j%♔qK♕♴♢%"%⚂♮♼n♾☥♢☱♧% %v⚟%&%hR☦%s%OZ♬⚗☟%e%p♶☧☱⚐⚋⚑⚅♱♸%t%☡☻♖⚐P♤K% %C☶Q%"%♬♴⚐☲P⚂♭pVB%x%LyI♙☤u%=%♶⚒☟♩C☦☥%k%♖x♹☠LJZe%"%⚙M☹⚇☵⚂♱♧Q% %☳%&%♩♬Tc%s%wze♴☟B⚂♙oa%e%⚋♾%t%♙⚁☱⚙% %☱♫RJ⚛♵d♵fd%"%⚔h%y%BC♕p⚜zFj♥%=%q♫JnLi%l%♶♫♶♵%"%⚛♠⚌♡% %⚊♸⚊F☶nq♚%&%☹⚖%s%♵y⚜W⚒♢♆☱☸c%e%♮⚗⚆♖♛⚔♩c☥♱%t%rO♩ge♟% %☻I⚈T%"%A%z%☥⚃g⚀♅♲⚔%=%V☠d⚝♕♸♔h♟%m%⚂♰♝%"%E⚗M⚍♩qd♅♚♡% %☸☦u♦⚃♆⚍☳%&%♨♽VU☴⚗♜h☹%s%♛%e%⚌♢♼♜⚅♯v♧%t%♖⚇ZhEB♡% %V⚘♨♭U♻♨♹♸%"%♼☤☧H%a%⚊aea%=%u♶%n%♢☣♧%"%r⚃☤♫lVCHS% %♫♖⚜♲♳♜⚀♼%&%⚁%s%J%e%☶♮⚅Y⚈%t%☳U☱☰☰% %⚕X☣C⚌H%"%♬%b%♲☢F☣♛Q%=%☢XN⚎⚒d♅%o%☻⚗%"%⚑♰♔⚃RNS⚞⚂% %HW⚎⚝G⚘♬♥⚈%&%M☰⚗⚜pS%s%u%e%♶%t%P⚅☸♨♛b☦♵% %l⚑F%"%♙♯♴%c%☻d⚊♰w%=%sQ⚝J☵Q♪♙T%p%P♠⚃♗♯%"%☧⚋⚇♩% %♅⚚♛⚚⚆%&%☱f⚖⚚g♵⚒⚑Ar%s%j♡jMAYV%e%nqD⚘YE⚙%t%⚝% %♩df%"%♕☴♫%d%☦%=%Y⚁%q%s⚊☧⚖♡♟♢%"%☧anj♡⚁⚑⚙♤% %⚜☶yl⚑pP%&%G♾u♳♾%s%Aa♳⚌⚛i⚕%e%♖%t%♬Q☥♚ukP♠% %ON⚏T⚊♯♅♙%"%u♛⚜⚘%e%♨y♮☵♚☤♨%=%wp☻☵⚃☲%r%♬☤j%"%♥♯♦♬⚊v☞c% %☰⚗☻♣bX♅%&%⚋%s%⚈%e%⚊♶♅%t%⚖♕⚎⚂⚝% %⚐k☣♰♩♖⚞Y♸%"%⚃OCN⚒cLU%f%⚈⚁%=%Z♠♕⚛x♆Y♼B%s%☰uf♔GV♝K%"%HZ☢% %⚘ud⚒K%&%☟♔W☡U♴♳vL♖%s%♖c♣♦Z%e%⚖♅⚕♕⚙♮%t%Y☤% %♻S♠M%"%⚖RZz%g%a♛Z☠☦♭d☦%=%☣c⚘u☷xJ%t%n☳%"%♟S⚑♡MAL♔% %☢%&%d♦☷⚑%s%♽♥%e%♮%t%Q♕☲♱♪☶Pk♲P% %☦%"%t♘♥☻⚛⚒⚔☟%h%r%=%S♽⚘♜%u%r%"%⚈♶M⚀% %♯K%&%⚇♽♲Ed%s%hI⚝⚅⚍♤%e%lr⚅⚕♚♣⚞b%t%mif☟⚔p☰♥⚎⚔% %⚉☱⚝♪x%"%♸m⚙♧☣%i%O♤A%=%B%v%♶♚♡x%"%o♤⚇♞⚑Z% %⚂♩%&%⚐♴⚉⚜☣♅♆%s%☴⚇⚎♵⚋♢☰⚇☧%e%☴D⚏a%t%v♳⚘⚑% %♩e☸G%"%♩♹l⚐♯b☞%j%⚆♶⚑o♫Os♩♚%=%g♵☧♾⚝⚘♙Dr%w%⚙♞t♹☷cnS%"%R⚃t⚞♩⚌⚜f% %⚅B♪☧k♢♭%&%PvM♭s♡%s%V%e%☡S⚛♼U%t%x♼⚐♰H⚑☳♮% %☣T⚆♔⚂⚃☶%"%l♱♰♹%k%Oq%=%q%x%⚃⚜♵♢%"%♜⚍♫♦☤hqg% %♟MU⚆S♙⚉Av%&%♟♴♞%s%♕♡⚖⚉⚄O⚆☞%e%C☰O⚞⚆T♻♛☢%t%⚈O⚉h♔% %♨cY⚌♮%"%♗KyR☵%l%☵%=%Rkz☞⚕☻BM%y%♝♳YR%"%♶♳O% %u☴♪%&%LVsZq♽⚈X%s%☷♫D⚅⚗AJ%e%☧⚄J♗n♘☱⚉%t%♸⚄♞v⚈U% %♩t♯⚉jN⚍%"%L♜☤f♻♡☢♆%m%♩K⚜⚒zY%=%☰mx♔⚇♭☶⚇%z%♡⚉☲VQha%"%⚒⚋⚙⚃♹U♼⚊% %f☻Ic♾nL%&%Z⚖☦%s%⚇%e%⚁%t%♫♛xs☠% %♆W♞B%"%Y☵♖♼%N%gY%1%♙klo☦⚙⚀♡♽♡%=%♢⚐%A%♸⚅q⚞☸♤%"%Kpy⚆♅⚋⚋☤⚚% %kk%&%p⚌♟♞%s%☣♴v♤⚍♾⚝♻☵♚%e%⚁⚗gze♛☴%t%♣J♠♙☱☡♞♦☹K% %☴z%"%♢⚗♢Xb♆Rk%O%⚃♆♝xH♪☹⚖Ms%1%♫⚘wG⚛z⚏⚟♰%=%⚔U☰M☱t☟W%B%♮♴%"%ir% %g%&%n⚌⚎⚐⚖♲♚%s%☹bz⚍☰R%e%⚏J☣jZ%t%H♟D⚅⚀c♨☸R% %☴M♴☱F♕u%"%v⚛⚇⚅♗♱☸%P%b♤⚆⚙♪%1%♢lF%=%x%C%♧☰⚑☴☠%"%♚⚕♶♮⚄CN⚎Gm% %☸G♽%&%☟♧J♘♡T%s%♳♻⚜☢⚕%e%PQ%t%⚘Ra☤♼♔☸% %L♢♨☞⚛⚗Z♧⚝V%"%g♩♪⚕☱%Q%S☢cot⚈♧♴⚝%1%♪E%=%⚖♯E♘%D%♲♚U♨t♜%"%d⚟⚗s☲⚔n☻⚉⚊% %C♦☥⚅%&%☻EN%s%JWAU⚝%e%♜s☹♖%t%Uc⚜% %♾u⚊♮E♡k%"%♆Fy⚁☤c⚄ou♱%R%E♾☦%1%♠⚁♅♾♲zTz%=%♕♰☠⚗S⚌b%E%⚂p♢EE☟⚌♦b☟%"%♯b♝⚉♹⚉D% %☰♼M☞f☦%&%♭♕♤W♩%s%♨♸p%e%Z♪☴☶♔R%t%♕⚃% %⚏rjnT%"%⚘♆♨☟Z♟%S%☦⚁E⚖%1%a♤☦♯⚑♯%=%☤Z♳⚍⚌♭iUH⚈%F%wZ♼C⚌☵F⚁♰%"%Zf♡♤☹☧⚄☹⚐♦% %a☞♪⚀⚕♘♘%&%m☴J%s%⚉⚎☶U♶m⚙⚏B☤%e%♸☵iz♡%t%⚘T⚇♙X♞u% %♆♘⚀W⚗⚐♖♝%"%♖⚊YAw♝⚟%T%⚐p%1%☱f♞☷☱%=%Ig♚☱eA♣☣%G%♤♛%"%DzT% %RR%&%⚊♕☣%s%♫♠♼%e%o♡%t%♵⚃☦⚑⚌% %☤☹♵%"%g☞%U%A♮☲♩⚋♶⚈%1%♫%=%♹w♤♽J♼☹♽%H%♝r☰%"%nf♨♗⚇⚎% %♧s☟♦☢☶x☢⚊%&%a♅♙☦♾⚃♟V%s%Mo♱Do%e%S☶♸%t%W☱K♧♭% %☦♲☤c⚙☡dQP♪%"%sE♖p♮%V%☸⚜Oy☹☧N⚆%1%♥☣☰☹⚍♞c%=%☤⚀⚎☡x⚀st⚕%I%♹♯♮q⚄L♙%"%♭V☱♜☷⚚♜☥% %⚏☲⚉P♨%&%♾VO♢⚌⚁%s%r⚕⚞♹♘q☢%e%A⚜%t%⚁K⚁⚀o♹% %♰w☦g%"%g♸a☣t♦%W%F♛☸n⚖%1%c♛%=%♹%J%⚏B♡W%"%♧% %⚉⚆♫⚀⚏X♕X%&%♕%s%⚜⚙☻☦r♦S⚆☹♗%e%j♪⚍☣☞%t%♡cA♚% %⚛yb⚇♶hk♢♥W%"%♼⚗g♧t♻☸%X%♘♵R⚐%1%☧⚜⚇⚏☥☴⚈F⚋♼%=%⚘☸♚F⚌%K%W⚜♭mt♤%"%⚟d% %☵♖%&%♫S♅⚝⚉⚌%s%☣♘♛⚆☶lE%e%♶⚌♹♶☶jw♪%t%K♰☷♡Y♭⚆% %♫hf⚌C%"%♾⚇☣♜♬♭♣%Y%♗☻nQ%1%SX♝jBv♙%=%♳☡g%L%z%"%☱⚝E⚜♔⚔♯⚉% %B♱Y☞⚊ik⚝l%&%OjI⚙☻☢♤☣%s%♚⚛☠♕t⚄⚄♢♻%e%♼♗l☹⚞J⚃☞%t%a☲♨S♾v☷IV♙% %☱♹⚝XA♯♰x%"%⚐⚐HG☵KyK%Z%d%1%B⚌☷N⚔%=%♬dY⚜☴⚈☵%M%D⚜☣♱♡R⚎♨%"%☰% %⚛⚑☲U%&%w♜♗p♼☹♚♅HC%s%qQ⚞P⚖⚉X%e%♅%t%☟% %♅%"%⚍♨♖⚕w⚋☥%A%♮%1%♭☞♜☟%=%♗♠⚀aY⚐♵%N%♕⚚y☴♽♘♯♗⚛♯%"%⚆o% %⚏V♠♢%&%♨♙⚜⚙%s%U⚕♽♳♾♞NP⚒⚋%e%⚑t%t%⚋⚘lA♱% %♆a☦%"%♰%B%k⚒⚙♰D⚇%1%☱L♛⚏♦♥w♙a%=%☰☳☻☟%O%♫EVo♢⚞%"%♡GE⚏♽♗⚁% %♚a♾v%&%☞⚒R☸☱☠%s%⚈⚂⚚⚑☢♜⚗X♣%e%☦⚗DJ☞K⚉⚌j♖%t%☱h⚗tRb% %☠B♴☠D%"%⚃⚎fUr☴♸%C%n%1%☣☴K☟☹%=%W♵L⚁%P%♝⚔♜⚏♻X⚑☵♗w%"%☢% %♅⚕⚘Z♝Ak♮%&%♬b⚈%s%⚚♰%e%☦♳♪♶♗♣♜MW⚛%t%♱♔nfS⚚♚☳% %Yx☻♱M⚚♧☥⚑%"%♧⚙⚏rx☧Y☠%D%l%1%⚋♖⚒☥%=%X♱♴vA♠♯⚕♳%Q%mh☧⚒⚒N%"%vu♭X☣r⚎% %♨nF☸%&%j☰♭%s%☡rn♾♵%e%V♰♴%t%a♧% %pL⚎♧%"%☠☶♢%E%♻⚏Aq♕%1%Z♶♝g♬♴♻☻⚈♆%=%⚛K%R%⚚♥♟♧c♆⚐♘f♗%"%♻⚘♬Rp♡♦A% %♬T⚕♚♰SY⚋⚂♭%&%⚚Y⚂%s%⚘☟N⚝K♕%e%⚃⚕X%t%H⚞♧% %uk♫♩bi☰%"%☞u⚞⚉⚕q⚉♔%F%♻♧♟%1%♔%=%☦♩⚆⚍♼%S%C♻⚗☷☶J⚎p⚋⚖%"%☸⚏e♴♗b% %♦x⚅%&%⚇♬%s%☲♰a☵%e%♱⚘♡♨WW%t%I♹♻♴♚♟b% %⚝⚞⚀♻q⚎%"%CD♛%G%P⚆♆♫%1%☞PT%=%♤U☹%T%⚔♶w⚗♜☲♞%"%Q⚅☱☶% %⚃☥⚊☴♫v♨♞⚘%&%♕☣Dx⚞%s%⚆♙%e%⚁⚙⚅S%t%t% %p♞⚂♽♲⚑%"%⚃WS♩♸cw%H%♤☱%1%♴⚅♱c♨iDQ%=%♾⚒o%U%♳i☳%"%H♶hra% %♡⚏vK%&%ht%s%☹♴a♜%e%⚃%t%⚛t% %♡%"%♥bx⚗♢⚏♅%I%♽☞DCxQ♽♙⚅%1%I♳♵⚙%=%ih♘⚅⚐☻♠☶%V%⚒♖☢%"%S♤♶♥B☹☲♦% %⚞⚈bD♥%&%♗☠T⚙d♖Y☱%s%♬N♥♦⚐☵♸%e%♽⚛R☻♽t♲⚌⚋R%t%Ih⚇☹♯% %W♪VnV♕F♬⚜%"%♥SU☟♣♗♕⚀%J%♙fG♨aT%1%♦⚒♯%=%v♠Y☢☢%W%W⚚♕Oi⚉⚜z♶♖%"%y☢⚌♗☧g% %⚜♣⚛♹I♟⚐⚏%&%b♧⚅⚟j♴♤⚅⚊%s%Y⚄♞♼EU☹%e%☟L♮%t%☵☣E⚆♖☵c% %♘iNx♹y♙%"%IJ⚂♖%K%JoW♦fF♞♚♦♝%1%F♬D♶♶w%=%RuCk♥b☦♰☟%X%♡%"%♾LQ% %☳☢Z♶♴⚉♚%&%⚊Pxn☹♽%s%♫%e%G♹☧⚅☻%t%⚀☟B☱% %⚈♟m♮o♨♻♰Xc%"%♲♕☟%L%⚄S⚅E%1%⚘C♵⚟⚜%=%☟S♽☧⚀Y⚂♣s%Y%♅Za⚍⚉tY♛%"%♝♸y% %F♘s☦☰♲%&%♫w⚟⚌♴♡♘♥♝♵%s%CY%e%J⚘⚌%t%e% %⚕♡⚋i%"%Ic%M%J%1%♰♤♡KtB☱⚐⚖♪%=%♞N♜%Z%♦☳⚁☰♽♡⚀⚑♡♖%"%t% %QNwHn%&%⚎♥⚛♵♙u♕%s%qaR♔w%e%f♴T♦%t%♼♴☰♟⚂☦♕⚟% %♬u♧H⚖%"%☵%l%♜⚙♠⚘y%u%☧♢a⚆%l%♢⚃☹%=%CIkw%:%vj%"%♠☻H%
"""
banner = Center.XCenter("""
 ██████╗  ██████╗ ██████╗ ███████╗ █████╗ ████████╗██╗  ██╗███████╗██████╗ 
██╔════╝ ██╔═══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗
██║  ███╗██║   ██║██║  ██║█████╗  ███████║   ██║   ███████║█████╗  ██████╔╝
██║   ██║██║   ██║██║  ██║██╔══╝  ██╔══██║   ██║   ██╔══██║██╔══╝  ██╔══██╗
╚██████╔╝╚██████╔╝██████╔╝██║     ██║  ██║   ██║   ██║  ██║███████╗██║  ██║
 ╚═════╝  ╚═════╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
 Made by Godfather and K.Dot#0001\n\n
""")

print(Colorate.Vertical(Colors.yellow_to_red, banner, 2))
file = Write.Input("What is the exact file name or path of file you want to obfuscate? (with file extension pls) -> ", Colors.yellow_to_red, interval=0.025)

def obfuscate(file):
    try:
        os.remove(f'{file}.obfuscated.bat')
        os.remove(f'{file}.obfuscated.super.bat')
    except:
        pass
    switch = False
    with open(f'{file}', 'r+', encoding='utf-8') as original:
        for lines in original:
            lines.count(':')
            if lines.count(':') == 1:
                with open(f'{file}.obfuscated.bat', 'a+', encoding='utf-8') as f:
                    f.write(lines) # TEMP FIX FOR NOT FINDING FUNCTIONS BATCH
            for char in lines:
                if switch == False:
                    if '\n' in char:
                        with open(f'{file}.obfuscated.bat', 'a+', encoding='utf-8') as f:
                            f.write("\n")
                    elif "%" in char:
                        with open(f'{file}.obfuscated.bat', 'a+', encoding='utf-8') as f:
                            f.write("%")
                            switch = True #thx baum for making this work :sob:
                    else:
                        random_num = randint(5, 12)
                        random_string = ''.join(random.choice('☞☟☠☡☢☣☤☥☦☧☰☱☲☳☴☵☶☷☸♕☻♡☹♆♔♅♖♘♗♙♚♛♜♝♞♟♠♡♢♣♤♥♦♧♨♩♪♫♬♭♮♯♰♱♲♳♴♵♶♶♸♹♻♼♽♾⚀⚁⚂⚃⚄⚅⚆⚇⚈⚉⚊⚋⚌⚍⚎⚏⚐⚑⚒⚔⚕⚖⚗⚘⚙⚚⚛⚜⚝⚞⚟') for kdot in range(random_num))
                        with open(f'{file}.obfuscated.bat', 'a+', encoding='utf-8') as f:
                            if char in string.ascii_letters:
                                if char.islower():
                                    coded0 = codecs.encode(char, 'rot_13')
                                    coded = coded0.replace(coded0, f"%{coded0}%")
                                    f.write(f"{coded}%{random_string}%")
                                else:
                                    coded0 = codecs.encode(char, 'rot_13').upper()
                                    coded = coded0.replace(coded0, f'%{coded0}1%')
                                    f.write(f"{coded}%{random_string}%")
                            else:
                                f.write(f"{char}%{random_string}%")

                else:
                    if "%" in char:
                        with open(f'{file}.obfuscated.bat', 'a+', encoding='utf-8') as f:
                            f.write("%")
                            switch = False
                    elif '\n' in char:
                        with open(f'{file}.obfuscated.bat', 'a+', encoding='utf-8') as f:
                            f.write("\n")
                    else:
                        with open(f'{file}.obfuscated.bat', 'a+', encoding='utf-8') as f:
                            f.write(char) # spent like 2 hours trying to fix this and found baums again :sob: https://github.com/baum1810/batchobfuscator

    with open(f'{file}.obfuscated.bat', 'r+', encoding='utf-8') as f:
        everything = f.read()
    with open(f'{file}.obfuscated.bat', 'w+', encoding='utf-8') as f:
        f.write(f"{code}\n{everything}")

    out_hex = []

    out_hex.extend(["FF", "FE", "26", "63", "6C", "73", "0D", "0A", "FF", "FE", "0A", "0D"])
    with open(f'{file}.obfuscated.bat','rb') as f:
            penis = f.read()

    out_hex.extend(['{:02X}'.format(b) for b in penis])

    with open(f'{file}.obfuscated.super.bat', 'wb') as f:
        for i in out_hex:
            f.write(bytes.fromhex(i))

if __name__ == '__main__':
    obfuscate(file)
    print(Colorate.Color(Colors.green, "Obfuscated file successfully", False))
