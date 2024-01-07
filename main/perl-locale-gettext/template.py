pkgname = "perl-locale-gettext"
pkgver = "1.07"
pkgrel = 1
build_style = "perl_module"
hostmakedepends = ["gmake", "perl"]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Permits access from Perl to the gettext() family of functions"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/release/gettext"
# source = f"$(CPAN_SITE)/Locale/gettext-{pkgver}.tar.gz"
source = (
    f"https://cpan.metacpan.org/authors/id/P/PV/PVANDRY/gettext-{pkgver}.tar.gz"
)
sha256 = "909d47954697e7c04218f972915b787bd1244d75e3bd01620bc167d5bbc49c15"
