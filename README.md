Este script te devuelve la lista de bancos que tengan >= cuotas que las configuradas en `my_banks`.

Ejemplos:

```python
my_banks = {
            'Emitida por American Express': 6,
            'HSBC': 6
           }
```

```
$ ./main.py
$
```

```python
my_banks = {
            'Emitida por American Express': 2,
            'HSBC': 6
           }
```

```
$ ./main.py
American Express. Emitida por American Express 3 installments!
$
```
