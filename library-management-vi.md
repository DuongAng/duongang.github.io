# Hệ thống Quản lý Thư viện
## Library Management System

---

## Mục lục
1. [Mô tả dự án](#1-mô-tả-dự-án)
2. [Chức năng hệ thống](#2-chức-năng-hệ-thống)
3. [Các module và tính năng](#3-các-module-và-tính-năng)
4. [Công nghệ](#4-công-nghệ)
5. [Mục đích hệ thống](#5-mục-đích-hệ-thống)
6. [Yêu cầu chức năng và phi chức năng](#6-yêu-cầu-chức-năng-và-phi-chức-năng)
7. [Kiến trúc cơ sở dữ liệu](#7-kiến-trúc-cơ-sở-dữ-liệu)
8. [Ràng buộc toàn vẹn dữ liệu](#8-ràng-buộc-toàn-vẹn-dữ-liệu)
9. [Trigger](#9-trigger)
10. [Chỉ mục](#10-chỉ-mục)
11. [Triển khai (Giai đoạn 3)](#11-triển-khai-giai-đoạn-3)
12. [Cài đặt và chạy](#12-cài-đặt-và-chạy)

---

## 1. Mô tả dự án

Hệ thống Quản lý Thư viện là một ứng dụng web được thiết kế để tự động hóa các quy trình phục vụ thư viện. Hệ thống cho phép quản lý sách, người dùng, quy trình mượn và trả sách, cũng như phạt do trễ hạn.

Dự án được phát triển bằng các công nghệ hiện đại: **Spring Boot** cho backend và **React** cho frontend, với cơ sở dữ liệu **PostgreSQL**.

---

## 2. Chức năng hệ thống

| Chức năng | Mô tả |
|---------|----------|
| Quản lý sách | Thêm, sửa, xóa sách |
| Quản lý người dùng | Đăng ký, phân quyền, xóa |
| Mượn sách | Yêu cầu mượn, phê duyệt, từ chối |
| Trả sách | Xác nhận trả sách, tự động tính phạt |
| Quản lý phạt | Xem, thanh toán, xóa phạt |
| Nhật ký hoạt động | Ghi lại tất cả các hành động trong hệ thống |
| Xác thực | JWT token để truy cập an toàn |

---

## 3. Các module và tính năng

### 3.1 Quản trị viên (Admin)

| Tính năng | Mô tả |
|------------------|----------|
| Quản lý người dùng | Xem tất cả người dùng, thay đổi quyền, xóa |
| Quản lý sách | CRUD đầy đủ cho sách, tác giả, thể loại, nhà xuất bản |
| Quản lý mượn sách | Phê duyệt/từ chối yêu cầu, xác nhận trả sách |
| Quản lý phạt | Xem tất cả phạt, xác nhận thanh toán, xóa |
| Nhật ký hoạt động | Xem tất cả hành động trong hệ thống, xóa log |

### 3.2 Nhân viên thư viện (Staff)

| Tính năng | Mô tả |
|------------------|----------|
| Quản lý sách | Thêm, sửa, xóa sách |
| Quản lý mượn sách | Phê duyệt/từ chối yêu cầu mượn |
| Trả sách | Xác nhận trả sách |
| Quản lý phạt | Xem phạt, xác nhận thanh toán |

### 3.3 Độc giả (User)

| Tính năng | Mô tả |
|------------------|----------|
| Xem danh mục | Tìm kiếm và xem sách có sẵn |
| Yêu cầu mượn sách | Gửi yêu cầu mượn sách |
| Sách của tôi | Xem các lần mượn hiện tại và trước đó |
| Phạt của tôi | Xem phạt và trạng thái |
| Hồ sơ | Chỉnh sửa thông tin cá nhân, đổi mật khẩu |

---

## 4. Công nghệ

### Backend
| Công nghệ | Phiên bản | Mục đích |
|------------|--------|------------|
| Java | 17 | Ngôn ngữ lập trình |
| Spring Boot | 3.x | Framework cho backend |
| Spring Security | 6.x | Xác thực và phân quyền |
| Spring Data JPA | 3.x | Làm việc với cơ sở dữ liệu |
| JWT | - | Token để xác thực |
| Lombok | - | Giảm boilerplate code |
| Maven | - | Quản lý dependencies |

### Frontend
| Công nghệ | Phiên bản | Mục đích |
|------------|--------|------------|
| React | 18.x | Thư viện cho UI |
| Vite | 5.x | Công cụ build |
| Tailwind CSS | 3.x | CSS framework |
| Axios | - | HTTP client |
| React Router | 6.x | Định tuyến |
| Lucide React | - | Icon |

### Cơ sở dữ liệu
| Công nghệ | Mục đích |
|------------|------------|
| PostgreSQL | CSDL chính |

---

## 5. Mục đích hệ thống

### Vấn đề

Quản lý thư viện truyền thống gặp phải một số vấn đề:
- **Ghi chép thủ công** sách dẫn đến sai sót và mất dữ liệu
- **Thiếu kiểm soát** thời hạn trả sách
- **Khó tìm kiếm** sách trong danh mục
- **Quản lý không hiệu quả** phạt và nợ
- **Không có lịch sử** các thao tác và kiểm tra

### Mục tiêu

Tạo hệ thống tự động hóa để:
- **Đơn giản hóa** quy trình mượn và trả sách
- **Tự động hóa** tính phạt khi trễ hạn
- **Đảm bảo** tìm kiếm nhanh trong danh mục
- **Lưu nhật ký** tất cả thao tác để kiểm tra
- **Phân quyền truy cập** theo vai trò người dùng

---

## 6. Yêu cầu chức năng và phi chức năng

### Yêu cầu chức năng

| ID | Yêu cầu |
|----|------------|
| FR1 | Hệ thống phải cho phép đăng ký người dùng mới |
| FR2 | Hệ thống phải hỗ trợ ba vai trò: Admin, Staff, User |
| FR3 | Người dùng có thể tìm kiếm sách theo tên, tác giả, thể loại |
| FR4 | Độc giả có thể gửi yêu cầu mượn sách |
| FR5 | Staff/Admin có thể phê duyệt hoặc từ chối yêu cầu |
| FR6 | Hệ thống tự động tính phạt khi trễ hạn |
| FR7 | Hệ thống lưu nhật ký tất cả hành động của người dùng |
| FR8 | Admin có thể quản lý người dùng và quyền của họ |

### Yêu cầu phi chức năng

| ID | Yêu cầu |
|----|------------|
| NFR1 | Thời gian phản hồi API không quá 2 giây |
| NFR2 | Mật khẩu được lưu dưới dạng mã hóa (BCrypt) |
| NFR3 | Hệ thống phải hoạt động trên các trình duyệt hiện đại |
| NFR4 | Giao diện phải trực quan và dễ hiểu |
| NFR5 | Hệ thống phải hỗ trợ nhiều người dùng cùng làm việc |

---

## 7. Kiến trúc cơ sở dữ liệu

### Sơ đồ ER (Thực thể)

![image](./data/1.png)

![image](./data/2.png)


### Các bảng cơ sở dữ liệu

| Bảng | Mô tả |
|---------|----------|
| roles | Vai trò người dùng (ADMIN, STAFF, USER) |
| users | Người dùng hệ thống |
| books | Sách trong danh mục |
| book_copies | Bản sao sách trong thư viện |
| categories | Thể loại sách |
| authors | Tác giả sách |
| book_authors | Liên kết sách và tác giả (M:N) |
| publishers | Nhà xuất bản |
| libraries | Chi nhánh thư viện |
| borrow_records | Bản ghi mượn sách |
| fines | Phạt do trễ hạn |
| activity_logs | Nhật ký hoạt động |

---

## 8. Ràng buộc toàn vẹn dữ liệu (Constraints)

### Users
```sql
ALTER TABLE users
    ADD CONSTRAINT users_username_unique UNIQUE (username),
    ADD CONSTRAINT users_email_unique UNIQUE (email);
```
**Mục đích:** Đảm bảo tên đăng nhập và email là duy nhất cho mỗi người dùng.

### Books
```sql
ALTER TABLE books
    ADD CONSTRAINT books_isbn_unique UNIQUE (isbn),
    ADD CONSTRAINT books_total_quantity_check CHECK (total_quantity >= 0),
    ADD CONSTRAINT books_available_quantity_check 
        CHECK (available_quantity >= 0 AND available_quantity <= total_quantity);
```
**Mục đích:** ISBN duy nhất, số lượng sách không thể âm.

### Roles
```sql
ALTER TABLE roles
    ADD CONSTRAINT roles_name_unique UNIQUE (name);
```
**Mục đích:** Không thể tạo hai vai trò giống nhau.

### Borrow Records
```sql
ALTER TABLE borrow_records
    ADD CONSTRAINT borrowrecords_due_after_borrow CHECK (due_date >= borrow_date),
    ADD CONSTRAINT borrowrecords_return_after_borrow 
        CHECK (return_date IS NULL OR return_date >= borrow_date),
    ADD CONSTRAINT borrowrecords_fine_rate_check CHECK (daily_fine_rate >= 0);
```
**Mục đích:** Kiểm tra logic ngày tháng và tỷ lệ phạt.

### Fines
```sql
ALTER TABLE fines
    ADD CONSTRAINT fines_amount_check CHECK (amount >= 0),
    ADD CONSTRAINT fines_latedays_check CHECK (late_days >= 0);
```
**Mục đích:** Số tiền phạt và số ngày trễ không thể âm.

---

## 9. Trigger

### Giảm số lượng khi mượn
```sql
CREATE OR REPLACE FUNCTION decrease_available_quantity()
RETURNS TRIGGER AS $$
BEGIN
    IF (SELECT available_quantity FROM books WHERE id = NEW.book_id) <= 0 THEN
        RAISE EXCEPTION 'Book is not available';
    END IF;
    
    UPDATE books
    SET available_quantity = available_quantity - 1
    WHERE id = NEW.book_id;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_decrease_quantity
BEFORE INSERT ON book_copies
FOR EACH ROW
EXECUTE FUNCTION decrease_available_quantity();
```
**Mục đích:** Khi mượn sách, tự động giảm số lượng có sẵn.

### Tăng số lượng khi trả
```sql
CREATE OR REPLACE FUNCTION increase_available_quantity()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.return_date IS NOT NULL AND OLD.return_date IS NULL THEN
        UPDATE books
        SET available_quantity = available_quantity + 1
        WHERE id = (SELECT book_id FROM book_copies WHERE id = NEW.book_copy_id);
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_increase_quantity
AFTER UPDATE ON borrow_records
FOR EACH ROW
EXECUTE FUNCTION increase_available_quantity();
```
**Mục đích:** Khi trả sách, tự động tăng số lượng có sẵn.

> **Lưu ý:** Trong phiên bản hiện tại, logic thay đổi số lượng sách được thực hiện ở tầng ứng dụng (trong BorrowService.java) để kiểm soát và xử lý lỗi tốt hơn.

---

## 10. Chỉ mục

```sql
-- Tìm kiếm sách theo tên
CREATE INDEX idx_books_title ON books(title);

-- Tìm kiếm tác giả theo tên
CREATE INDEX idx_authors_name ON authors(name);

-- Tìm kiếm sách theo thể loại
CREATE INDEX idx_books_category ON books(category_id);

-- Tìm kiếm bản ghi mượn theo người dùng
CREATE INDEX idx_borrow_records_user ON borrow_records(user_id);

-- Tìm kiếm bản ghi mượn theo trạng thái
CREATE INDEX idx_borrow_records_status ON borrow_records(status);
```
**Mục đích:** Tăng tốc tìm kiếm và lọc dữ liệu.

---

## 11. Triển khai (Giai đoạn 3)

### Cấu trúc dự án

```
library-management/
├── backend/
│   └── src/main/java/com/library/
│       ├── controller/     # REST API controllers
│       ├── service/        # Business logic
│       ├── repository/     # JPA repositories
│       ├── entity/         # Database entities
│       ├── dto/            # Data Transfer Objects
│       ├── security/       # JWT, Security Config
│       └── config/         # Configurations
│
└── frontend/
    └── src/
        ├── components/     # React components
        ├── pages/          # Pages
        ├── services/       # API services
        └── context/        # React Context
```

### Các thành phần chính Backend

| Thành phần | Mục đích |
|-----------|------------|
| SecurityConfig | Cấu hình Spring Security, bộ lọc JWT |
| JwtUtil | Tạo và xác thực JWT token |
| GlobalExceptionHandler | Xử lý lỗi tập trung |
| DataInitializer | Khởi tạo dữ liệu ban đầu |

### API Endpoints

| Phương thức | Endpoint | Mô tả | Quyền truy cập |
|-------|----------|----------|--------|
| POST | /api/auth/register | Đăng ký | Tất cả |
| POST | /api/auth/login | Đăng nhập | Tất cả |
| GET | /api/books | Danh sách sách | Tất cả đã xác thực |
| POST | /api/books | Thêm sách | Staff, Admin |
| DELETE | /api/books/{id} | Xóa sách | Staff, Admin |
| POST | /api/borrows | Yêu cầu mượn | User |
| PUT | /api/borrows/{id}/approve | Phê duyệt mượn | Staff, Admin |
| PUT | /api/borrows/{id}/return | Xác nhận trả | Staff, Admin |
| GET | /api/fines | Danh sách phạt | Staff, Admin |
| PUT | /api/fines/{id}/pay | Thanh toán phạt | Staff, Admin |
| GET | /api/activity-logs | Nhật ký hoạt động | Admin |
| GET | /api/users | Danh sách người dùng | Admin |

### Quy trình mượn sách

```
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│  User    │     │  PENDING │     │ BORROWING│     │ RETURNED │
│ Request  │────►│ (Chờ)    │────►│ (Đang mượn)│───►│ (Hoàn tất)│
└──────────┘     └──────────┘     └──────────┘     └──────────┘
                      │                 │
                      ▼                 ▼
                 ┌──────────┐     ┌──────────┐
                 │ REJECTED │     │  OVERDUE │
                 │ (Từ chối)│     │ + Phạt   │
                 └──────────┘     └──────────┘
```

### Đặc điểm triển khai

1. **Soft Delete** — Khi xóa người dùng hoặc sách, lịch sử vẫn được giữ trong borrow_records (username, book_title được lưu riêng)

2. **Activity Logging** — Tất cả hành động quan trọng được ghi vào nhật ký:
   - Đăng ký người dùng
   - Yêu cầu mượn sách
   - Phê duyệt/từ chối yêu cầu
   - Trả sách
   - Thanh toán/xóa phạt
   - Hành động quản trị

3. **JWT Authentication** — Xác thực an toàn bằng token

4. **Role-based Access Control** — Phân quyền truy cập theo vai trò thông qua @PreAuthorize

---

## 12. Cài đặt và chạy

### Yêu cầu
- Java 17+
- Node.js 18+
- PostgreSQL 14+
- Maven

### Backend
```bash
cd backend
# Cấu hình application.properties (CSDL)
mvn spring-boot:run
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```



*Hệ thống Quản lý Thư viện © 2026*
