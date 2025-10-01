pkgname = "newsflash"
pkgver = "4.1.4"
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
sha256 = "25a940e59cf118b1ef818225f748981a0ef089cff54774cd9e8ac0436eeec932"

if self.profile().wordsize == 32:
    broken = "needs atomic64"


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(
        f"build/src/{self.profile().triplet}/release/news_flash_gtk",
        name="io.gitlab.news_flash.NewsFlash",
    )
