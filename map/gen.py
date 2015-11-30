import time
import MySQLdb
import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials

#google spread
json_key = json.load(open('/home/ec2-user/scripts/g_api.json'))
scope = ['https://spreadsheets.google.com/feeds']
credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
gc = gspread.authorize(credentials)
s = gc.open_by_key('1R-mEJqgQKbyOJuAHO-iLFsNJR8sB5UQC3YE-C7fOSJ8')

#mysql
conn = MySQLdb.connect("localhost","root","clusteringshelter()","shelter" )
cursor = conn.cursor()


def get_tables():
    q = "SELECT table_name \
        FROM information_schema.TABLES \
        WHERE table_name like '%_CORE' and table_schema like 'shelter'"
    cursor.execute(q)
    rs = cursor.fetchall()
    return [v[0] for v in rs]

def get_cols(t):
    q = "SELECT `COLUMN_NAME` \
        FROM `INFORMATION_SCHEMA`.`COLUMNS` \
        WHERE `TABLE_SCHEMA`='shelter' \
		AND DATA_TYPE like 'decimal' \
        AND `TABLE_NAME`='%s';" % (t)
    c = ["_CREATOR_URI_USER", "_LAST_UPDATE_DATE"] 
    cursor.execute(q)
    rs = cursor.fetchall()
    c += [v[0] for v in rs if v[0].upper().endswith('_LAT') or v[0].upper().endswith('_LNG')]
    return ['cast(%s as char(200))' % v for v in c], c

def arr_up(cols, vals):
    if len(cols) == len(vals):
        cd = {}
        ret = []
        for i,v in enumerate(cols):
    	     cd[v] = vals[i]

        ret += [v for v in [cd]]
        return ret

def standardize(w):
	for i,v in enumerate(w):
		if v.upper().endswith('_LAT'):
			w[i] = 'lat'
		elif v.upper().endswith('_LNG'):
 			w[i] = 'lng'
		elif v.upper() == '_LAST_UPDATE_DATE':
			w[i] = 'up'
		elif v.upper() == '_CREATOR_URI_USER':
			w[i] = 'desc'
 
	return w

def pull_vals():
	car = []
	for t in get_tables():
		formatted, names = get_cols(t)
	
		q = "select '%s', %s from %s" % (t, ",".join(formatted), t)
	        cursor.execute(q)
	        rs = cursor.fetchall()
	
		names = ['tbl_nm'] + standardize(names)
		if len(rs) > 0:
		    for e in rs:
		        car += arr_up(names, e)		
	return car

def send(d):
	print 'd is: ' + str(d)
	w = s.get_worksheet(0)
	dv = ['tbl_nm','up','desc','lat','lng']	
	i = 1
	w.insert_row(dv, i)
	if d is not None:
		for v in d:
			if v.has_key('lat') and v['lat'] != '0.0000000000':
				i += 1
				row = []
				for k in dv:
					if v.has_key(k):
						row.append(v[k])
					else:
						row.append('')
				w.insert_row(row, i)
				print 'inserted: ' + str(row)
			

def clear_sheet():
	w = s.get_worksheet(0)
	r = w.range('A1:F100')
	for c in r:
		c.value = ''
	w.update_cells(r)	

if __name__ == '__main__':
	d = pull_vals()
	clear_sheet()
	send(d)
