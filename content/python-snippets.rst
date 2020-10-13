:Title: Python Snippets
:Date: 2017-11-05
:Modified: 2020-01-4
:Category: logs
:Slug: python-cheatsheet
:Tags: python, notes, cheatsheet, snippets
:Summary: Code snippets


.. contents:: Table of Contents

Snippets 
========

Profiling
---------

.. code-block:: python

    >>> from time import sleep
    >>> from timeit import Timer
    >>> def run_foo():
    ...     time.sleep(3)
    ...     print("done")
    ... 
    >> t = Timer(lambda: run_foo())
    >>> print(t.timeit(number=1))
    done
    3.0032635959996696
    >>> print(t.timeit(number=5))
    done
    done
    done
    done
    done
    15.013195956000345
    >>> 

.. code-block:: python

  >>> import timeit
  >>> timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
  0.2326357249985449

.. code-block:: python

   import time
   def timing(func):
       def wrapper():
           start = time.time()
           func()
           finish = time.time()
           print('Elapsed time: {}'.format(finish - start))
       return wrapper

   @timing
   def f1():
       elements = [1] * 100000
       for _ in range(len(elements)):
           elements.pop()

   @timing
   def f2():
       elements = [1] * 100000
       for _ in range(len(elements)):
           elements.pop(0)

   f1()  # Elapsed time: 0.007998943328857422
   f2()  # Elapsed time: 0.9251341819763184

.. code-block:: python

  import time
  import contextlib

  @contextlib.contextmanager
  def report_time(test):
      """
      Profiling execution
      """
      t0 = time.time()
      yield
      print("Time needed for `%s' called: %.2fs"
            % (test, time.time() - t0))

    # Usage:
    with report_time("run_foo"):
        ...

.. code-block:: python

    import time

    start = time.monotonic()
    time.sleep(0.2)
    end = time.monotonic()

    print("start: {:>9.2f}".format(start))
    print("end: {:>9.2f}".format(end))
    print("span: {:>9.2f}".format(end - start))

.. code-block:: python

    import time

    start = time.perf_counter()
    i = 0
    while i < 100000:
        i = i + 1

    elapsed_time = time.perf_counter() - start
    print("Elapsed time: {}".format(elapsed_time))

Timer
-----

.. code-block:: python

    import signal
    from time import sleep
    import socket

    try:
        TimeoutError
    except NameError:
        # Python2
        TimeoutError = socket.timeout


    class Timeout:
        def __init__(self, seconds, timeout_message=""):
            self.seconds = int(seconds)
            self.timeout_message = timeout_message

        def _timeout_handler(self, signum, frame):
            print(self.timeout_message)
            raise TimeoutError(self.timeout_message)

        def __enter__(self):
            signal.signal(signal.SIGALRM, self._timeout_handler)  # Set handler for SIGALRM
            signal.alarm(self.seconds)  # start countdown for SIGALRM to be raised

        def __exit__(self, exc_type, exc_val, exc_tb):
            signal.alarm(0)  # Cancel SIGALRM if it's scheduled
            return exc_type is TimeoutError  # Suppress TimeoutError


    with Timeout(3, timeout_message="Timeout message!"):
        # Some long running task...
        sleep(10)


Logging
-------

.. code-block:: python

    import logging
    from contextlib import contextmanager


    @contextmanager
    def log(level):
        logger = logging.getLogger()
        current_level = logger.getEffectiveLevel()
        logger.setLevel(level)
        try:
            yield
        finally:
            logger.setLevel(current_level)


    def some_function():
        logging.debug("Debug level information...")
        logging.error("Error...")
        logging.warning("Warning message...")


    with log(logging.DEBUG):
        some_function()


FizzBuzz
--------

.. code-block:: python

  for i in range(1, 101):
     if (i % 3) == 0 and (i % 5) == 0:
        print('FizzBuzz')
     elif (i % 3) == 0:
        print('Fizz')
     elif (i % 5) == 0:
        print('Buzz')
     else:
        print(i)

