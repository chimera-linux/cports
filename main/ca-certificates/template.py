pkgname = "ca-certificates"
pkgver = "20250619"
pkgrel = 0
build_style = "makefile"
make_use_env = True
hostmakedepends = ["openssl3", "perl"]
makedepends = ["openssl3-devel"]
depends = ["debianutils", "openssl3"]
# replace the openssl implementation
provides = ["openssl-c_rehash=4"]
triggers = [
    "/usr/share/ca-certificates",
    "/etc/ssl/certs",
    "/etc/ca-certificates/update.d",
]
pkgdesc = "Common CA certificates for SSL/TLS"
license = "GPL-2.0-or-later AND MPL-2.0"
url = "https://gitlab.alpinelinux.org/alpine/ca-certificates"
source = f"{url}/-/archive/{pkgver}/ca-certificates-{pkgver}.tar.gz"
sha256 = "fef3719c6a8073b937fb575de5bd4e64117b3b22429d8a2d69cc699031dcfc1e"
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
