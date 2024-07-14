pkgname = "harec"
pkgver = "0.24.0"
pkgrel = 0
archs = ["aarch64", "riscv64", "x86_64"]
build_style = "makefile"
make_env = {"VERSION": pkgver, "LOCALVER": "chimera"}
make_build_args = [f"ARCH={self.profile().arch}"]
make_check_args = list(make_build_args)
depends = ["qbe"]
checkdepends = ["binutils", *depends]
pkgdesc = "Hare compiler"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-3.0-only"
url = "https://git.sr.ht/~sircmpwn/harec"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "add6a7c4cbfd130c5e9fcecd2d43bec39640ed9f9cfbe9166e4b7e945a46b7de"
tool_flags = {
    # Taken from configs/linux.mk
    "CFLAGS": ["-std=c11", "-D_XOPEN_SOURCE=700", "-Iinclude"],
}
hardening = ["vis", "cfi"]


def pre_build(self):
    self.cp("configs/linux.mk", "config.mk")
