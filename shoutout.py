from models.user import User

from auth.sign_in import login
from auth.reg import reg
from models.comment import Comment

print('==================================================================')
print('                      WELCOME TO SHOUTOUT                         ')
print('==================================================================')


login()
Comment.browse()
