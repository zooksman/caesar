#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
import caesar

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Caesar Cipher</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>
        <a href="/">Caesar Cipher</a>
    </h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

encrypted = ""
class Index(webapp2.RequestHandler):
    def get(self):
    	
        # main form
		main_form = """
		<form action="/encrypt" method="post">
			<label>
				<strong>Enter the number of places to rotate the string.</strong>
				<input type="text" name="rot" value="0" />
			</label>
			<label>
				<strong>Enter some text to be encrypted.</strong>
				<input type="text" name="tbe" value="{}" />
			</label>
			<input type="submit" name="encrypt"/>
		</form>
		""".format(self.request.get("encrypted"))
		
		self.response.write(page_header + main_form + page_footer)

class EncryptText(webapp2.RequestHandler):
	def post(self):
		tbe = cgi.escape(self.request.get("tbe"))
		rot = self.request.get("rot")
		result = caesar.encrypt(tbe, rot)
		print(encrypted)
		self.redirect('/?encrypted=' + result)

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/encrypt', EncryptText)
], debug=True)
