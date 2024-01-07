pkgname = "perl-convert-binhex"
pkgver = "1.125"
pkgrel = 1
build_style = "perl_module"
hostmakedepends = ["gmake", "perl"]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Perl module to extract data from Macintosh BinHex files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/release/Convert-BinHex"
source = f"$(CPAN_SITE)/Convert/Convert-BinHex-{pkgver}.tar.gz"
sha256 = "513591b4be46bd7eb91e83197721b4a045a9753a3dd2f11de82c9d3013226397"
# missing checkdepends
options = ["!check"]
