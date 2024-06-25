from flask import render_template, request
from app import app
from app.utils import log_parser, event_detector

@app.route('/')
def index():
    events = log_parser.collect_logs()
    threats = event_detector.detect_threats(events)
    return render_template('index.html', threats=threats)

@app.route('/report')
def report():
    threats = event_detector.detect_threats()
    return render_template('report.html', threats=threats)
