class Building(object):
	def __init__(self, bid, bposition, bhp, btype, bunits, pid):
		self._id = bid
		self._x = bposition[0]
		self._y = bposition[1]
		self._hp = bhp
		self.neutral_hp = bhp
		self.captured_hp = 2 * bhp
		self._type = btype
		self._units = bunits
		self.player_id = pid

	def Capture(self, pid, uhp):
		"""
		Subtracts the capturing unit's hp from this
		buildings hp. Returns 0 if the building has
		been fully captured, or the remaining hp of
		the building.
		"""
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
		result = []

		for t in self._units:
			valid = False
			if self._units[t] > pcredit:
				valid = True
			result.append( (t, self._units[t], valid) )

		return result

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
