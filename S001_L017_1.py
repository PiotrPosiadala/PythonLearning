def calculate_paint(efficency_ltr_per_m2, *m2):
    total_area = efficency_ltr_per_m2 * sum(m2)
    print(total_area)

calculate_paint(2,3,4,5)

rooms = [3,4,5]
calculate_paint(2,*rooms)