.. code-block:: python

  for i in range(1,101): print(i,i%3*"FIZZ",i%5*"BUZZ"

  for i in range(1,101): print(bool(i%3)*bool(i%5)*str(i)+(not bool(i%3))*"fizz"+(not bool(i%5))*"buzz")

Time & Dates
------------

.. code-block:: python

  # One year from today
  datetime.date.today() + datetime.timedelta(1*365/12)


.. code-block:: python

  # convert an NYC flight arrival time to a UTC datetime.
  >>> arrival_nyc = '2015-09-15 20:23:24'
  >>> time_format = '%Y-%m-%d  %H:%M:%S'


  >>> nyc_dt_naive = datetime.strptime(arrival_nyc,  time_format)
  >>> eastern = pytz.timezone('US/Eastern')
  >>> nyc_dt = eastern.localize(nyc_dt_naive)
  >>> utc_dt = pytz.utc.normalize(nyc_dt.astimezone(pytz.utc))
  >>> print(utc_dt)

  # convert it to San Francisco local time
  >>> pacific = pytz.timezone('US/Pacific')
  >>> sf_dt = pacific.normalize(utc_dt.astimezone(pacific))
  >>> print(sf_dt)

  # to nepal local time
  >>> nepal = pytz.timezone('Asia/Katmandu')
  >>> nepal_dt = nepal.normalize(utc_dt.astimezone(nepal))
  >>> print(nepal_dt)

  >>>
  2015-09-16 00:23:24+00:00
  2015-09-15 17:23:24-07:00
  2015-09-16 06:08:24+05:45

Normalize utc
-------------

.. code:: python

   from datetime import datetime
   import pytz

   def now_utc_normalize()
       est = pytz.timezone('US/Eastern')
       d = datetime.now(pytz.utc)
       d = est.normalize(d.astimezone(est))
       return d


Compatibly with Python2 and Python3
-----------------------------------

Using six package
~~~~~~~~~~~~~~~~~

.. code:: python


   import six

   if six.PY2:
       # Python 2 code
       print("python2")
   else:
       # Python 3 code
       print("python3")

Using sys package
~~~~~~~~~~~~~~~~~

.. code:: python


   import sys

   if sys.version_info[0] == 3:
       # Python 3 code
   else:
       # Python 2 code

Open file
~~~~~~~~~

.. code:: python

       if sys.version_info[:2] >= (3, 0):
           JSON_DATA = json.load(open("filename.json"))
       else:
           JSON_DATA = json.load(file("filename.json"))

Files
-----

Create file and write content if not exist
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python


       with open('name', 'xt') as f:
           f.write('Hello\n')

Pickle save:
~~~~~~~~~~~~

.. code:: python


       import cPickle as pickle
       with open('data.p', 'wb') as fp:
           pickle.dump(data, fp)

Pickle load:
~~~~~~~~~~~~

.. code:: python


       with open('data.p', 'rb') as fp:
           data = pickle.load(fp)

Iterating over a file
~~~~~~~~~~~~~~~~~~~~~

.. code:: python


       with open('filename.txt') as f:
            for line in f:
                print(line)

Json file
~~~~~~~~~

.. code:: python


   def save_to_json_file(fname, d):
       with open(fname, 'w') as fp:
           json.dump(d, fp)

   def open_json(fname):
       with open(fname) as f:
           return json.load(f)

   def update_json_file(fname, d):
       data = open_json(fname)
       data.update(d)
       save_to_json_file(fname, data)

Http Server
-----------

Python2
~~~~~~~

.. code:: python


       python -m SimpleHTTPServer 8000

Python3
~~~~~~~

.. code:: python


       python -m http.server 8000

Smtp Debugging Server
---------------------

.. code:: sh


       python -m smtpd -n -c DebuggingServer localhost:25

Argaparse
---------

.. code:: python


   import json
   import argparse

   ap = argparse.ArgumentParser()
   ap.add_argument("-f", "--file", required=True, help="Path to json file")
   args = vars(ap.parse_args())

   def read_file(fname):
       with open(fname) as fp:
           try:
               return json.load(fp)
           except ValueError:
               print("Select valid json file")

   data = read_file(args['file'])

.. code:: python

   import argparse

   # Functions here

   if __name__ == "__main__":
       parser = argparse.ArgumentParser(description='Create Marketing Report')
       parser.add_argument('--accounts',
                           action='store_true',
                           help='Process Account Data')
       parser.add_argument('--sales',
                           action='store_true',
                           help='Process Sales Data')
       args = parser.parse_args()
       # Process accounts
       if args.accounts:
           # Do something
       # Process sales
       if args.sales:
           # Do Something

.. code:: python

   parser.add_argument('-v', '--verbose', action='count', default=0)
   parser.add_argument('-q', '--quiet', action='count', default=0)

   logging_level = logging.WARN + 10*args.quiet - 10*args.verbose

   # script -qqq ->         # no logging at all
   # script -vv -> DEBUG    # detailed info
   # script -v -> INFO      # confirmation that things according to plan
   # script -> WARNING      # something unexpected
   # script -q -> ERROR     # some function error
   # script -qq -> CRITICAL # something failed application must close

--------------

Swapping Variables
------------------

.. code:: python


   a, b = b, a

Reversing
---------

.. code:: python


   my_list = [1, 2, 3]

   print(list(reversed(my_list)))

Remove duplicates
-----------------

.. code:: python


   list(set(li)) # create unordered list with no duplicates

Preserve order no duplicates
----------------------------

.. code:: python


   from collections import OrderedDict

   d =  OrderedDict()

   for x in li:

       d[x] = 1

       print(list(d.keys()))


   # or a terrible oneliner:

   from collections import OrderedDict

   print(OrderedDict(zip(li, [1]*len(li))).keys())


   # or

   from collections import OrderedDict

   print(list(OrderedDict.fromkeys(li)))

Inverting a dictionary using zip 
---------------------------------

(i.e create a list with keys and values swapped)

.. code:: python


    dict(zip(di.values(),di.keys()))

    via dictionary comprehension (python >=2.7)

    {v: k for k, v in di.items()}

    dict(map(reversed, di.items()))

Merge dictionary
---------------

Copy and update
~~~~~~~~~~~~~~~

.. code:: python


   context = defaults.copy()
   context.update(user)

Dictionary comprehension
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python


   context = {k: v for d in [defaults, user] for k, v in d.items()}

Dictionary unpacking in Python 3.5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python


   context = {**defaults, **user}

Flattening lists
----------------

.. code:: python


   a=[[1],[2],[3,4],[5,6],[7,8,9]]

   print(list(itertools.chain(*a)))

Sort a list of tuples by 2nd item
---------------------------------

.. code:: python


   from operator import itemgetter

   data = [(1,4,3),(1,2,3),(4,5,6),(7,8,9)]
   data.sort(key=itemgetter(1))

   #alternately with no need to import:

   sorted(data, key = lambda x:x[1])

Unique list that preserves the order 
--------------------------------------------------------

The original order (by first occurrence)

.. code:: python


   first_list = [1,2,5,4,1,3,5]
   unique_order_maintained = sorted(list(set(first_list)),key=lambda x:
   first_list.index(x))

Loading a csv file into a listed dictionary
-------------------------------------------

.. code:: python


   listed_dictionary = list(csv.DictReader(open('filename.csv', 'r')))

Use named tuple instead of a class for simple scenarios
--------------------------------------------------------

.. code:: python


   from collections import namedtuple

   # define new type
   BuildInput = namedtuple('BuildInput', ['name', 'files'])

   # test scenarios
   b1 = BuildInput('test_build_1', ['file1.txt', 'file2.txt'])
   print(b1) # output: BuildInput(name='test_build_1', files=['test1.txt',
   'test2.txt'])

   b2 = BuildInput(name='test_build_2', files=['file3.txt', 'file4.txt'])
   another_b1 = BuildInput(name='test_build_1', files=['file1.txt', 'file2.txt'])

   assert b1 != b2, 'b1 and b2 should be different'
   assert b1 == another_b1, 'b1 and another_b1 should be equal'

