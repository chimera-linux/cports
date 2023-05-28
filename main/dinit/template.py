pkgname = "dinit"
pkgver = "0.16.999"
_commit = "34736fba7ee2796d565b3bfa2792159d0a5c6d25"
pkgrel = 2
build_style = "gnu_configure"
configure_args = ["--syscontrolsocket=/run/dinitctl"]
make_cmd = "gmake"
make_dir = "."
make_check_args = ["check-igr"]  # additional target
hostmakedepends = ["gmake"]
pkgdesc = "Service manager and init system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://davmac.org/projects/dinit"
# source = f"https://github.com/davmac314/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
source = f"https://github.com/davmac314/{pkgname}/archive/{_commit}.tar.gz"
sha256 = "a45f6ec06cfe900d977c0d4c9b53f0bdadb0b6a514bfdfb7aa5a4433ecedac66"
hardening = ["vis", "cfi"]

tool_flags = {"CXXFLAGS": ["-fno-rtti"]}

configure_gen = []
