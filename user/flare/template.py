pkgname = "flare"
pkgver = "0.21.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "blueprint-compiler",
    "cargo-auditable",
    "desktop-file-utils",
    "gettext",
    "meson",
    "pkgconf",
    "protobuf-protoc",
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
    "rust-std",
    "sqlcipher-devel",
    "sqlite-devel",
]
pkgdesc = "Unofficial Signal Desktop app"
license = "AGPL-3.0-only"
url = "https://mobile.schmidhuberj.de/flare"
source = f"https://gitlab.com/schmiddi-on-mobile/flare/-/archive/{pkgver}/flare-{pkgver}.tar.gz"
sha256 = "80638b22753a39ed1583cbff2d2dcb837848ba3f75909145c4b27e3476f0ec26"

if self.profile().wordsize == 32:
    broken = "needs atomic64"


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
