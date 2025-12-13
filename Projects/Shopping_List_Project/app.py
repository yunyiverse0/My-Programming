from flask import Flask, render_template, request, jsonify
import pymysql

app = Flask(__name__)

# DB 연결 설정 (한윤이 님 환경에 맞게 수정 필요)
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'shh..',
    'db': 'shopping_list_project',
    'charset': 'utf8'
}

def get_db_connection():
    return pymysql.connect(**db_config)

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    # 1. 검색어와 카테고리 필터 처리
    search_query = request.args.get('search', '')
    category_filter = request.args.get('category', '')

    sql = "SELECT * FROM products WHERE name LIKE %s"
    params = [f'%{search_query}%']

    if category_filter:
        sql += " AND category = %s"
        params.append(category_filter)

    cursor.execute(sql, params)
    products = cursor.fetchall()

    # 2. 각 상품별로 연결된 링크 정보 가져오기 (이 부분이 핵심입니다)
    # 실제로는 JOIN을 쓰는 게 좋지만, 이해를 돕기 위해 로직을 풀어서 씁니다.
    for product in products:
        cursor.execute("SELECT platform_name, buy_url FROM product_links WHERE product_id = %s", (product['id'],))
        product['links'] = cursor.fetchall() 
        # 결과 예시: [{'platform_name': '무신사', 'url': '...'}, {'platform_name': '지그재그', 'url': '...'}]

    cursor.close()
    conn.close()

    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
