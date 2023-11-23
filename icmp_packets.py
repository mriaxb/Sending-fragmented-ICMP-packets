from scapy.all import *

# Função para criar e enviar pacotes ICMP com fragmentos da carga útil
def send_fragmented_icmp_packets(destination_ip, payload):
    # Fragmenta a carga útil em pedaços (tamanho ajustável)
    fragment_size = 1
    payload_fragments = [payload[i:i+fragment_size] for i in range(0, len(payload), fragment_size)]

    # Envia cada fragmento como um pacote ICMP separado
    for fragment in payload_fragments:
        # Criação do pacote ICMP Echo Request com o fragmento da carga útil
        icmp_packet = IP(dst=destination_ip) / ICMP() / Raw(load=fragment)

        # Exibição do pacote criado
        print(f"Pacote ICMP fragmentado:")
        icmp_packet.show()

        # Envio do pacote
        send(icmp_packet)

# Exemplo de uso
if __name__ == "__main__":
    # IP de destino e carga útil personalizada
    target_ip = "192.168.3.20"
    custom_payload = "SSI{H4ck3rs_w1n}"

    # Chama a função para enviar fragmentos da carga útil em pacotes ICMP
    send_fragmented_icmp_packets(target_ip, custom_payload)
