def count_posts_in_category(response_body):
    count = 0
    for x in response_body:
        if isinstance(response_body[x], list):
            count += len(response_body[x])
    return count


