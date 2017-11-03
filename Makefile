report.pdf : main.tex ODE.py
	python3 ODE.py
	pdflatex main.tex
