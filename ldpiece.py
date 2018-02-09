import hashlib
import pandas as pd



class Triple(object):

	
	def __init__(self, s=None, p=None, o=None):

		self.s = s
		self.p = p
		self.o = o

	
	def __repr__(self):

		return "< %s --> %s --> %s >" % (self.s, self.p, self.o)

	
	def as_pd_series(self):

		return pd.Series([self.s, self.p, self.o], index=['s', 'p', 'o'], name=self.md5_id())

	def md5_id(self):

		'''
		Generate md5 hash of spo values
		'''

		spo_string = "%s%s%s" % (self.s, self.p, self.o)
		return hashlib.md5(spo_string.encode('utf-8')).hexdigest()



class Graph(object):

	
	def __init__(self):

		self.graph = pd.DataFrame(columns=['s','p','o'])

	
	def add_triple(self, t):
		
		self.graph = self.graph.append(t.as_pd_series())






