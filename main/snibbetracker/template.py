pkgname = "snibbetracker"
pkgver = "1.1.1"
pkgrel = 1
build_style = "makefile"
make_dir = "res/linux"
makedepends = ["sdl2-compat-devel"]
pkgdesc = "Fakebit music tracker"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "MIT"
url = "https://github.com/lundstroem/snibbetracker"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e8d587e70547fbe94de89a95582efcd0ea00cda2632a27082577e520e16dbb78"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_file("README.md", "usr/share/doc/snibbetracker")
