# Copyright 2016, 2022 John J. Rofrano. All Rights Reserved.
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

# pylint: disable=too-few-public-methods

"""
Test Factory to make fake objects for testing
"""
import factory
from factory.fuzzy import FuzzyChoice, FuzzyDecimal
from service.models import Product, Category


class ProductFactory(factory.Factory):
    """Creates fake products for testing"""

    class Meta:
        """Maps factory to data model"""

        model = Product

    id = factory.Sequence(lambda n: n)
   ## Add code to create Fake Products 

import studentInfo
from studentInfo.fuzzy import FuzzyChoice, FuzzyDecimal
from service.models import studentInfo,Courses


class studentInfo(studentInfo.Factory):
    """Creates fake products for testing"""

    class Meta:
        """Maps factory to data model"""

        model =studentInfo

    id = factory.Sequence(lambda n: n)
   ## Add code to create Fake studentInfo

   def test_update_a_studentInfo(self):
        """It Update a Product"""
        studentInfo = studentInfoFactory()
        studentInfo.id = None
        studentInfo.create()
        self.assertIsNotNone(product.id)
        studentInfo.name = "testing_update"
        original_id = studentInfo.id
        studentInfo.update()
        self.assertEqual(studentInfo.id, original_id)
        self.assertEqual(studentInfo.name, "testing_update")
       studentsInfo= studentInfo.all()
        self.assertEqual(len( studentsInfo), 1)
        self.assertEqual(products[0].id, original_id)
        self.assertEqual(products[0].name, "testing_update")
       

