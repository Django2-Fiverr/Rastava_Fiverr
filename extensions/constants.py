import datetime
from category.models import Category
from comment.models import Comment

CATEGORY = Category.objects.all()
COMMENTS = Comment.objects.all()


def set_comment_publish():
    for comment in COMMENTS:
        if comment.status and not comment.publish:
            comment.publish = datetime.datetime.now()
            comment.save()
