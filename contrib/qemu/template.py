pkgname = "qemu"
pkgver = "8.2.1"
pkgrel = 0
build_style = "gnu_configure"
# TODO vde
configure_args = [
    "--enable-cap-ng",
    "--enable-capstone",
    "--enable-curl",
    "--enable-curses",
    "--enable-dbus-display",
    "--enable-docs",
    "--enable-guest-agent",
    "--enable-jack",
    "--enable-gtk",
    "--enable-kvm",
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
    "--enable-vhost-net",
    "--enable-virtfs",
    "--enable-tpm",
    "--enable-usb-redir",
    "--enable-virglrenderer",
    "--enable-vnc",
    "--enable-vnc-jpeg",
    "--enable-zstd",
    "--disable-linux-user",
    "--disable-glusterfs",
    "--disable-debug-info",
    "--disable-bsd-user",
    "--disable-werror",
    "--disable-xen",
    "--audio-drv-list=pa,pipewire,jack,sdl",
]
make_cmd = "gmake"
hostmakedepends = [
    "bash",
    "bison",
    "bzip2",
    "flex",
    "gettext",
    "gmake",
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
    "fuse-devel",
    "glib-devel",
    "gnutls-devel",
    "gtk+3-devel",
    "libaio-devel",
    "libcacard-devel",
    "libcap-ng-devel",
    "libcurl-devel",
    "libiscsi-devel",
    "libjpeg-turbo-devel",
    "libnfs-devel",
    "libnuma-devel",
    "libpulse-devel",
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
    "pcsc-lite-devel",
    "pipewire-devel",
    "pipewire-jack-devel",
    "pixman-devel",
    "sdl-devel",
    "sdl_image-devel",
    "snappy-devel",
    "usbredir-devel",
    "virglrenderer-devel",
    "vte-gtk3-devel",
    "zlib-devel",
    "zstd-devel",
]
pkgdesc = "Generic machine emulator and virtualizer"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND LGPL-2.1-only"
url = "https://qemu.org"
source = f"https://download.qemu.org/qemu-{pkgver}.tar.xz"
sha256 = "8562751158175f9d187c5f22b57555abe3c870f0325c8ced12c34c6d987729be"
suid_files = ["usr/libexec/qemu-bridge-helper"]
file_modes = {
    "etc/qemu/bridge.conf": ("root", "_qemu", 0o640),
    "usr/libexec/qemu-bridge-helper": ("root", "_qemu", 0o4710),
}
# maybe someday
options = ["!cross", "!check"]

system_users = ["_qemu"]

if self.profile().endian == "little":
    configure_args += ["--enable-spice"]
    makedepends += ["spice-devel", "spice-protocol"]
else:
    configure_args += ["--disable-spice"]


def post_install(self):
    self.install_service(self.files_path / "qemu-ga")

    self.install_file(self.files_path / "qemu.conf", "usr/lib/sysusers.d")
    self.install_file(self.files_path / "80-kvm.rules", "usr/lib/udev/rules.d")
    self.install_file(self.files_path / "bridge.conf", "etc/qemu")

    # no elf files in /usr/share
    self.mv(self.destdir / "usr/share/qemu", self.destdir / "usr/lib/qemu")
    self.install_link("../lib/qemu", "usr/share/qemu")

    self.rm(self.destdir / "usr/share/doc", recursive=True)


@subpackage("qemu-guest-agent")
def _guest_agent(self):
    self.pkgdesc = "QEMU guest agent"
    self.depends = []

    return [
        "etc/dinit.d/qemu-ga",
        "usr/bin/qemu-ga",
    ]


@subpackage("qemu-img")
def _img(self):
    self.pkgdesc = "QEMU command line tools for manipulating disk images"
    self.depends = []

    return [
        "usr/bin/qemu-img",
        "usr/bin/qemu-io",
        "usr/bin/qemu-nbd",
        "usr/bin/qemu-storage-daemon",
    ]


@subpackage("qemu-tools")
def _tools(self):
    self.pkgdesc = "QEMU support tools"
    self.depends = []

    return [
        "usr/bin/qemu-edid",
        "usr/bin/qemu-keymap",
        "usr/bin/elf2dmp",
    ]


@subpackage("qemu-pr-helper")
def _pr_helper(self):
    self.pkgdesc = "QEMU pr helper utility"
    self.depends = []

    return [
        "usr/bin/qemu-pr-helper",
        "usr/share/man/man8/qemu-pr-helper.8",
    ]


@subpackage("qemu-vhost-user-gpu")
def _vhost_user_gpu(self):
    self.pkgdesc = "QEMU vhost user GPU device"
    self.depends = []

    return [
        "usr/libexec/vhost-user-gpu",
        "usr/lib/qemu/vhost-user/50-qemu-gpu.json",
    ]


def _spkg(sname):
    @subpackage(f"qemu-system-{sname}")
    def _system(self):
        self.pkgdesc = f"{pkgname} (system-{sname})"
        self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
        self.options = ["foreignelf"]

        extras = []

        match sname:
            case "aarch64":
                extras = [
                    "usr/lib/qemu/edk2-aarch64-code.fd",
                    "usr/lib/qemu/firmware/60-edk2-aarch64.json",
                ]
            case "alpha":
                extras = ["usr/lib/qemu/palcode-clipper"]
            case "arm":
                extras = [
                    "usr/lib/qemu/edk2-arm-code.fd",
                    "usr/lib/qemu/edk2-arm-vars.fd",
                    "usr/lib/qemu/npcm7xx_bootrom.bin",
                    "usr/lib/qemu/firmware/60-edk2-arm.json",
                ]
            case "hppa":
                extras = [
                    "usr/lib/qemu/hppa-firmware.img",
                ]
                self.options += ["execstack"]
            case "i386":
                extras = [
                    "usr/lib/qemu/edk2-i386-code.fd",
                    "usr/lib/qemu/edk2-i386-secure-code.fd",
                    "usr/lib/qemu/edk2-i386-vars.fd",
                    "usr/lib/qemu/firmware/50-edk2-i386-secure.json",
                    "usr/lib/qemu/firmware/60-edk2-i386.json",
                ]
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
                    "usr/lib/qemu/s390-netboot.img",
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
                extras = [
                    "usr/lib/qemu/edk2-x86_64-code.fd",
                    "usr/lib/qemu/edk2-x86_64-secure-code.fd",
                    "usr/lib/qemu/firmware/50-edk2-x86_64-secure.json",
                    "usr/lib/qemu/firmware/60-edk2-x86_64.json",
                ]

        # never strip them
        self.nostrip_files = extras

        return [f"usr/bin/qemu-system-{sname}"] + extras


for _sys in [
    "aarch64",
    "alpha",
    "arm",
    "avr",
    "cris",
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
    "nios2",
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

configure_gen = []
