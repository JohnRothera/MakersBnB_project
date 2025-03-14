"""
When: I go to makersbnb/spaces
Then: I should see the spaces page
"""
def test_spaces_get(db_connection, web_client):
    db_connection.seed('seeds/makers_bnb_Bowie.sql')
    response = web_client.get('/spaces')
    assert response.status_code == 200
    # did the page load??

"""
When: I go to makersbnb/spaces/123
Then: I should get redirected to 404 page as it does not exist
"""
def test_spaces_123_get(db_connection, web_client):
    db_connection.seed('seeds/makers_bnb_Bowie.sql')
    response = web_client.get('/spaces/123')
    assert response.status_code == 404