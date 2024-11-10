pkgname = "j4-dmenu-desktop"
pkgver = "3.1"
pkgrel = 1
build_style = "meson"
configure_args = ["-Denable-tests=true"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["catch2-devel", "fmt-devel", "spdlog-devel"]
checkdepends = ["python-pytest"]
pkgdesc = "Application launcher using dmenu"
maintainer = "wipet <47226783+whypet@users.noreply.github.com>"
license = "GPL-3.0-or-later"
url = "https://github.com/enkore/j4-dmenu-desktop"
source = f"{url}/archive/r{pkgver}.tar.gz"
sha256 = "0e6cf25663cc220e3e3e2bc013fe957c3e4a44f900b5ee6a7609cd501021652d"
