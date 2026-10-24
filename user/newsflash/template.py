pkgname = "newsflash"
pkgver = "5.2.5"
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
    "clapper-devel",
    "gtksourceview-devel",
    "libadwaita-devel",
    "libxml2-devel",
    "openssl3-devel",
    "rust-std",
    "webkitgtk4-devel",
]
pkgdesc = "Feed reader designed for the GNOME desktop"
license = "GPL-3.0-or-later"
url = "https://gitlab.com/news-flash/news_flash_gtk"
source = f"{url}/-/archive/v.{pkgver}/news_flash_gtk-v.{pkgver}.tar.gz"
sha256 = "a52cd40581808e5fd8f0fef61463c1ff6e0bff45352b8b971979be95440e010c"

if self.profile.wordsize == 32:
    broken = "needs atomic64"


def post_prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()


def post_patch(self):
    from cbuild.util import cargo

    cargo.clear_vendor_checksums(self, "aws-lc-sys-0.43.0")


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    from cbuild.util import cargo

    self.install_bin(
        cargo.target_path(self, "news_flash_gtk", "build/src"),
        name="io.gitlab.news_flash.NewsFlash",
    )
