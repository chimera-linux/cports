pkgname = "qemu"
pkgver = "9.2.0"
pkgrel = 2
build_style = "gnu_configure"
# TODO vde
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
    "--enable-bpf",
    "--enable-cap-ng",
    "--enable-capstone",
    "--enable-curl",
    "--enable-curses",
    "--enable-dbus-display",
    "--enable-docs",
    "--enable-gtk",
    "--enable-guest-agent",
    "--enable-jack",
    "--enable-kvm",
    "--enable-libdw",
    "--enable-libnfs",
    "--enable-libssh",
    "--enable-linux-aio",
    "--enable-linux-io-uring",
    "--enable-lzo",
    "--enable-numa",
    "--enable-pie",
    "--enable-sdl",
    "--enable-seccomp",
    "--enable-snappy",
    "--enable-system",
    "--enable-tpm",
    "--enable-usb-redir",
    "--enable-vhost-net",
    "--enable-virglrenderer",
    "--enable-virtfs",
    "--enable-vnc",
    "--enable-vnc-jpeg",
    "--enable-zstd",
    "--disable-bsd-user",
    "--disable-debug-info",
    "--disable-glusterfs",
    "--disable-linux-user",
    "--disable-oss",
    "--disable-werror",
    "--disable-xen",
    "--audio-drv-list=pa,pipewire,jack,sdl",
]
# actually meson
configure_gen = []
hostmakedepends = [
    "bash",
    "bison",
    "bzip2",
    "flex",
    "gettext",
    "meson",
    "ninja",
    "perl",
    "pkgconf",
    "python-sphinx",
    "python-sphinx_rtd_theme",
]
makedepends = [
    "bzip2-devel",
    "capstone-devel",
    "dtc-devel",
    "elfutils-devel",
    "fuse-devel",
    "glib-devel",
    "gnutls-devel",
    "gtk+3-devel",
    "keyutils-devel",
    "libaio-devel",
    "libbpf-devel",
    "libcacard-devel",
    "libcap-ng-devel",
    "libcbor-devel",
    "curl-devel",
    "libdrm-devel",
    "libiscsi-devel",
    "libjpeg-turbo-devel",
    "libnfs-devel",
    "libpulse-devel",
    "libsasl-devel",
    "libseccomp-devel",
    "libslirp-devel",
    "libssh-devel",
    "liburing-devel",
    "libusb-devel",
    "linux-headers",
    "linux-pam-devel",
    "lzo-devel",
    "ncurses-devel",
    "nss-devel",
    "numactl-devel",
    "pcsc-lite-devel",
    "pipewire-devel",
    "pipewire-jack-devel",
    "pixman-devel",
    "sdl2-compat-devel",
    "sdl2_image-devel",
    "snappy-devel",
    "usbredir-devel",
    "virglrenderer-devel",
    "vte-gtk3-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
scripts = {"pre-install": True, "pre-upgrade": True}
pkgdesc = "Generic machine emulator and virtualizer"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND LGPL-2.1-only"
url = "https://qemu.org"
source = f"https://download.qemu.org/qemu-{pkgver}.tar.xz"
sha256 = "f859f0bc65e1f533d040bbe8c92bcfecee5af2c921a6687c652fb44d089bd894"
tool_flags = {
    # see libbpf comment about bpf headers
    "CFLAGS": ["-I/usr/include/bpf/uapi"],
    "CXXFLAGS": ["-I/usr/include/bpf/uapi"],
}
file_modes = {
    "etc/qemu/bridge.conf": ("root", "_qemu", 0o640),
    "usr/lib/qemu-bridge-helper": ("root", "_qemu", 0o4710),
}
# maybe someday
options = ["!cross", "!check"]

if self.profile().endian == "little":
    configure_args += ["--enable-spice"]
    makedepends += ["spice-devel", "spice-protocol"]
else:
    configure_args += ["--disable-spice"]


def init_configure(self):
    ljobs = 4 if self.make_jobs >= 4 else self.make_jobs
    # qemu links a lot of big exes at once so ensure there is not more than four
    self.configure_args += [f"-Dbackend_max_links={ljobs}"]


def post_install(self):
    self.install_service(self.files_path / "qemu-ga")

    self.install_sysusers(self.files_path / "qemu.conf")
    self.install_file(self.files_path / "80-kvm.rules", "usr/lib/udev/rules.d")
    self.install_file(self.files_path / "bridge.conf", "etc/qemu")

    # no elf files in /usr/share
    self.rename("usr/share/qemu", "usr/lib/qemu", relative=False)
    self.install_link("usr/share/qemu", "../lib/qemu")

    self.uninstall("usr/share/doc")


@subpackage("qemu-guest-agent")
def _(self):
    self.pkgdesc = "QEMU guest agent"
    self.depends = []

    return [
        "usr/lib/dinit.d/qemu-ga",
        "usr/bin/qemu-ga",
    ]


@subpackage("qemu-img")
def _(self):
    self.pkgdesc = "QEMU command line tools for manipulating disk images"
    self.depends = []

    return [
        "usr/bin/qemu-img",
        "usr/bin/qemu-io",
        "usr/bin/qemu-nbd",
        "usr/bin/qemu-storage-daemon",
    ]


@subpackage("qemu-tools")
def _(self):
    self.pkgdesc = "QEMU support tools"
    self.depends = []

    return [
        "usr/bin/qemu-edid",
        "usr/bin/qemu-keymap",
        "usr/bin/elf2dmp",
    ]


@subpackage("qemu-pr-helper")
def _(self):
    self.pkgdesc = "QEMU pr helper utility"
    self.depends = []

    return [
        "usr/bin/qemu-pr-helper",
        "usr/share/man/man8/qemu-pr-helper.8",
    ]


@subpackage("qemu-vhost-user-gpu")
def _(self):
    self.pkgdesc = "QEMU vhost user GPU device"
    self.depends = []

    return [
        "usr/lib/vhost-user-gpu",
        "usr/lib/qemu/vhost-user/50-qemu-gpu.json",
    ]


@subpackage("qemu-edk2-firmware")
def _(self):
    self.pkgdesc = "QEMU edk2 firmware files"
    self.depends = []

    return [
        "usr/lib/qemu/firmware",
        "usr/lib/qemu/edk2*",
    ]


def _spkg(sname):
    @subpackage(f"qemu-system-{sname}")
    def _(self):
        self.subdesc = f"system-{sname}"
        self.depends = [self.parent]
        self.options = ["foreignelf"]

        extras = []

        match sname:
            case "aarch64":
                self.depends += [self.with_pkgver("qemu-edk2-firmware")]
            case "alpha":
                extras = ["usr/lib/qemu/palcode-clipper"]
            case "arm":
                self.depends += [self.with_pkgver("qemu-edk2-firmware")]
                extras = [
                    "usr/lib/qemu/npcm7xx_bootrom.bin",
                ]
            case "hppa":
                extras = [
                    "usr/lib/qemu/hppa-firmware.img",
                    "usr/lib/qemu/hppa-firmware64.img",
                ]
                self.options += ["execstack"]
            case "i386":
                self.depends += [self.with_pkgver("qemu-edk2-firmware")]
            case "ppc":
                extras = [
                    "usr/lib/qemu/openbios-ppc",
                    "usr/lib/qemu/u-boot.e500",
                    "usr/lib/qemu/u-boot-sam460-20100605.bin",
                ]
                self.options += ["execstack"]
            case "riscv32":
                extras = [
                    "usr/lib/qemu/opensbi-riscv32-generic-fw_dynamic.bin",
                ]
            case "riscv64":
                extras = [
                    "usr/lib/qemu/opensbi-riscv64-generic-fw_dynamic.bin",
                ]
            case "s390x":
                extras = [
                    "usr/lib/qemu/s390-ccw.img",
                ]
                self.options += ["execstack", "textrels"]
            case "sparc":
                extras = [
                    "usr/lib/qemu/openbios-sparc32",
                ]
                self.options += ["execstack"]
            case "sparc64":
                extras = [
                    "usr/lib/qemu/openbios-sparc64",
                ]
                self.options += ["execstack"]
            case "x86_64":
                self.depends += [self.with_pkgver("qemu-edk2-firmware")]

        # never strip them
        self.nostrip_files = extras

        return [f"usr/bin/qemu-system-{sname}", *extras]


for _sys in [
    "aarch64",
    "alpha",
    "arm",
    "avr",
    "hppa",
    "i386",
    "loongarch64",
    "m68k",
    "microblaze",
    "microblazeel",
    "mips",
    "mips64",
    "mips64el",
    "mipsel",
    "or1k",
    "ppc",
    "ppc64",
    "riscv32",
    "riscv64",
    "rx",
    "s390x",
    "sh4",
    "sh4eb",
    "sparc",
    "sparc64",
    "tricore",
    "x86_64",
    "xtensa",
    "xtensaeb",
]:
    _spkg(_sys)
