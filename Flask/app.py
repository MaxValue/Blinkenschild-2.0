#!/usr/bin/env python3
# coding: utf-8

'''
TODO:
	frontend
		Layout styling
		control elements
	backend
		calling scripts
			download youtube video
				link
			display picture
				infinite
				show for X seconds
			display text
				color
		handling frontend calls

FRONTEND WORKFLOW:
	display controls
		youtube link field, play button
		picture upload button, seconds chooser, display button
		text field (FUTURE: calculate width for pixels and turn red if not on 1 screen), color chooser, write button

FUTURE:
	session ids? identifying multi user.
	Queue
'''

from flask import Flask,render_template, request,json

app = Flask(__name__)

@app.route('/')
def hello():
	return render_template('main.html', current_task='Nothing') # TODO: should display what the schild is currently doing

@app.route('/api/youtube', methods=['POST', 'PUT'])
def youtube():
	print('youtube was called') # DEBUG
	if request.method == 'POST':
		videolink = request.form['yt_video']
		# TODO: Needs to call backend script, backend script should return success code which gets returned below
		return json.dumps({'status':'OK','msg':'Downloaded video {}'.format(videolink)})
	elif request.method == 'PUT':
		videolink = request.form['yt_video']
		# TODO: As far as I know the current backend script can only download but not display?
		return json.dumps({'status':'OK','msg':'Playing video {}'.format(videolink)})

@app.route('/api/picture', methods=['POST', 'PUT'])
def picture():
	print('picture was called') # DEBUG
	if request.method == 'POST':
		for filename in request.files: # TODO: multipart mode on form
			print(filename)
			# TODO: Save files with their checksums and return the checksums
		return json.dumps({'status':'OK','msg':'Downloaded video {}'.format(videolink)})
	elif request.method == 'PUT':
		# How do we know which files?
		# TODO: Needs to call backend script, backend script should return success code which gets returned below
		return json.dumps({'status':'OK','msg':'Playing video {}'.format(videolink)})

	return json.dumps({'status':'OK','picture':'YESS!'})

@app.route('/api/text', methods=['PUT'])
def write_text():
	print('write_text was called') # DEBUG
	text = request.form['text']
	textcolor = request.form['color']
	# TODO: Needs to call backend script, backend script should return success code which gets returned below
	return json.dumps({'status':'OK','msg':'Displaying text {} in color {}'.format(text, textcolor)})

if __name__=="__main__":
	app.run()
