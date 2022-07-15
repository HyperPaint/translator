console.log("Hello World!");

correctPrograms =
[
"Var a, b, c;\na = 1\nb = 1 / a + a\nc = a - b * b",
"Var a, b, c;\na = a\nb = b\nc = c",
"Var a;\na = 1 + - 1",
"Var algebra;\nalgebra = 0 + - 0\n",
"Var bank;\nbank = 0\nbank = (bank + (1) + 1)",
]

incorrectPrograms =
[
"Var a, b, c\na = 1\nb = 1 / a + a\nc = a - b * b",
"Var a, b, c;\na = a\nb == b\nc = c",
"Var a;\na = 1 + - + - 1\n",
"algebra = 0 + - 0\nVar algebra;",
"Var bank;\nbank = 0\nbank = ((bank + (1)) + 1))",
]

function setCorrectProgram(index)
{
	return correctPrograms[index];
}

function setIncorrectProgram(index)
{
	return incorrectPrograms[index];
}