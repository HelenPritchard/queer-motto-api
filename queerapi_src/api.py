import flask, random, datetime, json
from flask import request, jsonify
import sqlite3
from flask import g
from multiprocessing import Value
import pytz
from tokens import secrettoken1, secrettoken2, f1, f2
from removed_words import delWords
from refused_words import refWords
from refusal_messages import refusal_messages
from intact_words import intact

app = flask.Flask(__name__, static_url_path='', static_folder='static')
app.config["DEBUG"] = True
app.config["PROPAGATE_EXCEPTIONS"] = False

counter = Value('i', 0)
DATABASE = 'queermottoapi.db'
availableWords = open('static/files/RNN_EditedText.txt', 'r', encoding='utf8')
wordList = availableWords.read()
wordList = wordList.split()
seedText = "not for self but for all"
seedTextList = seedText.split()
tz = pytz.timezone('Europe/Berlin')

for word in wordList:
    for delword in delWords:
        if word == delword:
            wordList.remove(word)

def build_error_one():
    refusalOne = 'Your motto request is refused. REFUSAL 400: ' + random.choice(refusal_messages)
    return(refusalOne)

def build_error_two():
    refusalTwo = 'Your motto request is refused. REFUSAL 401: ' + random.choice(refusal_messages)
    return(refusalTwo)

def build_error_three():
    refusalThree = 'Your motto request is refused. REFUSAL 402: ' + random.choice(refusal_messages)
    return(refusalThree)

# Generating a dict that will be used for the phrases when called upon
toChooseFrom = {}

def build_word_dict():
    for i in range(len(seedTextList)):
        # Current word in the seed phrase
        current = seedTextList[i]
        # Going through the letters in the above word
        for y in range(len(current)):
            charNeeded = current[y]
            for item in wordList:
                if item not in intact:
                    item = item.lower()
                if (len(item)-1) >= y:
                    addKey = str(y) + item[y]
                    if addKey not in toChooseFrom.keys():
                        toChooseFrom[addKey] = []
                        toChooseFrom[addKey].append(item)
                    else:
                        toChooseFrom[addKey].append(item)

build_word_dict()

# Importing the database and turning it into dictionaries
def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def add_db(api_phrase_str,timestamp,org,seedText,request_type):
    query = "INSERT INTO mottos (generated_motto,timestamp,organisation,seedtext,request_type) VALUES (?,?,?,?,?)"
    args = (api_phrase_str,timestamp,org,seedText,request_type)

    try:
        con = get_db()
        cur = con.cursor()
        cur.execute(query, args)
        con.commit()

    except Error as error:
        print(error)

    finally:
        cur.close()
        con.close()

def add_error_db(timestamp,org,seedText,request_type,refusal_code,refusal_message):
    query = "INSERT INTO mottos (timestamp,organisation,seedtext,request_type,refusal_code,refusal_message) VALUES (?,?,?,?,?,?)"
    args = (timestamp,org,seedText,request_type,refusal_code,refusal_message)

    try:
        con = get_db()
        cur = con.cursor()
        cur.execute(query, args)
        con.commit()

    except Error as error:
        print(error)

    finally:
        cur.close()
        con.close()

