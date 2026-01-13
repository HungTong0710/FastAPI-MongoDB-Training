# FastAPI & MongoDB Training - Setup Guide

- Chào các bạn. Để đảm bảo chúng ta có nhiều thời gian thực hành (coding) nhất có thể, các bạn vui lòng **hoàn thành các bước chuẩn bị dưới đây tại nhà**.

## Bước 0: Prerequisites
- Python (3.9 trở lên)
- Visual Studio Code (Editor)
- MongoDB Community Server (Database) via https://www.mongodb.com/try/download/community

## Bước 1: Clone Project

Mở Terminal (hoặc CMD/PowerShell) và chạy lệnh sau để tải mã nguồn về máy:

```bash

git clone https://github.com/HungTong0710/FastAPI-MongoDB-Training.git
cd FastAPI-MongoDB-Training

```
## Bước 2: Tạo môi trường ảo (Virtual Environment)

Đối với Windows:

```Bash

python -m venv venv
.\venv\Scripts\activate

```
Đối với MacOS / Linux:

```Bash

python3 -m venv venv
source venv/bin/activate

```
(Sau khi chạy, bạn sẽ thấy chữ (venv) xuất hiện ở đầu dòng lệnh).

## Bước 3: Cài đặt thư viện (QUAN TRỌNG)
### 3.1. Cài đặt PyTorch (CPU Only) - Copy đúng lệnh dành cho máy của bạn:

- Cho Windows:

``` Bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
```
- Cho MacOS / Linux:

```Bash
pip install torch
```
### 3.2. Cài đặt `requirements` Sau khi cài xong torch ở trên:

```Bash
pip install -r requirements.txt
```
## Bước 4: Tải trước Model AI
Model AI cần tải về trước để tránh nghẽn mạng tại lớp. Chạy lệnh:

```Bash
python setup_model.py
```
*** Kiểm tra thành công *** 
Nếu Bước 4 hiện thông báo:

`Model loaded and ready!`

--- You're all done! See you at this exciting training session. ---

***Hung Tong***