pkgname = "amberol"
pkgver = "2025.1"
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
license = "GPL-3.0-or-later"
url = "https://apps.gnome.org/Amberol"
source = f"https://gitlab.gnome.org/World/amberol/-/archive/{pkgver}/amberol-{pkgver}.tar.gz"
sha256 = "087623631bee272240d64258c47efbbdf64c5fc46ce8f5e2d3d987feb30ad69d"
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
