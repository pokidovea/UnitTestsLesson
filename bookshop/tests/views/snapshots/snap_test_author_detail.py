# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_correct_response 1'] = '''<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <title>Bookshop
    - author
</title>

    

    
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-light bg-light mb-5">
    <div class="container-fluid">
        <a class="navbar-brand" href="/">Bookshop</a>

    </div>
</nav>


    <div class="container">
        <div class="row">
            <h1 class="col">Vasya (1987-...)</h1>
        </div>
        <div class="row align-items-center">
            <div class="col-4">
                <img src="/media/images/vasya.png" alt="" class="img-thumbnail">
            </div>
            <div class="col-8">
                <div class="row">
                    <div class="col-4 px-0">Country:</div>
                    <div class="col-8">
                        Russia
                    </div>
                </div>
                <div class="row">
                    <div class="col-4 px-0">Bio:</div>
                    <div class="col-6">Test</div>
                </div>
                <div class="row">
                    <div class="col-4 px-0">Books:</div>
                    <div class="col-8">
                        
                    </div>
                </div>
            </div>
        </div>
    </div>

</body>
</html>
'''
