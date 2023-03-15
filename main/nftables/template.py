pkgname = "nftables"
pkgver = "1.0.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-json", "--with-python-bin=/usr/bin/python3", "--with-cli=editline"
]
hostmakedepends = ["pkgconf", "python", "flex", "pkgconf"]
makedepends = [
    "jansson-devel", "libmnl-devel", "libnftnl-devel", "libedit-devel",
    "gmp-devel", "linux-headers"
]
pkgdesc = "Netfilter nftables userspace tools"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "http://netfilter.org/projects/nftables"
source = f"{url}/files/{pkgname}-{pkgver}.tar.bz2"
sha256 = "8d1b4b18393af43698d10baa25d2b9b6397969beecac7816c35dd0714e4de50a"
hardening = ["vis", "cfi"]

def post_install(self):
    fpath = self.files_path
    self.install_file(fpath / "nftables-start", "usr/libexec", mode = 0o755)
    self.install_service(fpath / "nftables")

@subpackage("libnftables")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()

@subpackage("nftables-devel")
def _devel(self):
    return self.default_devel()
