===================================================================
Using JSON API to create, retrieve, update and delete WCC Documents
===================================================================

Implementation is using plone.jasonapi.routes

https://github.com/ramonski/plone.jsonapi.routes

Testing can be done using Advanced REST Client for Chrome
https://chrome.google.com/webstore/detail/advanced-rest-client/hgmloofddffdnphfgcellkdfbfbjeloo

Retrieving WCC Documents
========================

Return a list of all wcc.document added to a site in JSON format
----------------------------------------------------------------

http://10.1.1.4:8080/Plone/@@API/plone/api/1.0/wccdocuments

Return JSON details of specific wcc.document
--------------------------------------------

For each wcc.document in the list above, there is a uid api link, which
will return JSON values for specific document. This uid will also be
used for updating and delete calls.

http://10.1.1.4:8080/Plone/@@API/plone/api/1.0/wccdocuments/ab94a476a46d47869710ee9a61067149

Adding/Creating WCC Document
============================

First we need to know the uid of folder to create the document. Add a
normal Plone folder, can call it myfolder

Return a list of all folders and find the uid for myfolder folder:

http://10.1.1.4:8080/Plone/@@API/plone/api/1.0/folders

This uid will be used as the reference container when adding
wcc.documents

In Advanced REST Client:

1. URL to post is link to API with create and uid of folder at the end

eg.

http://10.1.1.4:8080/Plone/@@API/plone/api/1.0/wccdocuments/create/409f6df1028c490da8ca20c031f634f0

Method is POST (radio button)


Working test example:

{
    "title" : "Test Documents",
    "effective" : "2001-05-11",
    "expires" : "2015-12-11",
    "description" : "Just a document description" ,
    "subjects": ["physics", "maths"],
    "document_type": "Letter",
    "document_owner": "WCC Presidents",
    "text": "<h3>dota my ass</h3>\n<p>Busan, 30 October to 8 November 2013</p>\n<p>I am pleased to send greetings to all participants at the 10th Assembly of the World Council of Churches. I applaud the WCC for its work with the United Nations to advance our common goals.",

    "related_links": [{"url": "http://www.google.com", "description": "rosmah", "label": "bn"}, {"url": "http://www.yahoo.com", "description": "nik aziz", "label": "haron din"}],
    "file": {"filename": "wcc.zip", "data": "UEsDBBQDAAAIAPaSmUSo5CIlUAQAAGIIAAAHAAAAd2NjLnR4dG1Vy47UMBC88xWtOYdleAohhAR7QkKAEIgDIOQ4naRZx7b8mCEg/p1qZxiWx2o1k3G3y9XV1c73G4S/XZHieEePaHcs467bFnkc2RY5bIE7+/3tm/v7N2/fPse/RkmcT9HbCN25Fh042ySxSPAtI4aEh1Mw1/4LsPMOgYf7/XlPsHVhXz6XNbLGXnApnP4Jh6PnpPH3l5f0GhxkwHL+lVf4a9Ho4/nukyEUQ8tKJufHt/D7o38cnzyr2fiO7u7plS2h50Ql0EN6GQ686C9Uc/fxrbglPyezUHRsMg+al9kPNCXmIn7KumKco2hSESvRgAeZQmVmur0vMz3NGaBupTC2xfchuYEuQ/VWnC5ezjXZmfMF4aQYnalDS9TaxpBIAHgM6YqOAjiNvPNSwOWlUXE3BsPBeMsUaiIbliV4moJx+eJcxStEgOK0hMGsJJl6zlyoX8nOqID9xBnw4G5TyJkmDlMycRZrXEe2ulKTcWRQfWInk4SayYlX5pdOFlNYkQDTUYSSqawdsT9ICl67hr0DA3FotIEY/OjEloYYUFfC6YlNychbdNHQ5EKPfehwRKWsZCeFboAZwgc/NV02gNYFWCN3JN66OgjCPvib503KIqTJePm2qfdXPVMKNV6T7Sm0Z7TBIgZR+xTMcGJ1TbZOk5aaCwhAThdA1cC5Xo/Q/kQO0WEt0xXDi1NjH8aTXhf05regbAYUQNZ4ms2BCd/sQ1o0KFCscmu0VydIAjXnwrGV3CRLDC7O3YSP7ObXmV0EcZXC9KFC79OxgKNF/AAX/Gq88Y1Ao5zQfs5Zs3KwwmW9oGcr5ZiQoWgLoihFC2kdYls6dV/ErKHuxsdB+K5ZecEUnArTpN7AejKFktaWiOMTD1sRY8iFE01qhjabjpPauwVLgs6/G/T2CC3Xm6OkDP54rgDERidFQC1XO6vsDLeFRSyqKTDhyYKLnB5phIjNC385FtssJ9ikem2LDdB3Dsdzv9tgmm1g2iUkZd2GArSVh53bUObZoLxtKDsaU1hUsuAOEPI8CW0PL1H7qetrqPjcvIPQ1kQN6CUQQ0iN8KE6D316pw1t0C2+mITcfE2pf2+Op86JCtuuITmIO08Fun9APZCE4KQywoB0xITx9fnrKP3t2476mrX8zJucVmF/GWgbLyQ1twjGZwXXkBlAEXoA9O+6u2aYXBSrRgKRbbQzcAHYPD8ZFFoIt37iRfJyce3utsAqpG50etsqNqRUyUuSvhYVFhwkE48A1/uwTQx4aMQZZcg4FwbYtAHKZsLNq0kYIzRLxCGQSOwMczTSfRU3ACEXaeWYzcGqLcpPSl88hV8X84k1XmI3ttcYxDXo1mfY6UrflB++72pyeNhNZt11f75isZox1KZowJmeW6LxR5N2Pzo6b72SxVz9Z/MXM5j5j71wrFl2Pz51G5tRHGP5e3vwZuEz/sU3iQ3RFKOLvcn84N7ux40b+L/xE1BLAQI/AxQDAAAIAPaSmUSo5CIlUAQAAGIIAAAHAAAAAAAAAAAAIIC0gQAAAAB3Y2MudHh0UEsFBgAAAAABAAEANQAAAHUEAAAAAA=="}

}

