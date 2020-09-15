from . import utils as _utils
from . import rp as _rp
import json as _json
from functools import reduce as _reduce

class Election:
	"""
	This is a wrapper class to store votes, it allows for easy use of the
	methods in rp.py without having to track inputs. 

	Initialize as an empty Election(), or with a list of dicts of votes. 
	Candidates will be automatically filled in from the votes. (Note, this can
	lead to missing candidates if no one ranked that candidate). 
	"""

	def __init__(self, votes=[]):
		self.votes = votes
		self._update_on_vote()

	def _update_on_vote(self):
		self.single_winner = None
		self.full_order = None
		self.candidates, self.votes = _utils.gen_cand_and_clean(self.votes)

	def set_votes(self, new_votes):
		self.votes = new_votes
		self._update_on_vote()
	
	def get_candidates(self):
		return self.candidates
	
	def get_votes(self):
		return self.votes

	def get_winner(self):
		if self.single_winner is not None:
			return self.single_winner
		temp = _rp.run(self.candidates, self.votes)
		self.single_winner = temp
		return self.single_winner

	def get_full_order(self):
		if self.full_order is not None:
			return self.full_order
		temp = _rp.full_order(self.candidates, self.votes)
		self.full_order = temp
		return self.full_order

	def load(self, votes):
		"""
		This method loads a JSON string representing a list of dicts into
		the votes of the Election object. It can also accept an already loaded
		list of dicts. 
		"""
		# Case of JSON string, otherwise assume list
		if type(votes) == str:
			try:
				votes = _json.loads(votes)
			except ValueError as e:
				raise e
		
		try:
			assert(type(votes) == list and type(votes[0]) == dict)
		except AssertionError:
			raise ValueError("Votes not formatted correctly, must be \
							  list of dicts")
		except IndexError:
			self.set_votes([])
			return

		self.votes = votes
		self._update_on_vote()








