# @author Jonathan Stout

class Moves(object):
	def __init__(self, unit_conf):
		"""
		Unit can make moves specified by unit_conf.
		Conf ex.
		attack_e,move_a,capture_e
		attack_e,move_a,capture_e
		unload_e,supply_e,move_a

		e = unit is done after this move.
		a = unit can choose another move if available.

		Stored as (action_name, action_available, stops_unit)
		"""
		self.actions = []
		self.can_act = True
		acts = unit_conf.split(",")
		for a in acts:
			a.split("_")
			if a[1] == "e":
				self.actions.append(a[0], True, True)
			else:
				self.actions.append(a[0], True, False)

	def can_act(self):
		return self.can_act

	def available_actions(self):
		"""
		Yield all actions.
		"""
		for act in self.actions:
			yield act

	def new_turn(self):
		"""
		Turn has started. Make all actions available for next
		turn.
		"""
		for a in self.actions:
			a[1] = True

	def capture(self):
		self.capture[1] = False
		if self.capture[2]: self.can_act = False

	def supply(self):
		self.supply[1] = False
		if self.supply[2]: self.can_act = False

	def unload(self):
		self.unload[1] = False
		if self.unload[2]: self.can_act = False

	def move(self):
		self.move[1] = False
		if self.move[2]: self.can_act = False

	def attack(self):
		self.attack[1] = False
		if self.move[2]: self.can_act = False
