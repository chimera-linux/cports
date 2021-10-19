pkgname = "ca-certificates"
pkgver = "20210119"
pkgrel = 0
hostmakedepends = ["openssl"]
depends = ["openssl<=2.0", "run-parts"]
triggers = [
    "/usr/share/ca-certificates",
    "/usr/local/share/ca-certificates",
    "/etc/ssl/certs",
    "/etc/ca-certificates/update.d"
]
pkgdesc = "Common CA certificates for SSL/TLS"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND MPL-2.0"
url = "https://tracker.debian.org/pkg/ca-certificates"
source = f"$(DEBIAN_SITE)/main/c/{pkgname}/{pkgname}_{pkgver}.tar.xz"
sha256 = "daa3afae563711c30a0586ddae4336e8e3974c2b627faaca404c4e0141b64665"
# no tests
options = ["!check", "keepempty", "brokenlinks"]

def post_patch(self):
    from cbuild.util import compiler
    import re

    self.cp(self.files_path / "certdata2pem.c", ".")
    with self.profile("host"):
        cc = compiler.C(self)
        cc.invoke(
            ["certdata2pem.c"], "mozilla/certdata2pem"
        )

    self.cp(self.files_path / "remove-expired-certs.sh", "mozilla")

    with open(self.cwd / "mozilla/Makefile", "r") as ifile:
        with open(self.cwd / "mozilla/Makefile.new", "w") as ofile:
            for ln in ifile:
                ln = ln.replace("python3 certdata2pem.py", "./certdata2pem")
                ln = re.sub(
                    "(.*)(certdata2pem.*)",
                    "\\1\\2\n\\1./remove-expired-certs.sh",
                    ln
                )
                ofile.write(ln)

    self.mv("mozilla/Makefile.new", "mozilla/Makefile")

def init_build(self):
    from cbuild.util import make
    self.make = make.Make(self)

def do_build(self):
    self.make.build()

def do_install(self):
    self.install_dir("usr/share/" + pkgname)
    self.install_dir("usr/bin")
    self.install_dir("etc/ssl/certs")

    self.install_link("bin", "usr/sbin")

    self.make.install()

    self.install_dir("usr/share/man/man8")
    self.install_file("sbin/update-ca-certificates.8", "usr/share/man/man8")

    cpath = self.destdir / "usr/share/ca-certificates"
    with open(self.destdir / "etc/ca-certificates.conf", "w") as ofile:
        for f in cpath.rglob("*.crt"):
            ofile.write(str(f.relative_to(cpath)))
            ofile.write("\n")

    self.install_link(
        "/etc/ssl/certs/ca-certificates.crt", "etc/ssl/certs.pem"
    )
    self.rm(self.destdir / "usr/sbin")

    self.install_dir("etc/ca-certificates/update.d")
