class QuotaSingleton:
    # Variable de clase donde guardaremos el único objeto que se va a crear
    _instance = None

    # __new__ carga antes que init y es quien crea el objeto en memoria
    # desde aquí controlaremos si existe o no el objeto
    # ** Recibe cls en vez de self ya que el objeto aún no esta creado "fisicamente" y lo que recibe es una clase
    def __new__(cls):
        # Si no existe la instancia, la creamos.
        if cls._instance is None:
            # Llamamos al método __new__ de la clase padre (object) para crearlo
            cls._instance = super(QuotaSingleton, cls).__new__(cls)
            # Creamos un controlador para gestionar el __init__
            cls._instance._initialized = False
        # devolvemos el objeto
        return cls._instance

    # Al devolver desde __new__ el objeto que tenemos guardado en la variable de clase
    # __init__  se ejecutará sobre este objeto
    # Esto lo que hace es inicializarlo cada vez que se le llama
    # por lo que para mantener sus atributos usamos el controlador de inicialización
    def __init__(self, initial_quota: int = 100):
        # Solo inicializamos la cuota la PRIMERA vez que se crea el objeto
        if self._initialized:
            return

        self.quota = initial_quota
        self._initialized = True

    # Creamos un método para restar quota
    # El método restará la quota que se le indique
    # y devolverá el propio objeto, por si queremos realizar mas operaciones sobre él
    def check_quota(self, amount: int):
        self.quota -= amount
        return self
