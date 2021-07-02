pkgname = "byacc"
version = "20210520"
revision = 1
build_style = "gnu_configure"
configure_args = ["--program-transform=s,^,b,"]
short_desc = "Berkeley yacc, a LALR(1) parser generator"
maintainer = "q66 <q66@chimera-linux.org>"
license="Public Domain"
homepage = "http://invisible-island.net/byacc/"
distfiles = [f"ftp://ftp.invisible-island.net/{pkgname}/{pkgname}-{version}.tgz"]
checksum = ["d7d31dae72cb973482ef7f975609ae401ccc12ee3fb168b67a69526c60afe43e"]

def post_install(self):
    self.install_license("README", "LICENSE")

    import shutil

    self.install_link("byacc", "usr/bin/yacc")
    self.install_link("byacc.1", "usr/share/man/man1/yacc.1")
