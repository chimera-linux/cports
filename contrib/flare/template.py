pkgname = "flare"
pkgver = "0.15.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "blueprint-compiler",
    "cargo-auditable",
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
sha256 = "23306cf6f14a35eeea39b426e1bdaf05cc7fab47b6ba55a24675c6ba20ad7a6c"


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
