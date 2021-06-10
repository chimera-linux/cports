pkgname = "byacc"
version = "20210520"
revision = 1
build_style = "gnu_configure"
configure_args = ["--program-transform=s,^,b,"]
short_desc = "Berkeley yacc, a LALR(1) parser generator"
maintainer = "q66 <daniel@octaforge.org>"
license="Public Domain"
homepage = "http://invisible-island.net/byacc/"
distfiles = [f"ftp://ftp.invisible-island.net/{pkgname}/{pkgname}-{version}.tgz"]
checksum = ["d7d31dae72cb973482ef7f975609ae401ccc12ee3fb168b67a69526c60afe43e"]

alternatives = [
    ("yacc", "yacc", "/usr/bin/byacc"),
    ("yacc", "yacc.1", "/usr/share/man/man1/byacc.1")
]

def post_install(self):
    self.install_license("README", "LICENSE")
