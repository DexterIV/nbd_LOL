# Opis restAPI

## 1. Zwracanie gier z tabeli ``plays``.
   __parametry__: liczba rekordów ( >= 1 i całkowita)
   __wywołanie__: ``/league?number={liczba_rekordów}``
   __metoda__: ``GET``
   __przykładowa odpowiedź__:
   
```
  [
    [
        "3483133404",
        "{\"gameId\":3483133404,\"platformId\":\"EUW1\",\"gameCreation\":
        1515166293636,\"gameDuration\":2441,\"queueId\":420,\"mapId\":11,\"
        seasonId\":9,\"gameVersion\":\"7.24.212.5337\",\"gameMode\":\"CLASSIC\",
        \"gameType\":\"MATCHED_GAME\",\"teams\":[{\"teamId\":100,\"win\":\"Fail\
        .....
```
  __kody błędów__: 
  ```500``` - brak parametru lub błędny parametr
  
## 2. Dodanie gry to tabeli ``plays``.

   __parametry__: brak
   __wywołanie__: ``/league/``
   __metoda__: ``POST``
   __body__: JSON
   
```
{
	"gameid": "123455",
	"datablob": "przykładowa gra"
}
```
   __odpowiedź__:
   
```
 <html>
    <body>
        <h1>Success</h1>
    </body>
</html>
```
  __kody błędów__: 
  ```500``` - błędny json
  
## 3. Usunięcie rekordu z tabeli ``plays``

   __parametry__: brak
   __wywołanie__: ``/league/``
   __metoda__: ``DELETE``
   __body__:
   
   ```
   {
	"gameid": "111"
}
   ```
   __odpowiedź__:
   
```
 <html>
    <body>
        <h1>Success</h1>
    </body>
</html>
```
  __kody błędów__: 
  ```500``` - próba usunięcia nieistiejącego obiektu, niepoprawne lub brak argumentów


## 4. Zmiana rekordu w tabeli ``plays``

  __parametry__: brak
   __wywołanie__: ``/league/``
   __metoda__: ``PUT``
   __przykład body__: JSON
   
  ```
  {
	"gameid": "111",
	"column_name": "datablob",
	"value": "nowa wartość"
}
  ```
   __odpowiedź__:
   
```
 <html>
    <body>
        <h1>Success</h1>
    </body>
</html>
```
  __kody błędów__: 
  ```500``` - próba usunięcia nieistiejącego obiektu, niepoprawne lub brak argumentów

## 5. Wyświetlenie jednej gry z tabeli ``plays``

  __parametry__: brak
  __wywołanie__: ``/league/gameid``
  __metoda__: ``GET``
  __przykładowa odpowiedź__:
   
```
  [
    [
        "3483133404",
        "{\"gameId\":3483133404,\"platformId\":\"EUW1\",\"gameCreation\":
        1515166293636,\"gameDuration\":2441,\"queueId\":420,\"mapId\":11,\"
        seasonId\":9,\"gameVersion\":\"7.24.212.5337\",\"gameMode\":\"CLASSIC\",
        \"gameType\":\"MATCHED_GAME\",\"teams\":[{\"teamId\":100,\"win\":\"Fail\
        .....
```
  __kody błędów__: 
  ```500``` - próba usunięcia nieistiejącego obiektu, niepoprawne lub brak argumentów
  
  
## 6. Strona główna 

  __parametry__: brak
  __wywołanie__: ``/``
  __metoda__: ``GET``
  __odpowiedź__:
   
```
<html>
    <body>
        <h1>Nierelacyjne bazy danych</h1>
    </body>
</html>
```

