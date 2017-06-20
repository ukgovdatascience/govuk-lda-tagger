All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the {organization} nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Description: =================
        Python Stop Words
        =================
        
        .. contents:: Table of contents
        
        Overview
        --------
        
        Get list of common stop words in various languages in Python.
        
        .. image:: https://secure.travis-ci.org/Alir3z4/python-stop-words.png
           :alt: Build Status
           :target: http://travis-ci.org/Alir3z4/python-stop-words
        
        
        .. image:: https://coveralls.io/repos/Alir3z4/python-stop-words/badge.png
           :alt: Coverage Status
           :target: https://coveralls.io/r/Alir3z4/python-stop-words
        
        
        .. image:: https://pypip.in/d/stop-words/badge.png
           :alt: Downloads
           :target: https://pypi.python.org/pypi/stop-words/
        
        
        .. image:: https://pypip.in/v/stop-words/badge.png
           :alt: Version
           :target: https://pypi.python.org/pypi/stop-words/
        
        
        .. image:: https://pypip.in/egg/stop-words/badge.png
           :alt: Egg
           :target: https://pypi.python.org/pypi/stop-words/
        
        
        .. image:: https://pypip.in/wheel/stop-words/badge.png
           :alt: Wheel
           :target: https://pypi.python.org/pypi/stop-words/
        
        
        .. image:: https://pypip.in/format/stop-words/badge.png
           :alt: Format
           :target: https://pypi.python.org/pypi/stop-words/
        
        .. image:: https://pypip.in/license/stop-words/badge.png
           :alt: License
           :target: https://pypi.python.org/pypi/stop-words/
        
        Available languages
        -------------------
        
        * Arabic
        * Catalan
        * Danish
        * Dutch
        * English
        * Finnish
        * French
        * German
        * Hungarian
        * Italian
        * Norwegian
        * Portuguese
        * Romanian
        * Russian
        * Spanish
        * Swedish
        * Turkish
        * Ukrainian
        
        Installation
        ------------
        ``stop-words`` is available on PyPi
        
        http://pypi.python.org/pypi/stop-words
        
        So easily install it by ``pip``
        ::
        
            $ pip install stop-words
        
        Or by ``easy_install``
        ::
        
            $ easy_install stop-words
        
        Another way is by cloning ``stop-words``'s `git repo <https://github.com/Alir3z4/python-stop-words>`_ ::
        
            $ git clone git://github.com/Alir3z4/python-stop-words.git
        
        Then install it by running:
        ::
        
            $ python setup.py install
        
        
        Basic usage
        -----------
        ::
        
            from stop_words import get_stop_words
        
            stop_words = get_stop_words('en')
            stop_words = get_stop_words('english')
        
            from stop_words import safe_get_stop_words
        
            stop_words = safe_get_stop_words('unsupported language')
        
        Python compatibility
        --------------------
        
        Python-stop-words has been originally developed for Python 2, but has been
        ported and tested for Python 3.2 to Python 3.4.
        
Platform: UNKNOWN
Classifier: Programming Language :: Python
Classifier: Intended Audience :: Developers
Classifier: Operating System :: OS Independent
Classifier: Topic :: Software Development
