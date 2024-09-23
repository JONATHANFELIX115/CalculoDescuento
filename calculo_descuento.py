def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento basado en el monto total de la compra y el porcentaje de descuento.

    :param monto_total: Monto total de la compra
    :param porcentaje_descuento: Porcentaje de descuento (por defecto 10%)
    :return: Monto del descuento calculado
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento
# Llamada a la función con el porcentaje de descuento por defecto (10%)
monto_total_1 = 200
descuento_1 = calcular_descuento(monto_total_1)
monto_final_1 = monto_total_1 - descuento_1
print(f"Monto total: ${monto_total_1}")
print(f"Descuento: ${descuento_1}")
print(f"Monto final a pagar: ${monto_final_1}")

# Llamada a la función con un porcentaje de descuento específico (20%)
monto_total_2 = 500
descuento_2 = calcular_descuento(monto_total_2, 20)
monto_final_2 = monto_total_2 - descuento_2
print(f"Monto total: ${monto_total_2}")
print(f"Descuento: ${descuento_2}")
print(f"Monto final a pagar: ${monto_final_2}")

