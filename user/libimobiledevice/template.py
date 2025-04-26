pkgname = "libimobiledevice"
_commit = "a6b6c35d1550acbd2552d49c2fe38115deec8fc0"
pkgver = "1.3.0_git20250228"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static"]  # prevent building python binding .a
hostmakedepends = [
    "pkgconf",
    "automake",
    "libtool",
    "python",
    "python-cython",
    "python-setuptools",
]
makedepends = [
    "python-devel",
    "glib-devel",
    "openssl3-devel",
    "libusb-devel",
    "libusbmuxd-devel",
    "libplist-devel",
    "libtatsu-devel",
]
pkgdesc = "Library to communicate with Apple devices"
license = "LGPL-2.1-only"
url = "https://libimobiledevice.org"
source = f"https://github.com/libimobiledevice/libimobiledevice/archive/{_commit}.tar.gz"
sha256 = "047e785299592be9bb130ca37ecd3a4b6f991b1e34ee0d614b201f79e4a03e66"
options = ["!cross"]


def pre_configure(self):
    # remove if building from release tarball
    (self.srcdir / ".tarball-version").write_text(pkgver)


@subpackage("libimobiledevice-python")
def _(self):
    self.subdesc = "Python bindings"
    self.depends += ["python"]

    return ["usr/lib/python3*"]


@subpackage("libimobiledevice-devel")
def _(self):
    return self.default_devel()


@subpackage("libimobiledevice-progs")
def _(self):
    return self.default_progs()
