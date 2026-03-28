class Document:
    
    def __init__(self, id, name, path, thumbnail_path, tags, description, uploaded_date, lecture_date, total_pages):
        self.id = id
        self.name = name
        self.path = path
        self.thumbnail_path = thumbnail_path
        self.tags = tags
        self.description = description
        self.uploaded_date = uploaded_date
        self.lecture_date = lecture_date
        self.total_pages = total_pages