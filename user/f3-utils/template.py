pkgname = "f3-utils"
pkgver = "8.0"
pkgrel = 0
build_style = "makefile"
make_build_args = ["all", "extra"]
make_install_args = ["install-extra"]
make_use_env = True
makedepends = ["argp-standalone", "parted-devel", "linux-headers", "udev-devel"]
pkgdesc = "Flash devices tester"
maintainer = "jabuxas <jabuxas@proton.me>"
license = "GPL-3.0-only"
url = "https://github.com/AltraMayor/f3"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "fb5e0f3b0e0b0bff2089a4ea6af53278804dfe0b87992499131445732e311ab4"
tool_flags = {
    "LDFLAGS": ["-largp"],
}
# no check target
options = ["!check"]
