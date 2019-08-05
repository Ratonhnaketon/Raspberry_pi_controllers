# Controladores para Raspberry pi 

Este projeto facilita a automatização de projetos IoT (Internet das Coisas) numa placa Raspberry usando python 2
Se baseia no próprio prinpício de um sistema IoT: vários componentes que conversam com um componente central.
Este projeto define isso por controlador mestre e controlador escravo. Precisa de pelo menos 1 controlador mestre para funcionar.

# Classes

* ### [MasterController](https://github.com/Ratonhnaketon/Raspberry_pi_controllers/blob/master/Core/masterController.py)

  Define o controlador mestre.  
  
  <ControllerName>(MasterController):
	def __init__(self, ...variables):
		MasterController.__init__(self)
  
* ### [SlaveController](https://github.com/Ratonhnaketon/Raspberry_pi_controllers/blob/master/Core/slaveController.py)

  Define o controlador escravo.  
  
  <ControllerName>(SlaveController):
	def __init__(self, ...variables):
		SlaveController.__init__(self)
	
	Métodos:    
	* assignPins(pins (list)) retorno (null)    
   	* setPin(pin (int), voltage ('HIGH' ou 'LOW')) retorno (null)
	  
* ### [StateMachine](https://github.com/Ratonhnaketon/Raspberry_pi_controllers/blob/master/StateMachine/controller.py)

	Define a máquina de estados

	<StateMachineName> = StateMachine(states (dict), variables (dict), initState(string), opts = { debug (bool), timer (int) })

	Métodos:  
	* start() retorno (null)