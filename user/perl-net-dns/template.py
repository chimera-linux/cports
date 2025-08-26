pkgname = "perl-net-dns"
pkgver = "1.52"
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
source = f"$(CPAN_SITE)/Net/Net-DNS-{pkgver}.tar.gz"
sha256 = "c9884fcb08e4d03c23188d4e10836c2382fcb65b69859581a20845a3235a7203"


def post_install(self):
    self.install_license("LICENSE")
