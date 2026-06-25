pkgname = "flare"
pkgver = "0.20.3"
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
sha256 = "1e5d5481fb5a66039808088a1a9cbee66e812f37a8ddff0700373987052969f1"

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
