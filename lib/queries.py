GET_RESERVATIONS = """
SELECT
    r.reservation_date,
    v.name AS venue_name,
    v.location AS venue_location,
    c.name AS customer_name,
    s.section AS seat_section,
    s.row AS seat_row,
    s.number AS seat_number,
    s.is_held
FROM
    reservations r
JOIN
    customers c ON r.customer_id = c.id
JOIN
    venues v ON v.id = r.venue_id
JOIN
    seats s ON s.id = r.seat_id;
"""
