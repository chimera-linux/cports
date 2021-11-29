pkgname = "perl-net-ssleay"
pkgver = "1.90"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["gmake", "perl", "openssl"]
makedepends = ["perl", "zlib-devel", "openssl-devel"]
depends = ["perl"]
pkgdesc = "Perl extension for using OpenSSL"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Artistic-2.0"
url = "https://metacpan.org/release/Net-SSLeay"
source = f"$(CPAN_SITE)/Net/Net-SSLeay-{pkgver}.tar.gz"
sha256 = "f8696cfaca98234679efeedc288a9398fcf77176f1f515dbc589ada7c650dc93"
# missing checkdepends
options = ["!check"]
