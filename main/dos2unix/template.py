pkgname = "dos2unix"
pkgver = "7.5.7"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["pkgconf", "gettext"]
checkdepends = ["perl"]
pkgdesc = "Line ending converter"
license = "BSD-2-Clause"
url = "https://waterlander.net/dos2unix"
source = f"{url}/files/dos2unix-{pkgver}.tar.gz"
sha256 = "669ee27120ae71589f638fe3a167d6ea54f8633f5ab1b282551bd7a7c9510dfa"


def post_install(self):
    self.install_license("COPYING.txt")
