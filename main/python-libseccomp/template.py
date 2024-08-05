# update libseccomp alongside this
pkgname = "python-libseccomp"
pkgver = "2.5.5"
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
sha256 = "7082b016d3cbda3e15c0e71ebd018023d693bb7507389b32f943db13f935e01d"
# no tests
options = ["!check"]
