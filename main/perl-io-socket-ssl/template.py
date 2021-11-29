pkgname = "perl-io-socket-ssl"
pkgver = "2.072"
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
sha256 = "b5bee81db3905a9069340a450a48e1e1b32dec4ede0064f5703bafb9a707b89d"
# missing checkdepends
options = ["!check"]
