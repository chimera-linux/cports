pkgname = "geopard"
pkgver = "1.7.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "blueprint-compiler",
    "cargo-auditable",
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "meson",
    "pkgconf",
]
makedepends = ["gtk4-devel", "libadwaita-devel", "rust-std"]
pkgdesc = "GTK 4 Gemini client"
license = "GPL-3.0-or-later"
url = "https://ranfdev.com/projects/geopard"
source = (
    f"https://github.com/ranfdev/Geopard/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "3a0e00438000f80a5bd599e14aa5982a2676a4c9b4a763dfc2fa3d804cb0034a"


def prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)
    del self.make_env["CARGO_BUILD_TARGET"]
