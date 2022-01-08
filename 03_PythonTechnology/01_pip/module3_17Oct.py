'''
python --version: prezinta versiunea de python
Python 3.7.4
X.Y.Z
X -> major revision:
Y -> minor revision:
Z -> Bug | Patch revision:

Pip - reprezinta managerul prin care se instaleaza package-rui
PyPi - locul (serverul) de unde pip aduce packager-urile

1. python -m pip list                       : listeaza toate package
2. python -m pip install Django             : instaleaza package-ul Django
3. python -m pip install Django==3.0.1      : instaleaza o versiune specifica
4. python -m pip install --upgrade Django   : aduce package-ul instalat la ultima versiune
5. python -m pip show Django                : afiseaza informatii despre packege-ul instalat
6. python -m pip uninstall Django           : dezinstaleaza package-ul Django
7. python -m pip freeze > lista.txt         : genereaza o lista fizica cu toate package-urile instalate
8. python -m pip install -r lista.txt       : va parcurge lista si va instala fiecare package din ea

'''