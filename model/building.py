class Building(object):
	def __init__(self, btype, bposition, json, bid, pid):
		self._id = bid
		self._x = bposition[0]
		self._y = bposition[1]
		self._hp = json["hp"]
		#self.neutral_hp = bhp
		#self.captured_hp = 2 * bhp
		self._type = btype
		self._units = json["units"]
		self.player_id = pid

	def capture(self, pid, uhp):
		"""
		Subtracts the capturing unit's hp from this
		buildings hp. Returns 0 if the building has
		been fully captured, or the remaining hp of
		the building.
		"""
		# Figure out how to trace hp so if a unit
		# stops caping, the building hp is recovered.
		tmp_hp = self._hp - uhp
		if tmp_hp > 0:
			self._hp = tmp_hp
			return self._hp
		else:
			self._hp = self.captured_hp
			self.player_id = pid
			return 0

	def GetHP(self):
		"""
		Returns the hp of this building.
		"""
		return self._hp
	
	def GetBID(self):
		return self._id

	def GetPlayerID(self):
		"""
		Returns the player id who ownes this building.
		"""
		return self.player_id

	def GetPosition(self):
		"""
		Returns the position of this building as a tuple
		in the form (x,y).
		"""
		return (self._x, self._y)

	def GetType(self):
		"""
		Returns the type of this building.
		"""
		return self._type

	def ListUnits(self, pcredit):
		"""
		Returns a list of tuples in the form of
		( str.unit_type, int.unit_cost, boolean.unit_valid ).
		"""
		for _type in self._units:
			if self._units[_type] > pcredit:
				#valid = True
				yield (_type, self._units[_type], True)
			else:
				yield (_type, self._units[_type], False)

	def RestoreHP(self):
		"""
		Restores the hp of this building to its previous
		state, whether neutral or occupied.
		"""
		if self.player_id is None:
			self._hp = self.neutral_hp
		else:
			self._hp = self.captured_hp

	def QuoteUnit(self, utype):
		"""
		Returns the cost of a unit or None if the unit
		type is not buildable.
		"""
		return self._units[utype] if utype in self._units else None
    
	def __str__(self):
		s = "bID: {}, Type: {}, Position: ({}, {}), ".format(self._id, self._type, self._x, self._y)
		s += "pID: {}, HP: {}, Units: {}".format(self.player_id, self._hp, self._units)
		return s
