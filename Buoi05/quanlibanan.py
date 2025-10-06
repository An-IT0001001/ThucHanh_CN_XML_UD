from lxml import etree

tree = etree.parse("quanlybanan.xml")
root = tree.getroot()

# 1. Lấy tất cả bàn
print("1. Tất cả bàn:", root.xpath("//BAN/TENBAN/text()"))

# 2. Lấy tất cả nhân viên
print("2. Tất cả nhân viên:", root.xpath("//NHANVIEN/TENV/text()"))

# 3. Lấy tất cả tên món
print("3. Tất cả tên món:", root.xpath("//MON/TENMON/text()"))

# 4. Lấy tên nhân viên có mã NV02
print("4. Tên nhân viên có mã NV02:", root.xpath("//NHANVIEN[MANV='NV02']/TENV/text()"))

# 5. Lấy tên và số điện thoại của nhân viên NV03
print("5. Tên và SDT của NV03:", root.xpath("//NHANVIEN[MANV='NV03']/TENV/text() | //NHANVIEN[MANV='NV03']/SDT/text()"))

# 6. Lấy tên món có giá > 50,000
print("6. Tên món có giá > 50,000:", root.xpath("//MON[GIA>50000]/TENMON/text()"))

# 7. Lấy số bàn của hóa đơn HD03
print("7. Số bàn của hóa đơn HD03:", root.xpath("//HOADON[SOHD='HD03']/SOBAN/text()"))

# 8. Lấy tên món có mã M02
print("8. Tên món có mã M02:", root.xpath("//MON[MAMON='M02']/TENMON/text()"))

# 9. Lấy ngày lập của hóa đơn HD03
print("9. Ngày lập của hóa đơn HD03:", root.xpath("//HOADON[SOHD='HD03']/NGAYLAP/text()"))

# 10. Lấy tất cả mã món trong hóa đơn HD01
mamons = root.xpath("//HOADON[SOHD='HD01']//MAMON/text()")
print("10. Mã món trong hóa đơn HD01:", mamons)

# 11. Lấy tên món trong hóa đơn HD01
tenmons = [root.xpath(f"//MON[MAMON='{ma}']/TENMON/text()")[0]
           for ma in mamons if root.xpath(f"//MON[MAMON='{ma}']/TENMON/text()")]
print("11. Tên món trong hóa đơn HD01:", tenmons)

# 12. Lấy tên nhân viên lập hóa đơn HD02
manv_hd02 = root.xpath("//HOADON[SOHD='HD02']/MANVREF/text()")
if manv_hd02:
    tennv_hd02 = root.xpath(f"//NHANVIEN[MANV='{manv_hd02[0]}']/TENV/text()")
    print("12. Tên nhân viên lập hóa đơn HD02:", tennv_hd02)
else:
    print("12. Không tìm thấy hóa đơn HD02")

# 13. Đếm số bàn
print("13. Tổng số bàn:", len(root.xpath("//BAN")))

# 14. Đếm số hóa đơn lập bởi NV01
print("14. Số hóa đơn lập bởi NV01:", len(root.xpath("//HOADON[MANVREF='NV01']")))

# 15. Lấy tên tất cả món có trong hóa đơn của bàn số 2
mamons_ban2 = root.xpath("//HOADON[SOBAN='2']//MAMON/text()")
tenmons_ban2 = [root.xpath(f"//MON[MAMON='{ma}']/TENMON/text()")[0]
                for ma in mamons_ban2 if root.xpath(f"//MON[MAMON='{ma}']/TENMON/text()")]
print("15. Tên món trong hóa đơn bàn số 2:", tenmons_ban2)

# 16. Lấy tất cả nhân viên từng lập hóa đơn cho bàn số 3
nv_ban3 = root.xpath("//HOADON[SOBAN='3']/MANVREF/text()")
ten_nv_ban3 = [root.xpath(f"//NHANVIEN[MANV='{nv}']/TENV/text()")[0]
               for nv in nv_ban3 if root.xpath(f"//NHANVIEN[MANV='{nv}']/TENV/text()")]
print("16. Nhân viên lập hóa đơn cho bàn số 3:", list(set(ten_nv_ban3)))

# 17. Lấy tất cả hóa đơn mà nhân viên nữ lập
hd_nu = root.xpath("//HOADON[MANVREF=//NHANVIEN[GIOITINH='Nữ']/MANV]/SOHD/text()")
print("17. Hóa đơn nhân viên nữ lập:", hd_nu)

# 18. Lấy tất cả nhân viên từng phục vụ bàn số 1
nv_ban1 = root.xpath("//HOADON[SOBAN='1']/MANVREF/text()")
ten_nv_ban1 = [root.xpath(f"//NHANVIEN[MANV='{nv}']/TENV/text()")[0]
               for nv in nv_ban1 if root.xpath(f"//NHANVIEN[MANV='{nv}']/TENV/text()")]
print("18. Nhân viên từng phục vụ bàn số 1:", list(set(ten_nv_ban1)))

# 19. Lấy tất cả món được gọi nhiều hơn 1 lần trong các hóa đơn
mamon_all = root.xpath("//CTHD/MAMON/text()")
mon_counts = {ma: mamon_all.count(ma) for ma in set(mamon_all) if mamon_all.count(ma) > 1}
mon_nhieu = [root.xpath(f"//MON[MAMON='{ma}']/TENMON/text()")[0] for ma in mon_counts]
print("19. Món được gọi nhiều hơn 1 lần:", mon_nhieu)

# 20. Lấy tên bàn + ngày lập hóa đơn tương ứng SOHD='HD02'
ban_hd02 = root.xpath("//HOADON[SOHD='HD02']/SOBAN/text()")
ngay_hd02 = root.xpath("//HOADON[SOHD='HD02']/NGAYLAP/text()")
if ban_hd02 and ngay_hd02:
    tenban_hd02 = root.xpath(f"//BAN[SOBAN='{ban_hd02[0]}']/TENBAN/text()")
    print("20. HD02 - Tên bàn + ngày lập:", f"{tenban_hd02[0]} - {ngay_hd02[0]}")
else:
    print("20. Không tìm thấy HD02 hoặc dữ liệu bàn/ ngày lập.")
