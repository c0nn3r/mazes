import svgwrite as sw

svg = sw.Drawing(filename='test.svg', size=('100px','100px'))
svg.add(svg.line((25,25), (75,75), stroke=sw.rgb(10,10,10,'%')))
svg.save()