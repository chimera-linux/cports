pkgname = "amberol"
pkgver = "2024.1"
pkgrel = 0
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
    "rust-std",
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
sha256 = "2be110f5a5781fc4d11abf8686335e055866ce6df40562ed5eabab16916faceb"
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
