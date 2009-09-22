#!/usr/bin/env python

# Copyright 2009 John Kleint
#
# This is free software, licensed under the Lesser Affero General 
# Public License, available in the accompanying LICENSE.txt file.


"""
Unit tests for googlemaps.

"""


import unittest
import doctest
try:
    import json
except ImportError:
    import simplejson as json
    
import googlemaps
from googlemaps import GoogleMaps    

    
# You might need an actual key to run the tests.
GMAPS_API_KEY=''


class Test(unittest.TestCase):
    """Unit tests for googlemaps."""

    def test_geocode(self):
        """Test googlemaps geocode() and address_to_latlng()"""
        
        expected = """
        {
            "Status": {
                "code": 200,
                "request": "geocode"
            },
            "Placemark": [
                {
                    "Point": {
                        "coordinates": [
                            -122.085035,
                            37.423138999999999,
                            0
                        ]
                    },
                    "ExtendedData": {
                        "LatLonBox": {
                            "west":-122.0872906,
                            "east":-122.08099540000001,
                            "north": 37.425119600000002,
                            "south": 37.418824399999998
                        }
                    },
                    "AddressDetails": {
                        "Country": {
                            "CountryName": "USA",
                            "AdministrativeArea": {
                                "AdministrativeAreaName": "CA",
                                "Locality": {
                                    "PostalCode": {
                                        "PostalCodeNumber": "94043"
                                    },
                                    "Thoroughfare": {
                                        "ThoroughfareName": "1600 Amphitheatre Pkwy"
                                    },
                                    "LocalityName": "Mountain View"
                                }
                            },
                            "CountryNameCode": "US"
                        },
                        "Accuracy": 8
                    },
                    "id": "p1",
                    "address": "1600 Amphitheatre Pkwy, Mountain View, CA 94043, USA"
                }
            ],
            "name": "1600 amphitheatre mountain view ca"
        }
        """

        expected = json.loads(expected)     # Ensure it's valid JSON
        gmaps = GoogleMaps(GMAPS_API_KEY)
        actual = gmaps.geocode(expected['name'])
        self.assertEqual(actual, expected)

        (lat, lng) = gmaps.address_to_latlng(expected['name'])
        self.assertEqual(lat, expected['Placemark'][0]['Point']['coordinates'][1])
        self.assertEqual(lng, expected['Placemark'][0]['Point']['coordinates'][0])


    def test_reverse_geocode(self):
        """Test googlemaps reverse_geocode() and latlng_to_address()"""
        
        expected = """
        {
            "Status": {
                "code": 200, 
                "request": "geocode"
            }, 
            "Placemark": [
                {
                    "Point": {
                        "coordinates": [
                            -73.961448399999995, 
                            40.714222599999999, 
                            0
                        ]
                    }, 
                    "ExtendedData": {
                        "LatLonBox": {
                            "west": -73.964614499999996, 
                            "east": -73.958319299999999, 
                            "north": 40.717377399999997, 
                            "south": 40.7110822
                        }
                    }, 
                    "AddressDetails": {
                        "Country": {
                            "CountryName": "USA", 
                            "AdministrativeArea": {
                                "AdministrativeAreaName": "NY", 
                                "Locality": {
                                    "PostalCode": {
                                        "PostalCodeNumber": "11211"
                                    }, 
                                    "Thoroughfare": {
                                        "ThoroughfareName": "275-291 Bedford Ave"
                                    }, 
                                    "LocalityName": "Brooklyn"
                                }
                            }, 
                            "CountryNameCode": "US"
                        }, 
                        "Accuracy": 8
                    }, 
                    "id": "p1", 
                    "address": "275-291 Bedford Ave, Brooklyn, NY 11211, USA"
                }, 
                {
                    "Point": {
                        "coordinates": [
                            -73.961151000000001, 
                            40.714320999999998, 
                            0
                        ]
                    }, 
                    "ExtendedData": {
                        "LatLonBox": {
                            "west": -73.964298600000006, 
                            "east": -73.958003399999996, 
                            "north": 40.717468599999997, 
                            "south": 40.7111734
                        }
                    }, 
                    "AddressDetails": {
                        "AddressLine": [
                            "GRAND ST at BEDFORD AV"
                        ], 
                        "Accuracy": 9
                    }, 
                    "id": "p2", 
                    "address": "GRAND ST at BEDFORD AV, Williamsburg, NY 11211, USA"
                }, 
                {
                    "Point": {
                        "coordinates": [
                            -73.960998000000004, 
                            40.714709999999997, 
                            0
                        ]
                    }, 
                    "ExtendedData": {
                        "LatLonBox": {
                            "west": -73.964145599999995, 
                            "east": -73.957850399999998, 
                            "north": 40.717857600000002, 
                            "south": 40.711562399999998
                        }
                    }, 
                    "AddressDetails": {
                        "AddressLine": [
                            "BEDFORD AV at GRAND ST"
                        ], 
                        "Accuracy": 9
                    }, 
                    "id": "p3", 
                    "address": "BEDFORD AV at GRAND ST, Williamsburg, NY 11211, USA"
                }, 
                {
                    "Point": {
                        "coordinates": [
                            -73.961860000000001, 
                            40.713523000000002, 
                            0
                        ]
                    }, 
                    "ExtendedData": {
                        "LatLonBox": {
                            "west": -73.965007600000007, 
                            "east": -73.958712399999996, 
                            "north": 40.7166706, 
                            "south": 40.710375399999997
                        }
                    }, 
                    "AddressDetails": {
                        "AddressLine": [
                            "BEDFORD AV at S 2 ST"
                        ], 
                        "Accuracy": 9
                    }, 
                    "id": "p4", 
                    "address": "BEDFORD AV at S 2 ST, Williamsburg, NY 11211, USA"
                }, 
                {
                    "Point": {
                        "coordinates": [
                            -73.954344000000006, 
                            40.714063000000003, 
                            0
                        ]
                    }, 
                    "ExtendedData": {
                        "LatLonBox": {
                            "west": -73.969845100000001, 
                            "east": -73.920281000000003, 
                            "north": 40.718204999999998, 
                            "south": 40.697932999999999
                        }
                    }, 
                    "AddressDetails": {
                        "Country": {
                            "CountryName": "USA", 
                            "AdministrativeArea": {
                                "AdministrativeAreaName": "NY", 
                                "Locality": {
                                    "LocalityName": "New York", 
                                    "DependentLocality": {
                                        "DependentLocalityName": "Williamsburg"
                                    }
                                }
                            }, 
                            "CountryNameCode": "US"
                        }, 
                        "Accuracy": 4
                    }, 
                    "id": "p5", 
                    "address": "Williamsburg, New York, NY, USA"
                }, 
                {
                    "Point": {
                        "coordinates": [
                            -73.956555100000003, 
                            40.714278999999998, 
                            0
                        ]
                    }, 
                    "ExtendedData": {
                        "LatLonBox": {
                            "west": -73.969954000000001, 
                            "east": -73.922888999999998, 
                            "north": 40.725284000000002, 
                            "south": 40.698051999999997
                        }
                    }, 
                    "AddressDetails": {
                        "Country": {
                            "CountryName": "USA", 
                            "AdministrativeArea": {
                                "PostalCode": {
                                    "PostalCodeNumber": "11211"
                                }, 
                                "AdministrativeAreaName": "NY"
                            }, 
                            "CountryNameCode": "US"
                        }, 
                        "Accuracy": 5
                    }, 
                    "id": "p6", 
                    "address": "Brooklyn, NY 11211, USA"
                }, 
                {
                    "Point": {
                        "coordinates": [
                            -73.947738400000006, 
                            40.7204391, 
                            0
                        ]
                    }, 
                    "ExtendedData": {
                        "LatLonBox": {
                            "west": -73.974546000000004, 
                            "east": -73.920913999999996, 
                            "north": 40.739339000000001, 
                            "south": 40.692166
                        }
                    }, 
                    "AddressDetails": {
                        "AddressLine": [
                            "Brooklyn Community School District 14"
                        ], 
                        "Accuracy": 0
                    }, 
                    "id": "p7", 
                    "address": "Brooklyn Community School District 14, New York, NY, USA"
                }, 
                {
                    "Point": {
                        "coordinates": [
                            -73.959494000000007, 
                            40.652876200000001, 
                            0
                        ]
                    }, 
                    "ExtendedData": {
                        "LatLonBox": {
                            "west": -74.056686999999997, 
                            "east": -73.832920999999999, 
                            "north": 40.739434000000003, 
                            "south": 40.550333999999999
                        }
                    }, 
                    "AddressDetails": {
                        "Country": {
                            "CountryName": "USA", 
                            "AdministrativeArea": {
                                "AddressLine": [
                                    "Kings"
                                ], 
                                "AdministrativeAreaName": "NY"
                            }, 
                            "CountryNameCode": "US"
                        }, 
                        "Accuracy": 3
                    }, 
                    "id": "p8", 
                    "address": "Kings, New York, USA"
                }, 
                {
                    "Point": {
                        "coordinates": [
                            -73.959494000000007, 
                            40.652876200000001, 
                            0
                        ]
                    }, 
                    "ExtendedData": {
                        "LatLonBox": {
                            "west": -74.056686999999997, 
                            "east": -73.832920999999999, 
                            "north": 40.739434000000003, 
                            "south": 40.550333999999999
                        }
                    }, 
                    "AddressDetails": {
                        "Country": {
                            "CountryName": "USA", 
                            "AdministrativeArea": {
                                "AdministrativeAreaName": "NY", 
                                "Locality": {
                                    "LocalityName": "Brooklyn"
                                }
                            }, 
                            "CountryNameCode": "US"
                        }, 
                        "Accuracy": 4
                    }, 
                    "id": "p9", 
                    "address": "Brooklyn, NY, USA"
                }
            ], 
            "name": "40.714224,-73.961452"
        }
        """

        expected = json.loads(expected)     # Ensure it's valid JSON
        lat = float(expected['name'].split(',')[0])
        lng = float(expected['name'].split(',')[1])
        gmaps = GoogleMaps(GMAPS_API_KEY)
        actual = gmaps.reverse_geocode(lat, lng)
        self.assertEqual(actual, expected)      
        # This is very sensitive to floating-point error, but it doesn't seem
        # worth writing a recursive approximate-fp JSON equality routine.
        
        address = gmaps.latlng_to_address(lat, lng)
        self.assertEqual(address, expected['Placemark'][0]['address'])
        

    def test_local_search(self):
        """Test googlemaps local_search()."""
        gmaps = GoogleMaps(GMAPS_API_KEY, referrer_url='http://www.google.com/')
        local = gmaps.local_search('sushi san francisco, ca')
        result = local['responseData']['results'][0]
        self.assertEqual(result['titleNoFormatting'], 'Sushi Groove')
        
        results = gmaps.local_search('Starbucks Los Angeles, CA', numresults=GoogleMaps.MAX_LOCAL_RESULTS)
        self.assertEqual(results['responseStatus'], googlemaps.STATUS_OK)
        self.assertNotEqual(results['responseData'], None)
        self.assertNotEqual(results['responseData']['cursor'], None)
        results = results['responseData']['results']
        self.assertEqual(len(results), GoogleMaps.MAX_LOCAL_RESULTS)
        for result in results:
            self.assertEqual(result['GsearchResultClass'], 'GlocalSearch')
            self.assert_(result['titleNoFormatting'].lower().find('starbucks') >= 0)
            self.assertEqual(result['region'], 'CA')
            

    def test_directions(self):
        """Test googlemaps directions()"""
        
        gmaps = GoogleMaps(GMAPS_API_KEY)
        results = gmaps.directions('10th St. & Constitution Ave. NW, Washington, D.C. 20560',
                                   '200 6th St SW, Washington, DC 20024, USA')
        self.assertEqual(results['Status']['code'], googlemaps.STATUS_OK)
        self.assert_(results['Directions']['Duration']['seconds'] in range(100, 130))
        self.assert_(results['Directions']['Distance']['meters'] in range(1000, 1050))
        routes = results['Directions']['Routes']
        self.assert_(len(routes) >= 1)
        self.assertEqual(routes[0]['Duration'], results['Directions']['Duration'])
        self.assertEqual(routes[0]['Distance'], results['Directions']['Distance'])
        self.assert_(routes[0]['Steps'][0]['descriptionHtml'].find('Constitution Ave') >= 0)
        self.assert_(routes[0]['Steps'][1]['descriptionHtml'].find('7th St') >= 0)
        self.assert_(routes[0]['Steps'][2]['descriptionHtml'].find('Independence Ave') >= 0)
        
    def test_doctests(self):
        """Run googlemaps doctests"""
        doctest.testmod(googlemaps)
        
        
if __name__ == "__main__":
    unittest.main()