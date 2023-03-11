pkgname = "qemu"
pkgver = "7.2.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-gtk",
    "--enable-sdl",
    "--enable-jack",
    "--enable-vhost-net",
    "--enable-virtfs",
    "--audio-drv-list=pa,oss,jack,alsa,sdl",
    "--enable-linux-user",
    "--enable-system",
    "--enable-docs"
]
make_cmd = "gmake"
hostmakedepends = ["python", "ninja", "pkgconf", "bzip2", "gmake", "bash", "perl", "ugetopt", "python-sphinx",
                   "python-sphinx_rtd_theme"]
makedepends = [
    # misc deps
    "glib-devel", "pixman-devel", "libaio-devel", "libbz2-devel", "linux-headers",
    "libgcrypt-devel", "libcap-ng-devel", "nss-devel", "libaio-devel", "gnutls-devel",
    "libcurl-devel", "dtc-devel", "snappy-devel", "libjpeg-turbo-devel",
    # gtk support
    "gtk+3-devel", "vte-gtk3-devel",
    # sdl support
    "sdl-devel", "sdl_image-devel",
    # pulseaudio support
    "libpulse-devel",
    # jack support
    "jack-devel",
    # alsa support
    "alsa-lib-devel",
    # FUSE support
    "fuse-devel",
    # seccomp support
    "libseccomp-devel",
    # curse support
    "ncurses-devel",
    # usb redir support
    "usbredir-devel",
    # smart card support
    "pcsclite-devel", "libcacard-devel",
    # scsi support
    "libiscsi-devel",
    # pam support
    "linux-pam-devel",
    # numa
    "libnuma-devel",
    # slirp for user networking
    "libslirp-devel",
    # virgl renderer, for virtual gpu
    "virglrenderer-devel"
]
pkgdesc = "Generic and open source machine emulator and virtualizer"
maintainer = "eater <=@eater.me>"
license = "GPL-2.0 AND (BSD-3-Clause OR MIT)"
url = "https://qemu.org"
source = f"https://download.qemu.org/qemu-{pkgver}.tar.xz"
sha256 = "5b49ce2687744dad494ae90a898c52204a3406e84d072482a1e1be854eeb2157"
nostrip_files = ["hppa-firmware.img", "openbios-ppc", "openbios-sparc32", "openbios-sparc64",
                 "opensbi-riscv32-generic-fw_dynamic.elf", "opensbi-riscv64-generic-fw_dynamic.elf", "palcode-clipper",
                 "s390-ccw.img", "s390-netboot.img", "u-boot.e500"]
# either the checks are flaky, or require touching kvm
options = ["!check", "foreignelf", "execstack"]
exec_wrappers = [("/usr/bin/ugetopt", "getopt")]

_user_archs = [
    "aarch64", "aarch64_be", "alpha", "arm", "armeb", "cris", "hexagon", "hppa", "i386", "loongarch64",
    "m68k", "microblaze", "microblazeel", "mips", "mips64", "mips64el", "mipsel", "mipsn32", "mipsn32el",
    "nios2", "or1k", "ppc", "ppc64", "ppc64le", "riscv32", "riscv64", "s390x", "sh4", "sh4eb", "sparc",
    "sparc32plus", "sparc64", "x86_64", "xtensa", "xtensaeb"
]

# spice only supports little endian environments
if self.profile().endian == "little":
    hostmakedepends += ["spice-devel"]


def post_install(self):
    self.mv(self.destdir / "usr/share/qemu", self.destdir / "usr/lib/qemu")
    self.ln_s("../lib/qemu", self.destdir / "usr/share/qemu")

    # script expects folder to be there
    self.mkdir(self.destdir / "usr/share/binfmts", parents=True)
    self.do(self.chroot_cwd / "scripts/qemu-binfmt-conf.sh",
            "--debian",
            "--qemu-path", "/usr/bin",
            "--exportdir", self.chroot_destdir / "usr/share/binfmts",
            # preserve
            "--preserve-argv0", "yes",
            # fix_binary
            "--persistent", "yes",
            # credentials
            "--credential", "yes")


@subpackage("qemu-ga")
def _ga(self):
    self.depends = []
    self.pkgdesc += " (guest agent)"
    return ["usr/bin/qemu-ga"]


@subpackage("qemu-ga-man")
def _ga_man(self):
    self.depends = [f"qemu-ga={pkgver}-r{pkgrel}", "base-man"]
    self.install_if = [f"qemu-ga={pkgver}-r{pkgrel}", "base-man"]
    self.pkgdesc += "(guest agent - manual pages)"
    return ["usr/share/man/man*/qemu-ga.*"]


@subpackage("qemu-utils")
def _utils(self):
    self.depends = []
    self.pkgdesc += " (utils)"
    return ["usr/bin/qemu-img", "usr/bin/qemu-io", "usr/bin/qemu-nbd"]


@subpackage("qemu-utils-man")
def _utils(self):
    self.depends = [f"qemu-utils={pkgver}-r{pkgrel}", "base-man"]
    self.install_if = [f"qemu-utils={pkgver}-r{pkgrel}", "base-man"]
    self.pkgdesc += " (utils - manual pages)"
    return ["usr/share/man/man*/qemu-img.*", "usr/share/man/man*/qemu-nbd.*"]


@subpackage("qemu-user")
def _user(self):
    self.pkgdesc += " (user mode)"
    return [f"usr/bin/qemu-{arch}" for arch in _user_archs]


@subpackage("qemu-user-binfmt")
def _binfmt(self):
    self.install_if = [f"qemu-user={pkgver}-r{pkgrel}", "binfmt-support"]
    self.depends += [f"qemu-user={pkgver}-r{pkgrel}", "binfmt-support", "!qemu-user-static-binfmt"]
    self.pkgdesc += " (user mode - binfmt support)"
    return ["usr/share/binfmts"]
