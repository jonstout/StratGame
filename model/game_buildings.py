from building import Building

class GameBuildings(object):
	def __init__(self, config, map_config, player_ids):
		self.confs = {}
		self.buildings = {}
		self.id_gen = BuildingIDGenerator()

		for btype in config:
			self.confs[btype] = config[btype]

		for i in range( len(map_config) ):
			for bconfig in map_config[i]:
				x = bconfig["position"][0]
				y = bconfig["position"][1]
				btype = bconfig["type"]
				
				bid = self.id_gen.next()
				bhp = self.confs[_type]["hp"]
				bunits = self.confs[_type]["units"]
				
				pid = player_ids[i]
				self.buildings[bid] = Building(bid, (x,y), bhp, btype, bunits, pid)

	def CaptureBuilding(self, bid, pid, uhp):
		"""
		Subtracts the capturing unit's hp from building
		bid's hp. Returns 0 if the building has	been
		fully captured, or the remaining hp of the
		building.
		"""
		return self.buildings[bid].Capture(pid, uhp)

	def GetPosition(self, bid):
		"""
		Returns the position of building bid as a tuple
		in the form (x,y).
		"""
		return self.buildings[bid].GetPosition()

	def OwnedByPlayer(self, bid, pid):
		"""
		Returns True if pid is the id of building
		bid's owner.
		"""
		return pid == self.buildings[bid].GetPID()

	def QuoteUnit(self, bid, utype):
		"""
		Returns the cost of a unit or None if the unit
		type is not buildable.
		"""
		return self.buildings[bid].QuoteUnit(utype)

def BuildingIDGenerator():
	bid_start = 100
	while True :
		bid_start += 1
		yield bid_start