# install locations
PREFIX = /usr/local
BINDIR = $(PREFIX)/bin
MANDIR = $(PREFIX)/share/man
SRCDIR = $(PREFIX)/src
STDLIB = $(SRCDIR)/hare/stdlib

# variables used during build
PLATFORM = linux
ARCH = $(CBUILD_TARGET_MACHINE)
HAREFLAGS =
HARECFLAGS = -a$(ARCH)
QBEFLAGS =
ASFLAGS =
LDLINKFLAGS = --gc-sections -z noexecstack -z pack-relative-relocs

# commands used by the build script
HAREC = harec
QBE = qbe
AS = as
LD = ld
SCDOC = scdoc

# build locations
HARECACHE = .cache
BINOUT = .bin

# variables that will be embedded in the binary with -D definitions
HAREPATH = $(SRCDIR)/hare/stdlib:$(SRCDIR)/hare/third-party
VERSION=$$(./scripts/version)

# For cross-compilation, modify the variables below
AARCH64_AS=aarch64-chimera-linux-musl-as
AARCH64_CC=aarch64-chimera-linux-musl-cc
AARCH64_LD=aarch64-chimera-linux-musl-ld

RISCV64_AS=riscv64-chimera-linux-musl-as
RISCV64_CC=riscv64-chimera-linux-musl-cc
RISCV64_LD=riscv64-chimera-linux-musl-ld

X86_64_AS=x86_64-chimera-linux-musl-as
X86_64_CC=x86_64-chimera-linux-musl-cc
X86_64_LD=x86_64-chimera-linux-musl-ld
