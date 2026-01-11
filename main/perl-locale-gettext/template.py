pkgname = "perl-locale-gettext"
pkgver = "1.07"
pkgrel = 3
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Permits access from Perl to the gettext() family of functions"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/pod/Locale::gettext"
source = (
    f"https://cpan.metacpan.org/authors/id/P/PV/PVANDRY/gettext-{pkgver}.tar.gz"
)
sha256 = "909d47954697e7c04218f972915b787bd1244d75e3bd01620bc167d5bbc49c15"
