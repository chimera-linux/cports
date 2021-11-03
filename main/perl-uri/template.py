pkgname = "perl-uri"
pkgver = "5.09"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["gmake", "perl"]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Perl Uniform Resource Identifiers class (URI, RFC 2396)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/release/URI"
source = f"$(CPAN_SITE)/URI/URI-{pkgver}.tar.gz"
sha256 = "03e63ada499d2645c435a57551f041f3943970492baa3b3338246dab6f1fae0a"
# missing checkdepends
options = ["!check"]
