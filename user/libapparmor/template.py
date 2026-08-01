# match to apparmor
pkgname = "libapparmor"
pkgver = "5.0.2"
pkgrel = 0
build_wrksrc = "libraries/libapparmor"
build_style = "gnu_configure"
configure_args = ["--with-python"]
hostmakedepends = [
    "autoconf",
    "autoconf-archive",
    "automake",
    "bison",
    "flex",
    "gettext",
    "gsed",
    "libtool",
    "pkgconf",
    "python-devel",
    "python-setuptools",
    "swig",
]
makedepends = ["python-devel"]
pkgdesc = "Library for AppArmor"
license = "GPL-2.0-or-later"
url = "https://gitlab.com/apparmor/apparmor"
source = f"{url}/-/archive/v{pkgver}/apparmor-v{pkgver}.tar.gz"
sha256 = "bef45f228c0bde2f80d9630084e56bd8020b3fc4dfa7ee48a6aca585bb5ea0ed"
# vis: breaks symbols
hardening = ["!vis"]
# dejagnu
options = ["!check"]
# gsed: used to generate headers
exec_wrappers = [("/usr/bin/gsed", "sed")]


@subpackage("libapparmor-devel")
def _(self):
    return self.default_devel()


@subpackage("python-apparmor")
def _(self):
    self.subdesc = "Python bindings"
    return ["usr/lib/python*"]
