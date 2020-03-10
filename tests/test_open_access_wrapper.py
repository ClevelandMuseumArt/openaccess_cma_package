import sys
import unittest
import validators
from openaccess_cma import openaccess_cma_search

class TestOpenAccessPIPModule(unittest.TestCase):
	
	def test_cc0(self):
		with self.assertRaises(ValueError):
			openaccess_cma_search(cc0='12')
		d,q = openaccess_cma_search(cc0=1, limit=1)
		self.assertEqual(d['data'][0]['share_license_status'], 'CC0')

	def test_has_image(self):
		d,q = openaccess_cma_search(has_image=1, indent=1, limit=100)
		for val in d['data']:
			self.assertTrue(val['images'] is not None)
			for k,v in val['images'].items():
				self.assertTrue(validators.url(v['url']))

	def test_skip(self):
		d1, _ = openaccess_cma_search(q="monet")
		d2, _ = openaccess_cma_search(q="monet",skip=1)
		self.assertEqual(d1['data'][2], d2['data'][1])
		self.assertEqual(d1['data'][3], d2['data'][2])
		d3, _ = openaccess_cma_search(q="monet")
		d4, _ = openaccess_cma_search(q="monet",skip=5)
		self.assertEqual(d3['data'][6], d4['data'][1])
		self.assertEqual(d3['data'][7], d4['data'][2])

	def test_skip(self):
		d1, _ = openaccess_cma_search(q="monet")
		d2, _ = openaccess_cma_search(q="monet",skip=1)
		self.assertEqual(d1['data'][2], d2['data'][1])
		self.assertEqual(d1['data'][3], d2['data'][2])
		d3, _ = openaccess_cma_search(q="monet")
		d4, _ = openaccess_cma_search(q="monet",skip=5)
		self.assertEqual(d3['data'][6], d4['data'][1])
		self.assertEqual(d3['data'][7], d4['data'][2])

	def test_department(self):
		with self.assertRaises(ValueError):
			openaccess_cma_search(department="Vegetables")
		d,_ = openaccess_cma_search(q="cezanne",department="Drawings")
		self.assertEqual(d['data'][0]['department'], "Drawings")

	def test_department(self):
		with self.assertRaises(ValueError):
			openaccess_cma_search(department="Vegetables")
		d,_ = openaccess_cma_search(q="cezanne",department="Drawings")
		self.assertEqual(d['data'][0]['department'], "Drawings")

	def test_limit(self):
		with self.assertRaises(ValueError):
			openaccess_cma_search(limit="c d.")
		with self.assertRaises(ValueError):
			openaccess_cma_search(limit="HELLO")
		d,_ = openaccess_cma_search(q="cezanne",department="Drawings",limit =10)
		self.assertTrue(len(d['data'])<=10)
		d,_ = openaccess_cma_search(q="China",limit =10)
		self.assertTrue(len(d['data'])==10)

if __name__ == '__main__':
    unittest.main()
