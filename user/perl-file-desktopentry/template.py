pkgname = "perl-file-desktopentry"
pkgver = "0.22"
pkgrel = 1
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl"]
depends = [
    "perl-file-basedir",
    "perl-uri",
]
checkdepends = [*depends]
pkgdesc = "Perl module to handle .desktop files"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/pod/File::DesktopEntry"
source = f"$(CPAN_SITE)/File/File-DesktopEntry-{pkgver}.tar.gz"
sha256 = "169c01e3dae2f629767bec1a9f1cdbd6ec6d713d1501e0b2786e4dd1235635b8"
