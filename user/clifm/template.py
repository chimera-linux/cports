pkgname = "clifm"
pkgver = "1.29"
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
sha256 = "dfdc0f339437345d9d5d8c2cb4bd43294c05821ebc8d5f0c9abfa4eec8f6c905"
# no tests
options = ["!check"]
