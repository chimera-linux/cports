pkgname = "perl-uri"
pkgver = "5.13"
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
sha256 = "27159527b4210c48599279b57f7ebe3169ef698478f285cefd8ccd943c199929"
# missing checkdepends
options = ["!check"]
