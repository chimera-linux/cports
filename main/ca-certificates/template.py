pkgname = "ca-certificates"
pkgver = "20241010"
pkgrel = 0
build_style = "makefile"
make_use_env = True
hostmakedepends = ["openssl", "perl"]
makedepends = ["openssl-devel"]
depends = ["debianutils", "openssl"]
# replace the openssl implementation
provides = ["openssl-c_rehash=4"]
triggers = [
    "/usr/share/ca-certificates",
    "/etc/ssl/certs",
    "/etc/ca-certificates/update.d",
]
pkgdesc = "Common CA certificates for SSL/TLS"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND MPL-2.0"
url = "https://gitlab.alpinelinux.org/alpine/ca-certificates"
source = f"{url}/-/archive/{pkgver}/ca-certificates-{pkgver}.tar.gz"
sha256 = "71d4356bdf636b3ab45cb7076a95aaeb0352107ff902bcae6df81c64cc9fe39c"
compression = "deflate"
# no tests
options = ["!check"]


def pre_install(self):
    self.install_dir("usr/bin")
    self.install_link("usr/sbin", "bin")


def post_install(self):
    cpath = self.destdir / "usr/share/ca-certificates"
    # static ca-certificates.conf
    with open(cpath / "ca-certificates.conf", "w") as ofile:
        for f in sorted(cpath.rglob("*.crt")):
            ofile.write(str(f.relative_to(cpath)))
            ofile.write("\n")

    self.install_file(
        self.files_path / "c_rehash.update",
        "usr/share/ca-certificates",
        mode=0o755,
    )
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.uninstall("usr/local")
    self.uninstall("usr/sbin")
