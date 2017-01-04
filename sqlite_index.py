import sqlite3
import datetime
import string
import random
import time


class SqliteTest(object):
	"""docstring for ClassName"""
	
	email_domen_list = ['@ya.com', '@list.ru', 
						'@gmail.com', '@ra.net']
	empl_adress_list = ['California', 'Texas', 'Norway', 'Rich-Mond',
						'Texas', 'South-Hall', 'Houston']

	sql_create_t = { 'create_tab' : '''CREATE TABLE IF NOT EXISTS stocks (								
								employee_id INTEGER,
								employee_name TEXT,
								employee_age INTEGER,
								adress TEXT,
								date TEXT, 
								email TEXT,
								is_bank_account INTEGER
								)'''
					}
	sql_insert = { 'insert' : '''INSERT INTO stocks (employee_id,
									 employee_name,
									 employee_age,
									 adress,
									 date,
									 email,
									 is_bank_account) 
								 	VALUES('%d', '%s', '%d', '%s', '%s', '%s', '%d')'''

				 }
	
	sql_index = { 'idx_by_email' : '''CREATE INDEX IF NOT EXISTS idx_ya ON 
									  stocks (email)''',
				  'idx_com' : '''CREATE INDEX IF NOT EXISTS idx ON 
				  			 stocks (employee_age, employee_name, adress, email)'''
				}

	sql_select = { 'slc_all' : 'SELECT * FROM stocks',
				   'slc_rowid_eml_name' : '''SELECT rowid, employee_name, employee_age 
				   				FROM stocks WHERE 
								employee_age>43 AND 
								employee_name LIKE "a%" AND								
								adress="Texas" AND
								email LIKE "ya%"''',
				   'slc_rowid_idx' : '''SELECT rowid FROM stocks INDEXED BY
		 							idx_ya WHERE email LIKE "ya%"''',
		 		   'slc_empl_id' : 'SELECT employee_id FROM stocks',
		 		   'slc_by_idx_com' : '''SELECT rowid, employee_name, employee_age
		 		   					  FROM stocks INDEXED BY idx WHERE
		 		   					  employee_age>43 AND 
										employee_name LIKE "a%" AND								
										adress="Texas" AND
										email LIKE "ya%"'''
		 		 }


	def __init__(self, name_table):				
		self.connect = sqlite3.connect(name_table)
		self.cursor = self.connect.cursor()
		self.cursor.execute(self.sql_create_t['create_tab'])
		self.connect.commit()
		

	def insert_table(self):
		eml = ''.join(random.choice(string.ascii_lowercase) for i in range(15)) \
					+ (random.choice(self.email_domen_list))
		epml_id = random.randint(1, 100000)
		empl_name = ''.join(random.choice(string.ascii_letters) for i in range(15))
		empl_age = random.randint(23, 55)
		empl_adress = random.choice(self.empl_adress_list)
		date = str(datetime.datetime.now())
		is_ba = random.randint(0, 2)
		
		self.cursor.execute(self.sql_insert['insert']  % 
								 	(epml_id, empl_name, empl_age, 
								 	empl_adress, date, eml, is_ba))
		self.connect.commit()


	def printAll(self):
		self.cursor.execute(self.sql_select['slc_all'])	
		print(self.cursor.fetchall())		
		

	def pr(self, ls):
		for i in ls:
			print(i)


	def print_ya_com(self, status):		
		bt = time.time()			
		self.cursor.execute(self.sql_select['slc_rowid_eml_name'])		
		et = time.time()	
		self.pr(self.cursor.fetchall())		
		print(status, ':', et - bt)


	def create_index(self, sql_create_idx):
		'''return status(str)'''
		self.cursor.execute(sql_create_idx)
		return 'index created'


	def print_ya_com_by_index(self, status):
		bt = time.time()
		try:
			self.cursor.execute(self.sql_select['slc_rowid_idx'])
		except sqlite3.OperationalError as err:
			print('sqlite3 err: {0}'.format(err))			
		et = time.time()
		print(status, ':', et - bt)
		#print(self.cursor.fetchall())		


	def print_where_empl_id(self, status):
		bt = time.time()	
		print(self.sql_select['slc_empl_id'])			
		self.connect.execute(self.sql_select['slc_empl_id'])
		et = time.time()	
		print(self.cursor.fetchall())	
		print(status, ':', et - bt)


	def drop_index(self):
		'''return status(str)'''
		try:
			self.cursor.execute('DROP INDEX idx_ya')
			return 'index droped'
		except sqlite3.OperationalError as err:
			print('sqlie3 err: {0}'.format(err))
			return 'index has not created'


	def close_connection(self):
		self.connect.close()

	def query(self, sql_str, status):
		bt = time.time()	
		self.cursor.execute(sql_str)
		#self.pr(self.cursor.fetchall())
		et = time.time()	
		print(status, ':', et - bt, '\n')



s = SqliteTest('example.db')

#for i in range(15):
#	print(i)
#	s.insert_table()

#status = 'without index'
#s.query(s.sql_select['slc_rowid_eml_name'], status)

#status = s.create_index(s.sql_index['idx_com'])
#s.query(s.sql_select['slc_by_idx_com'], status)
#s.print_ya_com(status)
#status = s.drop_index()
#s.print_ya_com(status)

s.close_connection()