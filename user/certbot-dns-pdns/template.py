pkgname = "certbot-dns-pdns"
pkgver = "0.1.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-poetry-core",
]
depends = ["certbot"]
pkgdesc = "PowerDNS authenticator plugin for certbot"
license = "Apache-2.0"
url = "https://github.com/kaechele/certbot-dns-pdns"
source = f"$(PYPI_SITE)/c/certbot_dns_pdns/certbot_dns_pdns-{pkgver}.tar.gz"
sha256 = "d059d1c1cc21eab259a24ee69c1d9d8fb077fd90f58cf8de904b0f5bd576986f"
# no tests
options = ["!check"]
