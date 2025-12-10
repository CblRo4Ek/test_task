import sys
import re
import dns.resolver

EMAIL_RE = re.compile(r"^[^@\s]+@([^@\s]+\.[^@\s]+)$")

# Создаем резолвер вручную (особенно важно для macOS)
resolver = dns.resolver.Resolver(configure=False)
resolver.nameservers = [
    "8.8.8.8",      # Google DNS
    "8.8.4.4",
    "1.1.1.1",      # Cloudflare
    "1.0.0.1",
]
resolver.timeout = 3
resolver.lifetime = 3


def read_emails_from_file(path: str):
    with open(path, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def read_emails_from_stdin():
    return [line.strip() for line in sys.stdin if line.strip()]


def resolve(domain, record_type):
    try:
        return resolver.resolve(domain, record_type)
    except:
        return None


def check_dns(domain: str):
    mx_valid = False
    domain_exists = False

    # MX
    mx = resolve(domain, "MX")
    if mx:
        mx_valid = True
        domain_exists = True
        return domain_exists, mx_valid

    # A
    if resolve(domain, "A"):
        domain_exists = True
        return domain_exists, mx_valid

    # AAAA
    if resolve(domain, "AAAA"):
        domain_exists = True
        return domain_exists, mx_valid

    return domain_exists, mx_valid


def main():
    if len(sys.argv) >= 2 and sys.argv[1] not in ("-", "--"):
        emails = read_emails_from_file(sys.argv[1])
    else:
        emails = read_emails_from_stdin()

    for email in emails:
        m = EMAIL_RE.match(email)
        if not m:
            print(f"{email} - некорректный формат email")
            continue

        domain = m.group(1)

        domain_exists, mx_valid = check_dns(domain)

        if not domain_exists:
            print(f"{email} - домен отсутствует")
        elif mx_valid:
            print(f"{email} - домен валиден")
        else:
            print(f"{email} - MX-записи отсутствуют или некорректны")


if __name__ == "__main__":
    main()
