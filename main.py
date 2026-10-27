while True:
    print("Menu")
    print("1. Nhập thông tin sinh viên")
    print("2. Xem danh sách sinh viên")
    print("3. Xoá sinh viên")
    print("4. Cập nhật thông tin sinh viên")
    print("0. Thoát")
    chon = int(input("Mời bạn chọn: "))
    if chon == 0:
        break
    elif chon == 1:
        print("Đây là chức năng nhập thông tin sinh viên")
    elif chon ==2:
        print("Chức năng xem danh sách Sinh viên")
    elif chon==3:
        print("Chức năng xoá sinh viên")
    elif chon==4:
        print("Cập nhật thông tin sinh viên")
    else:
        print("Vui lòng chọn từ 0..3")