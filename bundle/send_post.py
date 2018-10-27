import requests
import csv
rows = []
def conv_Date(a):
    a=a.split('-')
    mon = {
        'Jan':1,
        'Feb':2,
        'Mar':3,
        'Apr':4,
        'May':5,
        'Jun':6,
        'Jul':7,
        'Aug':8,
        'Sep':9,
        'Oct':10,
        'Nov':11,
        'Dec':12
    }
    a=a[2]+'-'+str(mon[a[1]])+'-'+a[0]
    return a
with open('1.csv') as f:
     csv_reader = csv.reader(f, delimiter=',')
     for row in csv_reader:
            rows.append(row)
    
""" mutation insert_GS {
  insert_GS(
    objects: [
      {
        isin: "",
        return_rate: "",
        date_of_issue: "",
        date_of_maturity: "",
        outstanding_stock: "",
      }
    ]
  ) {
    returning {
      isin
    }
  }
} """

url = "https://bundle-sudo.herokuapp.com/v1alpha1/graphql"
post_data= {"query":'mutation insert_GS {insert_GS(objects:[{isin:"'+str(rows[x][0])+'",return_rate:"'+str(float(rows[x][1].split('%')[0]))+'",date_of_issue:"'+str(conv_Date(rows[x][2]))+'",date_of_maturity:"'+conv_Date(rows[x][3])+'",outstanding_stock:"'+rows[x][4]+'",}]) {returning {isin} }}',"operationName":"insert_GS"}
r = requests.post(url, data=post_data, headers={'X-Hasura-Access-Key':'sudo-bundle','Content-Type':'application/json'})
#rows[1][1].split('%')[0]
print(r.status_code, r.reason)