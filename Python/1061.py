dia_i = input().split(' ')[1]
hora_i, min_i, seg_i = input().split(' : ')

dia_f = input().split(' ')[1]
hora_f, min_f, seg_f = input().split(' : ')

seg_i = int(seg_i) + int(min_i) * 60 + int(hora_i) * 3600 + int(dia_i) * 86400
seg_f = int(seg_f) + int(min_f) * 60 + int(hora_f) * 3600 + int(dia_f) * 86400

segundos_distancia = seg_f - seg_i

dias = segundos_distancia // 86400
segundos_distancia -= dias * 86400
print(f'{dias} dia(s)')

horas = segundos_distancia // 3600
segundos_distancia -= horas * 3600
print(f'{horas} hora(s)')

minutos = segundos_distancia // 60
segundos_distancia -= minutos * 60
print(f'{minutos} minuto(s)')
print(f'{segundos_distancia} segundo(s)')
