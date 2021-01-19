# Queer Motto API Manual
<img src="images/key1.jpg" width="600">
<p>
<img src="images/key3.png" width="600">

## Project title
Queer Motto API: To know exactly how many times to cry

**Description:**

“Queer Motto API” software-as-service lets you develop websites and applications to retrieve and display allied mottos, for urban dreams lying in wait, anti-facist guiding principles of living, queer love ethics, authoritarian resistances, unsettle normative computational culture, revolutions, political movements, destruction of smart city infrastructures, class struggles, municipal identities, art practices, joyful engagements and violent direct action.

Our mandate:
* undisciplined and vulnerable,
* reorganise your collective life and fight injustices in the present,
* NAP and be RESTful,
* render computers unusable,
* refuse tokenisms,
* (re)externalise risks,
* make use of accident and injury,
* networks of pleasure,
* launch relentless attacks.

ALL ACCUMULATED & QUE(E)RY IN REALTIME PROGRAMATICALLY.

Thank you; have a nice day!

## Examples of allied mottos

Generated from the Queer Motto API:

<img src="images/key2.png" width="600">

!!need updated image with the upper case

```html
Neurode not better
Formed to performance
System's perfection I'll different
Be fusion autonomous
Free wosk narrated
Are clack political
```

## NAPPY API Specification - r1

**USAGE:**
```html
https://toknowexactlyhowmanytimestocry.net/queermottoAPI/r1/refusal?
rq=generate&org=refuse-tokenisms-tt-2021
```

**NOTES:**
1. Any incompleted parameters/values will result in generating refusal code and messages.
2. The parameter of `org` is the key authetication parameter, and the example above is for testing only in which we do not guarantee the service level.
3. Please contact us for the new `org` value if you want to use this NAPPY API in your projects or organizations.

### Parameters

`rq`  
string  
REQUIRED

**Request types:**

| Value | Description |
| -------- | -------- |
| `generate`    | a new motto request  |
| `motto_log`   | retrieve all the generated mottos   |
| `all_log`   | retrieve all the generated mottos and refusal records|

**NOTE:**

1. Any incompleted parameters/values will result in generating refusal code and messages.

---

`org`  
string  
REQUIRED

> A unique identity for each organization/user to `generate` mottos <e.g xxxxxxx-xxxxxxxxx-xx-xxxx>.

**NOTE:**
1. Please contact us for the org value if you want to use this NAPPY API
2. Any incompleted parameters/values will result in generating refusal code and messages.

---
### API Response

`200 application/json`

The API returns a JSON file.

**EXAMPLE:**

#### 1. when `rq=generate` (with a valid org value):

**Returned format:** JSON

**Description:** Return an allied motto

```json
"Names to activities\\nForce rotation World\\nSharing female culture profound\\nBe survival after\\nFact today world\\nAre plants political"
```
After parsing it will read as:

```html
Names to activities
Force rotation World
Sharing female culture profound
Be survival after
Fact today world
Are plants political
```

**NOTE:**

*To use the generated text, your end (at the program level) can parse the delimiter `\\n` in which it signifies the next line of the motto.*

---

#### 2. **when `rq=motto_log`:**

**Returned format:** JSON

**Description:** Return all the generated allied mottos.

**USAGE:**

```html
https://toknowexactlyhowmanytimestocry.net/queermottoAPI/r1/refusal?rq=motto_log
```

**EXAMPLE:**
<img src="images/log1.png" width="600">

!!replace another image when the server is ready

| Field | Description           |
| -------- | --------           |
| 0    | Generated mottos       |
| 1    | Timestamp (CET time)   |
| 2    | Organizational name    |
| 3    | Seed Text              |

---
#### 3. **when `rq=all_log` :**

**Returned format:** JSON

**Description:** Return all the logs from the server, including various request types, the generated mottos and refusal messages. The fields 0 and 2 would be null when no mottos are generated.

**USAGE:**

```html
https://toknowexactlyhowmanytimestocry.net/queermottoAPI/r1/refusal?rq=all_log
```

**EXAMPLE:**
<img src="images/log2.png" width="600">