def add_other_db(timestamp,seedText,request_type):
    query = "INSERT INTO mottos (timestamp,seedtext,request_type) VALUES (?,?,?)"
    args = (timestamp,seedText,request_type)

    try:
        con = get_db()
        cur = con.cursor()
        cur.execute(query, args)
        con.commit()

    except Error as error:
        print(error)

    finally:
        cur.close()
        con.close()

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Queer API</h1>
<p>A prototype API.</p>'''


@app.route('/queermottoAPI/r1/refusal', methods=['GET'])
def api_args():
    moment = datetime.datetime.now(tz)
    timestamp = moment.__str__()
    rqstr = str(request.args['rq'])
    if rqstr == "all_log":
        all_slogans = query_db('SELECT * FROM mottos;')
        moment = datetime.datetime.now(tz)
        timestamp = moment.__str__()
        request_type = 'all_log request'
        add_other_db(timestamp,seedText,request_type)
        with counter.get_lock():
            counter.value += 1
        return jsonify(all_slogans)

    if rqstr == "motto_log":
        success_slogans = query_db('SELECT generated_motto,timestamp,organisation,seedtext FROM mottos WHERE generated_motto IS NOT NULL AND generated_motto!="";')
        moment = datetime.datetime.now(tz)
        request_type = 'motto_log request'
        add_other_db(timestamp,seedText,request_type)
        with counter.get_lock():
            counter.value += 1
        timestamp = moment.__str__()
        return jsonify(success_slogans)

    if 'org' in request.args:
        orgVal = str(request.args['org'])
        orgVal = bytes(orgVal, encoding='utf-8')
        if (rqstr == "generate" and orgVal == f1.decrypt(secrettoken1)) or (rqstr == "generate" and orgVal == f2.decrypt(secrettoken2)):
            if orgVal == f1.decrypt(secrettoken1):
                org = "transmediale"
            elif orgVal == f2.decrypt(secrettoken2):
                org = "test"
            # Generate the motto
            api_phrase_str = ''
            for i in range(len(seedTextList)):
                # Current word in the seed phrase
                current = seedTextList[i]
                # Going through the letters in the above word
                api_phrase = []
                for y in range(len(current)):
                    testKey = str(y) + current[y]
                    # print(current[y],random.choice(toChooseFrom[testKey]))
                    api_phrase.append(random.choice(toChooseFrom[testKey]))
                api_phrase[0] = api_phrase[0].capitalize()
                api_phrase_str_word = ' '.join(api_phrase)
                api_phrase_str = api_phrase_str + '\\n' + api_phrase_str_word
                api_phrase_str_word = ''
            api_phrase_str = api_phrase_str[2:]

            request_type = 'generate request'

            # Check if one of the words has been refused
            for elem in refWords:
                if elem in api_phrase_str:
                    refusal_code = 400
                    refusal_message = build_error_one()
                    add_error_db(timestamp,org,seedText,request_type,refusal_code,refusal_message)
                    with counter.get_lock():
                        counter.value += 1
                    return jsonify(refusal_message)

            # Check the date
            moment = datetime.datetime.now(tz)
            if (moment.month==3 and moment.day==9) or (moment.month==5 and moment.day==1) or (moment.month==7 and moment.day==20):
                refusal_code = 402
                refusal_message = build_error_three()
                add_error_db(timestamp,org,seedText,request_type,refusal_code,refusal_message)
                with counter.get_lock():
                    counter.value += 1
                return jsonify(refusal_message)

            # Check if the counter is smaller than 10
            out = counter.value
            if out < 10:
                with counter.get_lock():
                    counter.value += 1
                    out = counter.value
                add_db(api_phrase_str,timestamp,org,seedText,request_type)
                return jsonify(api_phrase_str)
            else:
                with counter.get_lock():
                    counter.value = 0
                refusal_code = 402
                refusal_message = build_error_three()
                add_error_db(timestamp,org,seedText,request_type,refusal_code,refusal_message)
                return jsonify(refusal_message)
    else:
        moment = datetime.datetime.now(tz)
        timestamp = moment.__str__()
        refusal_code = 401
        refusal_message = build_error_two()
        org = 'someone'
        request_type = 'unknown request'
        out = counter.value
        if out < 10:
            with counter.get_lock():
                counter.value += 1
                out = counter.value
            add_error_db(timestamp,org,seedText,request_type,refusal_code,refusal_message)
            return jsonify(refusal_message)
        else:
            with counter.get_lock():
                counter.value = 0
            refusal_code = 402
            refusal_message = build_error_three()
            add_error_db(timestamp,org,seedText,request_type,refusal_code,refusal_message)
            return jsonify(refusal_message)


@app.errorhandler(400)
def error_fourzerozero(e):
    moment = datetime.datetime.now(tz)
    timestamp = moment.__str__()
    refusal_code = 401
    refusal_message = build_error_two()
    org = 'someone'
    request_type = 'unknown request'
    out = counter.value
    if out < 10:
        with counter.get_lock():
            counter.value += 1
        add_error_db(timestamp,org,seedText,request_type,refusal_code,refusal_message)
        return jsonify(refusal_message)
    else:
        with counter.get_lock():
            counter.value = 0
        refusal_code = 402
        refusal_message = build_error_three()
        add_error_db(timestamp,org,seedText,request_type,refusal_code,refusal_message)
        return jsonify(refusal_message)

@app.errorhandler(404)
def error_fourzerofour(e):
    moment = datetime.datetime.now(tz)
    timestamp = moment.__str__()
    refusal_code = 401
    refusal_message = build_error_two()
    org = 'someone'
    request_type = 'unknown request'
    out = counter.value
    if out < 10:
        with counter.get_lock():
            counter.value += 1
        add_error_db(timestamp,org,seedText,request_type,refusal_code,refusal_message)
        return jsonify(refusal_message)
    else:
        with counter.get_lock():
            counter.value = 0
        refusal_code = 402
        refusal_message = build_error_three()
        add_error_db(timestamp,org,seedText,request_type,refusal_code,refusal_message)
        return jsonify(refusal_message)

@app.errorhandler(500)
def error_fivezerozero(e):
    moment = datetime.datetime.now(tz)
    timestamp = moment.__str__()
    refusal_code = 401
    refusal_message = build_error_two()
    org = 'someone'
    request_type = 'unknown request'
    out = counter.value
    if out < 10:
        with counter.get_lock():
            counter.value += 1
        add_error_db(timestamp,org,seedText,request_type,refusal_code,refusal_message)
        return jsonify(refusal_message)
    else:
        with counter.get_lock():
            counter.value = 0
        refusal_code = 402
        refusal_message = build_error_three()
        add_error_db(timestamp,org,seedText,request_type,refusal_code,refusal_message)
        return jsonify(refusal_message)

# app.run()
