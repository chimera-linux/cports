pkgname = "clifm"
pkgver = "1.27.1"
pkgrel = 0
build_style = "makefile"
makedepends = [
    "acl-devel",
    "file-devel",
    "libcap-devel",
    "linux-headers",
    "readline-devel",
]
pkgdesc = "Shell-like, command line terminal file manager"
license = "GPL-2.0-or-later"
url = "https://github.com/leo-arch/clifm"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "a35cd1ccbb83f1261c3c5b14b5b4733cf0555be68579b3cb19fa8b36076a5339"
# no tests
options = ["!check"]
