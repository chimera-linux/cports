pkgname = "perl-io-socket-ssl"
pkgver = "2.081"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["gmake", "perl"]
makedepends = ["perl", "perl-net-ssleay", "perl-uri"]
depends = list(makedepends)
pkgdesc = "SSL sockets with IO::Socket interface"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/release/IO-Socket-SSL"
source = f"$(CPAN_SITE)/IO/IO-Socket-SSL-{pkgver}.tar.gz"
sha256 = "07bdf826a8d6b463316d241451c890d1012fa2499a83d8e3d00ce0a584618443"
# missing checkdepends
options = ["!check"]
