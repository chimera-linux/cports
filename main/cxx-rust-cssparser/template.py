pkgname = "cxx-rust-cssparser"
pkgver = "1.1.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cargo-auditable",
    "cmake",
    "corrosion",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
    "qt6-qtbase",
]
makedepends = [
    "qt6-qtbase-devel",
    "rust-std",
]
pkgdesc = "Library for parsing CSS"
license = "BSD-2-Clause"
url = "https://invent.kde.org/libraries/cxx-rust-cssparser"
source = f"$(KDE_SITE)/cxx-rust-cssparser/cxx-rust-cssparser-{pkgver}.tar.xz"
sha256 = "c88f883f67d132240f7ef5c8b8fe4f743a79c448b98ac88f2be3b68264840358"
# needs network
options = ["!check"]


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc="rust").vendor()


def post_install(self):
    self.install_license("LICENSES/BSD-2-Clause.txt")


@subpackage("cxx-rust-cssparser-devel")
def _(self):
    return self.default_devel()
