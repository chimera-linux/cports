pkgname = "gcc-bootstrap"
pkgver = "11.2.1"
pkgrel = 0
depends = [f"binutils-{self.profile().arch}"]
pkgdesc = "GCC bootstrap binaries"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://musl.cc"
source = f"https://more.musl.cc/{pkgver}/x86_64-linux-musl/{self.profile().triplet.split('-')[0]}-linux-musl-native.tgz"
options = [
    "!strip",
    "!scanrundeps",
    "!scanshlibs",
    "!lintstatic",
    "brokenlinks",
]

match self.profile().arch:
    case "aarch64":
        sha256 = (
            "daf336cafa2c3c7daf42f6a46edc960f10a181fcf15ab9f1c43b192e8ad2a069"
        )
    case "ppc64le":
        sha256 = (
            "8dcc9295573e86cbd5a5f8be832cfee0e933e4a7c861cf0a0e99b204402977e1"
        )
    case "ppc64":
        sha256 = (
            "a9f7b7a5cd0673867228017d63041c9b8b4543e8792357da051b45bdfe3d2b0f"
        )
    case "ppc":
        sha256 = (
            "5f9f746e929de8fcf339442401ef5ad142b627dec152d8d9889fa73855b43c16"
        )
    case "riscv64":
        sha256 = (
            "affeea316358b3ea95423c805f37d1f34a3dd441096f49bca742bac44c83291e"
        )
    case "x86_64":
        sha256 = (
            "eb1db6f0f3c2bdbdbfb993d7ef7e2eeef82ac1259f6a6e1757c33a97dbcef3ad"
        )
    case _:
        broken = f"not yet built for {self.profile().arch}"


def install(self):
    for d in self.cwd.iterdir():
        if d.name == "usr":
            continue
        self.install_files(d, "usr/lib/gcc-bootstrap")
    # needed for the binaries to run
    self.install_link("usr/lib/gcc-bootstrap/usr", ".")
    # default to our native linker because what they ship does not support
    # relr so it will fail to link to any of our regular libraries...
    archn = self.profile().triplet.split("-")[0]
    self.uninstall("usr/lib/gcc-bootstrap/bin/ld")
    self.uninstall(f"usr/lib/gcc-bootstrap/{archn}-linux-musl/bin/ld")
    self.install_link("usr/lib/gcc-bootstrap/bin/ld", "../../../bin/ld.bfd")
    self.install_link(
        f"usr/lib/gcc-bootstrap/{archn}-linux-musl/bin/ld",
        "../../../../bin/ld.bfd",
    )
