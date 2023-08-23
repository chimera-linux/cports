pkgname = "dinit"
pkgver = "0.17.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--syscontrolsocket=/run/dinitctl"]
configure_gen = []
make_cmd = "gmake"
make_dir = "."
make_check_args = ["check-igr"]  # additional target
hostmakedepends = ["gmake"]
pkgdesc = "Service manager and init system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://davmac.org/projects/dinit"
source = f"https://github.com/davmac314/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "f3ce6eaaabd571edc16f54907cd6062f22ed5d4b6f9ae6fc1c6533f39469b1f0"
tool_flags = {"CXXFLAGS": ["-fno-rtti"]}
hardening = ["vis", "cfi"]
