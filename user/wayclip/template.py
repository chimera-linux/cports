pkgname = "wayclip"
pkgver = "0.5"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["pkgconf", "wayland-progs"]
makedepends = ["wayland-devel"]
pkgdesc = "Wayland clipboard utility"
license = "ISC"
url = "https://git.sr.ht/~noocsharp/wayclip"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "a73a6f59bf974f5ad5eafe5ce16921083fca05b5b1ddc979023c082be8dc23e6"
# No upstream test suite available
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
