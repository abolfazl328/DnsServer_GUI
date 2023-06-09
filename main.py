import dns.resolver
import tkinter as tk


def print_input(domain, name_server, text_box):
    # Set the DNS server to use
    # Get the DNS records for the domain
    resolver = dns.resolver.Resolver()
    resolver.nameservers = name_server  # Use Google's public DNS server
    records = {}

    # Get the SOA record
    try:
        result = resolver.resolve(domain, 'SOA')
        records['SOA'] = [str(r) for r in result]
    except dns.resolver.NoAnswer:
        pass

    # Get the A record
    try:
        result = resolver.resolve(domain, 'A')
        records['A'] = [str(r) for r in result]
    except dns.resolver.NoAnswer:
        pass

    # Get the MX record
    try:
        result = resolver.resolve(domain, 'MX')
        records['MX'] = [str(r.exchange) for r in result]
    except dns.resolver.NoAnswer:
        pass

    # Get the NS records

    try:
        result = resolver.resolve(domain, 'NS')
        records['NS'] = [str(r) for r in result]
    except dns.resolver.NoAnswer:
        pass

    # Get the CNAME records

    try:
        result = resolver.resolve(domain, 'CNAME')
        records['CNAME'] = [str(r) for r in result]
    except dns.resolver.NoAnswer:
        pass

    # Get the PTR records

    try:
        result = resolver.resolve(domain, 'PTR')
        records['PTR'] = [str(r) for r in result]
    except dns.resolver.NoAnswer:
        pass

    # Get the HINFO records

    try:
        result = resolver.resolve(domain, 'HINFO')
        records['HINFO'] = [str(r) for r in result]
    except dns.resolver.NoAnswer:
        pass

    # Get the MINFO records

    try:
        result = resolver.resolve(domain, 'MINFO')
        records['MINFO'] = [str(r) for r in result]
    except dns.resolver.NoAnswer:
        pass

    # Get the MG records

    try:
        result = resolver.resolve(domain, 'MG')
        records['MG'] = [str(r) for r in result]
    except dns.resolver.NoAnswer:
        pass

    # Get the TXT records

    try:
        result = resolver.resolve(domain, 'TXT')
        records['TXT'] = [str(r) for r in result]
    except dns.resolver.NoAnswer:
        pass

    # Get the WKS records

    try:
        result = resolver.resolve(domain, 'WKS')
        records['WKS'] = [str(r) for r in result]
    except dns.resolver.NoAnswer:
        pass

    # Get the NULL records

    try:
        result = resolver.resolve(domain, 'NULL')
        records['NULL'] = [str(r) for r in result]
    except dns.resolver.NoAnswer:
        pass

    # Get the AAAA records

    try:
        result = resolver.resolve(domain, 'AAAA')
        records['AAAA'] = [str(r) for r in result]
    except dns.resolver.NoAnswer:
        pass

    text_box.delete("1.0", "end")
    v.pack(side=tk.RIGHT, fill='y')
    v.config(command=text_box.yview)
    text_box.pack()

    print(f"DNS records for {domain}:")
    for record_type, record_values in records.items():
        print(f"{record_type} record: {', '.join(record_values)}")
        text_box.insert("end", f"{record_type}: record: {', '.join(record_values)}\n")
        text_box.tag_add("red", str(int(text_box.index('end').split('.')[0]) - 2) + ".0",
                         str(int(text_box.index('end').split('.')[0]) - 2) + "." + str(len(record_type) + 1))
        text_box.tag_configure("red", foreground="red")
        text_box.tag_configure("blue", foreground="blue")
        text_box.tag_add("blue", str(int(text_box.index('end').split('.')[0]) - 2) + "." + str(len(record_type) + 2),
                         str(int(text_box.index('end').split('.')[0]) - 1) + ".0")


def delete_dns_server_temp_entry(e):
    DNSNameServerEntry.delete(0, "end")


def delete_domain_temp_entry(e):
    DomainEntry.delete(0, "end")


window = tk.Tk()
window.config(bg='#F7E5D0')
window.title("DNS_SERVER")

DNSNameServer = tk.Label(text="Dns name server:", font=("Arial", 14), bg='#F7E5D0')
DNSNameServer.pack()

DNSNameServerEntry = tk.Entry(bg="#ffffff", fg="#333333", highlightcolor="#2196f3", highlightthickness=2, font=("Arial", 14))
DNSNameServerEntry.insert(0, "8.8.8.8")
DNSNameServerEntry.pack()
DNSNameServerEntry.bind("<FocusIn>", delete_dns_server_temp_entry)

Domain = tk.Label(text="Domain:", font=("Arial", 14), bg='#F7E5D0')
Domain.pack()

DomainEntry = tk.Entry(bg="#ffffff", fg="#333333", highlightcolor="#2196f3", highlightthickness=2, font=("Arial", 14))
DomainEntry.insert(0, "lms.ui.ac.ir")
DomainEntry.pack()
DomainEntry.bind("<FocusIn>", delete_domain_temp_entry)

v = tk.Scrollbar(window, orient='vertical')
textBox = tk.Text(yscrollcommand=v.set, font=("Arial", 14), bg='#FFF5EE')

Button = tk.Button(text="get all queries", font=("Arial", 14), foreground="#212121", background="#2196f3", border="2px solid",
                   command=lambda: print_input(DomainEntry.get(), [DNSNameServerEntry.get()], textBox))
Button.pack(pady=5)

window.resizable(False, False)
window.geometry("400x400")
window.mainloop()

# Query the DNS server
