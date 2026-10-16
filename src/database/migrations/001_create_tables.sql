/*
-----------------------------------------
CREATE SCHEMA
-----------------------------------------
*/
CREATE SCHEMA IF NOT EXISTS bcb;


/*
-----------------------------------------
TABLE CALENDAR
-----------------------------------------
*/
CREATE TABLE IF NOT EXISTS bcb.calendar AS
WITH RECURSIVE dates AS (
    SELECT DATE '1980-01-01' AS date
    UNION ALL
    SELECT (date + INTERVAL '1 day')::date
    FROM dates
    WHERE date < DATE '2065-12-31'
)
SELECT
    date,
    EXTRACT(YEAR FROM date)::int AS year,
    EXTRACT(MONTH FROM date)::int AS month,
    TO_CHAR(date, 'Month') AS month_name,
    TO_CHAR(date, 'Mon') AS month_short,
    EXTRACT(DAY FROM date)::int AS day,
    EXTRACT(DOY FROM date)::int AS day_of_year,
    EXTRACT(WEEK FROM date)::int AS week_number,
    EXTRACT(QUARTER FROM date)::int AS quarter,
    'Q' || EXTRACT(QUARTER FROM date)::int AS quarter_name,
    TO_CHAR(date, 'YYYY-MM') AS year_month,
    CASE WHEN EXTRACT(ISODOW FROM date) IN (6,7) THEN TRUE ELSE FALSE END AS is_weekend
FROM dates;


/*
-----------------------------------------
TABLE IPCA (GERAL)
-----------------------------------------
*/
CREATE TABLE IF NOT EXISTS bcb.ipca_geral (
    date DATE NOT NULL,
    indice FLOAT,
    acumulado FLOAT,
    acumulado12m FLOAT,
    nindice FLOAT,
    created_at TIMESTAMP DEFAULT NOW()
);


/*
-----------------------------------------
TABLE IPCA GRUPOS
-----------------------------------------
*/
CREATE TABLE IF NOT EXISTS bcb.ipca_grupos (
    date DATE NOT NULL,
    indice FLOAT,
    acumulado FLOAT,
    peso FLOAT,
    categoria TEXT,
    categoria_nome TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);


/*
-----------------------------------------
TABLE IPCA SUBGRUPOS
-----------------------------------------
*/
CREATE TABLE IF NOT EXISTS bcb.ipca_subgrupos (
    date DATE NOT NULL,
    indice FLOAT,
    acumulado FLOAT,
    peso FLOAT,
    categoria TEXT,
    categoria_nome TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);


/*
-----------------------------------------
TABLE IPCA ITENS
-----------------------------------------
*/
CREATE TABLE IF NOT EXISTS bcb.ipca_itens (
    date DATE NOT NULL,
    indice FLOAT,
    acumulado FLOAT,
    peso FLOAT,
    categoria TEXT,
    categoria_nome TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);


/*
-----------------------------------------
TABLE IPCA SUBITENS
-----------------------------------------
*/
CREATE TABLE IF NOT EXISTS bcb.ipca_subitens (
    date DATE NOT NULL,
    indice FLOAT,
    acumulado FLOAT,
    peso FLOAT,
    categoria TEXT,
    categoria_nome TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);



/*
-----------------------------------------
TABLE SELIC META
-----------------------------------------
*/
CREATE TABLE IF NOT EXISTS bcb.selic_meta (
    date DATE PRIMARY KEY,
    value FLOAT,
    series_id INT,
    created_at TIMESTAMP DEFAULT NOW()
);


/*
-----------------------------------------
TABLE SELIC OVER
-----------------------------------------
*/
CREATE TABLE IF NOT EXISTS bcb.selic_over (
    date DATE PRIMARY KEY,
    value FLOAT,
    series_id INT,
    created_at TIMESTAMP DEFAULT NOW()
);



/*
-----------------------------------------
TABLE IPCA TAXONOMIA MACRO
-----------------------------------------
*/
CREATE TABLE IF NOT EXISTS bcb.ipca_taxonomia (
    subitem_id varchar primary key,
    bloco_macro varchar not null,
    sub_bloco varchar null,
    categoria_cidada varchar null,
    subcategoria_cidada varchar null
);

