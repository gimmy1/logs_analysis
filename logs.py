#! /usr/bin/env python
import psycopg2


def connect(database_name="news"):
    try:
        db = psycopg2.connect("dbname={}".format(
            database_name
        ))
        cursor = db.cursor()
        return db, cursor
    except:
        print("Connect error")


def popular_articles():
    db, cursor = connect()
    cursor.execute("Select title, Count(*) as views from articles Join log On path Like Concat('%', slug, '%') Where status = '200 OK' Group By title Order by views Desc Limit 3;")
    articles = cursor.fetchall()
    print("What are the 3 most popular articles of All-time?")
    for (name, view) in articles:
        print(" {} - {} views".format(name, view))
    db.close()


def popular_authors():
    db, cursor = connect()
    cursor.execute("Select name, Count(*) as views from articles Join authors on authors.id = articles.author Join log on log.path Like Concat ('%', slug, '%') Where status = '200 OK' Group By name Order By views Desc;")
    authors = cursor.fetchall()
    print("Who are most popular authors? Rank by views")
    for (name, view) in authors:
        print(" {} - {} views".format(name, view))
    db.close()


def percentage_errors():
    db, cursor = connect()
    cursor.execute("Select date, percentage From errs Where percentage > 1;")
    error = cursor.fetchall()
    print("On what day did requests lead to errors greater than 1%?")
    for (day, err) in error:
        print(" {0:%B %d, %Y} - {1:.2f} % errors".format(day, err))
    db.close()

if __name__ == "__main__":
    popular_articles()
    popular_authors()
    percentage_errors()
