pkgname = "libopenraw"
pkgver = "0.3.7"
pkgrel = 4
build_style = "gnu_configure"
configure_args = ["--disable-static"]
hostmakedepends = [
    "autoconf-archive",
    "automake",
    "cargo",
    "libtool",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "curl-devel",
    "gdk-pixbuf-devel",
    "libjpeg-turbo-devel",
    "libxml2-devel",
    "rust-std",
]
pkgdesc = "RAW format parsing library"
license = "LGPL-3.0-or-later"
url = "https://libopenraw.freedesktop.org"
source = f"{url}/download/libopenraw-{pkgver}.tar.xz"
sha256 = "0ece41951b2cd91e43f6a8a5c6a894bbc8b5923b4e49a82ebb6d8ce62bded68c"
# CFI: breaks ljpegtest
# VIS: breaks libopenraw-gnome
hardening = ["!vis", "!cfi"]
# LTO: breaks testbititerator
options = ["!lto"]


def post_extract(self):
    # replace with our vendor config
    self.rm("lib/mp4/.cargo/config.toml")


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc="lib/mp4").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)
    # so target/release is not triple-prefixed for buildsystem integration
    del self.make_env["CARGO_BUILD_TARGET"]


@subpackage("libopenraw-devel")
def _(self):
    return self.default_devel()
