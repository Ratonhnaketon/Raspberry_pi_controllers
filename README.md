# Controladores para Raspberry pi 

Este projeto facilita a automatização de projetos IoT (Internet das Coisas) numa placa Raspberry usando python 2
Se baseia no próprio prinpício de um sistema IoT: vários componentes que conversam com um componente central.
Este projeto define isso por controlador mestre e controlador escravo. Precisa de pelo menos 1 controlador mestre para funcionar.

# Classes

* ### [MasterController](https://github.com/Ratonhnaketon/Raspberry_pi_controllers/blob/master/Core/masterController.py)

  Define o controlador mestre.<br>
####	Declaração
```python
<ControllerName>(MasterController):  
def __init__(self, ...variables):  
	MasterController.__init__(self)
```  

* ### [SlaveController](https://github.com/Ratonhnaketon/Raspberry_pi_controllers/blob/master/Core/slaveController.py)

  Define o controlador escravo.<br/>
####	Declaração  
```python
<ControllerName>(SlaveController):  
	def __init__(self, ...variables):  
		SlaveController.__init__(self)
```

####	Métodos:   
```python 
assignPins(pins: list) return None    
setPin(pin: int, voltage: ('HIGH' | 'LOW')) return None
```

* ### [StateMachine](https://github.com/Ratonhnaketon/Raspberry_pi_controllers/blob/master/StateMachine/controller.py)

	Define a máquina de estados  
```python
<StateMachineName> = StateMachine(states: dict, variables: dict, initState: str, args: dict({ debug: bool, timer: int }))
```

####	Métodos:
```python  
start() return None  
```

* ### [State](https://github.com/Ratonhnaketon/Raspberry_pi_controllers/blob/master/StateMachine/controller.py)

	Define os estados  
```python
<StateName> = State(name: (str), func: (def), nextStateConditions: dict({ nextState: str, conditions: dict }))
```

####	Métodos:
```python  
start() return None  
```