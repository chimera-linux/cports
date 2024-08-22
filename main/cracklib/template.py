pkgname = "cracklib"
pkgver = "2.10.2"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--disable-static"]
hostmakedepends = [
    "automake",
    "bash",
    "gettext-devel",
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
    "2689cd4a3a8df2bbe033aba56bedd1becfa82235505109ca45b4d2a5f652aef6",
    "02b52483c812462fbbc183ab2976ce077e1af0f6c55303e0a0ff1306b0c9c7df",
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
def _(self):
    return self.default_devel()


@subpackage("cracklib-words")
def _(self):
    self.subdesc = "large word list"
    self.depends = [self.parent]

    return ["usr/share/cracklib/cracklib-words.gz"]
