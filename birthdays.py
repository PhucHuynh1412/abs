my_family = {'Phúc': 'ngày 24 tháng 12','Hiếu': 'ngày 13 tháng 10','Đông':'ngày 25 tháng 2','Vi': 'ngày 7 tháng 8'}

while True:
    name = input('Tên bạn là: ')
    name = name.title()
    if name == '':
        break
    if name in my_family:
        print(f'Ngày sinh của {name} là {my_family[name]}')
    else:
        print('Bạn chưa có thông tin ngày sinh')
        print('Bạn sinh ngày mấy tháng mấy')
        ngay_sinh = input()
        my_family[name] = ngay_sinh
        print('Ngày sinh của bạn đã được cập nhật')

print(my_family)

