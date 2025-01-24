######################################################################
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
######################################################################

# spell: ignore Rofrano jsonify restx dbname
"""
Product Store Service with UI
"""
from flask import jsonify, request, abort
from flask import url_for  # noqa: F401 pylint: disable=unused-import
from service.models import Product
from service.common import status  # HTTP Status Codes
from . import app


######################################################################
# H E A L T H   C H E C K
######################################################################
@app.route("/health")
def healthcheck():
    """Let them know our heart is still beating"""
    return jsonify(status=200, message="OK"), status.HTTP_200_OK


######################################################################
# H O M E   P A G E
######################################################################
@app.route("/")
def index():
    """Base URL for our service"""
    return app.send_static_file("index.html")


######################################################################
#  U T I L I T Y   F U N C T I O N S
######################################################################
def check_content_type(content_type):
    """Checks that the media type is correct"""
    if "Content-Type" not in request.headers:
        app.logger.error("No Content-Type specified.")
        abort(
            status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            f"Content-Type must be {content_type}",
        )

    if request.headers["Content-Type"] == content_type:
        return

    app.logger.error("Invalid Content-Type: %s", request.headers["Content-Type"])
    abort(
        status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
        f"Content-Type must be {content_type}",
    )


######################################################################
# C R E A T E   A   N E W   P R O D U C T
######################################################################
@app.route("/studentInfo", methods=["POST"])
def create_studentsInfo():
    """
    Creates a studentInfo
    This endpoint will create a Product based the data in the body that is posted
    """
    app.logger.info("Request to Create a studentInfo...")
    check_content_type("application/json")

    data = request.get_json()
    app.logger.info("Processing: %s", data)
    studentInfo = studentInfo()
    studentInfo.deserialize(data)
    studentInfo.create()
    app.logger.info("Product with new id [%s] saved!", studentInfo.id)

    message = studentInfo.serialize()

    #
    # Uncomment this line of code once you implement READ A studentInfo
    #
    # location_url = url_for("get_studentsInfo", studentInfo_id=product.id, _external=True)
    location_url = "/"  # delete once READ is implemented
    return jsonify(message), status.HTTP_201_CREATED, {"Location": location_url}


######################################################################
# L I S T   A L L   P R O D U C T S
######################################################################

#
#     def test_get_studentinfo(self):
        """It should Get a single studentinfo"""
        # get the id of a studentinfo
        test_studentinfo = self._create_studentsinfo(1)[0]
        response = self.client.get(f"{BASE_URL}/{test_studentinfo.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.get_json()
        self.assertEqual(data["name"], test_studentinfo.name)

#

######################################################################
# R E A D   A   P R O D U C T
######################################################################

#
##     def test_get_studentinfo(self):
        """It should Get a single studentinfo"""
        # get the id of a studentinfo
        test_studentinfo = self._create_studentsinfo(1)[0]
        response = self.client.get(f"{BASE_URL}/{test_studentinfo.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.get_json()
        self.assertEqual(data["name"], test_studentinfo.name)
#

######################################################################
# U P D A T E   A   P R O D U C T
######################################################################

#
# PLACE YOUR CODE TO UPDATE A PRODUCT HERE
    def test_update_studentinfo(self):
        """It should Update an existing Product"""
        # create a studentinfo to update
        test_studentinfo = studentinfoFactory()
        response = self.client.post(BASE_URL, json=test_studentinfo.serialize())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # update the studentinfo
        new_studentinfo = response.get_json()
        new_studentinfo["name"] = "unknown"
        response = self.client.put(f"{BASE_URL}/{new_studentinfo['id']}", json=new_studentinfo)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_studentinfo = response.get_json()
        self.assertEqual(updated_studentinfo["description"], "unknown")

#

######################################################################
# D E L E T E   A   P R O D U C T
######################################################################


#
# PLACE YOUR CODE TO DELETE A PRODUCT HERE
    def test_delete_studentinfo(self):
        """It should Delete astudentinfo"""
       studentsinfo = self._create_studentsinfo(5)
        studentinfo_count = self.get_studentinfo_count()
        test_studentinfo = studentsinfo[0]
        response = self.client.delete(f"{BASE_URL}/{test_studentinfo.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(response.data), 0)
        # make sure they are deleted
        response = self.client.get(f"{BASE_URL}/{test_studentinfo.id}")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        new_count = self.get_product_count()
        self.assertEqual(new_count, studentinfo_count - 1)

#
