# test_views.py
"""
Test views for kaysworld
"""

def test_index_ok(client):
    """
    A simple test which ensures that a request made to
    the site's root index (i.e. '/') responds with an HTTP "OK"
    response, which is represented by the status code 200.
    """
    # Make a GET request to / and store the response object
    # using the Django test client.
    response = client.get('/')
    # Assert that the status_code is 200 (OK)
    assert response.status_code == 200
