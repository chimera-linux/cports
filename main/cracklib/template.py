pkgname = "cracklib"
pkgver = "2.9.10"
pkgrel = 0
build_wrksrc = f"{pkgname}"
build_style = "gnu_configure"
configure_args = ["--disable-static"]
hostmakedepends = ["pkgconf", "gettext-tiny-devel"]
depends = ["cmd:gzip!chimerautils"]
triggers = ["/usr/share/cracklib"]
pkgdesc = "Password checking library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/cracklib/cracklib"
source = [
    f"{url}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz",
    f"{url}/releases/download/v{pkgver}/{pkgname}-words-{pkgver}.gz"
]
sha256 = [
    "6d7726ce2ab9ee35aa46a511f12badb059b3ceb7932c7fe64806d265b898aa63",
    "7159ced894bebe0eacfad29bc8e6b08a6991ac1b53f5ff90c1d6abd3f36fda54",
]

def post_extract(self):
    self.mv(f"{pkgname}-{pkgver}", f"{pkgname}")

def post_install(self):
    self.install_file(
        f"../{pkgname}-words-{pkgver}", "usr/share/cracklib",
        name = "cracklib-words"
    )
    # compress
    for f in (self.destdir / "usr/share/cracklib").iterdir():
        with open(f.with_name(f.name + ".gz"), "wb") as cf:
            self.do(
                "gzip", "-c",
                self.chroot_destdir / f.relative_to(self.destdir),
                stdout = cf
            )
            f.unlink()

@subpackage("cracklib-devel")
def _devel(self):
    return self.default_devel()

@subpackage("cracklib-words")
def _words(self):
    self.pkgdesc = f"{pkgdesc} (large word list)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]

    return ["usr/share/cracklib/cracklib-words.gz"]
