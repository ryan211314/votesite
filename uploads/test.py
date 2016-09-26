import win32com.client
app=win32com.client.DispatchEx('Word.Application')
doc=app.Documents.Open('1.docx')
app.Visible = True
app.ScreenUpdating = True


find=app.Selection.Find
find.Text=u'@ss@'
find.Replacement.Text=u'ad'
find.Execute(Replace=2)

doc = Document(filename)
doc.paragraphs
doc.tables[0].rows[0].cells[].text


