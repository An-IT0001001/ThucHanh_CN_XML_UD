from lxml import etree

tree = etree.parse("sinhvien.xml")
root = tree.getroot()

# 1. Lấy tất cả sinh viên (in dưới dạng XML)
print("1. Tất cả sinh viên:")
students = root.xpath("//student")
for s in students:
    print(etree.tostring(s, pretty_print=True, encoding="unicode"))
print()

# 2. Liệt kê tên tất cả sinh viên
print("2. Tên tất cả sinh viên:", root.xpath("//student/name/text()"))
print()

# 3. Lấy tất cả id của sinh viên
print("3. ID của tất cả sinh viên:", root.xpath("//student/id/text()"))
print()

# 4. Lấy ngày sinh của sinh viên có id = 'SV01'
print("4. Ngày sinh SV01:", root.xpath("//student[id='SV01']/date/text()"))
print()

# 5. Lấy các khóa học (tên khóa trong enrollment)
print("5. Các khóa học:", root.xpath("//enrollment/course/text()"))
print()

# 6. Lấy toàn bộ thông tin của sinh viên đầu tiên (dạng text từng trường)
print("6. Thông tin sinh viên đầu tiên:")
first = root.xpath("//student[1]")[0]
print("id:", first.findtext("id"))
print("name:", first.findtext("name"))
print("date:", first.findtext("date"))
print()

# 7. Lấy mã sinh viên đăng ký khóa học 'Vatly203'
print("7. Mã sinh viên đăng ký Vatly203:", root.xpath("//enrollment[course='Vatly203']/studentRef/text()"))
print()

# 8. Lấy tên sinh viên học môn 'Toan101'
print("8. Tên sinh viên học Toan101:",
      root.xpath("//student[id=//enrollment[course='Toan101']/studentRef]/name/text()"))
print()

# 9. Lấy tên sinh viên học môn 'Vatly203'
print("9. Tên sinh viên học Vatly203:",
      root.xpath("//student[id=//enrollment[course='Vatly203']/studentRef]/name/text()"))
print()

# 10. Lấy ngày sinh của sinh viên có id='SV01' (nhắc lại)
print("10. Ngày sinh SV01:", root.xpath("//student[id='SV01']/date/text()"))
print()

# 11. Lấy tên và ngày sinh của mọi sinh viên sinh năm 1997
names_1997 = root.xpath("//student[starts-with(date,'1997')]/name/text()")
dates_1997 = root.xpath("//student[starts-with(date,'1997')]/date/text()")
print("11. Sinh viên sinh năm 1997 (tên - ngày):")
for n, d in zip(names_1997, dates_1997):
    print("-", n, "-", d)
print()

# 12. Lấy tên của các sinh viên có ngày sinh trước năm 1998
print("12. Sinh viên sinh trước 1998:", root.xpath("//student[number(substring(date,1,4)) < 1998]/name/text()"))
print()

# 13. Đếm tổng số sinh viên
print("13. Tổng số sinh viên:", int(root.xpath("count(//student)")))
print()

# 14. Lấy tất cả sinh viên chưa đăng ký môn nào (in tên)
print("14. Sinh viên chưa đăng ký môn học:",
      root.xpath("//student[not(id=//enrollment/studentRef)]/name/text()"))
print()

# 15. Lấy phần tử <date> anh em ngay sau <name> của SV01
print("15. <date> ngay sau <name> của SV01:",
      root.xpath("//student[id='SV01']/name/following-sibling::date/text()"))
print()

# 16. Lấy phần tử <id> anh em ngay trước <name> của SV02
print("16. <id> ngay trước <name> của SV02:",
      root.xpath("//student[id='SV02']/name/preceding-sibling::id/text()"))
print()

# 17. Lấy toàn bộ node <course> trong cùng một <enrollment> với studentRef='SV03'
print("17. Khóa học SV03:", root.xpath("//enrollment[studentRef='SV03']/course/text()"))
print()

# 18. Lấy sinh viên có họ là 'Trần'
print("18. Sinh viên có họ 'Trần':", root.xpath("//student[starts-with(name,'Trần')]/name/text()"))
print()

# 19. Lấy năm sinh của sinh viên SV01
print("19. Năm sinh SV01:", root.xpath("substring(//student[id='SV01']/date/text(),1,4)"))
print()
