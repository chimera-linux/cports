pkgname = "perl-io-socket-ssl"
pkgver = "2.094"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl", "perl-net-ssleay", "perl-uri"]
depends = [*makedepends]
pkgdesc = "SSL sockets with IO::Socket interface"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/release/IO-Socket-SSL"
source = f"$(CPAN_SITE)/IO/IO-Socket-SSL-{pkgver}.tar.gz"
sha256 = "b2446889cb5e20545d782c4676da1b235673a81c181689aaae2492589d84bf02"
# missing checkdepends
options = ["!check"]
