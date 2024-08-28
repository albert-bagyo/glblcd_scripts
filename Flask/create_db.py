from test_app import app, db, Student

with app.app_context():
    db.create_all()
    
    joshua = Student('Joshua', 20, 'female','green')
    mahama = Student('John Dramani Mahama', 99, 'female','red')
    
    
    db.session.add_all([joshua, mahama])
    db.session.commit()
    
    