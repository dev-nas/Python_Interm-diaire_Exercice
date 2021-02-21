class Account:
    """Classe de gestion d'un compte client"""
    # private attribute
    _id = 0
    _balance = 0.0
    _currency = "€"
    _client = None
    # public attribute
    overdraft = False
    
    def __init__(self, _id, client, balance=100):
        self._id = _id
        self._client = client
        self.balance = balance
        self._updateOverdraft()
    
    def __str__(self):
        return "_id: {}, balance: {:.2f} {}".format(self._id, self.balance, self._currency)
    
    # public method
    def getId(self):
        return self._id

    def displayBalance(self):
        return "{:.2f} {}".format(self.balance, self._currency)
    
    def deposit(self, value):
        """gestion des dépôts"""
        if value > 0:
            self._updateBalance(value)
            
    def withdraw(self, value):
        """gestion des retraits"""
        if value > 0:
            self._updateBalance(-1 * value)
    
    def getClientName(self):
        return self._client.getFullName()
            
    #private method
    def _updateBalance(self, value):
        """modfication du solde"""
        self.balance += value
        self._updateOverdraft()

    def _updateOverdraft(self):
        self.overdraft = bool(self.balance < 0)
    
