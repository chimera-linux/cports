pkgname = "perl-net-dns"
pkgver = "1.57"
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
sha256 = "7c98de329cb5d6a99abbb03aaad2866cb041092ed9936a7246908e170005b058"


def post_install(self):
    self.install_license("LICENSE")
