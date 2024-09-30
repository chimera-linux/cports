pkgname = "gpgme"
pkgver = "1.23.2"
pkgrel = 5
build_style = "gnu_configure"
make_dir = "."
# otherwise cmake files are broken
hostmakedepends = [
    "automake",
    "gnupg",
    "libtool",
    "pkgconf",
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
    "swig",
]
makedepends = [
    "glib-devel",
    "libassuan-devel",
    "libgpg-error-devel",
    "python-devel",
    "qt6-qtbase-devel",
]
depends = ["gnupg"]
pkgdesc = "GnuPG Made Easy"
maintainer = "eater <=@eater.me>"
license = "GPL-3.0-or-later"
url = "https://gnupg.org/software/gpgme/index.html"
source = f"https://gnupg.org/ftp/gcrypt/gpgme/gpgme-{pkgver}.tar.bz2"
sha256 = "9499e8b1f33cccb6815527a1bc16049d35a6198a6c5fae0185f2bd561bce5224"
patch_style = "patch"


def post_build(self):
    # builtin buildsystem is scuffed egg crap so build a wheel separately
    self.do(
        "python",
        "-m",
        "build",
        "--wheel",
        "--no-isolation",
        wrksrc="lang/python",
        env={"top_builddir": "../.."},
    )


def post_install(self):
    # uninstall the scuffed thing first
    self.uninstall("usr/lib/python*/site-packages/*.egg", glob=True)
    whl = (list((self.cwd / "lang/python/dist").glob("*.whl"))[0]).relative_to(
        self.cwd
    )
    # now install the not scuffed thing
    self.do(
        "python",
        "-m",
        "installer",
        "--compile-bytecode",
        "0",
        "--destdir",
        self.chroot_destdir,
        whl,
    )


@subpackage("gpgme-qt")
def _(self):
    self.subdesc = "Qt6 support"

    return ["usr/lib/libqgpgme*.so.*"]


@subpackage("gpgme-qt-devel")
def _(self):
    self.depends = [self.with_pkgver("gpgme-devel")]
    self.subdesc = "Qt6 support development files"

    return [
        "usr/include/QGpgME",
        "usr/include/qgpgme",
        "usr/lib/libqgpgmeqt*.so",
        "usr/lib/cmake/QGpgme*",
    ]


@subpackage("gpgme-devel")
def _(self):
    return self.default_devel()


@subpackage("gpgme-python")
def _(self):
    self.depends += ["python", self.parent]
    return ["usr/lib/python*"]
