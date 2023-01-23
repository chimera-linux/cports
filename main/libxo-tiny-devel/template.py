pkgname = "libxo-tiny-devel"
pkgver = "1.6.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-dependency-tracking",
    "--disable-libxo-options",
    "--disable-gettext",
    "--disable-shared",
    "--enable-text-only",
]
hostmakedepends = ["pkgconf"]
makedepends = ["musl-bsd-headers"]
depends = ["!libxo-devel"]
pkgdesc = "Library for generating text (tiny and static)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/Juniper/libxo"
source = f"https://github.com/Juniper/libxo/releases/download/{pkgver}/libxo-{pkgver}.tar.gz"
sha256 = "9f2f276d7a5f25ff6fbfc0f38773d854c9356e7f985501627d0c0ee336c19006"
tool_flags = {"CFLAGS": ["-Wno-unused-command-line-argument"]}
options = ["bootstrap", "!lto", "!splitstatic", "!scanpkgconf"]

# libxo does not respect LDFLAGS, so hack it in
def init_configure(self):
    tcflags = self.get_cflags(shell = True)
    tlflags = self.get_ldflags(shell = True)

    self.configure_env = {"CFLAGS": f"{tcflags} {tlflags}"}

# remove stuff we don't need
def post_install(self):
    self.rm(self.destdir / "usr/bin", recursive = True)
    self.rm(self.destdir / "usr/lib/libxo", recursive = True)
    self.rm(self.destdir / "usr/share", recursive = True)
