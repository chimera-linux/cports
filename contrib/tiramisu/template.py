pkgname = "tiramisu"
pkgver = "2.0.20240610"
pkgrel = 0
build_style = "makefile"
hostmakedepends = [
    "pkgconf",
    "vala",
]
makedepends = [
    "glib-devel",
]
pkgdesc = "Notification daemon that writes notifications to stdout"
maintainer = "leath-dub <fierceinbattle@gmail.com>"
license = "MIT"
url = "https://github.com/Sweets/tiramisu"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "b12f6eb40d75329e329c384e4972c9fc668dd8f5c8cafbbe0bebf19036aec53d"
# No check argument
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
