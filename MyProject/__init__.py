# PyMySQL ko MySQLdb ki jagah use karne ke liye (mysqlclient compile karne ki
# zaroorat nahi padti, Windows aur Render dono pe seedha kaam karta hai)
import pymysql
pymysql.install_as_MySQLdb()