2. For updating
   - get the uid for the wccdocument using
     http://10.1.1.4:8080/Plone/@@API/plone/api/1.0/wccdocuments/
   - then append the uid behind to get to the specific wccdocument
     http://10.1.1.4:8080/Plone/@@API/plone/api/1.0/wccdocuments/06e8be0abb894ac4a88d32689c9c3fb9
   - use the same json format as the one used for creating wccdocument to update


3. For deleting
   - get the uid for the wccdocument
     http://10.1.1.4:8080/Plone/@@API/plone/api/1.0/wccdocuments/
   - append delete before the uid
     http://10.1.1.4:8080/Plone/en/@@API/plone/api/1.0/wccdocument/delete/06e8be0abb894ac4a88d32689c9c3fb9


How to authenticate
===================
- Authentication use basic HTTP basic authentication

- To authenticate the header must have 

        Authorization: Basic userid:password

  in the header where "userid:password" is encoded in base64

- http://publib.boulder.ibm.com/infocenter/cicsts/v3r2/index.jsp?topic=%2Fcom.ibm.cics.ts.internet.doc%2Ftopics%2Fdfhtl2a.html


Example Using Python
====================
This example use python library "requests" to post the data

.. code-block:: python
    import request
    import json

    #for getting data
    payload = {'title': u'some new title'}
    headers = {'Content-type': 'application/json'}

    #request will auto encrypt it to base64
    auth = {'admin', 'password'}


    get_data = request.get("http://10.1.1.4:8080/Plone/en/@@API/plone/api/1.0/wccdocument", 
                          headers=headers, auth=auth)


    post_data = request.post("http://kulll:8080/Plone/en/@@API/plone/api/1.0/wccdocument/update/2a3bb9bc02264da7bf8f874d50bad69a", headers=headers, data=json.dumps(payload), auth=auth)




Multilingual
=============

Language should work when uploading in correct language folder structure
eg. sitename/de/Document as it using uids when referencing parent


 Known Bugs
==========

- currently using workaround for dexterity behaviours which doesnt work
  normally

-  wcc title, description, tags  using behaviours.
  https://github.com/ramonski/plone.jsonapi.routes/issues/9

- file doesn't work well with NamedBlobFiles
  https://github.com/ramonski/plone.jsonapi.routes/issues/10

- security is not enabled yet (http auth)
