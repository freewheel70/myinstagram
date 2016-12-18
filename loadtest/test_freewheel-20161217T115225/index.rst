======================
FunkLoad_ bench report
======================


:date: 2016-12-17 11:52:25
:abstract: Simply testing a default static page
           Bench result of ``Simple.test_freewheel``: 
           No test description

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents
.. |APDEXT| replace:: \ :sub:`1.5`

Bench configuration
-------------------

* Launched: 2016-12-17 11:52:25
* From: ip-172-31-18-197
* Test: ``test_Simple.py Simple.test_freewheel``
* Target server: http://52.221.228.19:8037/api
* Cycles of concurrent users: [10, 50, 100, 500]
* Cycle duration: 10s
* Sleeptime between request: from 0.0s to 0.5s
* Sleeptime between test case: 0.01s
* Startup delay between thread: 0.01s
* Apdex: |APDEXT|
* FunkLoad_ version: 1.16.1


Bench content
-------------

The test ``Simple.test_freewheel`` contains: 

* 1 page(s)
* 0 redirect(s)
* 2 link(s)
* 0 image(s)
* 0 XML RPC call(s)

The bench contains:

* 1453 tests
* 1457 pages
* 4458 requests


Test stats
----------

The number of Successful **Tests** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ================== ================== ================== ================== ==================
                CUs               STPS              TOTAL            SUCCESS              ERROR
 ================== ================== ================== ================== ==================
                 10              4.400                 44                 44             0.00%
                 50             14.500                145                145             0.00%
                100             17.400                174                174             0.00%
                500            109.000               1090               1090             0.00%
 ================== ================== ================== ================== ==================



Page stats
----------

The number of Successful **Pages** Per Second (SPPS) over Concurrent Users (CUs).
Note that an XML RPC call count like a page.

 .. image:: pages_spps.png
 .. image:: pages.png

 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                CUs             Apdex*             Rating               SPPS            maxSPPS              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                 10              0.975          Excellent              4.400             12.000                 44                 44             0.00%              0.008              0.677              5.158              0.011              0.097              3.725              4.100
                 50              0.952          Excellent             14.500             21.000                145                145             0.00%              0.007              1.457              6.118              0.009              0.302              5.094              5.564
                100              0.954          Excellent             17.300             41.000                173                173             0.00%              0.007              1.100              8.106              0.009              0.200              5.765              6.248
                500              0.916               Good            109.500            137.000               1095               1095             0.00%              0.007              1.671              9.232              0.011              0.209              5.141              5.567
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

 \* Apdex |APDEXT|

Request stats
-------------

The number of **Requests** Per Second (RPS) successful or not over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png

 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                CUs             Apdex*            Rating*                RPS             maxRPS              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                 10              0.960          Excellent             13.800             30.000                138                138             0.00%              0.008              0.389              5.057              0.009              0.024              0.359              3.678
                 50              0.920               Good             44.500             58.000                445                445             0.00%              0.007              0.807              6.070              0.008              0.022              4.052              4.800
                100              0.834               FAIR             57.000            113.000                570                570             0.00%              0.007              1.302              9.151              0.008              0.064              5.871              6.842
                500              0.849               FAIR            330.500            449.000               3305               3305             0.00%              0.007              1.286             17.507              0.010              0.041              4.715              5.441
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

 \* Apdex |APDEXT|

Slowest requests
----------------

The 5 slowest average response time during the best cycle with **500** CUs:

* In page 001, Apdex rating: FAIR, avg response time: 2.26s, link: ``/bootstrap/3.3.0/css/bootstrap.min.css``
  ``
* In page 001, Apdex rating: FAIR, avg response time: 1.54s, link: ``/bootstrap/3.3.0/css/bootstrap-theme.min.css``
  ``
* In page 001, Apdex rating: Excellent, avg response time: 0.02s, post: ``/api/search/image``
  `Search keyword`

Page detail stats
-----------------


