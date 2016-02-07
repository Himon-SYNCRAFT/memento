from memento import db


def create():
    """
    Main function - drop DB if exist, and recreate new one.
    """

    db.reflect()
    db.drop_all()
    db.create_all()

if __name__ == '__main__':
    create()
