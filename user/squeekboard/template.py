pkgname = "squeekboard"
pkgver = "1.43.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "bash",
    "cargo-auditable",
    "gettext",
    "meson",
    "pkgconf",
]
makedepends = [
    "at-spi2-core-devel",
    "cairo-devel",
    "feedbackd-devel",
    "glib-devel",
    "gnome-desktop-devel",
    "gtk+3-devel",
    "libbsd-devel",
    "wayland-protocols",
]
pkgdesc = "Legacy Phosh OSK"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/World/Phosh/squeekboard"
source = f"https://gitlab.gnome.org/World/Phosh/squeekboard/-/archive/v{pkgver}/squeekboard-v{pkgver}.tar.gz"
sha256 = "64c73636f6d8a6ffe9f1094c4084b184db3f60ac4e02bf8bff860060308c61ab"


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor(wrksrc=".")


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)

    # so target/release is not triple-prefixed for buildsystem integration
    del self.make_env["CARGO_BUILD_TARGET"]


def _(self):
    self.provides = ["phosh-keyboard=0"]
