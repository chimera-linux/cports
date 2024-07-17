pkgname = "cracklib"
pkgver = "2.10.0"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--disable-static"]
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "bash",
    "gettext-devel",
    "gmake",
    "libtool",
    "pkgconf",
]
depends = ["cmd:gzip!chimerautils"]
triggers = ["/usr/share/cracklib"]
pkgdesc = "Password checking library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/cracklib/cracklib"
source = [
    f"{url}/releases/download/v{pkgver}/cracklib-{pkgver}.tar.gz",
    f"{url}/releases/download/v{pkgver}/cracklib-words-{pkgver}.gz",
]
source_paths = [".", "words"]
sha256 = [
    "3451f0f28676268a0c6d8b0d5deff090d675a7cfe97825829785bcd9c25caf57",
    "2432e8fdb48b2228c2d83525fbc43bd388b6ce0c397312fab7af30bee8af3e96",
]
# working release por favor
options = ["!check"]


def post_install(self):
    self.install_file(
        f"./words/cracklib-words-{pkgver}",
        "usr/share/cracklib",
        name="cracklib-words",
    )
    # compress
    for f in (self.destdir / "usr/share/cracklib").iterdir():
        with open(f.with_name(f.name + ".gz"), "wb") as cf:
            self.do(
                "gzip",
                "-c",
                self.chroot_destdir / f.relative_to(self.destdir),
                stdout=cf,
            )
            f.unlink()


@subpackage("cracklib-devel")
def _devel(self):
    return self.default_devel()


@subpackage("cracklib-words")
def _words(self):
    self.subdesc = "large word list"
    self.depends = [self.parent]

    return ["usr/share/cracklib/cracklib-words.gz"]
