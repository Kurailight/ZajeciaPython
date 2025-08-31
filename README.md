# 📌 ZajeciaPython

Repozytorium zawiera zadania realizowane w ramach nauki języka Python oraz projekt zaliczeniowy:

System_do_notatek_z_wydatkow                                                                                                                                         
Projekt to aplikacja webowa napisana w Pythonie oparta o framework Flask, służąca do zapisywania i zarządzania wydatkami. Umożliwia rejestrację i logowanie użytkowników, dodawanie, edytowanie oraz usuwanie notatek o wydatkach, a także przeglądanie ich w formie listy lub prostego podsumowania. Logika aplikacji została oparta o programowanie obiektowe, a dane przechowywane są w bazie SQLite za pomocą SQLAlchemy. Kod został napisany zgodnie ze standardem PEP8 (użyto narzędzi flake8 (formatowanie, stylistyczne), black (formatowanie), pylint (logika, jakość). W projekcie dostarczono plik Dockerfile umożliwiający zbudowanie obrazu Dockera i uruchomienie aplikacji. Ponadto użyto testów jednostkowych oraz integracyjnych z użyciem pytest.                                                                                                         
                                                                                                
**Instrukcja uruchomienia lokalnego:**                                                                               
1. Klonowanie repozytorium                                                              
git clone https://github.com/Kurailight/ZajeciaPython.git                                                     
cd ZajeciaPython                                                         
2. Utworzenie i aktywacja środowiska wirtualnego                                                                
python -m venv virtenv                                                                                                                                              
Windows: virtenv\Scripts\activate
3. Instalacja zależności                                                                   
pip install -r requirements.txt                                                  
4. Ustawienie zmiennych środowiskowych w cmd                                                                
set FLASK_APP=run.py                                                                                                               
set SECRET_KEY=klucz                                                                                                                                   
5. Uruchomienie aplikacji                                                           
flask run

**Zbudowanie i uruchomienie obrazu Dockera:**
1. Klonowanie repozytorium                                                                        
git clone https://github.com/Kurailight/ZajeciaPython.git                                              
cd ZajeciaPython                                                            
2. Budowanie obrazu Dockera                                                           
docker build -t system-do-notatek-z-wydatkow .                                                                
3. Uruchomienie kontenera                                                           
docker run -d -p 5000:5000 system-do-notatek-z-wydatkow                                                                   
4. Dostęp do aplikacji                                                                
http://localhost:5000
