pkgname = "amberol"
pkgver = "2024.2"
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
    "gst-plugins-bad-devel",
    "libadwaita-devel",
    "rust-std",
]
depends = [
    "gst-plugins-bad",
    "gst-plugins-base",
    "gst-plugins-good",
]
checkdepends = ["bash"]
pkgdesc = "Music player for GNOME"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://apps.gnome.org/Amberol"
source = f"https://gitlab.gnome.org/World/amberol/-/archive/{pkgver}/amberol-{pkgver}.tar.gz"
sha256 = "93b1ef0c2ec5711aa5e170a4a0c81d62f97f6a92c0a74a011955be7022e7e555"
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
