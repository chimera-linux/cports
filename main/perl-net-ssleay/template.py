pkgname = "perl-net-ssleay"
pkgver = "1.94"
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
sha256 = "9d7be8a56d1bedda05c425306cc504ba134307e0c09bda4a788c98744ebcd95d"
# missing checkdepends
options = ["!check"]
