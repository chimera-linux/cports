pkgname = "flare"
pkgver = "0.17.3"
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
    "sqlite-devel",
]
pkgdesc = "Unofficial Signal Desktop app"
license = "AGPL-3.0-only"
url = "https://mobile.schmidhuberj.de/flare"
source = [
    f"https://gitlab.com/schmiddi-on-mobile/flare/-/archive/{pkgver}/flare-{pkgver}.tar.gz",
    # https://github.com/flathub/de.schmidhuberj.Flare/blob/09faecd07f1b2069c993e38fb50662768947c490/de.schmidhuberj.Flare.json#L129
    "https://github.com/whisperfish/presage/archive/ed011688fc8d9c0ee07c3d44743c138c1fa4dfda.tar.gz",
]
source_paths = [".", "presage"]
sha256 = [
    "79f3a0e35e53b28810eb30abb832a6463b99ef00530441a06f42010db78fd74d",
    "4e142d8f2bed05d2a085dae24f8b29929a21e0c6fb28d8515e9110a8c5507974",
]

if self.profile().wordsize == 32:
    broken = "needs atomic64"


def prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()


def post_patch(self):
    # https://github.com/flathub/de.schmidhuberj.Flare/blob/09faecd07f1b2069c993e38fb50662768947c490/de.schmidhuberj.Flare.json#L134
    # fixes errors like: set `DATABASE_URL` to use query macros online, or run `cargo sqlx prepare` to update the query cache
    self.mv("presage/.sqlx", "vendor/presage-store-sqlite")


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(f"build/target/{self.profile().triplet}/release/flare")
    self.install_license("LICENSE")
