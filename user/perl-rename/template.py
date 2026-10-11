pkgname = "perl-rename"
pkgver = "1.16.3"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl"]
checkdepends = ["perl"]
pkgdesc = "Renames multiple files using Perl regular expressions"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://github.com/pstray/rename"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6e298237ab49f87dafad22c16ab759b664745c508d06a2a0ca6142797e8b3aef"


def post_install(self):
    self.install_license("LICENSE")
