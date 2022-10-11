pkgname = "perl-uri"
pkgver = "5.15"
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
sha256 = "af31b673d91b1b96ea2842523ee03f54039f2ae6a5f40d9cdadf73221f8a586c"
# missing checkdepends
options = ["!check"]
