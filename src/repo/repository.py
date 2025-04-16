import psycopg2
from repo.partner_list_item import PartnerListItem
from repo.partner_edit_item import PartnerEditItem
from repo.partner_type_item import PartnerTypeItem


db_params = {
    'host': 'localhost',
    'port': 5432,
    'dbname': 'hexlet-demo-exam-2',
    'user': 'postgres',
    'password': 'postgres'
}


def create_connection():
    conn_str = f"host={db_params['host']} " + \
        f"port={db_params['port']} " + \
        f"dbname={db_params['dbname']} " + \
        f"user={db_params['user']} " + \
        f"password={db_params['password']} "
    conn = psycopg2.connect(conn_str)
    return conn


# Функция получает данные для главного окна приложения из БД
# Вычисление происходит на строне SQL по следующему алгоритму:
# Скидка вычисляется на основании суммы проданных элементов таблицы всех продаж
def get_records():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        with total_sales as (
            select pp.partner_id, sum(pp.product_amount) as total_sales
            from partner_products pp
            group by pp.partner_id
        )
        select
            p.id,
            pt.type_name,
            partner_name,
            director_name,
            phone,
            rating,
            case
                when total_sales > 300000 then 15
                when total_sales > 50000 then 10
                when total_sales > 10000 then 5
                else 0
            end as discount
        from partners p
            join partner_types pt
                on pt.id = p.partner_type
            left join total_sales
                on p.id = total_sales.partner_id
        order by partner_name;
    """)
    records = cursor.fetchall()
    result = []
    for record in records:
        result.append(PartnerListItem(*record))
    cursor.close()
    conn.close()
    return result


def get_record_by_id(record_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
       SELECT
            id,
            partner_type,
            partner_name,
            director_name,
            email,
            phone,
            address,
            rating
        FROM public.partners
        WHERE id = %s;
    """, [record_id])
    records = cursor.fetchall()
    result = None
    for record in records:
        result = PartnerEditItem(*record)
        break
    cursor.close()
    conn.close()
    return result


def update_record_by_id(record: PartnerEditItem):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT public.create_or_updatefuncName(%s, %s, %s);
        """,
        [
            record.id,
            record.full_name,
            record.birth_date
        ])
    conn.commit()
    cursor.close()
    conn.close()


def create_record(record: PartnerEditItem):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO public.partners (
            partner_type,
            partner_name,
            director_name,
            email,
            phone,
            address,
            rating
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s);
        """,
        [
            record.type,
            record.partner_name,
            record.director_name,
            record.email,
            record.phone,
            record.address,
            record.rating
        ])
    conn.commit()
    cursor.close()
    conn.close()


def get_partner_types():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, type_name
        FROM public.partner_types;
    """)
    records = cursor.fetchall()
    result = []
    for record in records:
        result.append(PartnerTypeItem(*record))
    cursor.close()
    conn.close()
    return result