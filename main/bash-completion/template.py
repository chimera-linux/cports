pkgname = "bash-completion"
pkgver = "2.11"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
make_install_args = ["profiledir=/etc/bash/bashrc.d"]
make_check_args = [
    "--ignore=test/t/test_csplit.py",
    "--ignore=test/t/test_date.py",
    "--ignore=test/t/test_ether_wake.py",
    "--ignore=test/t/test_gdb.py",
    "--ignore=test/t/test_hostname.py",
    "--ignore=test/t/test_ifup.py",
    "--ignore=test/t/test_kill.py",
    "--ignore=test/t/test_killall.py",
    "--ignore=test/t/test_make.py",
    "--ignore=test/t/test_patch.py",
    "--ignore=test/t/test_pr.py",
    "--ignore=test/t/test_printenv.py",
    "--ignore=test/t/test_python.py",
    "--ignore=test/t/test_renice.py",
    "--ignore=test/t/test_rmdir.py",
    "--ignore=test/t/test_service.py",
    "--ignore=test/t/test_strip.py",
]
hostmakedepends = ["gmake", "pkgconf"]
checkdepends = [
    "asciidoc",
    "autoconf",
    "automake",
    "bash",
    "bison",
    "bzip2",
    "chrony",
    "cryptsetup",
    "cups",
    "curl",
    "desktop-file-utils",
    "dmesg",
    "e2fsprogs",
    "eog",
    "evince",
    "file",
    "file-roller",
    "fuse",
    "gnome-screenshot",
    "gperf",
    "gnupg",
    "hunspell",
    "imagemagick",
    "iproute2",
    "iptables",
    "iptables-nft",
    "iputils",
    "kmod",
    "lua5.4",
    "lvm2",
    "lz4",
    "mount",
    "musl-progs",
    "openssl",
    "pciutils",
    "perl",
    "pkgconf",
    "poppler",
    "python",
    "python-flake8",
    "python-pexpect",
    "python-pycodestyle",
    "python-pyflakes",
    "python-pytest",
    "ruby",
    "shadow",
    "texinfo",
    "usbutils",
    "util-linux",
    "xz",
]
depends = ["bash"]
pkgdesc = "Programmable completion functions for bash"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/scop/bash-completion"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "73a8894bad94dee83ab468fa09f628daffd567e8bef1a24277f1e9a0daf911ac"

configure_gen = []


def do_check(self):
    self.do("python", "-m", "pytest", *make_check_args)
