import pyexcel

a_list = [
    {"Name":"Khanh",
    "Age":20
    },
    {"Name":"Adam",
    "Age":25
    },
    {"Name":"Tien",
    "Age":21
    }
]

pyexcel.save_as(records=a_list, dest_file_name="list_Khanh.xlsx")