Fib generator
-------------

.. code:: python


   def fibgen(numb):
       a, b = 0, 1
       for i in range(0, numb):
           yield f'{i+1} {a}'
           a, b = b, a + b

   for item in fibgen(10):
       print(item)

.. code:: python

  #!/usr/bin/env python3

  import time
  import functools


  @functools.lru_cache(maxsize=128)
  def fibonacci(n):
      if n == 0:
          return 0
      elif n == 1:
          return 1
      return fibonacci(n - 1) + fibonacci(n - 2)


  def timer(method):

      def timed(*args, **kw):
          ts = time.time()
          result = method(*args, **kw)
          te = time.time()

          if 'log_time' in kw:
              name = kw.get('log_name', method.__name__.upper())
              kw['log_time'][name] = int((te - ts) * 1000)
          else:
              print("{}  {:.2f} ms".format(method.__name__, (te - ts) * 1000))
          return result

      return timed


  @timer
  def run():
      print(fibonacci(6))


  run()


Palindrome
----------

.. code-block:: python

    def is_palidrome(s):
        s = "".join(c.lower() for c in s if c != " ")
        return s == s[::-1]

    input_str = input("Pleas enter a word: ")

    if is_palidrome(input_str):
        print("Is palindrome")
    else:
        print("Is not a palindrome")


