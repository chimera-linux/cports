pkgname = "perl-net-dns"
pkgver = "1.51"
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
sha256 = "40eec0b2866c67b86505a1c79cbb4b131c98c0bb59f305aa48959c89093d4503"


def post_install(self):
    self.install_license("LICENSE")
