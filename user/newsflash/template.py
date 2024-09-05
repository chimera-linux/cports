pkgname = "newsflash"
pkgver = "3.3.4"
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
    "openssl-devel",
    "rust-std",
    "webkitgtk4-devel",
]
pkgdesc = "Feed reader designed for the GNOME desktop"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "GPL-3.0-or-later"
url = "https://gitlab.com/news-flash/news_flash_gtk"
source = f"{url}/-/archive/v.{pkgver}/news_flash_gtk-v.{pkgver}.tar.gz"
sha256 = "f408f4c2d1e1507008ef583868b8482708d13269b86b8e22d2ba73da9c93a0ae"


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