PAGE 001: Search keyword
~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url ``/api/search/image``

     .. image:: request_001.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                     10              1.000          Excellent                 44                 44             0.00%              0.008              0.009              0.014              0.008              0.009              0.011              0.013
                     50              1.000          Excellent                145                145             0.00%              0.007              0.009              0.017              0.008              0.008              0.011              0.014
                    100              1.000          Excellent                173                173             0.00%              0.007              0.009              0.023              0.008              0.009              0.013              0.014
                    500              1.000          Excellent               1095               1095             0.00%              0.007              0.017              0.105              0.008              0.015              0.031              0.036
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|
* Req: 002, link, url ``/bootstrap/3.3.0/css/bootstrap.min.css``

     .. image:: request_001.002.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                     10              0.980          Excellent                 49                 49             0.00%              0.018              0.303              4.951              0.022              0.044              0.324              0.830
                     50              0.866               Good                157                157             0.00%              0.013              1.350              5.908              0.021              0.286              4.576              5.085
                    100              0.695               POOR                218                218             0.00%              0.013              2.374              9.151              0.023              0.761              6.954              7.411
                    500              0.742               FAIR               1152               1152             0.00%              0.015              2.255             17.507              0.025              0.523              5.690              7.167
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|
* Req: 003, link, url ``/bootstrap/3.3.0/css/bootstrap-theme.min.css``

     .. image:: request_001.003.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                     10              0.900               Good                 45                 45             0.00%              0.009              0.853              5.057              0.011              0.045              3.678              4.769
                     50              0.899               Good                143                143             0.00%              0.009              1.021              6.070              0.011              0.035              4.470              5.099
                    100              0.844               FAIR                179                179             0.00%              0.009              1.245              7.326              0.012              0.179              5.346              6.322
                    500              0.810               FAIR               1058               1058             0.00%              0.008              1.545             11.854              0.014              0.279              4.715              5.083
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|

Definitions
-----------

* CUs: Concurrent users or number of concurrent threads executing tests.
* Request: a single GET/POST/redirect/xmlrpc request.
* Page: a request with redirects and resource links (image, css, js) for an html page.
* STPS: Successful tests per second.
* SPPS: Successful pages per second.
* RPS: Requests per second, successful or not.
* maxSPPS: Maximum SPPS during the cycle.
* maxRPS: Maximum RPS during the cycle.
* MIN: Minimum response time for a page or request.
* AVG: Average response time for a page or request.
* MAX: Maximmum response time for a page or request.
* P10: 10th percentile, response time where 10 percent of pages or requests are delivered.
* MED: Median or 50th percentile, response time where half of pages or requests are delivered.
* P90: 90th percentile, response time where 90 percent of pages or requests are delivered.
* P95: 95th percentile, response time where 95 percent of pages or requests are delivered.
* Apdex T: Application Performance Index, 
  this is a numerical measure of user satisfaction, it is based
  on three zones of application responsiveness:

  - Satisfied: The user is fully productive. This represents the
    time value (T seconds) below which users are not impeded by
    application response time.

  - Tolerating: The user notices performance lagging within
    responses greater than T, but continues the process.

  - Frustrated: Performance with a response time greater than 4*T
    seconds is unacceptable, and users may abandon the process.

    By default T is set to 1.5s this means that response time between 0
    and 1.5s the user is fully productive, between 1.5 and 6s the
    responsivness is tolerating and above 6s the user is frustrated.

    The Apdex score converts many measurements into one number on a
    uniform scale of 0-to-1 (0 = no users satisfied, 1 = all users
    satisfied).

    Visit http://www.apdex.org/ for more information.
* Rating: To ease interpretation the Apdex
  score is also represented as a rating:

  - U for UNACCEPTABLE represented in gray for a score between 0 and 0.5 

  - P for POOR represented in red for a score between 0.5 and 0.7

  - F for FAIR represented in yellow for a score between 0.7 and 0.85

  - G for Good represented in green for a score between 0.85 and 0.94

  - E for Excellent represented in blue for a score between 0.94 and 1.

Report generated with FunkLoad_ 1.16.1, more information available on the `FunkLoad site <http://funkload.nuxeo.org/#benching>`_.