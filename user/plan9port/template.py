pkgname = "plan9port"
pkgver = "0_git20250508"
pkgrel = 0
_commit = "df9b195ebfcd7d5fb673512ec7ec3b3df9981c61"
hostmakedepends = ["perl"]
makedepends = [
    "fontconfig-devel",
    "freetype-devel",
    "libx11-devel",
    "libxext-devel",
    "libxt-devel",
    "linux-headers",
]
pkgdesc = "Port of programs from Plan 9"
license = "MIT"
url = "https://9fans.github.io/plan9port"
source = f"https://github.com/9fans/plan9port/archive/{_commit}.tar.gz"
sha256 = "920232bc57c41b019e2254d67cbb332fe4dd5a5e90334a9174e8d0b51c4f0624"
options = ["!cross", "!lintstatic"]


def configure(self):
    with open(self.cwd / "LOCAL.config", "w") as config:
        config.write("CC9=" + self.get_tool("CC") + "\n")
        config.write(
            "CC9FLAGS='"
            + self.get_cflags(shell=True)
            + " "
            + self.get_ldflags(shell=True)
            + "'\n"
        )


def build(self):
    self.do("./INSTALL", "-b", env={"NPROC": str(self.make_jobs)})


def install(self):
    self.do("./INSTALL", "-c", env={"PLAN9_TARGET": "/usr/lib/plan9"})

    self.install_license("LICENSE")
    self.rm("LICENSE")

    self.rm(".github", recursive=True)
    self.rm(".gitignore")
    self.rm("configure")
    self.rm("Makefile")
    self.rm("install.log")
    self.rm("install.sum")
    self.rm("install.txt")

    self.install_files(".", "usr/lib", name="plan9")

    self.install_dir("usr/bin")
    self.install_link("usr/bin/9", "../lib/plan9/bin/9")
    self.install_file(
        self.files_path / "acme.desktop", "usr/share/applications"
    )
