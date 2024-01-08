pkgname = "cracklib"
pkgver = "2.9.11"
pkgrel = 1
build_wrksrc = f"{pkgname}"
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
    f"{url}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz",
    f"{url}/releases/download/v{pkgver}/{pkgname}-words-{pkgver}.gz",
]
sha256 = [
    "6213b986a5209fc0d4ca93734e349b8f66b36bfe9a3fae6eead14a15d82a68dc",
    "a68a711a3135739d7b67e9f360b33f0d4eccf9bd7fac4d17c0d5e456a91c517a",
]


def post_extract(self):
    self.mv(f"{pkgname}-{pkgver}", f"{pkgname}")


def post_install(self):
    self.install_file(
        f"../{pkgname}-words-{pkgver}",
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
    self.pkgdesc = f"{pkgdesc} (large word list)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]

    return ["usr/share/cracklib/cracklib-words.gz"]
