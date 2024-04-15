def check_ip_address(ip):
    octets = ip.split('.')

    if len(octets) != 4:
        print("Адрес — это четыре числа, разделённые точками.")
        return

    for octet in octets:
        if not octet.isdigit():
            print(f"{octet} — это не целое число.")
            return
        if int(octet) > 255:
            print(f"{octet} превышает 255.")
            return

    print("IP-адрес корректен.")


ip = input("Введите IP: ")
check_ip_address(ip)
