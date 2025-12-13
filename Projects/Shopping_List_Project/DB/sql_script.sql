-- =========================================
-- 1. 데이터베이스 생성
-- =========================================
CREATE DATABASE IF NOT EXISTS shopping_list_project
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_unicode_ci;

USE shopping_list_project;


-- =========================================
-- 2. 기존 테이블 초기화 (FK 고려)
-- =========================================
SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS product_links;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS users;

SET FOREIGN_KEY_CHECKS = 1;


-- =========================================
-- 3. 사용자 테이블
-- =========================================
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE COMMENT '아이디',
    password_hash VARCHAR(255) NOT NULL COMMENT '암호화된 비밀번호'
);


-- =========================================
-- 4. 상품 테이블
-- =========================================
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL COMMENT '이 상품을 등록한 사용자 ID',
    name VARCHAR(255) NOT NULL COMMENT '상품명',
    category VARCHAR(50) COMMENT '카테고리 (상의/하의 등)',
    image_url TEXT COMMENT '대표 이미지 URL',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_products_user
        FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE
);


-- =========================================
-- 5. 상품별 플랫폼 링크 테이블
-- =========================================
CREATE TABLE product_links (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL COMMENT '상품 ID',
    platform_name VARCHAR(50) NOT NULL COMMENT '플랫폼 이름',
    buy_url TEXT NOT NULL COMMENT '구매 URL',
    CONSTRAINT fk_links_product
        FOREIGN KEY (product_id)
        REFERENCES products(id)
        ON DELETE CASCADE
);


-- =========================================
-- 6. 테스트 데이터
-- =========================================

-- 사용자
INSERT INTO users (username, password_hash)
VALUES ('testuser', 'hashed_password_example');

-- 상품
INSERT INTO products (user_id, name, category, image_url) VALUES
(1, '나이키 윈드브레이커', '상의', 'https://dummyimage.com/300x300/000/fff&text=Nike'),
(1, '와이드 데님 팬츠', '하의', 'https://dummyimage.com/300x300/000/fff&text=Denim'),
(1, '아디다스 운동화', '신발', 'https://dummyimage.com/300x300/000/fff&text=Adidas');

-- 플랫폼 링크
INSERT INTO product_links (product_id, platform_name, buy_url) VALUES
(1, '무신사', 'https://www.musinsa.com'),
(1, '지그재그', 'https://zigzag.kr'),
(2, '에이블리', 'https://a-bly.com'),
(3, '아디다스 공홈', 'https://www.adidas.co.kr'),
(3, '무신사', 'https://www.musinsa.com'),
(3, 'KREAM', 'https://kream.co.kr');


-- =========================================
-- 7. 확인용 조회
-- =========================================
SELECT * FROM users;
SELECT * FROM products;
SELECT * FROM product_links;
