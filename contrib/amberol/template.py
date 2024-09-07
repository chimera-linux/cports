pkgname = "amberol"
pkgver = "0.10.3"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "cargo-auditable",
    "desktop-file-utils",
    "gettext",
    "meson",
    "pkgconf",
]
makedepends = [
    "dbus-devel",
    "gst-plugins-bad-devel",
    "libadwaita-devel",
]
depends = [
    "gst-plugins-bad",
    "gst-plugins-base",
    "gst-plugins-good",
]
pkgdesc = "Music player for GNOME"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://apps.gnome.org/Amberol"
source = f"https://gitlab.gnome.org/World/amberol/-/archive/{pkgver}/amberol-{pkgver}.tar.gz"
sha256 = "52372ec6f5ba066409e8dfc4a62fdb2c57e79f83a809cf295ff0e040eebb233b"
# broken below
options = ["!cross"]


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)
    # so target/release is not triple-prefixed for buildsystem integration
    del self.make_env["CARGO_BUILD_TARGET"]
