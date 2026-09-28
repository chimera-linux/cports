pkgname = "perl-io-socket-ssl"
pkgver = "2.095"
pkgrel = 1
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl", "perl-net-ssleay", "perl-uri"]
depends = [*makedepends]
pkgdesc = "SSL sockets with IO::Socket interface"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/release/IO-Socket-SSL"
source = f"$(CPAN_SITE)/IO/IO-Socket-SSL-{pkgver}.tar.gz"
sha256 = "7e764392b1b8bd44e654183c082b75be47800e98d7cd325f0e1b76c7d9a6b768"
# missing checkdepends
options = ["!check"]
