pkgname = "cracklib"
pkgver = "2.10.3"
pkgrel = 0
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
    "877b823198eb29aa1778b16a70cad05f7b54b164b3bf7ab656fc326c393f4c85",
    "1d9dd4d8eed30520d83c0f331ac8ddad5b0c78b9fe8a4f456edbba7b6f871250",
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
