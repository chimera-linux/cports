# update libseccomp alongside this
pkgname = "python-libseccomp"
pkgver = "2.6.0"
pkgrel = 0
build_wrksrc = "src/python"
build_style = "python_pep517"
make_build_env = {"VERSION_RELEASE": pkgver}
hostmakedepends = [
    "python-build",
    "python-cython",
    "python-installer",
    "python-setuptools",
]
makedepends = [
    "libseccomp-devel",
    "linux-headers",
    "python-devel",
]
pkgdesc = "High level interface to seccomp"
subdesc = "python bindings"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/seccomp/libseccomp"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "0889a8da98e37f86019c90789fd4ff7eda6e1ceb9ef07d4c51c67aeb50a77860"
# no tests
options = ["!check"]
