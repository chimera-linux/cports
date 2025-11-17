pkgname = "perl-net-dns"
pkgver = "1.53"
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
sha256 = "04acb4f177d57c147dcedc4bd70e23806af3db75a532f46f95461b2bc9a94959"


def post_install(self):
    self.install_license("LICENSE")
