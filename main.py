import dns.resolver


resolver = dns.resolver.Resolver()
resolver.nameservers = ['8.8.8.8']  # Use Google's public DNS server

# Query the DNS server
domain = input()

# Set the DNS server to use
# Get the DNS records for the domain
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
