# -*- coding:utf-8 -*-
class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]
    def collectdata(self, new_data):
        if new_data is None:
            return
        self.datas.append(new_data)

    def output_html(self):
        myfile=open('output.html','w')
        myfile.write('<html>')

        myfile.write('<body>')
        myfile.write('<table>')
        for data in self.datas:
            myfile.write('<tr>')
            myfile.write('<td>%s</td>'%data['url'])
            myfile.write('<td>%s</td>' % data['title'].encode('utf-8'))
            myfile.write('<td>%s</td>' % data['summary'].encode('utf-8'))
            myfile.write('</tr>')
        myfile.write('</table>')
        myfile.write('</body>')
        myfile.write('</html>')
        myfile.close()