pkgname = "cracklib"
pkgver = "2.10.1"
pkgrel = 0
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
    "9d5052e32625d65f2c3a9f9e3087d2edf6f592d40367b6eb3cae135d84ca064d",
    "530f24c9ca0e3b35a5c7ea4f281ca02b90813773db060681f56bb1559c5883be",
]


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
                "-9n",
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