| Field | Description |
| -------- | --------           |
| 0    | Generated mottos       |
| 1    | Timestamp (CET time)   |
| 2    | Organizational name    |
| 3    | Seed Text              |
| 4    | Refusal code           |
| 5    | Refusal message        |
| 6    | Request types          |

## Queer Motto API

<img src="images/sketch01.jpg" width="600">

### 1. Queer Motto Alliance

The project primarily includes two parts: the generative allied mottos and the refusal messages.

The generative mottos are based on manifestos and zines for queer and intersectional life as source text for machine learning and generative processes. The project uses recurrent neural networks to train and process sequences of collective voices, as well as the diastic algorithm to establish a poetic structure. Such a queer model opens up new imaginaries and forgotten language beyond the confines of accurate prediction and effective generalization.

The program also implements computational logics to perform refusal at the infrastructural level, generating refusal messages that are found in our list of queer and intersectional source text.

We invite users & requesters to think about how we can imagine refusal strategies at all levels of our lives. What forms of alternative we can build and make changes collectively.

> keeling on queer as an epistemology

### 2. Seed Text & Diastic Model + ML

<a href="http://siusoon.net/projects/finiteState_gallery_T2a_neato.svg" target="_blank">
<img src="https://i.imgur.com/6Tchm5M.png" with="600"></a>

("not for self but for all") -> more for the allied mottos

Queer API uses a RESTful architecture that is built from manifestos and zines for queer, Black, Asian and intersectional life as source text for machine learning and generative processes. Queer API contantly listens for Motto requests. The Mottos are generated through the mis/use of AI-specifically recurrent neural networks - a machine learning model which the Queer Serivce team use to train and process sequences of collective voices. The machine learning algorithm learns its writing style at a character-based level, however instead of a single authorial voice the model is trained on an alliance of queer writers. Such a queer model opens up new imaginaries and forgotten language beyond the confines of accurate prediction and effective generalization. We might understand this type of machine learning as replacing training with listening. A listening which might as Kara Keeling describes be a “generative proposition another world is possible, the insistence that such a world already is here now and it listens, with others, for the poetry, poetry, the refrains, the rhythms, and the noise such a world is making”. (2019, ix)

The mottos are written using a "diastic reading through" method a word coined by poet Jackson Mac Low from the Greek words "dia" (through) and "stichos"(a line of writing, a verse) in the 19. Diastic reading is a chance based deterministic method that relies on the use of two texts:

Seed Text
Source Text

To gather the inital collection for the source text the queer service team went urban dreaming, seeking out manifestos that are housed in the radical books shops and libraries in Kings Cross and Euston, places that are historically important for the queer movement. Although sites of historic significance for queer spaces, Kings Cross and Euston are both areas that have been effected significantly by the construction and changing urban fabric of London: Queer night-time spaces have been replaced by the relentless gentrification by tech companies and start-ups. The source text is an growing collection and manifestos can be proposed and entered into the model's listening.

The seed text Not for Self, but for All is used in different parts of the text generation. This seed text, which at first was mistaken for a corporate slogan, is Camden Council’s motto for their municipal identity which hangs prominently next to the Google offices in the heart of the new development of Kings Cross. Recurrent Queer Imaginaries is a call to reclaim queer spaces from corporate neocolonial imaginations, operational injustices and reimagine them differently for all, as a commitment to queer liberation.

"In employing such procedures, the writer reads through the source text, taking into the poem each successive unit which has the letters of the source words in corresponding places. The first linguistic unit in the poem begins with the first letter of the first word of the title or other seed, the second unit has the second letter of the first word of the seed in its second place, and so forth, possibly through multiple passes through the source string.
The motto's are generated from the machine learning model using a diastic algorithm a writing device created by  to establish a poetic structure."


### 3. Refusal logic

| Code   | Description |
-------- | ----------- |
| 400   | A refusal word is found in the generated motto |
| 401   | Infrastructure  & technical issues   |
| 402   | Every n API request counts & on specific nap dates   |

