pkgname = "cgit-pink"
pkgver = "1.4.1"
_gitver = "2.37.1"
pkgrel = 0
build_style = "makefile"
makedepends = ["openssl3-devel", "zlib-ng-compat-devel", "pcre2-devel"]
checkdepends = ["git"]
pkgdesc = "Updated fork of cgit, a web frontend for git"
license = "GPL-2.0-only"
url = "https://git.causal.agency/cgit-pink/about"
source = [
    f"https://git.causal.agency/cgit-pink/snapshot/cgit-pink-{pkgver}.tar.gz",
    f"https://www.kernel.org/pub/software/scm/git/git-{_gitver}.tar.xz",
]
sha256 = [
    "f1246c6c81305800c24e7eee2b224319ab5e57b1ddb07b4883aea845f29046d5",
    "c8162c6b8b8f1c5db706ab01b4ee29e31061182135dc27c4860224aaec1b3500",
]


def prepare(self):
    self.rm(f"cgit-pink-{pkgver}/git", recursive=True)
    self.mv(f"cgit-pink-{pkgver}/*", ".", glob=True)
    self.mv(f"git-{_gitver}", "git")


def pre_configure(self):
    with open(self.cwd / "cgit.conf", "w") as cf:
        cf.write(
            f"""
CC = {self.get_tool("CC")}
AR = {self.get_tool("AR")}
CFLAGS = {self.get_cflags(shell=True)}
LDFLAGS = {self.get_ldflags(shell=True)}
HOST_CPU = {self.profile().arch}
CGIT_SCRIPT_PATH = /usr/bin
CGIT_DATA_PATH = /usr/share/cgit
filterdir = /usr/share/cgit/filters
            """
        )
    with open(self.cwd / "git/config.mak", "w") as cf:
        cf.write(
            """
USE_LIBPCRE2 = Yes
NO_REGEX = Yes
            """
        )


def post_install(self):
    self.install_man("cgitrc.5.txt", "cgitrc", 5)


def check(self):
    with open(self.cwd / "cgitrc", "w") as rc:
        rc.write(f"scan-path={self.chroot_cwd}")
    self.mkdir("testrepo")
    self.do(
        "git",
        "init",
        "--bare",
        "-b",
        "trunk",
        wrksrc="testrepo",
    )
    with open(self.cwd / "cgi-response", "w") as cr:
        self.do(
            "./cgit",
            env={
                "PATH_INFO": "/testrepo",
                "CGIT_CONFIG": f"{self.chroot_cwd}/cgitrc",
            },
            stdout=cr,
        )
    with open(self.cwd / "cgi-response", "r") as cr:
        response = cr.read()
    headers = response.split("\r\n", 1)[0]
    for line in headers.split("\r\n"):
        key, value = line.split(": ", 1)
        if key.lower() == "status" and not value.startswith("200"):
            raise Exception(f"test call returned status {value}")


@subpackage("cgit-pink-filters")
def _(self):
    self.subdesc = "included filters"
    self.depends = [
        "mandoc",
        "python",
        "python-docutils",
        "python-markdown",
        "python-pygments",
    ]
    return ["usr/share/cgit/filters"]
