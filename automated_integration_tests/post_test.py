import requests

from endpoints import GET_ENDPOINT, POST_ENDPOINT, HEADERS, DELETE_ENDPOINT
from helper import count_posts_in_category


def test_check_new_blog_posts_can_be_added_and_removed_in_category():
    # Get all blog posts in category 3
    before_blog_post = requests.get(GET_ENDPOINT + "3")
    before_blog_post_response_body = before_blog_post.json()

    # Count how many blog posts category 3 has before post
    before_blog_count = count_posts_in_category(before_blog_post_response_body)

    # Set up a new blog post for category 3
    payload = "{\n  \"body\": \"This is a brand new blog post\"," \
              "\n  \"category_id\": 3," \
              "\n  \"title\": \"New blog post\"\n}"

    new_post_response = requests.request("POST", url=POST_ENDPOINT, headers=HEADERS, data=payload)
    assert new_post_response.status_code == 201

    # Count how many blog posts category 3 has after post
    after_blog_post = requests.get(GET_ENDPOINT + "3")
    after_blog_post_response_body = after_blog_post.json()

    after_blog_count = count_posts_in_category(after_blog_post_response_body)

    # Assert that category 3 count has increased by 1
    assert after_blog_count == before_blog_count + 1

    # Delete the blog post that was created
    delete_blog = requests.request("DELETE", url=DELETE_ENDPOINT + str(after_blog_post_response_body['posts'][0]['id']))
    assert delete_blog.status_code == 204

    # Count how many blog posts category 3 has after deleted post
    after_deleted_blog_post = requests.get(GET_ENDPOINT + "3")
    after_deleted_blog_post_response_body = after_deleted_blog_post.json()

    after_deleted_blog_count = count_posts_in_category(after_deleted_blog_post_response_body)
    assert after_deleted_blog_count == after_blog_count - 1
