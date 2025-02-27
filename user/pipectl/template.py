pkgname = "pipectl"
pkgver = "0.5.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DINSTALL_DOCUMENTATION=ON"]
hostmakedepends = ["cmake", "ninja", "scdoc"]
pkgdesc = "Named pipe management utility"
license = "GPL-3.0-or-later"
url = "https://github.com/Ferdi265/pipectl"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8addbcfac652ddfe88fc47ed10855dc5da3ae3cd3421be9d3ad3a5fb9f9227fd"
hardening = ["vis", "cfi"]
# no tests defined
options = ["!check"]
