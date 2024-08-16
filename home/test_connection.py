import pyodbc

def test_connection():
    server = 'LC-LAPTOP\SQLEXPRESS'  # Tên hoặc địa chỉ IP của máy chủ SQL Server
    database = 'webgear'  # Tên cơ sở dữ liệu
    username = 'sa'  # Tên người dùng
    password = '29102003'  # Mật khẩu
    driver = '{ODBC Driver 17 for SQL Server}'  # Trình điều khiển ODBC

    try:
        conn = pyodbc.connect(
            f'DRIVER={driver};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'UID={username};'
            f'PWD={password}'
        )
        print("Kết nối thành công!")
        conn.close()
    except pyodbc.Error as e:
        print(f"Lỗi kết nối: {e}")

if __name__ == "__main__":
    test_connection()