Example using standard libraries

.. code-block:: python

    from string import punctuation

    def is_palidrome(s):
        s = "".join(c.lower() for c in s if c not in punctuation+" ")
        return s == s[::-1]


Classes
-------

.. _python-2-1:

Python 2
~~~~~~~~

.. code:: python


   #!/usr/bin/env python
   # -*- coding: utf-8 -*-

   class Rectangle(object):

       def __init__(self, width, height):
           self.width = width
           self.height = height
           self.area = width * height

   class Square(Rectangle):

       def __init__(self, length):
           super(Square, self).__init__(length, length)

   s = Square(5)
   print(s.area) #25

.. _python-3-1:

Python 3
~~~~~~~~

.. code:: python


   #!/usr/bin/env python
   # -*- coding: utf-8 -*-

   class Rectangle(object):

       def __init__(self, width, height):
           self.width = width
           self.height = height
           self.area = width * height

   class Square(Rectangle):

       def __init__(self, length):
           super().__init__(length, length)

   s = Square(5)
   print(s.area) #25

Check for one condition
-----------------------

.. code:: python


       if any([user.is_admin, user.is_dude]):
           # Grant Access

Check for all condition
-----------------------

.. code:: python


       if all([user.is_admin, user.is_dude]):
           # Grant Access

Range check
-----------

.. code:: python


       status_code = 200
       if 200 <= status_code <= 299:
           print("HTTP call is success")

Copy a list
-----------

.. code:: python


       colors = ["black", "white", "blue"]
       colors = langs[:]
       new_colors.append("grey")
       print(colors, new_colors)
       # (["black", "white", "blue"],["black", "white", "blue", "grey"])

List comprehension
------------------

.. code:: python


       numbers = [1, 4, 5, 6]
       evens = [numb for numb in numbers if numb % 2 == 0]
       print(evens)
       [4, 6]

Frequency count
---------------

.. code:: python


       from collections import Counter
       frequency = Counter(words)
       print(frequency)
       Counter({'foo': 2, 'a': 1, 'the': 1, 'bar': 1})

Exceptions
----------

