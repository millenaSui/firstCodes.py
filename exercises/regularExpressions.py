# Recebe como entrada um endereço em IPv6 e retorna o resultado do mesmo endereço simplificado (RFC5952)

import re

IPv6 = input('Insira um endereço IPv6: ')

# Substitui múltiplos zeros por um só
IPv6 = re.sub('0000', '0', IPv6)
    
# Substitui os zeros em sequencia restantes por caracteres vazios
IPv6 = re.sub(r':0[0]+', ':', IPv6)
IPv6 = re.sub(r'0[0]+:', ':', IPv6)
IPv6 = re.sub(r':[:]+', ':', IPv6)

try:
    # Substitui a maior ocorrência de zeros repetidos
    sequencias = re.findall(r'[0]+[0:]+', IPv6)
    if (max(sequencias, key=len) > min(sequencias, key=len)):
        maior_sequencia = max(sequencias, key=len)
        IPv6 = re.sub(maior_sequencia, ':', IPv6, 1)
    print(IPv6)

except:
    print(IPv6)