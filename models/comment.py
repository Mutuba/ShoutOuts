from datetime import datetime

COMMENTS = []

class Comment:
    def __init__(self):
        self.current_date = str(datetime.now())
    def browse(self):
        return COMMENTS

    def read(self, id):
        return COMMENTS[id]

    def edit(self, id):
        pass
        
    def add(self, message, author, created_at, updated_at, updated_by=None, parent=None):
        id = len(COMMENTS) + 1
        COMMENTS.append(
            {
                id: {
                    'id': id,
                    'parent': parent,
                    'message': message,
                    'author': author,
                    'created_at': created_at,
                    'updated_at': updated_at,
                    'updated_by': updated_by,
                }
            }
        )
        return COMMENTS
        
    def delete(self, id):
        COMMENTS.remove(id)