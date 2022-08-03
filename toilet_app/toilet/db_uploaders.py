import os
import django
import csv
import sys

sys.path.append(os.pardir)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "toilet_grade_app.settings")
django.setup()

from toilet.models import *

CSV_PATH = '../toilet.csv'

def insert_toilet():
    with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
        data_reader = csv.DictReader(csvfile)
        print(data_reader)
        for row in data_reader:
            gender = 'BOTH' if int(row['MALE_WTRCLS_CNT']) > 0 and int(row['FEMALE_WTRCLS_CNT']) > 0  else 'MAN' if int(row['MALE_WTRCLS_CNT']) > 0 else 'WOMAN'
            Toilet.objects.create(name=row['PBCTLT_PLC_NM'], 
            address=row['REFINE_ROADNM_ADDR'], 
            gender=gender,
            isBisexual=row['MALE_FEMALE_TOILET_YN'] == 'Y',
            manToiletNum=int(row['MALE_WTRCLS_CNT']),
            womanToiletNum=int(row['FEMALE_WTRCLS_CNT']),
            urinalNum=int(row['MALE_UIL_CNT']),
            manDisabledToiletNum=int(row['MALE_DSPSN_WTRCLS_CNT']),
            womanDisabledToiletNum=int(row['FEMALE_DSPSN_WTRCLS_CNT']),
            disabledUrinalNum=int(row['MALE_DSPSN_UIL_CNT']),
            manChildToiletNum=int(row['MALE_CHILDUSE_WTRCLS_CNT']),
            womanChildToiletNum=int(row['FEMALE_CHILDUSE_WTRCLS_CNT']),
            childUrinalNum=int(row['MALE_CHILDUSE_UIL_CNT']),
            managementAgency=row['MANAGE_INST_NM'],
            phoneNumber=row['MANAGE_INST_TELNO'],
            openTime=row['OPEN_TM_INFO'],
            installationDate=row['INSTL_YY'],
            latitude=float(row['REFINE_WGS84_LAT']) if row['REFINE_WGS84_LAT'] != '' else None,
            longitude=float(row['REFINE_WGS84_LOGT']) if row['REFINE_WGS84_LOGT'] != '' else None)
    print('TOILET DATA UPLOADED SUCCESSFULY!')

insert_toilet()