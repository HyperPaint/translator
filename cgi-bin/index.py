import sys
import codecs

# замена кодировки вывода
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

import cgi
import cgitb

cgitb.enable()

# сохранение всех значений, полученных из формы в переменную
form = cgi.FieldStorage()
# стандартное значение для пустого значения
none = ""

# шаблон страницы
template = """
<!DOCTYPE HTML>
<html>
    <head>
        <meta charset="utf-8">
        <link rel = "stylesheet" href = "./../style.css">
        <script src = "./../script.js"></script>
    </head>
    <body>
        <h1>Транслятор</h1>
        
        <form method = "post" action = "./index.py">
            <div class = "flex-vertical-space">
                
                <div class = "flex-horizontal-space">
                    <input type = "submit" id = "translate" value = "Перевести">
                    <input type = "button" id = "reset" value = "Стереть">
                </div>

                <div class = "flex-horizontal-space">
                    <textarea class = "big-vh" name = "program" id = "program">{1}</textarea>
                    <textarea disabled class = "big-vh" name = "result-program" id = "result-program">{2}</textarea>
                </div>
            </div>
        </form>
        
        <h2>Готовые верные программы</h2>
        <div class = "flex-horizontal-space">
            <input type = "button" value = "Нажать 1" id = "programT1">
			<input type = "button" value = "Нажать 2" id = "programT2">
			<input type = "button" value = "Нажать 3" id = "programT3">
			<input type = "button" value = "Нажать 4" id = "programT4">
			<input type = "button" value = "Нажать 5" id = "programT5">
		</div>
        
        <h2>Готовые неверные программы</h2>
        <div class = "flex-horizontal-space">
			<input type = "button" value = "Нажать 1" id = "programF1">
			<input type = "button" value = "Нажать 2" id = "programF2">
			<input type = "button" value = "Нажать 3" id = "programF3">
			<input type = "button" value = "Нажать 4" id = "programF4">
			<input type = "button" value = "Нажать 5" id = "programF5">
		</div>
        
        <script>
            document.getElementById("reset").addEventListener("click", () => document.getElementById("program").value = "");
        
            document.getElementById("programT1").addEventListener("click", () => document.getElementById("program").value = setCorrectProgram(0));
            document.getElementById("programT2").addEventListener("click", () => document.getElementById("program").value = setCorrectProgram(1));
            document.getElementById("programT3").addEventListener("click", () => document.getElementById("program").value = setCorrectProgram(2));
            document.getElementById("programT4").addEventListener("click", () => document.getElementById("program").value = setCorrectProgram(3));
            document.getElementById("programT5").addEventListener("click", () => document.getElementById("program").value = setCorrectProgram(4));
            
            document.getElementById("programF1").addEventListener("click", () => document.getElementById("program").value = setIncorrectProgram(0));
            document.getElementById("programF2").addEventListener("click", () => document.getElementById("program").value = setIncorrectProgram(1));
            document.getElementById("programF3").addEventListener("click", () => document.getElementById("program").value = setIncorrectProgram(2));
            document.getElementById("programF4").addEventListener("click", () => document.getElementById("program").value = setIncorrectProgram(3));
            document.getElementById("programF5").addEventListener("click", () => document.getElementById("program").value = setIncorrectProgram(4));
        </script>
        
        {0}
    </body>
</html>
"""

bodyAppend = ""

# сборка body и отправка клиенту
def makeBody(append, data, resultProgram):
    # говорим браузеру что далее следует html документ
    print("Content-type: text/html\n")
    # даём html документ
    print(template.format(append, data, resultProgram))

# сборка таблицы
def makeTable(tableName, theadData, tbodyData):
    global bodyAppend
    bodyAppend += "<h2>{0}</h2>".format(tableName)
    bodyAppend += "<table class = \"table\">"
    bodyAppend += "<thead>"
    bodyAppend += "<tr>"
    for rowName in theadData:
        bodyAppend += "<th><p>{0}</p></th>".format(str(rowName))
    bodyAppend += "</tr>"
    bodyAppend += "</thead>"
    bodyAppend += "<tbody>"
    for rowData in tbodyData:
        bodyAppend += "<tr>"
        for cellData in rowData:
            bodyAppend += "<td><p>{0}</p></td>".format(str(cellData))
        bodyAppend += "</tr>"
    bodyAppend += "</tbody>"
    bodyAppend += "</table>"

data = form.getfirst("program", none)
if data == none:
    # сборка страницы и отправка клиенту
    makeBody("", "", "")
else:
    import lexer
    resultLex = lexer.analyze(data)
    makeTable("Лексический анализ", ("Тип", "Значение", "Строка"), resultLex)
    import yacc
    resultProgram, resultYacc = yacc.analyze(data, resultLex)
    makeTable("Синтаксический анализ", ("Терминал", "Статус", "Строка"), resultYacc)
    # сборка страницы и отправка клиенту
    makeBody(bodyAppend, data, resultProgram)
