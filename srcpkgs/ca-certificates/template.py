pkgname = "ca-certificates"
version = "20210119"
revision = 2
bootstrap = True
conf_files = ["/etc/ca-certificates.conf"]
wrksrc = "work"
make_cmd = "bmake"
hostmakedepends = ["openssl"]
depends = ["openssl<=2.0_1", "run-parts"]
short_desc = "Common CA certificates for SSL/TLS"
maintainer = "Orphaned <orphan@voidlinux.org>"
license = "GPL-2.0-or-later, MPL-2.0"
homepage = "https://tracker.debian.org/pkg/ca-certificates"

from cbuild import sites

distfiles = [f"{sites.debian}/main/c/{pkgname}/{pkgname}_{version}.tar.xz"]
checksum = ["daa3afae563711c30a0586ddae4336e8e3974c2b627faaca404c4e0141b64665"]

def post_extract(self):
    from cbuild.util import compiler
    import re
    import os

    cc = compiler.C(self)
    cc.invoke(
        [self.chroot_files_path / "certdata2pem.c"], "mozilla/certdata2pem"
    )

    self.copy(
        self.files_path / "remove-expired-certs.sh",
        "mozilla", root = self.abs_wrksrc
    )

    with open(self.abs_wrksrc / "mozilla/Makefile", "r") as ifile:
        with open(self.abs_wrksrc / "mozilla/Makefile.new", "w") as ofile:
            for ln in ifile:
                ln = ln.replace("python3 certdata2pem.py", "./certdata2pem")
                ln = re.sub(
                    "(.*)(certdata2pem.*)",
                    "\\1\\2\n\\1./remove-expired-certs.sh",
                    ln
                )
                ofile.write(ln)

    os.rename(
        self.abs_wrksrc / "mozilla/Makefile.new",
        self.abs_wrksrc / "mozilla/Makefile"
    )

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
    self.install_file(
        self.abs_wrksrc / "sbin/update-ca-certificates.8", "usr/share/man/man8"
    )

    cpath = self.destdir / "usr/share/ca-certificates"
    with open(self.destdir / "etc/ca-certificates.conf", "w") as ofile:
        for f in cpath.rglob("*.crt"):
            ofile.write(str(f.relative_to(cpath)))
            ofile.write("\n")

    self.install_link(
        "/etc/ssl/certs/ca-certificates.crt", "etc/ssl/certs.pem"
    )
    self.unlink("usr/sbin")
