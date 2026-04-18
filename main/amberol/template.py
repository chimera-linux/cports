pkgname = "amberol"
pkgver = "2026.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "blueprint-compiler",
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
sha256 = "2112eebac5c7b0aab7243c428c794aecb136168c326648cfbbd8654ea2cc7631"
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
