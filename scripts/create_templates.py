typical_problems = [('Stress', 'stress'), ('Relations with in-laws', 'relations_with_in_laws'), ('Money', 'money'), ('Sex', 'sex'), ('Housework', 'housework'), ('Becoming parents', 'becoming_parents')]
typical_problem_html = """<html>
<head>
<title>Solve %s Problems | InfluenceAPI</title>
<script src="/static/js/jquery-1.9.1.min.js"></script>
<link rel="stylesheet" type="text/css" href="/static/css/screen.css" />

</head>
<body>
<h2>Solve %s Problems</h2>
<ul id="subnav">
<li><a href="/marriage/love_map/">Love map</a></li>
<li><a href="/marriage/foundness_and_admiration/">Fondness and admiration</a></li>
<li><a href="/marriage/turn_toward/">Turn toward</a></li>
<li><a href="/marriage/accept_influence/">Accept influence</a></li>
<li><a href="/marriage/solve_solvable_problems/" class="current">Solve solvable problems</a>
<ul>
<li><a href="/marriage/solve_solvable_problems/typical_problems/" class="current">Typical problems</a></li>
<ul>
%s
</ul>
</li>
<li><a href="/marriage/overcome_gridlock/">Overcome gridlock</a></li>
<li><a href="/marriage/create_shared_meaning/">Create shared meaning</a></li>
</ul>
</li>
</ul>
</div>
</body>
</html>"""
for problem in typical_problems:
    nav = ''
    for p in typical_problems:
        if p == problem:
            nav += '<li><strong>%s</strong></li>\n' % (p[0])
        else:
            nav += '<li><a href="/marriage/solve_solvable_problems/typical_problems/%s/">%s</a></li>\n' % (p[1], p[0])
    html = typical_problem_html % (p[0], p[0], nav)
    import os
    f = open('/home/timtim/influenceapi/templates/marriage/solve_typical_problems_%s.html' % (problem[1]), 'w')
    f.write(html)
    f.close()
