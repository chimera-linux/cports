# update libseccomp alongside this
pkgname = "python-libseccomp"
pkgver = "2.6.1"
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
license = "LGPL-2.1-or-later"
url = "https://github.com/seccomp/libseccomp"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "f9a13e4c633d319a9240189760ca348caa0837c0ebe2a09b17061da8ceaf60f0"
# no tests
options = ["!check"]
