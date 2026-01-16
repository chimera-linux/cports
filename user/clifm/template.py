pkgname = "clifm"
pkgver = "1.28"
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
sha256 = "65ac33825fb55d6388c1044572e464a50ad367b607448774fb396d850b7c4420"
# no tests
options = ["!check"]
