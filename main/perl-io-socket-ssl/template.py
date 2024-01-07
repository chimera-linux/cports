pkgname = "perl-io-socket-ssl"
pkgver = "2.084"
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
sha256 = "a60d1e04e192363155329560498abd3412c3044295dae092d27fb6e445c71ce1"
# missing checkdepends
options = ["!check"]
