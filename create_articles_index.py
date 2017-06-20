#!/usr/bin/env python

import sys
import site_common as site_common

html_source = ''
html_source += '<div class="container">'
html_source += "<h1>Publications</h1>"
html_source += "<p>Below are some of the publications and articles I have written.</p>"

def extract_title(md_file):
    # extract the title of a post, from the first line in the file.
    with open(md_file, 'r') as f:
        first_line = f.readline()

    # skip hash and any whitespace in beginning.
    for i, c in enumerate(first_line):
        if not c.isspace() and c != "#":
            # found beginning of title
            return first_line[i:]

    return "Invalid Title!"

html_source += "<ul>"
html_source += "<li>J. Berntsson, N. Lin, and Z. Dezso, 'ExtSim: A Flexible Data Mapping and Synchronization Middleware for Scientific Visualization in Virtual Worlds,' in Journal of Virtual Worlds Research, issue 5, vol 2, pp. 4-13: Virtual Worlds Institute, 2010.</li>"
html_source += "<li><a href=\"http://eprints.qut.edu.au/16242/\">J. Berntsson, 'An Adaptive Framework for Internet-based Distributed Genetic Algorithms,' PhD Thesis, Faculty of Information Technology, Queensland University of Technology</a></li>"
html_source += "<li>J. Berntsson, 'G2DGA: An Adaptive Framework for Internet-based Distributed Genetic Algorithms,' in Proceedings of the Genetic and Evolutionary Computation Conference Workshop, pp. 346-349: ACM Press, 2005.</li>"
html_source += "<li>J. Berntsson and M. Tang, 'Dynamic Optimization of Migration Topology in Internet-based Distributed Genetic Algorithms,' in Proceedings of the Genetic and Evolutionary Computation Conference, vol. 2, pp. 1579-1580: ACM Press, 2005.</li>"
html_source += "<li>J. Berntsson and M. Tang, 'Adaptive Sizing of Populations and Number of Islands in Distributed Genetic Algorithms,' in Proceedings of the Genetic and Evolutionary Computation Conference, vol. 2, pp. 1575-1576: ACM Press, 2005.</li>"
html_source += "<li>J. Berntsson and M. Tang, 'A Comparative Study of Internet-based Parallel Distributed Genetic Algorithms.,' in Proceedings of the International Conference on Computational Intelligence for Modelling, Control & Automation, pp. 834-844: University of Canberra, 2004.</li>"
html_source += "<li>J. Berntsson and M. Tang. 'A Slicing Structure Representation for the Multi-Layer Floorplan Layout Problem,' in Applications of Evolutionary Computing: Proceedings of Evo Workshops 2004, Lecture Notes in Computer Science, vol. 3005., pp 188-197: Springer, 2004.</li>"
html_source += "<li>J. Berntsson and M. Tang, 'A Convergence Model for Asynchronous Parallel Genetic Algorithms,' in Proceedings of the Congress on Evolutionary Computation, vol. 4., pp. 2627-2634: IEEE-Press, 2003.</li>"
html_source += "<li>J. Berntsson and P. Lundberg, 'Evaluation of Case-based Reasoning Applied to Autoclave Curing,' M. Sc Thesis LiTH-IDA-Ex-9345, Linkoping, Sweden, 1994</li>"
html_source += "</ul>"
html_source += '</div>'

#html_source += "<ul>"
#for md_file in site_common.posts:
#
#    post_title = ""
#    if len(md_file) == 2:
#        post_title = md_file[1]
#    else:
#        post_title = extract_title(md_file)
#
#    html_file = ""
#    if len(md_file) == 2:
#        html_file = "posts/"+md_file[0][4:-5] + '.html'
#    else:
#        html_file = site_common.get_html_file(md_file)
#
#
#    html_source += "<li> <a href=\"{0}\">{1}</a>  </li>".format(
#        html_file,post_title )
#html_source += "</ul>"
#
#html_source += '</div>'

with open('src/template.html', 'r') as f:
    template=f.read()

output_file = "articles.html"

src = template.format(src=html_source)

with open(output_file, 'w') as f:
     f.write(src)
