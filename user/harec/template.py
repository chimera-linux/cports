pkgname = "harec"
pkgver = "0.24.2"
pkgrel = 1
archs = ["aarch64", "riscv64", "x86_64"]
build_style = "makefile"
make_env = {"VERSION": pkgver, "LOCALVER": "chimera"}
make_build_args = [f"ARCH={self.profile().arch}"]
make_check_args = [*make_build_args]
depends = ["qbe"]
checkdepends = ["binutils", *depends]
pkgdesc = "Hare compiler"
license = "GPL-3.0-only"
url = "https://git.sr.ht/~sircmpwn/harec"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "88b3961b236fbfe3a0dfb46bb954741fa5c031bbda6d07fbc238c98f0abb41a2"
tool_flags = {
    # Taken from configs/linux.mk
    "CFLAGS": ["-std=c11", "-D_XOPEN_SOURCE=700", "-Iinclude"],
}
hardening = ["vis", "cfi"]


def pre_build(self):
    self.cp("configs/linux.mk", "config.mk")
