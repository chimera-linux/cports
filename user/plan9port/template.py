pkgname = "plan9port"
pkgver = "0_git20250218"
pkgrel = 0
_commit = "13582b1a899b9644071791e862c935384c27cb35"
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
maintainer = "Erica Z <zerica@callcc.eu>"
license = "MIT"
url = "https://9fans.github.io/plan9port"
source = f"https://github.com/9fans/plan9port/archive/{_commit}.tar.gz"
sha256 = "6513538387caada63e68aa8cb9ab84a0c18deea9df6198b1d8bfec565fffce3d"
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
