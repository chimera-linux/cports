pkgname = "flare"
pkgver = "0.17.0"
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
    "https://github.com/whisperfish/presage/archive/123c1f926e359c21b34d099279ee8a92462ce96d.tar.gz",
]
source_paths = [".", "presage"]
sha256 = [
    "c8657ed46ecf536364d8e464aca557f1b6146cf5dc6d8b22a7e15a40ba396b7c",
    "df68e0ea9620c42878c036561595e90548872ffc037068f019bb7de1d24eabc9",
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
