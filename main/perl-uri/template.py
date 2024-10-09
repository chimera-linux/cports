pkgname = "perl-uri"
pkgver = "5.30"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Perl Uniform Resource Identifiers module"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/pod/URI"
source = f"$(CPAN_SITE)/URI/URI-{pkgver}.tar.gz"
sha256 = "be366cf5d923e2c0d63e5fe5f707f614a144020961a2a0fe0b2c922f5fb80a95"
# missing checkdepends
options = ["!check"]
