pkgname = "flare"
pkgver = "0.15.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "blueprint-compiler",
    "cargo",
    "desktop-file-utils",
    "gettext",
    "meson",
    "pkgconf",
    "protoc",
]
makedepends = [
    "cairo-devel",
    "gdk-pixbuf-devel",
    "glib-devel",
    "gtk4-devel",
    "gtksourceview-devel",
    "libadwaita-devel",
    "libspelling-devel",
    "pango-devel",
]
pkgdesc = "Unofficial Signal Desktop app"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "AGPL-3.0-only"
url = "https://mobile.schmidhuberj.de/flare"
source = f"https://gitlab.com/schmiddi-on-mobile/flare/-/archive/{pkgver}/flare-{pkgver}.tar.gz"
sha256 = "6bd9fe77f9e40fc3d081baf5bd5665b94b3514c5cc488305e46d2656b1f68f7b"


def prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(f"build/target/{self.profile().triplet}/release/flare")
    self.install_license("LICENSE")
