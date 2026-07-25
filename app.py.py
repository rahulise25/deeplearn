import streamlit as st
import streamlit.components.v1 as components
import json, sys, os

st.set_page_config(page_title="DeepLearn", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""<style>
#MainMenu,footer,header{visibility:hidden}
.block-container{padding:0!important;max-width:100%!important}
</style>""", unsafe_allow_html=True)

sys.path.insert(0, os.path.dirname(__file__))
from media_data import VIDEO_B64, VTT_B64, HI_CUES
hi_cues_json = json.dumps(HI_CUES, ensure_ascii=False)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>DeepLearn</title>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Syne:wght@700;800&display=swap" rel="stylesheet"/>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'DM Sans',sans-serif;background:#f8fafc;color:#0f172a}}
h1,h2,h3,h4{{font-family:'Syne',sans-serif}}
.page{{display:none}}
.page.active{{display:block}}

/* Buttons */
.btn{{border:none;border-radius:10px;padding:10px 20px;font-weight:600;cursor:pointer;font-family:'DM Sans',sans-serif;font-size:14px;transition:all .15s;display:inline-flex;align-items:center;gap:6px}}
.btn-primary{{background:#0ea5e9;color:#fff}}.btn-primary:hover{{background:#0284c7;transform:translateY(-1px)}}
.btn-green{{background:#16a34a;color:#fff}}.btn-green:hover{{background:#15803d}}
.btn-ghost{{background:transparent;color:#475569;border:1px solid #e2e8f0}}.btn-ghost:hover{{background:#f1f5f9}}
.btn-white{{background:#fff;color:#0c4a6e;font-weight:700}}.btn-white:hover{{background:#f0f9ff}}
.btn-sm{{padding:7px 14px;font-size:13px;border-radius:8px}}

/* Cards */
.card{{background:#fff;border:1px solid #e2e8f0;border-radius:16px;box-shadow:0 1px 4px rgba(0,0,0,0.05)}}
.course-card{{background:#fff;border:1px solid #e2e8f0;border-radius:16px;overflow:hidden;transition:all .2s;cursor:pointer}}
.course-card:hover{{box-shadow:0 8px 24px rgba(0,0,0,0.10);transform:translateY(-3px)}}

/* Inputs */
input,textarea,select{{font-family:'DM Sans',sans-serif;border:1px solid #e2e8f0;border-radius:10px;padding:10px 14px;width:100%;outline:none;font-size:14px;transition:border .15s;background:#fff}}
input:focus,textarea:focus{{border-color:#0ea5e9;box-shadow:0 0 0 3px rgba(14,165,233,0.12)}}

/* Nav */
.nav-link{{font-size:14px;font-weight:500;color:#475569;cursor:pointer;padding:6px 12px;border-radius:8px;transition:all .15s;border:none;background:transparent}}
.nav-link:hover,.nav-link.active{{color:#0ea5e9;background:#f0f9ff}}

/* Sidebar */
.sidebar-item{{display:flex;align-items:center;gap:10px;padding:10px 14px;border-radius:10px;cursor:pointer;font-weight:500;font-size:14px;color:#475569;transition:all .15s;border:none;background:transparent;width:100%;text-align:left}}
.sidebar-item:hover{{background:#f1f5f9;color:#0f172a}}
.sidebar-item.active{{background:#e0f2fe;color:#0284c7;font-weight:600}}

/* Misc */
.badge{{display:inline-block;padding:3px 10px;border-radius:20px;font-size:12px;font-weight:600}}
.badge-blue{{background:#e0f2fe;color:#0369a1}}
.badge-green{{background:#dcfce7;color:#15803d}}
.badge-purple{{background:#ede9fe;color:#6d28d9}}
.progress-bar{{height:6px;background:#e2e8f0;border-radius:3px;overflow:hidden}}
.progress-fill{{height:100%;background:linear-gradient(90deg,#0ea5e9,#38bdf8);border-radius:3px;transition:width .4s}}
.field-label{{font-size:13px;font-weight:600;color:#475569;margin-bottom:5px;display:block}}
.alert{{padding:11px 15px;border-radius:9px;font-size:13px;margin-bottom:12px}}
.alert-red{{background:#fee2e2;color:#991b1b;border:1px solid #fecaca}}
.alert-green{{background:#dcfce7;color:#166534;border:1px solid #bbf7d0}}
.tab-btn{{padding:8px 18px;border-radius:8px;cursor:pointer;font-weight:600;font-size:14px;border:none;background:transparent;color:#64748b;transition:all .15s;font-family:'DM Sans',sans-serif}}
.tab-btn.active{{background:#0ea5e9;color:#fff}}
.doc-card{{display:flex;align-items:center;gap:12px;padding:14px;border:1px solid #e2e8f0;border-radius:12px;background:#fff;cursor:pointer;transition:all .15s}}
.doc-card:hover{{border-color:#0ea5e9;background:#f0f9ff;transform:translateX(3px)}}
.msg-student{{background:#dbeafe;border-radius:12px 12px 4px 12px;padding:10px 14px;max-width:78%;margin-left:auto;font-size:14px;line-height:1.5}}
.msg-teacher{{background:#f1f5f9;border-radius:12px 12px 12px 4px;padding:10px 14px;max-width:78%;font-size:14px;line-height:1.5}}
.subtitle-overlay{{position:absolute;bottom:56px;left:50%;transform:translateX(-50%);background:rgba(0,0,0,0.78);color:#fff;padding:8px 20px;border-radius:8px;font-size:15px;max-width:82%;text-align:center;pointer-events:none;white-space:normal}}
.dubbed{{background:linear-gradient(135deg,rgba(139,92,246,.9),rgba(99,102,241,.9));animation:pulseGlow 1.5s infinite}}
@keyframes pulseGlow{{0%,100%{{box-shadow:0 0 10px rgba(139,92,246,.7)}}50%{{box-shadow:0 0 25px rgba(139,92,246,.9)}}}}.hero-bg{{background:linear-gradient(135deg,#0c4a6e 0%,#0369a1 50%,#0ea5e9 100%)}}
.search-bar{{display:flex;align-items:center;background:#fff;border-radius:12px;padding:6px 8px 6px 16px;box-shadow:0 4px 20px rgba(0,0,0,0.12);max-width:540px;width:100%}}
.search-bar input{{border:none;box-shadow:none;padding:8px 4px;font-size:15px;background:transparent}}
.search-bar input:focus{{box-shadow:none;border:none}}
.stat-num{{font-size:28px;font-weight:800;font-family:'Syne',sans-serif}}
</style>
</head>
<body>

<script>
// ═══════════════════════════ DATA STORE ═══════════════════════════
const DB = {{
  users:[
    {{id:'t1',role:'teacher',name:'Dr. Priya Sharma',email:'teacher@demo.com',password:'demo123',subject:'Python & NLP',cert:'certificate.pdf',verified:true}},
    {{id:'s1',role:'student',name:'Rahul Kumar',email:'student@demo.com',password:'demo123',teacherId:'t1'}}
  ],
  questions:[
    {{id:'q1',studentId:'s1',teacherId:'t1',question:'What is tokenization in NLP?',answer:'Tokenization splits text into smaller units called tokens — like words or subwords. It is the first step in most NLP pipelines.',ts:Date.now()-86400000}},
    {{id:'q2',studentId:'s1',teacherId:'t1',question:'How do I use for loops in Python?',answer:null,ts:Date.now()-3600000}}
  ]
}};

const COURSES = [
  {{id:'c1',title:'Python Crash Course',teacher:'Dr. Priya Sharma',teacherId:'t1',category:'Programming',level:'Beginner',duration:'9 min',students:1240,rating:4.8,progress:65,thumb:'https://images.unsplash.com/photo-1526379095098-d400fd0bf935?w=400',desc:'Master Python from scratch — variables, loops, functions, classes and more. Taught in Hindi with subtitles.',tags:['Python','Programming','Beginner']}},
  {{id:'c2',title:'NLP Fundamentals',teacher:'Dr. Priya Sharma',teacherId:'t1',category:'AI & NLP',level:'Intermediate',duration:'6 hr',students:980,rating:4.7,progress:0,thumb:'https://images.unsplash.com/photo-1677442135703-1787eea5ce01?w=400',desc:'Deep dive into Natural Language Processing — tokenization, embeddings, transformers and real-world applications.',tags:['NLP','AI','Python']}},
  {{id:'c3',title:'Deep Learning for NLP',teacher:'Dr. Priya Sharma',teacherId:'t1',category:'AI & NLP',level:'Advanced',duration:'8 hr',students:670,rating:4.9,progress:0,thumb:'https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=400',desc:'Build neural networks for text classification, sentiment analysis and sequence modelling using PyTorch.',tags:['Deep Learning','NLP','PyTorch']}},
  {{id:'c4',title:'Transformers & BERT',teacher:'Dr. Priya Sharma',teacherId:'t1',category:'AI & NLP',level:'Advanced',duration:'5 hr',students:540,rating:4.8,progress:0,thumb:'https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?w=400',desc:'Understand the transformer architecture from attention mechanisms to fine-tuning BERT for downstream tasks.',tags:['Transformers','BERT','NLP']}},
  {{id:'c5',title:'Speech Recognition',teacher:'Dr. Priya Sharma',teacherId:'t1',category:'AI & NLP',level:'Intermediate',duration:'5 hr',students:420,rating:4.6,progress:0,thumb:'https://images.unsplash.com/photo-1588196749597-9ff075ee6b5b?w=400',desc:'Build speech-to-text systems using deep learning and the Whisper model.',tags:['Speech','Audio','AI']}},
  {{id:'c6',title:'Data Structures in Python',teacher:'Dr. Priya Sharma',teacherId:'t1',category:'Programming',level:'Beginner',duration:'4 hr',students:1890,rating:4.7,progress:0,thumb:'https://images.unsplash.com/photo-1515879218367-8466d910aaa4?w=400',desc:'Master lists, tuples, dictionaries, sets, stacks and queues with hands-on Python examples.',tags:['Python','Data Structures','Beginner']}}
];

const DOCS=[
  {{name:'Assignment 1 – Python Basics.pdf',type:'assignment',icon:'📄',size:'245 KB'}},
  {{name:'Notes – Variables & Data Types.pdf',type:'notes',icon:'📝',size:'180 KB'}},
  {{name:'Assignment 2 – NLP Tokenization.pdf',type:'assignment',icon:'📄',size:'312 KB'}},
  {{name:'Cheatsheet – Python Syntax.pdf',type:'notes',icon:'📝',size:'98 KB'}},
  {{name:'Project Brief – Sentiment Analysis.pdf',type:'assignment',icon:'📄',size:'420 KB'}},
];

const VIDEO_SRC  = "data:video/mp4;base64,{VIDEO_B64}";
const HI_EN_CUES = [{{"start": 0.0, "end": 4.0, "hi": "नमस्ते और स्वागत है मेरे Python crash course में।", "en": "Hello and welcome to my Python crash course."}}, {{"start": 4.0, "end": 9.0, "hi": "इस tutorial में हम syntax, variables और data types सीखेंगे।", "en": "In this tutorial we'll learn syntax, variables and data types."}}, {{"start": 9.0, "end": 13.0, "hi": "हम numbers, strings, boolean values और operators भी देखेंगे।", "en": "We'll also see numbers, strings, boolean values and operators."}}, {{"start": 13.0, "end": 18.0, "hi": "साथ ही हम loops, functions, classes और objects समझेंगे।", "en": "We'll also understand loops, functions, classes and objects."}}, {{"start": 18.0, "end": 24.0, "hi": "अगर ये सब अभी confusing लग रहा है, तो पूरा tutorial देखें।", "en": "If this seems confusing right now, watch the full tutorial."}}, {{"start": 24.0, "end": 36.0, "hi": "अंत तक आपको इन सभी concepts की अच्छी understanding हो जाएगी।", "en": "By the end you'll have a good understanding of all these concepts."}}, {{"start": 36.0, "end": 49.0, "hi": "चलिए शुरुआत करते हैं और सबसे पहले comments को समझते हैं।", "en": "Let's begin — first let's understand comments."}}, {{"start": 49.0, "end": 56.0, "hi": "comments का उपयोग Python code को explain करने के लिए होता है।", "en": "Comments are used to explain Python code."}}, {{"start": 56.0, "end": 62.0, "hi": "comment हमेशा # से शुरू होता है और Python इसे ignore करता है।", "en": "A comment always starts with # and Python ignores it."}}, {{"start": 62.0, "end": 68.0, "hi": "आप comments को line की शुरुआत या end में लिख सकते हैं।", "en": "You can write comments at the start or end of a line."}}, {{"start": 68.0, "end": 80.0, "hi": "multiple lines के लिए triple quotes का उपयोग किया जा सकता है।", "en": "Triple quotes can be used for multiple lines."}}, {{"start": 80.0, "end": 88.0, "hi": "अब variables को देखते हैं।", "en": "Now let's look at variables."}}, {{"start": 88.0, "end": 96.0, "hi": "variable तब बनता है जब आप उसे value assign करते हैं।", "en": "A variable is created when you assign a value to it."}}, {{"start": 96.0, "end": 104.0, "hi": "example: x = 10, जहाँ x variable है।", "en": "Example: x = 10, where x is the variable."}}, {{"start": 104.0, "end": 112.0, "hi": "print(x) करने पर output 10 मिलेगा।", "en": "Running print(x) will give output 10."}}, {{"start": 112.0, "end": 122.0, "hi": "variables में number या string जैसे data store कर सकते हैं।", "en": "Variables can store data like numbers or strings."}}, {{"start": 122.0, "end": 132.0, "hi": "type casting के लिए string(), int() और float() का उपयोग होता है।", "en": "For type casting, use str(), int() and float()."}}, {{"start": 132.0, "end": 143.0, "hi": "strings single या double quotes में लिखी जाती हैं।", "en": "Strings are written in single or double quotes."}}, {{"start": 143.0, "end": 150.0, "hi": "variable names case-sensitive होते हैं।", "en": "Variable names are case-sensitive."}}, {{"start": 150.0, "end": 162.0, "hi": "अब data types जैसे str, int, float, list, tuple और bool देखते हैं।", "en": "Now let's see data types like str, int, float, list, tuple and bool."}}, {{"start": 162.0, "end": 170.0, "hi": "type() function से data type पता किया जा सकता है।", "en": "The type() function tells us the data type."}}, {{"start": 170.0, "end": 184.0, "hi": "int whole numbers होते हैं और float decimal numbers होते हैं।", "en": "int are whole numbers and float are decimal numbers."}}, {{"start": 184.0, "end": 197.0, "hi": "strings text होती हैं और quotes में लिखी जाती हैं।", "en": "Strings are text and are written inside quotes."}}, {{"start": 197.0, "end": 207.0, "hi": "len() function से string की length मिलती है।", "en": "The len() function gives the length of a string."}}, {{"start": 207.0, "end": 218.0, "hi": "boolean values True और False होती हैं।", "en": "Boolean values are True and False."}}, {{"start": 218.0, "end": 228.0, "hi": "comparisons जैसे 10 > 9 True return करते हैं।", "en": "Comparisons like 10 > 9 return True."}}, {{"start": 228.0, "end": 243.0, "hi": "if statement condition check करता है।", "en": "The if statement checks a condition."}}, {{"start": 243.0, "end": 256.0, "hi": "bool() function से values evaluate होती हैं।", "en": "The bool() function evaluates values."}}, {{"start": 256.0, "end": 269.0, "hi": "empty values, 0 और None False होते हैं।", "en": "Empty values, 0 and None are False."}}, {{"start": 269.0, "end": 288.0, "hi": "operators जैसे +, -, *, % और assignment operators उपयोग होते हैं।", "en": "Operators like +, -, *, % and assignment operators are used."}}, {{"start": 288.0, "end": 310.0, "hi": "lists multiple items store करती हैं और [] में लिखी जाती हैं।", "en": "Lists store multiple items and are written in []."}}, {{"start": 310.0, "end": 328.0, "hi": "list ordered होती है और duplicate values allow करती है।", "en": "A list is ordered and allows duplicate values."}}, {{"start": 328.0, "end": 346.0, "hi": "tuple immutable होता है और () में लिखा जाता है।", "en": "A tuple is immutable and is written in ()."}}, {{"start": 346.0, "end": 362.0, "hi": "set unordered होता है और duplicates allow नहीं करता।", "en": "A set is unordered and does not allow duplicates."}}, {{"start": 362.0, "end": 378.0, "hi": "dictionary key-value pairs store करता है।", "en": "A dictionary stores key-value pairs."}}, {{"start": 378.0, "end": 395.0, "hi": "if, elif और else conditions के लिए उपयोग होते हैं।", "en": "if, elif and else are used for conditions."}}, {{"start": 395.0, "end": 410.0, "hi": "Python indentation पर depend करता है।", "en": "Python depends on indentation."}}, {{"start": 410.0, "end": 430.0, "hi": "while loop तब तक चलता है जब तक condition True हो।", "en": "A while loop runs as long as the condition is True."}}, {{"start": 430.0, "end": 445.0, "hi": "for loop sequence पर iterate करता है।", "en": "A for loop iterates over a sequence."}}, {{"start": 445.0, "end": 465.0, "hi": "break loop को रोकता है और continue next iteration पर जाता है।", "en": "break stops the loop and continue goes to the next iteration."}}, {{"start": 465.0, "end": 485.0, "hi": "functions def keyword से define होती हैं।", "en": "Functions are defined using the def keyword."}}, {{"start": 485.0, "end": 505.0, "hi": "arguments functions को data देने के लिए उपयोग होते हैं।", "en": "Arguments are used to pass data to functions."}}, {{"start": 505.0, "end": 525.0, "hi": "Python object-oriented language है और class व object का उपयोग होता है।", "en": "Python is an object-oriented language and uses class and object."}}, {{"start": 525.0, "end": 545.0, "hi": "class एक blueprint होता है और object उसका instance होता है।", "en": "A class is a blueprint and an object is its instance."}}, {{"start": 545.0, "end": 568.0, "hi": "धन्यवाद, अगली वीडियो में मिलते हैं।", "en": "Thank you, see you in the next video."}}];
const KN_EN_CUES = [{{"start": 0.0, "end": 4.0, "kn": "ನಮಸ್ಕಾರ ಮತ್ತು ನನ್ನ Python crash course ಗೆ ಸ್ವಾಗತ.", "en": "Hello and welcome to my Python crash course."}}, {{"start": 4.0, "end": 9.0, "kn": "ಈ tutorial ನಲ್ಲಿ ನಾವು syntax, variables ಮತ್ತು data types ಕಲಿಯುತ್ತೇವೆ.", "en": "In this tutorial we'll learn syntax, variables and data types."}}, {{"start": 9.0, "end": 13.0, "kn": "ನಾವು numbers, strings, boolean values ಮತ್ತು operators ಕೂಡ ನೋಡುತ್ತೇವೆ.", "en": "We'll also see numbers, strings, boolean values and operators."}}, {{"start": 13.0, "end": 18.0, "kn": "loops, functions, classes ಮತ್ತು objects ಅನ್ನು ಸಹ ಅರ್ಥಮಾಡಿಕೊಳ್ಳುತ್ತೇವೆ.", "en": "We'll also understand loops, functions, classes and objects."}}, {{"start": 18.0, "end": 24.0, "kn": "ಇದೆಲ್ಲಾ ಈಗ confusing ಅನ್ನಿಸಿದರೆ, ಪೂರ್ಣ tutorial ನೋಡಿ.", "en": "If this seems confusing right now, watch the full tutorial."}}, {{"start": 24.0, "end": 36.0, "kn": "ಕೊನೆಯವರೆಗೆ ಎಲ್ಲ concepts ಚೆನ್ನಾಗಿ ಅರ್ಥವಾಗುತ್ತದೆ.", "en": "By the end you'll have a good understanding of all these concepts."}}, {{"start": 36.0, "end": 49.0, "kn": "ಪ್ರಾರಂಭಿಸೋಣ — ಮೊದಲು comments ಅರ್ಥಮಾಡಿಕೊಳ್ಳೋಣ.", "en": "Let's begin — first let's understand comments."}}, {{"start": 49.0, "end": 56.0, "kn": "Python code ವಿವರಿಸಲು comments ಉಪಯೋಗಿಸಲಾಗುತ್ತದೆ.", "en": "Comments are used to explain Python code."}}, {{"start": 56.0, "end": 62.0, "kn": "comment ಯಾವಾಗಲೂ # ನಿಂದ ಪ್ರಾರಂಭವಾಗುತ್ತದೆ ಮತ್ತು Python ಅದನ್ನು ignore ಮಾಡುತ್ತದೆ.", "en": "A comment always starts with # and Python ignores it."}}, {{"start": 62.0, "end": 68.0, "kn": "ಸಾಲಿನ ಆರಂಭ ಅಥವಾ ಅಂತ್ಯದಲ್ಲಿ comments ಬರೆಯಬಹುದು.", "en": "You can write comments at the start or end of a line."}}, {{"start": 68.0, "end": 80.0, "kn": "ಅನೇಕ ಸಾಲುಗಳಿಗೆ triple quotes ಉಪಯೋಗಿಸಬಹುದು.", "en": "Triple quotes can be used for multiple lines."}}, {{"start": 80.0, "end": 88.0, "kn": "ಈಗ variables ನೋಡೋಣ.", "en": "Now let's look at variables."}}, {{"start": 88.0, "end": 96.0, "kn": "value assign ಮಾಡಿದಾಗ variable ರಚನೆಯಾಗುತ್ತದೆ.", "en": "A variable is created when you assign a value to it."}}, {{"start": 96.0, "end": 104.0, "kn": "ಉದಾಹರಣೆ: x = 10, ಇಲ್ಲಿ x variable ಆಗಿದೆ.", "en": "Example: x = 10, where x is the variable."}}, {{"start": 104.0, "end": 112.0, "kn": "print(x) ಚಲಾಯಿಸಿದರೆ output 10 ಸಿಗುತ್ತದೆ.", "en": "Running print(x) will give output 10."}}, {{"start": 112.0, "end": 122.0, "kn": "Variables ನಲ್ಲಿ numbers ಅಥವಾ strings ಇಡಬಹುದು.", "en": "Variables can store data like numbers or strings."}}, {{"start": 122.0, "end": 132.0, "kn": "Type casting ಗೆ str(), int() ಮತ್ತು float() ಬಳಸಲಾಗುತ್ತದೆ.", "en": "For type casting, use str(), int() and float()."}}, {{"start": 132.0, "end": 143.0, "kn": "Strings single ಅಥವಾ double quotes ನಲ್ಲಿ ಬರೆಯಲಾಗುತ್ತದೆ.", "en": "Strings are written in single or double quotes."}}, {{"start": 143.0, "end": 150.0, "kn": "Variable names case-sensitive ಆಗಿರುತ್ತವೆ.", "en": "Variable names are case-sensitive."}}, {{"start": 150.0, "end": 162.0, "kn": "str, int, float, list, tuple ಮತ್ತು bool data types ನೋಡೋಣ.", "en": "Now let's see data types like str, int, float, list, tuple and bool."}}, {{"start": 162.0, "end": 170.0, "kn": "type() function ದಿಂದ data type ತಿಳಿಯಬಹುದು.", "en": "The type() function tells us the data type."}}, {{"start": 170.0, "end": 184.0, "kn": "int ಪೂರ್ಣ ಸಂಖ್ಯೆಗಳು ಮತ್ತು float ದಶಮಾಂಶ ಸಂಖ್ಯೆಗಳು.", "en": "int are whole numbers and float are decimal numbers."}}, {{"start": 184.0, "end": 197.0, "kn": "Strings ಪಠ್ಯವಾಗಿದ್ದು quotes ನಲ್ಲಿ ಬರೆಯಲಾಗುತ್ತದೆ.", "en": "Strings are text and are written inside quotes."}}, {{"start": 197.0, "end": 207.0, "kn": "len() function string ನ length ಕೊಡುತ್ತದೆ.", "en": "The len() function gives the length of a string."}}, {{"start": 207.0, "end": 218.0, "kn": "Boolean values True ಮತ್ತು False ಆಗಿರುತ್ತವೆ.", "en": "Boolean values are True and False."}}, {{"start": 218.0, "end": 228.0, "kn": "10 > 9 ನಂತಹ comparisons True return ಮಾಡುತ್ತವೆ.", "en": "Comparisons like 10 > 9 return True."}}, {{"start": 228.0, "end": 243.0, "kn": "if statement condition ಪರಿಶೀಲಿಸುತ್ತದೆ.", "en": "The if statement checks a condition."}}, {{"start": 243.0, "end": 256.0, "kn": "bool() function values evaluate ಮಾಡುತ್ತದೆ.", "en": "The bool() function evaluates values."}}, {{"start": 256.0, "end": 269.0, "kn": "Empty values, 0 ಮತ್ತು None False ಆಗಿರುತ್ತವೆ.", "en": "Empty values, 0 and None are False."}}, {{"start": 269.0, "end": 288.0, "kn": "+, -, *, % ನಂತಹ operators ಮತ್ತು assignment operators ಬಳಸಲಾಗುತ್ತದೆ.", "en": "Operators like +, -, *, % and assignment operators are used."}}, {{"start": 288.0, "end": 310.0, "kn": "Lists [] ನಲ್ಲಿ ಬರೆಯಲಾಗುತ್ತದೆ ಮತ್ತು ಅನೇಕ items store ಮಾಡುತ್ತದೆ.", "en": "Lists store multiple items and are written in []."}}, {{"start": 310.0, "end": 328.0, "kn": "List ordered ಆಗಿದ್ದು duplicate values allow ಮಾಡುತ್ತದೆ.", "en": "A list is ordered and allows duplicate values."}}, {{"start": 328.0, "end": 346.0, "kn": "Tuple immutable ಆಗಿದ್ದು () ನಲ್ಲಿ ಬರೆಯಲಾಗುತ್ತದೆ.", "en": "A tuple is immutable and is written in ()."}}, {{"start": 346.0, "end": 362.0, "kn": "Set unordered ಆಗಿದ್ದು duplicates allow ಮಾಡುವುದಿಲ್ಲ.", "en": "A set is unordered and does not allow duplicates."}}, {{"start": 362.0, "end": 378.0, "kn": "Dictionary key-value pairs store ಮಾಡುತ್ತದೆ.", "en": "A dictionary stores key-value pairs."}}, {{"start": 378.0, "end": 395.0, "kn": "if, elif ಮತ್ತು else conditions ಗೆ ಬಳಸಲಾಗುತ್ತದೆ.", "en": "if, elif and else are used for conditions."}}, {{"start": 395.0, "end": 410.0, "kn": "Python indentation ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿದೆ.", "en": "Python depends on indentation."}}, {{"start": 410.0, "end": 430.0, "kn": "while loop condition True ಇರುವವರೆಗೆ ಚಲಿಸುತ್ತದೆ.", "en": "A while loop runs as long as the condition is True."}}, {{"start": 430.0, "end": 445.0, "kn": "for loop sequence ಮೇಲೆ iterate ಮಾಡುತ್ತದೆ.", "en": "A for loop iterates over a sequence."}}, {{"start": 445.0, "end": 465.0, "kn": "break loop ನಿಲ್ಲಿಸುತ್ತದೆ ಮತ್ತು continue ಮುಂದಿನ iteration ಗೆ ಹೋಗುತ್ತದೆ.", "en": "break stops the loop and continue goes to the next iteration."}}, {{"start": 465.0, "end": 485.0, "kn": "Functions def keyword ನಿಂದ define ಮಾಡಲಾಗುತ್ತದೆ.", "en": "Functions are defined using the def keyword."}}, {{"start": 485.0, "end": 505.0, "kn": "Arguments functions ಗೆ data ರವಾನಿಸಲು ಬಳಸಲಾಗುತ್ತದೆ.", "en": "Arguments are used to pass data to functions."}}, {{"start": 505.0, "end": 525.0, "kn": "Python object-oriented language ಆಗಿದ್ದು class ಮತ್ತು object ಬಳಸುತ್ತದೆ.", "en": "Python is an object-oriented language and uses class and object."}}, {{"start": 525.0, "end": 545.0, "kn": "Class ಒಂದು blueprint ಆಗಿದ್ದು object ಅದರ instance ಆಗಿದೆ.", "en": "A class is a blueprint and an object is its instance."}}, {{"start": 545.0, "end": 568.0, "kn": "ಧನ್ಯವಾದಗಳು, ಮುಂದಿನ video ನಲ್ಲಿ ಭೇಟಿಯಾಗೋಣ.", "en": "Thank you, see you in the next video."}}];
let subtitleLang = 'hi'; // 'hi' = Hindi+English, 'kn' = Kannada+English

let currentUser = null;
let currentCourse = null;
let videoEl = null, dubbingOn = false, lastSpokenKey = null, availableVoices = [], speechOk = true;
let searchQuery = '';

// ═══════════════════════════ UTILS ═══════════════════════════
function uid(){{ return '_'+Math.random().toString(36).substr(2,9); }}
function setPage(id){{
  document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));
  const pg=document.getElementById(id);
  if(pg) pg.classList.add('active');
}}
function render(id,html){{ const el=document.getElementById(id); if(el) el.innerHTML=html; }}

// ═══════════════════════════ NAVBAR ═══════════════════════════
function updateNavbar(){{
  const authBtns = document.getElementById('nav-auth-btns');
  const userMenu = document.getElementById('nav-user-menu');
  const userName = document.getElementById('nav-user-name');
  if(currentUser){{
    authBtns.style.display='none'; userMenu.style.display='flex';
    userName.textContent = currentUser.name.split(' ')[0];
  }} else {{
    authBtns.style.display='flex'; userMenu.style.display='none';
  }}
}}

function goHome(){{
  setPage('page-home');
  renderCourseGrid(COURSES);
}}

function navDashboard(){{
  if(!currentUser){{ setPage('page-auth'); return; }}
  if(currentUser.role==='student') loadStudentDashboard();
  else loadTeacherDashboard();
}}

function logout(){{
  currentUser=null; stopDubbing();
  updateNavbar(); setPage('page-home');
}}

// ═══════════════════════════ SEARCH ═══════════════════════════
function doSearch(){{
  const q = document.getElementById('hero-search').value.trim().toLowerCase();
  searchQuery = q;
  const filtered = q ? COURSES.filter(c=>
    c.title.toLowerCase().includes(q)||
    c.category.toLowerCase().includes(q)||
    c.level.toLowerCase().includes(q)||
    c.tags.some(t=>t.toLowerCase().includes(q))
  ) : COURSES;
  setPage('page-home');
  renderCourseGrid(filtered);
  document.getElementById('browse-heading').textContent = q ? `Results for "${{q}}"` : 'All Courses';
  document.getElementById('home-search-bar').value = q;
}}

function filterCategory(cat){{
  document.querySelectorAll('.cat-btn').forEach(b=>b.classList.remove('active-cat'));
  event.target.classList.add('active-cat');
  const filtered = cat==='All' ? COURSES : COURSES.filter(c=>c.category===cat);
  renderCourseGrid(filtered);
  document.getElementById('browse-heading').textContent = cat==='All' ? 'All Courses' : cat;
}}

// ═══════════════════════════ HOME PAGE ═══════════════════════════
function renderCourseGrid(courses){{
  const grid = document.getElementById('course-grid');
  if(!grid) return;
  if(courses.length===0){{
    grid.innerHTML='<div style="grid-column:1/-1;text-align:center;padding:60px;color:#94a3b8"><div style="font-size:48px">🔍</div><p style="margin-top:12px;font-size:16px">No courses found. Try a different search.</p></div>';
    return;
  }}
  grid.innerHTML = courses.map(c=>`
    <div class="course-card" onclick="openCourseDetail('${{c.id}}')">
      <div style="position:relative">
        <img src="${{c.thumb}}" alt="${{c.title}}" style="width:100%;height:160px;object-fit:cover"/>
        <span class="badge badge-blue" style="position:absolute;top:10px;left:10px">${{c.level}}</span>
      </div>
      <div style="padding:16px">
        <div style="font-size:12px;color:#0ea5e9;font-weight:600;margin-bottom:6px">${{c.category}}</div>
        <h3 style="font-size:16px;font-weight:700;margin-bottom:6px;line-height:1.3">${{c.title}}</h3>
        <p style="font-size:13px;color:#64748b;margin-bottom:10px;line-height:1.4">${{c.desc.slice(0,80)}}...</p>
        <div style="font-size:12px;color:#94a3b8;margin-bottom:10px">👩‍🏫 ${{c.teacher}} &nbsp;·&nbsp; ⏱ ${{c.duration}}</div>
        <div style="display:flex;align-items:center;justify-content:space-between">
          <div style="display:flex;align-items:center;gap:4px;font-size:13px">
            <span style="color:#f59e0b">⭐</span>
            <strong>${{c.rating}}</strong>
            <span style="color:#94a3b8">(${{c.students.toLocaleString()}})</span>
          </div>
          ${{c.progress>0 ? `<span class="badge badge-green">${{c.progress}}% done</span>` : '<span style="font-size:12px;color:#0ea5e9;font-weight:600">Enroll →</span>'}}
        </div>
        ${{c.progress>0 ? `<div class="progress-bar" style="margin-top:10px"><div class="progress-fill" style="width:${{c.progress}}%"></div></div>` : ''}}
      </div>
    </div>
  `).join('');
}}

// ═══════════════════════════ COURSE DETAIL ═══════════════════════════
const COURSE_DESC = `This video introduces the fundamentals of Python programming in a clear and beginner-friendly manner. It covers the essential concepts required to build a strong foundation, including Python syntax, variables, data types, input and output, operators, and basic programming principles. Whether you're a student, a beginner, or someone looking to refresh your Python knowledge, this lesson provides a solid starting point for your programming journey. The concepts explained here will prepare you for more advanced topics and practical Python applications in areas such as software development, data science, artificial intelligence, and automation.`;

// Reviews store keyed by courseId
const REVIEWS = {{
  c1: [
    {{id:'r1',user:'Anjali M.',rating:5,text:'Amazing course! Explained everything so clearly. The Hindi subtitles were super helpful.',ts:Date.now()-172800000}},
    {{id:'r2',user:'Karan S.',rating:4,text:'Very well structured for beginners. Would love more exercises.',ts:Date.now()-86400000}},
  ]
}};
let selectedStar = 0;

function pickStar(val){{
  selectedStar = val;
  document.querySelectorAll('.star-btn').forEach(s=>{{
    s.style.opacity = parseInt(s.dataset.val) <= val ? '1' : '0.25';
  }});
}}

function submitReview(){{
  const text = document.getElementById('review-text').value.trim();
  const err  = document.getElementById('review-err');
  err.style.display='none';
  if(!selectedStar){{ err.textContent='Please select a star rating.'; err.style.display='block'; return; }}
  if(!text){{ err.textContent='Please write something before submitting.'; err.style.display='block'; return; }}
  if(!REVIEWS[currentCourse.id]) REVIEWS[currentCourse.id]=[];
  REVIEWS[currentCourse.id].push({{id:uid(),user:currentUser.name,rating:selectedStar,text,ts:Date.now()}});
  document.getElementById('review-text').value='';
  selectedStar=0; pickStar(0);
  renderReviews();
}}

function renderReviews(){{
  const list = REVIEWS[currentCourse?.id]||[];
  const avg  = list.length ? (list.reduce((a,r)=>a+r.rating,0)/list.length).toFixed(1) : null;
  const avgEl = document.getElementById('detail-avg-rating');
  if(avgEl) avgEl.textContent = avg ? `${{avg}} / 5  (${{list.length}} review${{list.length!==1?'s':''}})` : 'No reviews yet';
  render('detail-reviews-list', list.length===0
    ? '<p style="font-size:13px;color:#94a3b8;text-align:center;padding:12px 0">No reviews yet. Be the first!</p>'
    : list.slice().reverse().map(r=>`
      <div style="border-bottom:1px solid #f1f5f9;padding:12px 0">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:5px">
          <div style="width:30px;height:30px;background:linear-gradient(135deg,#0ea5e9,#38bdf8);border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:12px;font-weight:700">${{r.user[0]}}</div>
          <div>
            <div style="font-size:13px;font-weight:600">${{r.user}}</div>
            <div style="font-size:11px;color:#94a3b8">${{new Date(r.ts).toLocaleDateString()}}</div>
          </div>
          <div style="margin-left:auto;font-size:13px">${{'⭐'.repeat(r.rating)}}</div>
        </div>
        <p style="font-size:13px;color:#475569;line-height:1.6;margin-left:38px">${{r.text}}</p>
      </div>`).join(''));
}}

function openCourseDetail(courseId){{
  currentCourse = COURSES.find(c=>c.id===courseId);
  if(!currentCourse) return;
  setPage('page-course-detail');
  render('detail-thumb-wrap',`<img src="${{currentCourse.thumb}}" alt="${{currentCourse.title}}" style="width:100%;height:220px;object-fit:cover;border-radius:14px"/>`);
  render('detail-title', currentCourse.title);
  render('detail-meta',`<span>👩‍🏫 ${{currentCourse.teacher}}</span> &nbsp;·&nbsp; <span>⭐ ${{currentCourse.rating}}</span> &nbsp;·&nbsp; <span>👨‍🎓 ${{currentCourse.students.toLocaleString()}} students</span> &nbsp;·&nbsp; <span>⏱ ${{currentCourse.duration}}</span>`);
  render('detail-level',`<span class="badge badge-blue">${{currentCourse.level}}</span> <span class="badge badge-purple" style="margin-left:6px">${{currentCourse.category}}</span>`);
  // Use long description for Python course, short desc for others
  render('detail-desc', currentCourse.id==='c1' ? COURSE_DESC : currentCourse.desc);
  render('detail-tags', currentCourse.tags.map(t=>`<span class="badge" style="background:#f1f5f9;color:#475569;margin-right:4px;margin-bottom:4px">#${{t}}</span>`).join(''));
  // Docs list (fixed — no template literal inside Python f-string)
  const docsHtml = DOCS.map(d=>`
    <div style="display:flex;align-items:center;gap:8px;font-size:13px;color:#475569;padding:6px 0;border-bottom:1px solid #f8fafc">
      <span>${{d.icon}}</span><span style="flex:1">${{d.name}}</span>
      <span class="badge ${{d.type==='assignment'?'badge-blue':'badge-green'}}" style="font-size:11px">${{d.type}}</span>
    </div>`).join('');
  render('detail-docs-list', docsHtml);
  // Reviews
  renderReviews();
  // Show/hide review form
  const form   = document.getElementById('detail-review-form');
  const prompt = document.getElementById('detail-login-to-review');
  if(currentUser && currentUser.role==='student'){{ form.style.display='block'; prompt.style.display='none'; }}
  else{{ form.style.display='none'; prompt.style.display='block'; }}
  // Watch button
  const watchBtn = document.getElementById('detail-watch-btn');
  watchBtn.onclick = ()=>{{
    if(!currentUser){{ setPage('page-auth'); document.getElementById('auth-redirect-note').style.display='block'; return; }}
    loadCoursePlayer();
  }};
}}

// ═══════════════════════════ AUTH ═══════════════════════════
function showAuthTab(tab){{
  document.querySelectorAll('.auth-tab').forEach(t=>t.classList.remove('active'));
  document.querySelectorAll('.auth-panel').forEach(p=>p.style.display='none');
  document.getElementById('authtab-'+tab).classList.add('active');
  document.getElementById('authpanel-'+tab).style.display='block';
}}

function showLoginRole(role){{
  document.querySelectorAll('.role-btn').forEach(b=>{{ b.style.background='#f1f5f9'; b.style.color='#475569'; }});
  const btn=document.getElementById('rolebtn-'+role);
  btn.style.background='#0ea5e9'; btn.style.color='#fff';
  document.getElementById('login-role').value=role;
  document.getElementById('login-role-label').textContent = role==='student' ? '👨‍🎓 Student Login' : '👩‍🏫 Teacher Login';
}}

function doLogin(){{
  const email=document.getElementById('login-email').value.trim();
  const pass=document.getElementById('login-password').value.trim();
  const role=document.getElementById('login-role').value;
  const err=document.getElementById('login-err');
  err.style.display='none';
  if(!email||!pass){{ err.textContent='Please fill all fields.'; err.style.display='block'; return; }}
  const user=DB.users.find(u=>u.email===email&&u.password===pass&&u.role===role);
  if(!user){{ err.textContent='Wrong email/password or account type.'; err.style.display='block'; return; }}
  currentUser=user; updateNavbar();
  document.getElementById('auth-redirect-note').style.display='none';
  if(currentCourse) loadCoursePlayer();
  else if(role==='student') loadStudentDashboard();
  else loadTeacherDashboard();
}}

function doRegisterStudent(){{
  const name=document.getElementById('sreg-name').value.trim();
  const email=document.getElementById('sreg-email').value.trim();
  const pass=document.getElementById('sreg-pass').value.trim();
  const err=document.getElementById('sreg-err'); err.style.display='none';
  if(!name||!email||!pass){{ err.textContent='Please fill all fields.'; err.style.display='block'; return; }}
  if(DB.users.find(u=>u.email===email)){{ err.textContent='Email already registered.'; err.style.display='block'; return; }}
  const teacher=DB.users.find(u=>u.role==='teacher');
  const u={{id:uid(),role:'student',name,email,password:pass,teacherId:teacher?.id||null}};
  DB.users.push(u); currentUser=u; updateNavbar();
  if(currentCourse) loadCoursePlayer(); else loadStudentDashboard();
}}

function doRegisterTeacher(){{
  const name=document.getElementById('treg-name').value.trim();
  const email=document.getElementById('treg-email').value.trim();
  const pass=document.getElementById('treg-pass').value.trim();
  const subject=document.getElementById('treg-subject').value.trim();
  const certInp=document.getElementById('treg-cert');
  const cert=certInp.files.length?certInp.files[0].name:'no_cert.pdf';
  const err=document.getElementById('treg-err'); err.style.display='none';
  if(!name||!email||!pass||!subject){{ err.textContent='Please fill all fields.'; err.style.display='block'; return; }}
  if(DB.users.find(u=>u.email===email)){{ err.textContent='Email already registered.'; err.style.display='block'; return; }}
  const u={{id:uid(),role:'teacher',name,email,password:pass,subject,cert,verified:true}};
  DB.users.push(u); currentUser=u; updateNavbar(); loadTeacherDashboard();
}}

// ═══════════════════════════ VIDEO PLAYER ═══════════════════════════
function loadCoursePlayer(){{
  setPage('page-player');
  document.getElementById('player-course-title').textContent = currentCourse?.title||'';
  document.getElementById('player-teacher').textContent = currentCourse?.teacher||'';
  if(!document.getElementById('main-video')){{
    document.getElementById('video-wrap').innerHTML=`
      <video id="main-video" style="width:100%;border-radius:0;background:#000;display:block" controls crossorigin="anonymous">
        <source src="${{VIDEO_SRC}}" type="video/mp4"/>
        
      </video>
      <div id="sub-overlay" class="subtitle-overlay" style="display:none"></div>`;
    videoEl=document.getElementById('main-video');
    videoEl.addEventListener('timeupdate', onVideoTime);
    if(!('speechSynthesis' in window)){{ speechOk=false; }}
    else {{ const lv=()=>{{ const v=window.speechSynthesis.getVoices(); if(v.length) availableVoices=v; }}; lv(); window.speechSynthesis.onvoiceschanged=lv; }}
  }}
  renderPlayerDocs();
}}

function getCurrentCues(){{
  return subtitleLang==='kn' ? KN_EN_CUES : HI_EN_CUES;
}}

function onVideoTime(){{
  if(!videoEl) return;
  const t=videoEl.currentTime;
  const pct=videoEl.duration?(t/videoEl.duration*100):0;
  const pb=document.getElementById('player-progress'); if(pb) pb.style.width=pct+'%';
  const cues=getCurrentCues();
  const cue=cues.find(c=>t>=c.start&&t<c.end);
  const ov=document.getElementById('sub-overlay');
  if(ov){{
    if(cue){{
      const mainLine = subtitleLang==='kn' ? cue.kn : cue.hi;
      ov.innerHTML = `<span style="display:block;font-size:15px;font-weight:500">${{mainLine}}</span>`;
      ov.style.display='block';
      ov.className='subtitle-overlay'+(dubbingOn?' dubbed':'');
    }} else ov.style.display='none';
  }}
  if(dubbingOn&&cue){{
    const key=cue.start+'-'+cue.end;
    if(lastSpokenKey!==key){{
      lastSpokenKey=key; window.speechSynthesis.cancel();
      const mainLine = subtitleLang==='kn' ? cue.kn : cue.hi;
      const utt=new SpeechSynthesisUtterance(mainLine);
      utt.lang = subtitleLang==='kn' ? 'kn-IN' : 'hi-IN';
      utt.rate=0.9;
      const best=availableVoices.find(v=>v.lang===utt.lang)||availableVoices.find(v=>v.lang.startsWith(subtitleLang));
      if(best) utt.voice=best;
      window.speechSynthesis.speak(utt);
    }}
  }}
}}

function switchSubtitleLang(lang){{
  subtitleLang=lang;
  lastSpokenKey=null;
  window.speechSynthesis?.cancel();
  document.querySelectorAll('.sub-lang-btn').forEach(b=>{{
    b.style.background = b.dataset.lang===lang ? '#0ea5e9' : '#f1f5f9';
    b.style.color      = b.dataset.lang===lang ? '#fff'    : '#475569';
  }});
}}

function toggleDubbing(){{
  dubbingOn=!dubbingOn;
  const btn=document.getElementById('dub-btn');
  if(dubbingOn){{ btn.textContent='🔊 AI Dubbing: ON'; btn.style.cssText='background:#7c3aed;color:#fff;border:none;border-radius:8px;padding:7px 14px;font-size:13px;cursor:pointer;font-weight:600'; }}
  else {{ btn.textContent='🔇 AI Dubbing: OFF'; btn.style.cssText='background:#f1f5f9;color:#475569;border:1px solid #e2e8f0;border-radius:8px;padding:7px 14px;font-size:13px;cursor:pointer;font-weight:600'; stopDubbing(); dubbingOn=false; }}
}}
function stopDubbing(){{ window.speechSynthesis?.cancel(); lastSpokenKey=null; dubbingOn=false; }}

function renderPlayerDocs(){{
  const c=document.getElementById('player-docs');
  if(!c) return;
  c.innerHTML=DOCS.map(d=>`
    <div class="doc-card" onclick="alert('Download: '+this.querySelector('strong').textContent)">
      <span style="font-size:24px">${{d.icon}}</span>
      <div style="flex:1"><strong style="font-size:13px">${{d.name}}</strong>
        <div style="font-size:12px;color:#94a3b8;margin-top:2px">${{d.size}} · <span class="badge ${{d.type==='assignment'?'badge-blue':'badge-green'}}" style="font-size:11px">${{d.type}}</span></div>
      </div>
      <span style="color:#0ea5e9">⬇</span>
    </div>`).join('');
}}

// ═══════════════════════════ STUDENT DASHBOARD ═══════════════════════════
function loadStudentDashboard(){{
  setPage('page-student');
  const teacher=DB.users.find(u=>u.id===currentUser.teacherId);
  document.getElementById('stu-name').textContent=currentUser.name;
  document.getElementById('stu-teacher').textContent=teacher?teacher.name:'Dr. Priya Sharma';
  document.getElementById('stu-subject').textContent=teacher?teacher.subject:'Python & NLP';
  showStuSection('my-courses');
}}

function showStuSection(sec){{
  document.querySelectorAll('.stu-sec').forEach(s=>s.style.display='none');
  document.querySelectorAll('.stu-nav').forEach(b=>b.classList.remove('active'));
  document.getElementById('stusec-'+sec).style.display='block';
  document.getElementById('stunav-'+sec).classList.add('active');
  if(sec==='qa') renderStudentQA();
  if(sec==='my-courses') renderMyCourses();
}}

function renderMyCourses(){{
  const c=document.getElementById('stu-my-courses');
  if(!c) return;
  c.innerHTML=COURSES.map(course=>`
    <div class="course-card" onclick="openCourseDetail('${{course.id}}')">
      <img src="${{course.thumb}}" style="width:100%;height:130px;object-fit:cover"/>
      <div style="padding:14px">
        <h4 style="font-size:15px;margin-bottom:4px">${{course.title}}</h4>
        <p style="font-size:12px;color:#64748b;margin-bottom:8px">⏱ ${{course.duration}} · ${{course.level}}</p>
        ${{course.progress>0
          ? `<div class="progress-bar"><div class="progress-fill" style="width:${{course.progress}}%"></div></div><p style="font-size:12px;color:#0ea5e9;margin-top:5px">${{course.progress}}% complete</p>`
          : `<span style="font-size:12px;color:#94a3b8">Not started</span>`}}
      </div>
    </div>`).join('');
}}

function renderStudentQA(){{
  const c=document.getElementById('qa-messages'); if(!c) return;
  const myQs=DB.questions.filter(q=>q.studentId===currentUser.id);
  if(!myQs.length){{ c.innerHTML='<p style="text-align:center;color:#94a3b8;padding:40px">No questions yet. Ask your first doubt below!</p>'; return; }}
  c.innerHTML=myQs.map(q=>`
    <div style="margin-bottom:22px">
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:6px;justify-content:flex-end">
        <span style="font-size:12px;color:#94a3b8">${{new Date(q.ts).toLocaleDateString()}}</span>
        <div style="width:26px;height:26px;background:#0ea5e9;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:11px;font-weight:700">You</div>
      </div>
      <div class="msg-student">${{q.question}}</div>
      ${{q.answer
        ? `<div style="display:flex;align-items:center;gap:8px;margin:10px 0 5px">
             <div style="width:26px;height:26px;background:#16a34a;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:11px;font-weight:700">T</div>
             <span style="font-size:12px;color:#94a3b8">Teacher</span></div>
           <div class="msg-teacher">${{q.answer}}</div>`
        : `<div style="font-size:12px;color:#f59e0b;margin-top:8px;text-align:right">⏳ Awaiting reply...</div>`
      }}
    </div>`).join('');
  c.scrollTop=c.scrollHeight;
}}

function sendQuestion(){{
  const inp=document.getElementById('qa-input'); const text=inp.value.trim(); if(!text) return;
  const teacher=DB.users.find(u=>u.id===currentUser.teacherId);
  DB.questions.push({{id:uid(),studentId:currentUser.id,teacherId:teacher?.id,question:text,answer:null,ts:Date.now()}});
  inp.value=''; renderStudentQA();
}}

// ═══════════════════════════ TEACHER DASHBOARD ═══════════════════════════
function loadTeacherDashboard(){{
  setPage('page-teacher');
  document.getElementById('tea-name').textContent=currentUser.name;
  document.getElementById('tea-subject').textContent=currentUser.subject||'';
  showTeaSection('overview');
}}

function showTeaSection(sec){{
  document.querySelectorAll('.tea-sec').forEach(s=>s.style.display='none');
  document.querySelectorAll('.tea-nav').forEach(b=>b.classList.remove('active'));
  document.getElementById('teasec-'+sec).style.display='block';
  document.getElementById('teanav-'+sec).classList.add('active');
  if(sec==='overview') renderTeaOverview();
  if(sec==='qa') renderTeacherQA();
  if(sec==='students') renderStudentList();
}}

function renderTeaOverview(){{
  const myStudents=DB.users.filter(u=>u.role==='student'&&u.teacherId===currentUser.id);
  const myQs=DB.questions.filter(q=>q.teacherId===currentUser.id);
  const pending=myQs.filter(q=>!q.answer).length;
  render('tea-overview',`
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:16px;margin-bottom:24px">
      ${{sc('👨‍🎓','Enrolled Students',myStudents.length,'#0ea5e9')}}
      ${{sc('❓','Total Questions',myQs.length,'#8b5cf6')}}
      ${{sc('⏳','Pending Replies',pending,'#f59e0b')}}
      ${{sc('✅','Answered',myQs.length-pending,'#16a34a')}}
    </div>
    <div class="card" style="padding:20px">
      <h3 style="font-size:16px;margin-bottom:10px">Your Profile</h3>
      <p style="font-size:14px;color:#475569">Subject: <strong>${{currentUser.subject}}</strong></p>
      <p style="font-size:14px;color:#475569;margin-top:6px">Certificate: <span style="color:#0ea5e9">${{currentUser.cert||'N/A'}}</span></p>
    </div>`);
}}

function sc(icon,label,val,color){{
  return `<div class="card" style="padding:18px;text-align:center"><div style="font-size:30px">${{icon}}</div>
    <div class="stat-num" style="color:${{color}};margin:6px 0">${{val}}</div>
    <div style="font-size:13px;color:#64748b">${{label}}</div></div>`;
}}

function renderTeacherQA(){{
  const myQs=DB.questions.filter(q=>q.teacherId===currentUser.id);
  const c=document.getElementById('tea-qa-list'); if(!c) return;
  if(!myQs.length){{ c.innerHTML='<p style="text-align:center;color:#94a3b8;padding:40px">No student questions yet.</p>'; return; }}
  c.innerHTML=myQs.map(q=>{{
    const stu=DB.users.find(u=>u.id===q.studentId);
    return `<div class="card" style="padding:18px;margin-bottom:14px">
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px">
        <div style="width:34px;height:34px;background:#0ea5e9;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700">${{(stu?.name||'S')[0]}}</div>
        <div style="flex:1">
          <div style="font-weight:600;font-size:14px">${{stu?.name||'Student'}}</div>
          <div style="font-size:12px;color:#94a3b8">${{new Date(q.ts).toLocaleDateString()}}</div>
        </div>
        ${{q.answer?'<span class="badge badge-green">Answered</span>':'<span class="badge" style="background:#fef3c7;color:#92400e">Pending</span>'}}
      </div>
      <div style="background:#f8fafc;border-radius:9px;padding:11px;font-size:14px;margin-bottom:10px">${{q.question}}</div>
      ${{q.answer
        ? `<div style="background:#f0fdf4;border-radius:9px;padding:11px;font-size:14px;color:#166534">✅ ${{q.answer}}</div>`
        : `<div style="display:flex;gap:8px"><input type="text" id="ans-${{q.id}}" placeholder="Type your answer..." style="flex:1"/>
           <button class="btn btn-green btn-sm" onclick="submitAnswer('${{q.id}}')">Reply</button></div>`
      }}
    </div>`;
  }}).join('');
}}

function submitAnswer(qid){{
  const inp=document.getElementById('ans-'+qid); if(!inp) return;
  const text=inp.value.trim(); if(!text) return;
  const q=DB.questions.find(q=>q.id===qid); if(q) q.answer=text;
  renderTeacherQA();
}}

function renderStudentList(){{
  const myS=DB.users.filter(u=>u.role==='student'&&u.teacherId===currentUser.id);
  const c=document.getElementById('tea-students-list'); if(!c) return;
  if(!myS.length){{ c.innerHTML='<p style="text-align:center;color:#94a3b8;padding:40px">No students enrolled yet.</p>'; return; }}
  c.innerHTML=myS.map(s=>{{
    const qc=DB.questions.filter(q=>q.studentId===s.id).length;
    return `<div class="card" style="padding:16px;display:flex;align-items:center;gap:14px;margin-bottom:12px">
      <div style="width:42px;height:42px;background:linear-gradient(135deg,#0ea5e9,#38bdf8);border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:17px">${{s.name[0]}}</div>
      <div style="flex:1">
        <div style="font-weight:600">${{s.name}}</div>
        <div style="font-size:13px;color:#64748b">${{s.email}}</div>
      </div>
      <div style="font-size:13px;color:#94a3b8">${{qc}} question${{qc!==1?'s':''}}</div>
    </div>`;
  }}).join('');
}}
</script>

<!-- ══════════════════ HOME PAGE ══════════════════ -->
<div id="page-home" class="page active">
  <!-- Navbar -->
  <nav style="background:#fff;border-bottom:1px solid #e2e8f0;padding:0 28px;height:56px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:100">
    <div style="display:flex;align-items:center;gap:28px">
      <div onclick="goHome()" style="cursor:pointer;display:flex;align-items:center;gap:8px">
        <span style="font-size:22px">🧠</span>
        <span style="font-family:'Syne',sans-serif;font-weight:800;font-size:18px;color:#0c4a6e">DeepLearn</span>
      </div>
      <button class="nav-link" onclick="goHome()">Browse</button>
      <button class="nav-link" onclick="navDashboard()">My Learning</button>
    </div>
    <div style="display:flex;align-items:center;gap:10px">
      <div id="nav-auth-btns" style="display:flex;gap:8px">
        <button class="btn btn-ghost btn-sm" onclick="setPage('page-auth');showAuthTab('login')">Sign In</button>
        <button class="btn btn-primary btn-sm" onclick="setPage('page-auth');showAuthTab('sreg')">Sign Up</button>
      </div>
      <div id="nav-user-menu" style="display:none;align-items:center;gap:10px">
        <span style="font-size:14px;color:#475569">Hi, <strong id="nav-user-name"></strong></span>
        <button class="btn btn-ghost btn-sm" onclick="navDashboard()">Dashboard</button>
        <button class="btn btn-ghost btn-sm" onclick="logout()">Sign Out</button>
      </div>
    </div>
  </nav>

  <!-- Hero -->
  <div class="hero-bg" style="padding:60px 28px 50px">
    <div style="max-width:700px;margin:0 auto;text-align:center">
      <h1 style="color:#fff;font-size:40px;line-height:1.15;margin-bottom:14px">Learn AI & NLP with<br/>Real Hindi Lectures</h1>
      <p style="color:#bae6fd;font-size:16px;margin-bottom:30px">Courses taught by expert teachers · Hindi subtitles · AI voice dubbing</p>
      <div class="search-bar" style="margin:0 auto">
        <span style="font-size:18px;margin-right:4px">🔍</span>
        <input id="hero-search" type="text" placeholder="Search courses e.g. Python, NLP, AI..."
          onkeydown="if(event.key==='Enter') doSearch()" style="flex:1"/>
        <button class="btn btn-primary" onclick="doSearch()">Search</button>
      </div>
      <div style="display:flex;justify-content:center;gap:32px;margin-top:32px">
        <div style="text-align:center;color:#fff"><div class="stat-num" style="color:#7dd3fc">6</div><div style="font-size:13px;color:#93c5fd">Courses</div></div>
        <div style="text-align:center;color:#fff"><div class="stat-num" style="color:#7dd3fc">5,740</div><div style="font-size:13px;color:#93c5fd">Students</div></div>
        <div style="text-align:center;color:#fff"><div class="stat-num" style="color:#7dd3fc">4.8⭐</div><div style="font-size:13px;color:#93c5fd">Avg Rating</div></div>
      </div>
    </div>
  </div>

  <!-- Browse -->
  <div style="max-width:1100px;margin:0 auto;padding:36px 20px">
    <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;margin-bottom:24px">
      <h2 id="browse-heading" style="font-size:24px">All Courses</h2>
      <div style="display:flex;gap:8px;flex-wrap:wrap">
        <button class="btn btn-ghost btn-sm cat-btn active-cat" onclick="filterCategory('All')" style="font-size:13px">All</button>
        <button class="btn btn-ghost btn-sm cat-btn" onclick="filterCategory('Programming')" style="font-size:13px">Programming</button>
        <button class="btn btn-ghost btn-sm cat-btn" onclick="filterCategory('AI & NLP')" style="font-size:13px">AI & NLP</button>
      </div>
    </div>
    <div id="course-grid" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:20px"></div>
  </div>

  <!-- Search input in browse area -->
  <div style="max-width:1100px;margin:0 auto;padding:0 20px 16px">
    <div style="display:flex;gap:8px;max-width:400px">
      <input id="home-search-bar" type="text" placeholder="Search..." onkeydown="if(event.key==='Enter') doSearch()" style="font-size:13px"/>
      <button class="btn btn-primary btn-sm" onclick="doSearch()">Go</button>
    </div>
  </div>
</div>

<!-- ══════════════════ COURSE DETAIL PAGE ══════════════════ -->
<div id="page-course-detail" class="page">
  <nav style="background:#fff;border-bottom:1px solid #e2e8f0;padding:0 24px;height:56px;display:flex;align-items:center;gap:16px;position:sticky;top:0;z-index:100">
    <button class="btn btn-ghost btn-sm" onclick="goHome()">← Back</button>
    <span style="font-family:'Syne',sans-serif;font-weight:800;color:#0c4a6e">DeepLearn</span>
  </nav>
  <div style="max-width:1000px;margin:0 auto;padding:32px 20px;display:grid;grid-template-columns:1fr 320px;gap:28px">
    <!-- LEFT COLUMN -->
    <div>
      <div id="detail-level" style="margin-bottom:10px"></div>
      <h1 id="detail-title" style="font-size:26px;margin-bottom:10px"></h1>
      <p id="detail-meta" style="font-size:14px;color:#64748b;margin-bottom:14px;display:flex;gap:8px;flex-wrap:wrap"></p>
      <div id="detail-tags" style="margin-bottom:20px"></div>

      <!-- DESCRIPTION -->
      <div class="card" style="padding:20px;margin-bottom:16px">
        <h3 style="font-size:15px;margin-bottom:12px;color:#0c4a6e">📋 Description</h3>
        <p id="detail-desc" style="font-size:14px;color:#475569;line-height:1.8"></p>
      </div>

      <!-- INCLUDED MATERIALS -->
      <div class="card" style="padding:18px;margin-bottom:16px">
        <h3 style="font-size:15px;margin-bottom:12px;color:#0c4a6e">📂 Included Materials</h3>
        <div id="detail-docs-list" style="display:flex;flex-direction:column;gap:8px"></div>
      </div>

      <!-- REVIEWS -->
      <div class="card" style="padding:20px">
        <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px">
          <h3 style="font-size:15px;color:#0c4a6e">⭐ Student Reviews</h3>
          <span id="detail-avg-rating" style="font-size:13px;color:#f59e0b;font-weight:700"></span>
        </div>
        <div id="detail-reviews-list" style="margin-bottom:16px"></div>
        <!-- Add review form (only if logged in) -->
        <div id="detail-review-form" style="display:none;border-top:1px solid #e2e8f0;padding-top:16px">
          <div style="font-size:13px;font-weight:600;color:#475569;margin-bottom:8px">Leave a Review</div>
          <div style="display:flex;gap:6px;margin-bottom:10px" id="star-picker">
            <span class="star-btn" data-val="1" onclick="pickStar(1)" style="font-size:22px;cursor:pointer;opacity:0.3">⭐</span>
            <span class="star-btn" data-val="2" onclick="pickStar(2)" style="font-size:22px;cursor:pointer;opacity:0.3">⭐</span>
            <span class="star-btn" data-val="3" onclick="pickStar(3)" style="font-size:22px;cursor:pointer;opacity:0.3">⭐</span>
            <span class="star-btn" data-val="4" onclick="pickStar(4)" style="font-size:22px;cursor:pointer;opacity:0.3">⭐</span>
            <span class="star-btn" data-val="5" onclick="pickStar(5)" style="font-size:22px;cursor:pointer;opacity:0.3">⭐</span>
          </div>
          <textarea id="review-text" placeholder="Share your experience with this course..." rows="3" style="margin-bottom:10px;resize:vertical"></textarea>
          <button class="btn btn-primary btn-sm" onclick="submitReview()">Submit Review</button>
          <div id="review-err" style="font-size:12px;color:#dc2626;margin-top:6px;display:none"></div>
        </div>
        <div id="detail-login-to-review" style="border-top:1px solid #e2e8f0;padding-top:14px;text-align:center">
          <p style="font-size:13px;color:#94a3b8">Sign in to leave a review</p>
        </div>
      </div>
    </div>

    <!-- RIGHT COLUMN -->
    <div>
      <div id="detail-thumb-wrap" style="margin-bottom:16px"></div>
      <div class="card" style="padding:20px">
        <button id="detail-watch-btn" class="btn btn-primary" style="width:100%;justify-content:center;font-size:15px;padding:14px">▶ Watch Now</button>
        <p style="font-size:12px;color:#94a3b8;text-align:center;margin-top:10px">Login required to watch</p>
        <div id="auth-redirect-note" class="alert alert-red" style="display:none;margin-top:10px">Please sign in to watch this course.</div>
      </div>
    </div>
  </div>
</div>

<!-- ══════════════════ AUTH PAGE ══════════════════ -->
<div id="page-auth" class="page">
  <nav style="background:#fff;border-bottom:1px solid #e2e8f0;padding:0 24px;height:56px;display:flex;align-items:center;gap:16px;position:sticky;top:0;z-index:100">
    <button class="btn btn-ghost btn-sm" onclick="goHome()">← Back</button>
    <span style="font-family:'Syne',sans-serif;font-weight:800;color:#0c4a6e">DeepLearn</span>
  </nav>
  <div style="min-height:calc(100vh - 56px);display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#f0f9ff,#f8fafc);padding:24px">
    <div style="width:100%;max-width:460px">
      <div style="text-align:center;margin-bottom:24px">
        <div style="font-size:44px">🧠</div>
        <h1 style="font-size:28px;margin-top:8px;color:#0c4a6e">Join DeepLearn</h1>
      </div>
      <div class="card" style="padding:28px">
        <div id="auth-redirect-note" class="alert alert-red" style="display:none">Please sign in to watch this course.</div>
        <div style="display:flex;gap:4px;background:#f1f5f9;border-radius:10px;padding:4px;margin-bottom:22px">
          <button id="authtab-login" class="tab-btn active" style="flex:1" onclick="showAuthTab('login')">Sign In</button>
          <button id="authtab-sreg"  class="tab-btn" style="flex:1" onclick="showAuthTab('sreg')">Student</button>
          <button id="authtab-treg"  class="tab-btn" style="flex:1" onclick="showAuthTab('treg')">Teacher</button>
        </div>

        <!-- LOGIN -->
        <div id="authpanel-login" class="auth-panel">
          <div style="display:flex;gap:8px;margin-bottom:16px">
            <button id="rolebtn-student" class="role-btn btn" style="flex:1;background:#0ea5e9;color:#fff;border-radius:9px;padding:9px;font-size:13px;font-weight:600" onclick="showLoginRole('student')">👨‍🎓 Student</button>
            <button id="rolebtn-teacher" class="role-btn btn" style="flex:1;background:#f1f5f9;color:#475569;border-radius:9px;padding:9px;font-size:13px;font-weight:600" onclick="showLoginRole('teacher')">👩‍🏫 Teacher</button>
          </div>
          <div id="login-role-label" style="font-size:13px;color:#0ea5e9;font-weight:600;text-align:center;margin-bottom:14px">👨‍🎓 Student Login</div>
          <input type="hidden" id="login-role" value="student"/>
          <div id="login-err" class="alert alert-red" style="display:none"></div>
          <label class="field-label">Email</label>
          <input type="email" id="login-email" placeholder="you@example.com" style="margin-bottom:12px"/>
          <label class="field-label">Password</label>
          <input type="password" id="login-password" placeholder="••••••••" style="margin-bottom:18px"
            onkeydown="if(event.key==='Enter') doLogin()"/>
          <button class="btn btn-primary" style="width:100%;justify-content:center;padding:12px" onclick="doLogin()">Sign In →</button>
          <div style="background:#f8fafc;border-radius:9px;padding:12px;margin-top:14px;font-size:12px;color:#64748b;line-height:1.6">
            <strong>Demo accounts:</strong><br/>
            🎓 Student: student@demo.com / demo123<br/>
            👩‍🏫 Teacher: teacher@demo.com / demo123
          </div>
        </div>

        <!-- STUDENT REGISTER -->
        <div id="authpanel-sreg" class="auth-panel" style="display:none">
          <div id="sreg-err" class="alert alert-red" style="display:none"></div>
          <label class="field-label">Full Name</label>
          <input type="text" id="sreg-name" placeholder="Your name" style="margin-bottom:12px"/>
          <label class="field-label">Email</label>
          <input type="email" id="sreg-email" placeholder="you@example.com" style="margin-bottom:12px"/>
          <label class="field-label">Password</label>
          <input type="password" id="sreg-pass" placeholder="Create a password" style="margin-bottom:18px"/>
          <button class="btn btn-primary" style="width:100%;justify-content:center;padding:12px" onclick="doRegisterStudent()">Create Account →</button>
        </div>

        <!-- TEACHER REGISTER -->
        <div id="authpanel-treg" class="auth-panel" style="display:none">
          <div id="treg-err" class="alert alert-red" style="display:none"></div>
          <label class="field-label">Full Name</label>
          <input type="text" id="treg-name" placeholder="Dr. / Prof. Your Name" style="margin-bottom:12px"/>
          <label class="field-label">Email</label>
          <input type="email" id="treg-email" placeholder="you@university.com" style="margin-bottom:12px"/>
          <label class="field-label">Password</label>
          <input type="password" id="treg-pass" placeholder="Create a password" style="margin-bottom:12px"/>
          <label class="field-label">Subject / Specialisation</label>
          <input type="text" id="treg-subject" placeholder="e.g. Python & NLP" style="margin-bottom:12px"/>
          <label class="field-label">Upload Certificate</label>
          <input type="file" id="treg-cert" accept=".pdf,.jpg,.png" style="margin-bottom:18px;border:1px dashed #cbd5e1;background:#f8fafc"/>
          <button class="btn btn-green" style="width:100%;justify-content:center;padding:12px" onclick="doRegisterTeacher()">Register as Teacher →</button>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- ══════════════════ VIDEO PLAYER PAGE ══════════════════ -->
<div id="page-player" class="page">
  <nav style="background:#0c4a6e;padding:0 20px;height:52px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:100">
    <div style="display:flex;align-items:center;gap:14px">
      <button class="btn btn-sm" style="background:rgba(255,255,255,0.15);color:#fff;border:none" onclick="currentCourse?openCourseDetail(currentCourse.id):goHome()">← Back</button>
      <div>
        <div id="player-course-title" style="color:#fff;font-weight:700;font-size:15px"></div>
        <div id="player-teacher" style="color:#7dd3fc;font-size:12px"></div>
      </div>
    </div>
    <button class="btn btn-sm" style="background:rgba(255,255,255,0.15);color:#fff;border:none" onclick="logout()">Sign Out</button>
  </nav>
  <div style="display:grid;grid-template-columns:1fr 320px;min-height:calc(100vh - 52px)">
    <!-- Left: video + docs -->
    <div style="padding:20px;overflow-y:auto">
      <div style="max-width:680px;margin:0 auto 16px">
        <div style="position:relative;background:#000;border-radius:12px;overflow:hidden" id="video-wrap"></div>
      </div>
      <div style="background:#fff;border:1px solid #e2e8f0;border-radius:12px;padding:14px;margin-bottom:16px">
        <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:10px">
          <div style="flex:1;margin-right:16px">
            <div style="font-size:13px;font-weight:600;margin-bottom:6px;color:#475569">Video Progress</div>
            <div class="progress-bar"><div class="progress-fill" id="player-progress" style="width:0%"></div></div>
          </div>
          <button id="dub-btn" style="background:#f1f5f9;color:#475569;border:1px solid #e2e8f0;border-radius:8px;padding:7px 14px;font-size:13px;cursor:pointer;font-weight:600;white-space:nowrap" onclick="toggleDubbing()">🔇 AI Dubbing: OFF</button>
        </div>
        <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap">
          <span style="font-size:12px;font-weight:600;color:#475569">🌐 Subtitles:</span>
          <button class="sub-lang-btn" data-lang="hi" onclick="switchSubtitleLang(\'hi\')"
            style="background:#0ea5e9;color:#fff;border:none;border-radius:7px;padding:5px 12px;font-size:12px;font-weight:600;cursor:pointer">
            🇮🇳 Hindi + English
          </button>
          <button class="sub-lang-btn" data-lang="kn" onclick="switchSubtitleLang(\'kn\')"
            style="background:#f1f5f9;color:#475569;border:none;border-radius:7px;padding:5px 12px;font-size:12px;font-weight:600;cursor:pointer">
            🏴 Kannada + English
          </button>
        </div>
      </div>
      <div class="card" style="padding:18px">
        <h3 style="font-size:15px;margin-bottom:12px">📂 Assignments & Notes</h3>
        <div id="player-docs" style="display:flex;flex-direction:column;gap:8px"></div>
      </div>
    </div>
    <!-- Right: Q&A -->
    <div style="border-left:1px solid #e2e8f0;display:flex;flex-direction:column;background:#fff">
      <div style="padding:14px 16px;border-bottom:1px solid #e2e8f0;background:#f8fafc">
        <div style="font-weight:700;font-size:15px">💬 Ask a Doubt</div>
        <div style="font-size:12px;color:#64748b;margin-top:2px">Your teacher will reply here</div>
      </div>
      <div id="qa-messages" style="flex:1;overflow-y:auto;padding:16px;min-height:200px"></div>
      <div style="padding:12px;border-top:1px solid #e2e8f0;display:flex;gap:8px">
        <input type="text" id="qa-input" placeholder="Type your question..." style="flex:1;font-size:13px"
          onkeydown="if(event.key==='Enter') sendQuestion()"/>
        <button class="btn btn-primary btn-sm" onclick="sendQuestion()">Send</button>
      </div>
    </div>
  </div>
</div>

<!-- ══════════════════ STUDENT DASHBOARD ══════════════════ -->
<div id="page-student" class="page">
  <nav style="background:#fff;border-bottom:1px solid #e2e8f0;padding:0 20px;height:56px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:100">
    <div style="display:flex;align-items:center;gap:10px">
      <span onclick="goHome()" style="cursor:pointer;font-family:'Syne',sans-serif;font-weight:800;font-size:18px;color:#0c4a6e">🧠 DeepLearn</span>
      <span class="badge badge-blue">Student</span>
    </div>
    <div style="display:flex;align-items:center;gap:10px">
      <span style="font-size:14px;color:#475569">Hi, <strong id="stu-name"></strong></span>
      <button class="btn btn-ghost btn-sm" onclick="goHome()">Browse Courses</button>
      <button class="btn btn-ghost btn-sm" onclick="logout()">Sign Out</button>
    </div>
  </nav>
  <div style="display:flex;min-height:calc(100vh - 56px)">
    <div style="width:220px;background:#fff;border-right:1px solid #e2e8f0;padding:16px 10px;flex-shrink:0">
      <div style="background:#f0f9ff;border-radius:12px;padding:14px;margin-bottom:16px">
        <div style="font-size:11px;color:#0369a1;font-weight:700;letter-spacing:.5px">YOUR TEACHER</div>
        <div style="font-weight:700;font-size:14px;margin-top:5px" id="stu-teacher"></div>
        <div style="font-size:12px;color:#64748b" id="stu-subject"></div>
      </div>
      <button id="stunav-my-courses" class="sidebar-item stu-nav active" onclick="showStuSection('my-courses')">📚 My Courses</button>
      <button id="stunav-progress"   class="sidebar-item stu-nav"        onclick="showStuSection('progress')">📊 Progress</button>
      <button id="stunav-qa"         class="sidebar-item stu-nav"        onclick="showStuSection('qa')">💬 My Doubts</button>
    </div>
    <div style="flex:1;padding:24px;overflow-y:auto">
      <div id="stusec-my-courses" class="stu-sec">
        <h2 style="font-size:22px;margin-bottom:18px">📚 My Courses</h2>
        <div id="stu-my-courses" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:16px"></div>
      </div>
      <div id="stusec-progress" class="stu-sec" style="display:none">
        <h2 style="font-size:22px;margin-bottom:18px">📊 My Progress</h2>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:14px;margin-bottom:24px">
          <div class="card" style="padding:18px;text-align:center"><div style="font-size:28px">🎬</div><div class="stat-num" style="color:#0ea5e9">6</div><div style="font-size:13px;color:#64748b">Courses Available</div></div>
          <div class="card" style="padding:18px;text-align:center"><div style="font-size:28px">📄</div><div class="stat-num" style="color:#8b5cf6">5</div><div style="font-size:13px;color:#64748b">Documents</div></div>
        </div>
      </div>
      <div id="stusec-qa" class="stu-sec" style="display:none">
        <h2 style="font-size:22px;margin-bottom:6px">💬 My Doubts</h2>
        <p style="color:#64748b;font-size:14px;margin-bottom:18px">Questions you've asked. Teacher replies appear here.</p>
        <div class="card" style="display:flex;flex-direction:column;height:500px">
          <div id="qa-messages" style="flex:1;overflow-y:auto;padding:16px"></div>
          <div style="padding:12px;border-top:1px solid #e2e8f0;display:flex;gap:8px">
            <input type="text" id="qa-input" placeholder="Ask a question..." style="flex:1"
              onkeydown="if(event.key==='Enter') sendQuestion()"/>
            <button class="btn btn-primary btn-sm" onclick="sendQuestion()">Send</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- ══════════════════ TEACHER DASHBOARD ══════════════════ -->
<div id="page-teacher" class="page">
  <nav style="background:#0c4a6e;padding:0 20px;height:56px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:100">
    <div style="display:flex;align-items:center;gap:10px">
      <span style="font-family:'Syne',sans-serif;font-weight:800;font-size:18px;color:#fff">🧠 DeepLearn</span>
      <span class="badge" style="background:#0369a1;color:#bae6fd">Teacher</span>
    </div>
    <div style="display:flex;align-items:center;gap:10px">
      <div style="text-align:right"><div id="tea-name" style="color:#fff;font-size:14px;font-weight:600"></div><div id="tea-subject" style="color:#7dd3fc;font-size:12px"></div></div>
      <button class="btn btn-sm" style="background:rgba(255,255,255,0.15);color:#fff;border:none" onclick="logout()">Sign Out</button>
    </div>
  </nav>
  <div style="display:flex;min-height:calc(100vh - 56px)">
    <div style="width:220px;background:#fff;border-right:1px solid #e2e8f0;padding:16px 10px;flex-shrink:0">
      <button id="teanav-overview"  class="sidebar-item tea-nav active" onclick="showTeaSection('overview')">🏠 Overview</button>
      <button id="teanav-students"  class="sidebar-item tea-nav"        onclick="showTeaSection('students')">👨‍🎓 Students</button>
      <button id="teanav-qa"        class="sidebar-item tea-nav"        onclick="showTeaSection('qa')">💬 Student Q&A</button>
    </div>
    <div style="flex:1;padding:24px;overflow-y:auto">
      <div id="teasec-overview" class="tea-sec"><h2 style="font-size:22px;margin-bottom:18px">🏠 Overview</h2><div id="tea-overview"></div></div>
      <div id="teasec-students" class="tea-sec" style="display:none"><h2 style="font-size:22px;margin-bottom:18px">👨‍🎓 Students</h2><div id="tea-students-list"></div></div>
      <div id="teasec-qa" class="tea-sec" style="display:none"><h2 style="font-size:22px;margin-bottom:6px">💬 Student Q&A</h2><p style="color:#64748b;font-size:14px;margin-bottom:18px">Reply to your students' questions.</p><div id="tea-qa-list"></div></div>
    </div>
  </div>
</div>

<script>
// Boot
renderCourseGrid(COURSES);
updateNavbar();
// Category button active style
document.querySelectorAll('.cat-btn').forEach(b=>{{
  b.addEventListener('click',()=>{{
    document.querySelectorAll('.cat-btn').forEach(x=>{{x.style.background='';x.style.color='';x.classList.remove('active-cat');}});
    b.style.background='#0ea5e9'; b.style.color='#fff';
  }});
}});
</script>
</body>
</html>"""

components.html(html, height=900, scrolling=True)
