# Copyright 2016, 2023 John J. Rofrano. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Test cases for Product Model

Test cases can be run with:
    nosetests
    coverage report -m

While debugging just these tests it's convenient to use this:
    nosetests --stop tests/test_models.py:TestProductModel

"""
import os
import logging
import unittest
from decimal import Decimal
from service.models import Product, Category, db
from service import app
from tests.factories import ProductFactory

DATABASE_URI = os.getenv(
    "DATABASE_URI", "postgresql://postgres:postgres@localhost:5432/postgres"
)


######################################################################
#  P R O D U C T   M O D E L   T E S T   C A S E S
######################################################################
# pylint: disable=too-many-public-methods
class TestProductModel(unittest.TestCase):
    """Test Cases for Product Model"""

    @classmethod
    def setUpClass(cls):
        """This runs once before the entire test suite"""
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
        app.logger.setLevel(logging.CRITICAL)
        Product.init_db(app)

    @classmethod
    def tearDownClass(cls):
        """This runs once after the entire test suite"""
        db.session.close()

    def setUp(self):
        """This runs before each test"""
        db.session.query(Product).delete()  # clean up the last tests
        db.session.commit()

    def tearDown(self):
        """This runs after each test"""
        db.session.remove()

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################

    def test_create_a_product(self):
        """It should Create a product and assert that it exists"""
        product = Product(name="Fedora", description="A red hat", price=12.50, available=True, category=Category.CLOTHS)
        self.assertEqual(str(product), "<Product Fedora id=[None]>")
        self.assertTrue(product is not None)
        self.assertEqual(product.id, None)
        self.assertEqual(product.name, "Fedora")
        self.assertEqual(product.description, "A red hat")
        self.assertEqual(product.available, True)
        self.assertEqual(product.price, 12.50)
        self.assertEqual(product.category, Category.CLOTHS)
"""Students_Info"""
        def test_read_a_studentInfo(self):
        """It should Read a studentInfo"""
       studentsInfo= studentsInfoFactory()
      studentsInfo.id = None
       studentsInfo.create()
        self.assertIsNotNone(studentInfot.id)
       found_studentInfo=studentInfo.find(product.id)
        self.assertEqual(found_studentInfo.id, studentInfo.id)
        self.assertEqual(found_studentInfo.name, studentInfo.name)

def test_update_a_studentInfoUpdate(self):
        """It should Update a Product"""
        studentInfoUpdate = studentInfoFactory()
        studentInfo.id = None
        studentInfo.create()
        self.assertIsNotNone( studentInfo.id)
        # Change it an save it
        studentInfo.name = "testing"
        original_id =studentInfo.id
        studentInfo.update()
        self.assertEqual(studentInfo.id, original_id)
        self.assertEqual(studentInfo.name, "testing")
        # Fetch it back and make sure the id hasn't changed
        # but the data did change
        studentInfo = studentInfo.all()
        self.assertEqual(len(studentsInfo), 1)
        self.assertEqual(studentsInfo[0].id, original_id)
        self.assertEqual(studentsInfo[0].name, "testing")

 
       
