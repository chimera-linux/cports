pkgname = "ca-certificates"
pkgver = "20240203"
pkgrel = 1
build_style = "makefile"
make_use_env = True
hostmakedepends = ["openssl"]
depends = ["openssl", "debianutils"]
triggers = [
    "/usr/share/ca-certificates",
    "/usr/local/share/ca-certificates",
    "/etc/ssl/certs",
    "/etc/ca-certificates/update.d",
]
pkgdesc = "Common CA certificates for SSL/TLS"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND MPL-2.0"
url = "https://tracker.debian.org/pkg/ca-certificates"
source = (
    f"$(DEBIAN_SITE)/main/c/ca-certificates/ca-certificates_{pkgver}.tar.xz"
)
sha256 = "3286d3fc42c4d11b7086711a85f865b44065ce05cf1fb5376b2abed07622a9c6"
compression = "deflate"
# no tests
options = ["!check", "keepempty", "brokenlinks"]


def post_patch(self):
    from cbuild.util import compiler

    self.cp(self.files_path / "certdata2pem.c", ".")
    with self.profile("host"):
        cc = compiler.C(self)
        cc.invoke(["certdata2pem.c"], "mozilla/certdata2pem")

    self.cp(self.files_path / "remove-expired-certs.sh", "mozilla")


def pre_install(self):
    self.install_dir("usr/share/" + pkgname)
    self.install_dir("usr/bin")
    self.install_dir("etc/ssl/certs")
    self.install_link("usr/sbin", "bin")


def post_install(self):
    self.install_dir("usr/share/man/man8")
    self.install_file("sbin/update-ca-certificates.8", "usr/share/man/man8")

    cpath = self.destdir / "usr/share/ca-certificates"
    with open(self.destdir / "etc/ca-certificates.conf", "w") as ofile:
        for f in cpath.rglob("*.crt"):
            ofile.write(str(f.relative_to(cpath)))
            ofile.write("\n")

    self.install_link("etc/ssl/certs.pem", "certs/ca-certificates.crt")
    self.uninstall("usr/sbin")

    self.install_dir("etc/ca-certificates/update.d")
