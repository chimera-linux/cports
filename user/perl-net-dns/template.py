pkgname = "perl-net-dns"
pkgver = "1.54"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl"]
depends = [
    "perl-digest-hmac",
    "perl-digest-md5",
]
checkdepends = [
    "perl-test-pod",
    *depends,
]
pkgdesc = "Domain Name System interface"
license = "MIT"
url = "https://metacpan.org/pod/Net::DNS"
source = f"https://cpan.metacpan.org/authors/id/N/NL/NLNETLABS/Net-DNS-{pkgver}.tar.gz"
sha256 = "7abe0e03e8eead04bfe432d0d90ec0dd61b8ba71afad324a9c76acc6a6fbe2a4"


def post_install(self):
    self.install_license("LICENSE")
