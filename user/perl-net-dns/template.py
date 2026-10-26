pkgname = "perl-net-dns"
pkgver = "1.58"
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
sha256 = "6335e9e253bc457c7f7e26aaef673c613f62bde26ab8d1cbdd3ddfeb402871a7"


def post_install(self):
    self.install_license("LICENSE")
