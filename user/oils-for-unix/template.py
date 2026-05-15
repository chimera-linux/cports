pkgname = "oils-for-unix"
pkgver = "0.37.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    # make sure sysroot readline is used in cross builds
    "--readline",
    f"{self.profile().sysroot}/usr",
]
configure_gen = []
make_dir = "."
hostmakedepends = ["autoconf"]
makedepends = ["readline-devel"]
pkgdesc = "Unix shell with structured data"
license = "Apache-2.0"
url = "https://oils.pub"
source = f"{url}/download/oils-for-unix-{pkgver}.tar.gz"
sha256 = "f4d41d20a0523dbcfbd4ba231f82edf25b08d4965d65bc71fcb56666d6743000"
# check: no tests in tarball
options = ["!check"]


def build(self):
    self.do("_build/oils.sh", "--cxx", self.get_tool("CXX"))


def install(self):
    ovm_name = next(self.cwd.glob("_bin/*")).name

    self.do(
        "./install",
        f"_bin/{ovm_name}/oils-for-unix",
        env={"DESTDIR": self.chroot_destdir},
    )

    self.install_shell("/usr/bin/osh")
    self.install_shell("/usr/bin/ysh")
