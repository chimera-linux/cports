pkgname = "xbps"
version = "0.59.1"
revision = 5
bootstrap = True
build_style = "configure"
configure_args = ["--prefix=/usr", "--sysconfdir=/etc"]
make_cmd = "gmake"
short_desc = "XBPS package system utilities"
maintainer = "Juan RP <xtraeme@gmail.com>"
license = "BSD-2-Clause, BSD-3-Clause, ISC"
homepage = "https://github.com/void-linux/xbps"
changelog = "https://github.com/void-linux/xbps/blob/master/NEWS"
distfiles = [f"https://github.com/void-linux/xbps/archive/{version}.tar.gz"]
checksum = ["0cbd8d5f23a62047c75974bca21da9f004a94efffd7f37c68562a8dbc869fb2a"]

checkdepends = ["kyua"]
makedepends = ["zlib-devel", "openssl-devel", "libarchive-devel"]
depends = ["ca-certificates", "xbps-triggers"]

if not current.bootstrapping:
    hostmakedepends = ["gmake", "pkgconf"]

make_dirs = [("/etc/xbps.d", 0o755, "root", "root")]

def post_install(self):
    from cbuild import cpu

    self.install_dir("usr/share/xbps.d")

    with open(self.destdir / "usr/share/xbps.d/xbps-arch.conf", "w") as ofile:
        ofile.write(f"architecture={cpu.target()}\n")

    self.install_license("LICENSE")
    self.install_license("LICENSE.3RDPARTY")

@subpackage("libxbps")
def _lib(self):
    self.short_desc = short_desc + " - runtime library"

    def install():
        self.take("usr/lib/*.so.*")

    return install

@subpackage("libxbps-devel")
def _devel(self):
    self.short_desc = short_desc + " - runtime library - development files"
    self.depends = makedepends + [f"libxbps>={version}_{revision}"]

    def install():
        self.take("usr/include")
        self.take("usr/lib/*.a")
        self.take("usr/lib/*.so")
        self.take("usr/lib/pkgconfig")

    return install