There are three levels of refusal logic that point to different living conditions and open up other ways of being and actions. For the refusal code 400, it makes explicit [what](link_refusal_words) to refuse, such as "hate", "oppression" and "foreclosing" to consider wider injustice phenoemna. Refusal code 401 is more related to infrastrucure and technical issues, such as incompleted API parameters, server errors and connection problems, and these remind the effort and care that are required to maintain a technocultural system. The last refusal code 402 points to labour conditions, and encourages others to take naps and live restfully. The API will refuse to generate mottos when it exceeds the assigned count (which is 10 at the moment) of the API requests, as well as on specific dates, such as 8th of March (Women strike), 1st of May (Labour strike), and 20th Jul (Strike for Black Lives). With all these checking logics, a refusal message will be displayed instead of a motto.

[The refusal messages](link_refusal_msgs) are actions and statements that are taken from the queer and feminist source text. They are not tehnical errors, but to call for an attention to our living and societal conditions, that are highly computational, resources-driven and stressful, and to rethink what and why to refuse, and how we might reorganize and queer our collective life as a form of society-level operating system. As elaborated by Kara Keeling, this form of Queer service "facilitates and supports imaginative, unexpected, and ethical relations between and among living beings and the environment" (2014, 154).

**EXAMPLE OF A REFUSAL MESSAGE:**

Your motto request is refused. REFUSAL " + refusal_code +": " + "REFUSAL CONTENT in the form of an random array index"`

<img src="images/refusal1.png" width="600">

