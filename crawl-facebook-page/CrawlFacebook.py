from calendar import c
from facebook_scraper import get_posts


def readParams():
    page_name = input("\nNhap ten page ma ban muon crawl: ")
    page_nums = input("\nNhap so luong trang toi da: ")
    return [page_name, page_nums]


# post_id, text, comments_full {commenter_name, comment_text
# , replies {}}
def crawling_post(page_name, page_nums, file):
    for post in get_posts(page_name, pages=page_nums, options={"comments": True}):
        post_id = post['post_id']
        post_content = post['text']
        comments_container = []
        for comment in post['comments_full']:
            commenter_name = comment['commenter_name']
            comment_text = comment['comment_text']
            replies = comment['replies']

            comment_data = {
                "commenter_name": commenter_name,
                "comment_text": comment_text,
                "replies": replies
            }
            comments_container.append(comment_data)

        post_data = {
            "post_id": post_id,
            "post_content": post_content,
            "comments": comments_container
        }

        file.write(f"\n{post_data}\n")


def write_file(post_data, file_name):
    return 1


if __name__ == "__main__":
    # page_name, page_num = readParams()
    page_name = "ConfessionUIT"
    page_num = 2
    file_name = "result.txt"
    with open(f"{file_name}", 'w') as file:
        crawling_post(page_name, page_num, file)
