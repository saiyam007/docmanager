from db.database import get_connection

class AnalyticsService:
    def __init__(self):
        self.db = get_connection()

    def record_page_visit(self, document_id, page_number):
        if self.db is None:
            print("DB connection not established.")
            self.db = get_connection()
        cursor = self.db.cursor()
        cursor.execute("""Insert into page_visits (document_id, page_number, timestamp) values (?, ?, datetime('now'))""",
            (document_id, page_number),
        )
        print(f"Recorded visit for doc_id: {document_id}, page: {page_number}")
        self.db.commit()
    
    def get_unique_page_visits(self, document_id):
        if self.db is None:
            print("DB connection not established.")
            self.db = get_connection()
        cursor = self.db.cursor()
        cursor.execute("""SELECT COUNT(DISTINCT page_number) FROM page_visits WHERE document_id = ?""", (document_id,))
        result = cursor.fetchone()
        return result[0] if result else 0
    
    def record_app_visit(self, event_type):
        if self.db is None:
            print("DB connection not established.")
            self.db = get_connection()
        cursor = self.db.cursor()
        cursor.execute("""Insert into app_visits (event_type, timestamp) values (?, datetime('now'))""",
            (event_type,),
        )
        print(f"Recorded app visit: {event_type}")
        self.db.commit()
        
    def get_app_visits_count(self):
        if self.db is None:
            print("DB connection not established.")
            self.db = get_connection()
        cursor = self.db.cursor()
        cursor.execute("""SELECT event_type, COUNT(*) FROM app_visits  GROUP BY event_type """)
        result = cursor.fetchall()
        return result if result else []