pkgname = "cpanminus"
pkgver = "1.7049"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl"]
depends = ["perl"]
checkdepends = []
pkgdesc = "Get, unpack, build and install perl modules from CPAN"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/dist/App-cpanminus"
source = f"https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/App-cpanminus-{pkgver}.tar.gz"
sha256 = "b9ffb88e62a06aa91bd7d5a28ef6bdbb942608aea90e3969aa29b33640035214"


def post_install(self):
    # remove duplicate manpage
    self.uninstall("usr/share/man/man3/App::cpanminus::fatscript.3p")
