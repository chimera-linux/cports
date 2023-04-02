pkgname = "dinit"
pkgver = "0.16.999"
_commit = "42228a5e14833b28a2078e6ad2e5e3596cbdaff8"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--syscontrolsocket=/run/dinitctl"]
make_cmd = "gmake"
make_dir = "."
make_check_args = ["check-igr"] # additional target
hostmakedepends = ["gmake"]
pkgdesc = "Service manager and init system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = f"https://davmac.org/projects/dinit"
#source = f"https://github.com/davmac314/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
source = f"https://github.com/davmac314/{pkgname}/archive/{_commit}.tar.gz"
sha256 = "72bec3a7cd4ddb1d372ca358bf70f19e6798dfd10fdebe79403ac8906f9a6f5c"
hardening = ["vis", "cfi"]

tool_flags = {
    "CXXFLAGS": ["-fno-rtti"]
}
