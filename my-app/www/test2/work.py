#!/usr/bin/env python
# coding=utf-8

__author__ = 'zxy'
'''
this is a web api for my system.
'''
from flask import Flask, request, render_template, jsonify
from codecopyDetection import *
import test_by_file;

app = Flask(__name__)

kit = codecopy_detection()
@app.route('/',methods=['GET'])
def main():
	return render_template('home.html');

@app.route('/check_file',methods=['GET'])
def submit_form2():
	return render_template('form2.html',c1='请输入代码',c2='请输入代码');

@app.route('/check_str',methods=['GET'])
def submit_form1():
	return render_template('form1.html',c1='请输入代码',c2='请输入代码');

@app.route('/submit',methods=['POST'])
def write_ans():
	str1 = request.form['code1'];
	str2 = request.form['code2'];
	kit.fit(str1,str2);
	ans1 = kit.predict();
	ans2 = kit.print();
	return jsonify({'score':ans1,'substr':ans2.decode('utf-8')});

@app.route('/test',methods=['GET'])
def test():
	check = test_by_file.test();
	return jsonify(check);

if __name__ == '__main__':
	app.run(debug=False);