
print(' -- HỆ THỐNG TIẾP NHẬN BỆNH NHÂN --- ');
name_patient = input ( 'Nhập tên bệnh nhân: ');
age = int(input ('Mời bạn nhập tuổi: '));
symptom = input ('Mời bạn nhập triệu chứng bênh: ');

print(' - PHIẾU KHÁM BỆNH --- ');
print ('Tên bệnh nhân:', symptom);
print('Tuổi:', name_patient);
print ('Triệu chứng:', age);


# luồng ở đây là cho bệnh nhân nhập dữ liệu đầu vào sau đó in các dữ liệu đầu vào đó vào phiếu bệnh nhân và in ra 
# trưởng trình không crash vì giá trị vẫn được nhập đủ biến vẫn được gán đủ nhưng việc gán dữ liệu bị sai 
# Lỗi ở đây là do gán sai biến cho từng giá trị in ra 
# sửa : 
print(' -- HỆ THỐNG TIẾP NHẬN BỆNH NHÂN --- ');
name_patient = input ( 'Nhập tên bệnh nhân: ');
age = int(input ('Mời bạn nhập tuổi: '));
symptom = input ('Mời bạn nhập triệu chứng bênh: ');

print(' - PHIẾU KHÁM BỆNH --- ');
print ('Tên bệnh nhân:', name_patient);
print('Tuổi:', age);
print ('Triệu chứng:', symptom);