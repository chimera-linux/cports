pkgname = "perl-uri"
pkgver = "5.24"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["gmake", "perl"]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Perl Uniform Resource Identifiers module"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/release/URI"
source = f"$(CPAN_SITE)/URI/URI-{pkgver}.tar.gz"
sha256 = "466dd5a40b2c8e99d53692dc49b971561d5d7c2a30814e5ff0b63a4a25e2aaef"
# missing checkdepends
options = ["!check"]
