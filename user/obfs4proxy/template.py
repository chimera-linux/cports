pkgname = "obfs4proxy"
pkgver = "0.0.14"
pkgrel = 1
build_style = "go"
make_build_args = ["./obfs4proxy"]
hostmakedepends = ["go", "libcap-progs"]
pkgdesc = "Pluggable transport proxy for Tor. implementing obfs4"
license = "BSD-2-Clause AND GPL-3.0-or-later"
url = "https://github.com/Yawning/obfs4"
source = f"{url}/archive/refs/tags/obfs4proxy-{pkgver}.tar.gz"
sha256 = "a4b7520e732b0f168832f6f2fdf1be57f3e2cce0612e743d3f6b51341a740903"
file_modes = {
    "usr/bin/obfs4proxy": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/bin/obfs4proxy": {"security.capability": "cap_net_bind_service+ep"},
}


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("doc/obfs4proxy.1")
