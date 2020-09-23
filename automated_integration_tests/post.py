import requests
import pytest

HEADERS = {'Content-Type': 'application/json'}

GET_ENDPOINT = "http://localhost:8888/api/blog/categories/"
POST_ENDPOINT = "http://localhost:8888/api/blog/posts/"

def test_check_new_blog_posts_exist_in_category():
    # Get all category 3
    before_blog_post = requests.get(GET_ENDPOINT + "3")
    before_blog_post_response_body = before_blog_post.json()

    #Count how many blog posts category has before post
    before_blog_count = 0
    for x in before_blog_post_response_body:
        if isinstance(before_blog_post_response_body[x], list):
            before_blog_count += len(before_blog_post_response_body[x])
    print(before_blog_count)


    # Set up a new blog post for category 3
    payload = "{\n  \"body\": \"This is a brand new blog post\"," \
              "\n  \"category_id\": 3," \
              "\n  \"title\": \"New blog post\"\n}"

    new_post_response = requests.request("POST", url=POST_ENDPOINT, headers=HEADERS, data=payload)
    assert new_post_response.status_code == 201

    #Count how many blog posts category has after post
    after_blog_post = requests.get(GET_ENDPOINT + "3")
    after_blog_post_response_body = after_blog_post.json()


    after_blog_count = 0
    for x in after_blog_post_response_body:
        if isinstance(after_blog_post_response_body[x], list):
            after_blog_count += len(after_blog_post_response_body[x])
    print(after_blog_count)

    pytest.set_trace()
    assert after_blog_count == before_blog_count + 1