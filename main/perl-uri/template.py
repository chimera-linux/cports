pkgname = "perl-uri"
pkgver = "5.17"
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
sha256 = "5f7e42b769cb27499113cfae4b786c37d49e7c7d32dbb469602cd808308568f8"
# missing checkdepends
options = ["!check"]

# FIXME visibility
hardening = ["!vis"]
