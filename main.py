import dns.resolver
import tkinter as tk


def print_input(domain, name_server):
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

    # Print the DNS records for the domain
    print(records)
    # print(f"DNS records for {domain}:")
    # for record_type, record_values in records.items():
    #     print(f"{record_type} record: {', '.join(record_values)}")


def delete_temp_entry(e):
    e.delete(0, "end")



window = tk.Tk()
window.title("DNS_SERVER")

DNSNameServer = tk.Label(text="Dns name server")
DNSNameServer.pack()

DNSNameServerEntry = tk.Entry()
DNSNameServerEntry.insert(0, "8.8.8.8")
DNSNameServerEntry.pack()
DNSNameServerEntry.bind("<FocusIn>", delete_temp_entry)

Domain = tk.Label(text="Domain")
Domain.pack()

DomainEntry = tk.Entry()
DomainEntry.insert(0, "lms.ui.ac.ir")
DomainEntry.pack()
DomainEntry.bind("<FocusIn>", delete_temp_entry)

Button = tk.Button(text="get all queries", foreground="white", background="#71ebac", border="2px solid", command=lambda: print_input(DomainEntry.get(), [DNSNameServerEntry.get()]))
Button.pack()

window.resizable(False, False)
window.geometry("400x400")
window.mainloop()
# Query the DNS server

