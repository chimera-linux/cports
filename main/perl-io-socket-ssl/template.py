pkgname = "perl-io-socket-ssl"
pkgver = "2.083"
pkgrel = 1
build_style = "perl_module"
hostmakedepends = ["gmake", "perl"]
makedepends = ["perl", "perl-net-ssleay", "perl-uri"]
depends = list(makedepends)
pkgdesc = "SSL sockets with IO::Socket interface"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/release/IO-Socket-SSL"
source = f"$(CPAN_SITE)/IO/IO-Socket-SSL-{pkgver}.tar.gz"
sha256 = "904ef28765440a97d8a9a0df597f8c3d7f3cb0a053d1b082c10bed03bc802069"
# missing checkdepends
options = ["!check"]
