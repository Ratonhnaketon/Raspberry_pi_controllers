# Controladores para Raspberry pi 

Este projeto facilita a automatização de projetos IoT (Internet das Coisas) numa placa Raspberry usando python 2
Se baseia no próprio prinpício de um sistema IoT: vários componentes que conversam com um componente central.
Este projeto define isso por controlador mestre e controlador escravo. Precisa de pelo menos 1 controlador mestre para funcionar.

# Classes

* ### [MasterController](https://github.com/Ratonhnaketon/Raspberry_pi_controllers/blob/master/Core/masterController.py)

  Define o controlador mestre.  
  Parâmetros:  
    Não há  
  
  Métodos:  
    Não há  

* ### [SlaveController](https://github.com/Ratonhnaketon/Raspberry_pi_controllers/blob/master/Core/slaveController.py)

  Define o controlador escravo.  
  Parâmetros:  
    Não há  
    
   Métodos:  
   * assignPins  
      Parâmetros:   
      * pins (list)  
      Retorno:   
        Não há    
      
   * setPin  
      Parâmetros:   
      * pin (int)  
      * voltage ('HIGH' ou 'LOW')  
      Retorno:
        Não há  
      
* ### [StateMachine](https://github.com/Ratonhnaketon/Raspberry_pi_controllers/blob/master/Core/slaveController.py)