.. code:: python


       try:
          foo()
       except (IndexError, KeyError) as e:
           print("something went wrong")

Raising key error in dictionary
-------------------------------

.. code:: python


       #Easier to Ask for Forgiveness than Permission
       try:
           temp = d["foo"]
       except KeyError:
           raise KeyError("foo is missing")

Print to stout 
--------------

.. code:: python

  import sys

  class PrintOutput():
      """
      Print to both standard output and to a log file

      """
      def __init__(self, logfile):
          self.stdout = sys.stdout
          self.log = open(logfile, 'w')

      def write(self, text):
          self.stdout.write(text)
          self.log.write(text)
          self.log.flush()

      def close(self):
          self.stdout.close()
          self.log.close()

  PrintOutput('log.txt')
  print('Somethin to print')

Import module from parent
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    sys.path.insert(0, '../parent_dir')

Download files from web
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import urllib.request

    # Download the file from `url` and save it locally under `file_name`:
    with urllib.request.urlopen(url) as response, open(file_name, 'wb') as
    out_file:
        data = response.read() # a `bytes` object
            out_file.write(data)


Download and extract archives on the fly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import gzip

    # Read the first 64 bytes of the file inside the .gz archive located at `url`
    url = 'http://example.com/something.gz'
    with urllib.request.urlopen(url) as response:
        with gzip.GzipFile(fileobj=response) as uncompressed:
            file_header = uncompressed.read(64) # a `bytes` object
                # Or do anything shown above using `uncompressed`
                instead of `response`.


System version
~~~~~~~~~~~~~~

.. code-block:: python

    class HealthMonitor:
        def __init__(self, settings):
            assert sys.version_info >= (3,5)
            self.sys_type = self.get_sys_type()

        def get_sys_type(self):
            uname = platform.uname()
            if uname.system == 'Darwin':
                return 'Mac'
            elif uname.system == 'Linux':
                with open('/etc/os-release') as f:
                    osrelease = f.read()
                    if 'raspbian' in osrelease.lower():
                        return 'RPi'
                    elif 'ubuntu' in osrelease.lower():
                        return 'Ubuntu'
                    else:
                        return 'Linux'
            else:
                return 'Unknown'

        def reboot_this_computer(self):
            if self.sys_type == 'RPi':  # reboot only if RPi
                print('This is a mock reboot.')


Geolocate ip
------------

.. code:: python

    # wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
    # gunzip GeoLiteCity.dat.gz
    # pip install pygeoip

    import pygeoip
    rawdata = pygeoip.GeoIP('/home/user/GeoLiteCity.dat')
    def ipquery(ip):
        data = rawdata.record_by_name(ip)
        country = data['country_name']
        city = data['city']
        longi = data['longitude']
        lat = data['latitude']
        print('[x] '+str(city)+',' +str(country))
        print('[x] Latitude: '+str(lat)+ ', Longitude: '+ str(longi))

geopy
-----

.. code:: python

  from geopy import distance as geopy_distance

  def geocode_distance((x1, y1), (x2, y2), unit='km'):
     if (x1, y1) == (x2, y2):
         return 0
     d = geopy_distance.distance((x1, y1), (x2, y2))
     if unit == 'miles':
         return d.miles
     else:
         return d.kilometers

is prime number
-----------------

.. code:: python

  import math


  def is_prime(number):
      if number > 1:
          if number == 2:
              return True
          if number % 2 == 0:
              return False
          for current in range(3, int(math.sqrt(number) + 1), 2):
              if number % current == 0:
                  return False
          return True
      return False

  def check_prime_number(num):
      return '{} is prime {}'.format(num, is_prime(num))

  check_prime_number(534)

random user
-----------

.. code:: python

  """Fetch random user"""
  import json
  import requests

  url = 'https://randomuser.me/api/'


  def main():
      res = requests.get(url).json()
      j = json.dumps(res, indent=2)
      print(j)


  if __name__ == '__main__':
      main()
