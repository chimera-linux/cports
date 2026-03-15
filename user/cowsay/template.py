pkgname = "cowsay"
pkgver = "3.8.4"
pkgrel = 0
build_style = "makefile"
make_install_args = [
    f"DESTDIR=/destdir/{pkgname}-{pkgver}/{pkgname}",
    "prefix=/usr",
]
depends = ["perl"]
pkgdesc = "Configurable talking cows and other creatures"
license = "GPL-3.0-or-later"
url = "https://cowsay.diamonds"
source = (
    f"https://github.com/cowsay-org/cowsay/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "c15bc10712835d3a9bcda780dc9453362567bf48d1185905dc7ef2334d79aadd"
# no testsuite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
