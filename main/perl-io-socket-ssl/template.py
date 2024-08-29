pkgname = "perl-io-socket-ssl"
pkgver = "2.089"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl", "perl-net-ssleay", "perl-uri"]
depends = [*makedepends]
pkgdesc = "SSL sockets with IO::Socket interface"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/release/IO-Socket-SSL"
source = f"$(CPAN_SITE)/IO/IO-Socket-SSL-{pkgver}.tar.gz"
sha256 = "f683112c1642967e9149f51ad553eccd017833b2f22eb23a9055609d2e3a14d1"
# missing checkdepends
options = ["!check"]