## Server info & Tech spec
- Debian ver 10
- Web server: NINGX
- Python and Flask · PyPI
- Machine learning for text - Python, tensorflow and RNN
- MySQL lite
- Source code [link](https://git.vvvvvvaria.org/ccl/queerAPI)

## License

The project is licensed under a Collective Conditions for Re-Use (CC4r)

See more: https://gitlab.constantvzw.org/unbound/cc4r

## All Manifestos

* 80:20 (2011) by Lucia Tkacova and Anetta Mona Chisa
* 100 ANTI-THESES (1997) by Old Boys Network
* 100 IMPOSSIBLE ARTWORKS (2001) by Dora Garcia
* A CYBORG MANIFESTO (extract) (1991) by Donna Haraway
* ARCHIVAL PRAXIS (2013) by Jean Carlomusto
* A STATEMENT OF OUTRAGE AGAINST AMERICAN ASSIMILATIONISTS WHO PRACTICE APPEASEMENT OF HETERO TERROR IN THE WAKE OF A.I.D.S GENOCIDE IN THE UNITED STATES (2013) by Jerry Tartaglia, 2013.
* BEYOND DOMESTICATION (2013) by Richard Fung
* BITCH MUTANT MANIFESTO (1996) by VNS Matrix
* CYBERFEMINIST MANIFESTO FOR THE 21ST CENTURY (1991) by VNS Matrix (Josephine Starrs, Julianne Pierce, Francesca Da Rimini, Virginia Barratt)
* ECOSEX MANIFESTO (2011) by Elizabeth M. Stephens and Annie M. Sprinkle
* FEMINIST ART ACTION BRIGADE - MANIFESTO (2003) by Feminist Art Action Brigade (FAAB)!
* FEMINIST NOSIFICATION OF SOCIAL MEDIA (2019) by Purple Noise
* FOR HEAT AND LIGHT AND OUTRAGEOUSNESS (2013) by B. Ruby Rich.
* INTRODUCTORY RANT IN PERFORMANCE OF ASSISTED LIVING: DO YOU HAVE ANY MONEY? (2013) by Yvonne Rainer
* INTERNATIONALISTS ANSWERS TO A RENTED WORLD! (2013) by Marc Siegel
* IT’S CALLED DOMINANT CULTURE FOR A REASON (2013) by Matthew Tinkcom
* MANIFESTO AGAINST THE ‘BLACK CODE’ EDICT OF LOUIS XIV, 1685 by Pélagie Gbaguidi, May - June, 2008
* MANIFESTO FOR A QUEER SOUTH POLITICS (2016) by Pippa Holloway
* MANIFESTO (2019) by Pinko Pinko
* MIGRANT MANIFESTO (2011) by Tania Bruguera and Immigrant Movement International
* OCCUPY THE DREAM (2013) by Barbara Hammer
* PRELIMINARY NOTES FOR A BLACK MANIFESTO (1975–6) by Rasheed Araeen
* PROPOSITION FOR A BLACK POWER MANIFESTO (1971) by Ted Joans
* RADICAL SCHLOCK (2013) by Raquel Gutiérrez
* REFUGIA: MANIFESTO FOR BECOMING AUTONOMOUS ZONES (BAZ) (2002) by subRosa
* STATEMENT ON CENSORSHIP (1973) by Anita Steckel
* STOMP FOR THE SHADOWS (2013) by Pratibha Parmar
* SOULPOWER(2013) by Shari Frilot
* SURVIVAL: STRATEGY (1977) by Larry Mitchell and Ned Asta
* T TIME A QUEER MEDIA MANIFESTO (2013) by Susan Stryker
* GUERRILLA GIRLS' GUIDE TO BEHAVING BADLY (which you have to do most of the time in the world as we know it) (2010) by GUERRILLA GIRLS
* THE QUEER NATION MANIFESTO (1990) by Act Up
* THIS IS NORMAL (2013) by Shu Lea Cheang
* TOWARD A METHEXIC QUEER MEDIA (2013) by José Esteban Muñoz
* TRANIFEST: QUEER FUTURES (2013) by Julia R. Wallace and Kai M. Green

### newly added/suggestion:
- https://www.manifestno.com/
- [A Feminist Server Manifesto](https://areyoubeingserved.constantvzw.org/Summit_afterlife.xhtml)
published by Constant (2014)
- check out https://cyberfeminismindex.com/ and https://cross.virtualprivateserver.space
- [Feminist Principles of the Internet](https://feministinternet.org/)
- What Is the University For? A Story from the Dreamtime of a Possible Future - https://press.uchicago.edu/ucp/books/book/distributed/M/bo15571238.html
- Hamraie, A., & Fritsch, K. (2019). Crip technoscience manifesto. *Catalyst: Feminism, Theory, Technoscience*, 5(1), 1-34

## Suggested readings & projects

* [Queer Currents 2020: Queer Manifesto Reading](https://www.mediamatic.net/nl/page/378309/queer-currents-2020-queer-manifesto-reading)
* [Our HTML Roots and Simple Web APIs](https://www.oreilly.com/library/view/restful-web-clients/9781491921890/ch01.html)
* Snodgrass, Eric, and Soon Winnie. "API practices and paradigms: Exploring the protocological parameters of APIs as key facilitators of sociotechnical forms of exchange." First Monday 24.2 (2019).
* Gurses, Seda, and Joris Van Hoboken. "Privacy after the agile turn." (2017). (see the draft here: https://osf.io/preprints/socarxiv/9gy73/)
* Keeling, Kara. "Queer OS." Cinema Journal, vol. 53 no. 2, 2014, p. 152-157. Project MUSE, doi:10.1353/cj.2014.0004.
* Barnett, F., Blas, Z., Cárdenas, M., Gaboury, J., Johnson, J. M., & Rhee, M. (2016). [QueerOS: a user’s manual](https://dhdebates.gc.cuny.edu/read/untitled/section/e246e073-9e27-4bb2-88b2-af1676cb4a94). Debates in the digital humanities, 50-59.
* Keeling, Kara. *Queer times, Black futures*. NYU Press, 2019.

## Queer Service team

- [Winnie Soon](https://www.siusoon.net)
- [Helen V. Pritchard](http://www.helenpritchard.info)
- [Cristina Cochior](http://randomiser.info/)
- Nynne Lucca

## Credit and Acknowledgements

The project is commissioned by Transmediale in 2020-2021. Thanks to Nora O Murchú, Yidi Tsao, Anky Heidenreich, Holga Heißmeyer, Seda Gürses, Eric Snodgrass, Kara Keeling, Joasia Krysa, [Exhibition Research Lab](https://www.ljmu.ac.uk/research/centres-and-institutes/institute-of-art-and-technology/expertise/exhibition-research-lab)
